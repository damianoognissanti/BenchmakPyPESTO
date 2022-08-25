import os
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pandas as pd

def setUnscaledParameters(problem, dataframe, rowindex):
    for i in range(0,len(problem.x_free_ids)):
        parameterName = problem.x_free_ids[i]
        parameterValue = dataframe[parameterName]
        if problem.parameter_df.parameterScale[parameterName] == 'lin':
            problem.parameter_df.nominalValue[parameterName] = parameterValue[rowindex]
        if problem.parameter_df.parameterScale[parameterName] == 'log10':
            problem.parameter_df.nominalValue[parameterName] = 10**parameterValue[rowindex]

def getGradHessFromDataFrame(problem, dataFrameGrad, dataFrameHess, rowindex, gradMat, hessMat):
    # The non-free ids should have Hess=0 so only sets the other
    for ro in problem.x_free_indices:
        # extracts the Gradient
        parameterName = problem.x_ids[ro]
        parameterValue = dataFrameGrad[parameterName]
        gradMat[ro] = parameterValue[rowindex]
        # extracts the Hessian
        for co in problem.x_free_indices:
            parameterName = problem.x_ids[ro] + problem.x_ids[co]
            parameterValue = dataFrameHess[parameterName]
            hessMat[ro,co] = parameterValue[rowindex] 

# True solution and its derivatives
def solfun(par, c0, time) :
    return c0 * np.exp(par * time)
def Dsolfun(par, c0, time) :
    return time * c0 * np.exp(par * time)
def DDsolfun(par, c0, time) :
    return np.power(time,2) * c0 * np.exp(par * time)

# LogLik-function
def logLikFun(par, sigma, c0, time, obs):
    return np.log(sigma) + 0.5*np.log(2*np.pi) + 0.5 * np.power(((obs - solfun(par, c0, time)) / sigma),2)

# All important partial derivatives
def DlogLikFun_sigma(par, sigma, c0, time, obs) :
    return 1/sigma - ( np.power((obs - solfun(par, c0, time)),2) / np.power(sigma,3))
def DDlogLikFun_sigma_sigma(par, sigma, c0, time, obs) :
    return -1/np.power(sigma,2) + 3 * (np.power((obs - solfun(par, c0, time)),2) / np.power(sigma,4))
def DDlogLikFun_sigma_par(par, sigma, c0, time, obs) :
    return - (2*(obs - solfun(par, c0, time)) * ( - Dsolfun(par, c0, time)) / np.power(sigma,3))
def DlogLikFun_par(par, sigma, c0, time, obs) :
    return ((obs - solfun(par, c0, time)) / sigma) * ( - Dsolfun(par, c0, time) / sigma)
def DDlogLikFun_par_par(par, sigma, c0, time, obs) :
    return (np.power(( -Dsolfun(par, c0, time)),2) + (obs - solfun(par, c0, time)) * ( - DDsolfun(par, c0, time)) ) / np.power(sigma,2)

def calculateCostGradHess(dataFrameCost, rowindex, experimentalCondition, measurementData, trueGrad, trueHess):
    trueCost = 0.0
    # Create true solution given parameters
    testCaseCost = dataFrameCost.Cost[rowindex]
    alpha = dataFrameCost.alpha[rowindex]
    beta = dataFrameCost.beta[rowindex]
    sd_sebastian_rel = dataFrameCost.sd_sebastian_rel[rowindex]
    sd_damiano_rel = dataFrameCost.sd_damiano_rel[rowindex]
    sd_sebastian_new = dataFrameCost.sd_sebastian_new[rowindex]
    sd_damiano_new = dataFrameCost.sd_damiano_new[rowindex]
    
    for id in experimentalCondition.conditionId:
        obsData = measurementData.measurement[(measurementData.simulationConditionId == id)]
        noiseParam = measurementData.noiseParameters[(measurementData.simulationConditionId == id)]
        time = measurementData.time[(measurementData.simulationConditionId == id)]
        obsId = measurementData.observableId[(measurementData.simulationConditionId == id)]

        obsData = obsData.to_numpy()
        time = time.to_numpy()
        
        lentime = len(time)
        c0V = np.zeros(lentime)
        parV = np.zeros(lentime)
        sdV = np.zeros(lentime)
        gradIndPar = np.zeros(lentime)
        gradIndSd = np.zeros(lentime)
        
        parIndex = obsId == "sebastian_measurement"
        c0V[parIndex] = s0
        parV[parIndex] = alpha
        gradIndPar[parIndex] = 0

        parIndex = obsId == "damiano_measurement"
        c0V[parIndex] = d0
        parV[parIndex] = beta
        gradIndPar[parIndex] = 1

        sdIndex = noiseParam == "sd_sebastian_rel"
        sdV[sdIndex] = sd_sebastian_rel
        gradIndSd[sdIndex] = 2

        sdIndex = noiseParam == "sd_damiano_rel"
        sdV[sdIndex] = sd_damiano_rel
        gradIndSd[sdIndex] = 3

        sdIndex = noiseParam == "sd_sebastian_new"
        sdV[sdIndex] = sd_sebastian_new
        gradIndSd[sdIndex] = 4

        sdIndex = noiseParam == "sd_damiano_new"
        sdV[sdIndex] = sd_damiano_new
        gradIndSd[sdIndex] = 5
        
        gradIndSd = gradIndSd.astype(int)
        gradIndPar = gradIndPar.astype(int)
        for i in range(0,len(time)):
            # Calculate likelihood            
            trueCost += logLikFun(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            # Calculate gradient
            trueGrad[gradIndPar[i]] += DlogLikFun_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueGrad[gradIndSd[i]] += DlogLikFun_sigma(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            # Calculate hessian
            trueHess[gradIndPar[i], gradIndPar[i]] += DDlogLikFun_par_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndSd[i], gradIndSd[i]] += DDlogLikFun_sigma_sigma(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndPar[i], gradIndSd[i]] += DDlogLikFun_sigma_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndSd[i], gradIndPar[i]] += DDlogLikFun_sigma_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])        
    return trueCost

folder_base = "Benchmark-Models/"
test_folder_base = "Small_Tests/"
modelName = "Test_Cvijoviclab2022simple"
longModelName = "model_" + modelName 

s0 = 8.0
d0 = 4.0

# the yaml configuration file links to all needed files
yamlConfig = os.path.join(folder_base, modelName, modelName + ".yaml")

# import the model from yaml-file
importer = pypesto.petab.PetabImporter.from_yaml(yamlConfig)
petabProblem = importer.petab_problem

# open CSV-files with the Cost, Grad and Hess from Julia
testCasePath = os.path.join(test_folder_base, longModelName, "TestCase.csv")
testCaseGradPath = os.path.join(test_folder_base, longModelName, "TestCaseGrad.csv")
testCaseHessPath = os.path.join(test_folder_base, longModelName, "TestCaseHess.csv")
expCondPath = os.path.join(folder_base, modelName, "experimentalCondition_" + modelName + ".tsv")
measurementDataPath = os.path.join(folder_base, modelName, "measurementData_" + modelName + ".tsv")

dataFrametestCase = pd.read_csv(testCasePath)
dataFrametestCaseGrad = pd.read_csv(testCaseGradPath)
dataFrametestCaseHess = pd.read_csv(testCaseHessPath)
expCondDF = pd.read_csv(expCondPath, sep='\t')
measurementData = pd.read_csv(measurementDataPath, sep='\t')

# create and set options for the objective function
obj = importer.create_objective()
#obj.amici_solver.setMaxSteps(10000)
#obj.amici_solver.setRelativeTolerance(1e-15)
#obj.amici_solver.setAbsoluteTolerance(1e-15)

numberOfGuesses = len(dataFrametestCase)

for testCaseIndex in range(0,numberOfGuesses):
    setUnscaledParameters(petabProblem, dataFrametestCase, testCaseIndex)
    ret = obj(
            petabProblem.x_nominal_scaled,
            mode="mode_fun",
            sensi_orders=(0, 1, 2),
            return_dict=True
    )
    PythonCost = ret['fval']
    PythonGrad = ret['grad']
    PythonHess = ret['hess']
    
    JuliaCost = dataFrametestCase.Cost[testCaseIndex]
    numberOfParameters = len(PythonGrad)
    JuliaGrad = np.zeros(numberOfParameters)
    JuliaHess = np.zeros((numberOfParameters,numberOfParameters))

    trueGrad = np.zeros(numberOfParameters)
    trueHess = np.zeros((numberOfParameters,numberOfParameters))        

    getGradHessFromDataFrame(petabProblem, dataFrametestCaseGrad, dataFrametestCaseHess, testCaseIndex, JuliaGrad, JuliaHess)
    trueCost = calculateCostGradHess(dataFrametestCase, testCaseIndex, expCondDF, measurementData, trueGrad, trueHess)
    #print(PythonCost)
    #print(JuliaCost)
    #print(trueCost)
    print(np.linalg.norm(PythonCost-JuliaCost)/np.linalg.norm(PythonCost))
    #print(np.linalg.norm(JuliaCost-trueCost)/np.linalg.norm(JuliaCost))
    #print("")
    #print(PythonGrad)
    #print(JuliaGrad)
    #print(trueGrad)
    #print(np.linalg.norm(PythonGrad-JuliaGrad)/np.linalg.norm(PythonGrad))
    #print(np.linalg.norm(JuliaGrad-trueGrad)/np.linalg.norm(JuliaGrad))
    #print("")
    #print(PythonHess)
    #print(JuliaHess)
    #print(np.linalg.norm(PythonHess-JuliaHess)/np.linalg.norm(PythonHess))
    #print(np.linalg.norm(JuliaHess-trueHess)/np.linalg.norm(JuliaHess))
    #print("")    