import os

import amici
import matplotlib.pyplot as plt
import numpy as np
import petab

import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pypesto.visualize as visualize

import libsbml
import pandas as pd

#%matplotlib inline

# To download models (can be run in python with ! before git, i.e. !git clone ...)
# git clone --depth 1 https://github.com/Benchmarking-Initiative/Benchmark-Models-PEtab.git tmp/benchmark-models || (cd tmp/benchmark-models && git pull)

folder_base = "Benchmark-Models/"
test_folder_base = "Small_Tests/"
modelName = "Test_Cvijoviclab2022simple"

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

s0 = 8.0
d0 = 4.0





# the yaml configuration file links to all needed files
yamlConfig = os.path.join(folder_base, modelName, modelName + ".yaml")

# create a petab problem
petabProblem = petab.Problem.from_yaml(yamlConfig)

# import model to amici
importer = pypesto.petab.PetabImporter(petabProblem)
model = importer.create_model()

# print model properties
print("Model parameters:", list(model.getParameterIds()), "\n")
print("Model const parameters:", list(model.getFixedParameterIds()), "\n")
print("Model outputs:   ", list(model.getObservableIds()), "\n")
print("Model states:    ", list(model.getStateIds()), "\n")
# Load default properties
converterConfig = libsbml.SBMLLocalParameterConverter().getDefaultProperties()
petabProblem.sbml_document.convert(converterConfig)

# the csv with the parameter values
longModelName = "model_" + modelName 
testCasePath = os.path.join(test_folder_base, longModelName, "TestCase.csv")
testCaseGradPath = os.path.join(test_folder_base, longModelName, "TestCaseGrad.csv")
testCaseHessPath = os.path.join(test_folder_base, longModelName, "TestCaseHess.csv")

dataFrametestCase = pd.read_csv(testCasePath)
testCaseColumns = dataFrametestCase.columns

dataFrametestCaseGrad = pd.read_csv(testCaseGradPath)
testCaseGradColumns = dataFrametestCaseGrad.columns

dataFrametestCaseHess = pd.read_csv(testCaseHessPath)
testCaseHessColumns = dataFrametestCaseHess.columns

obj = importer.create_objective()
# for some models, hyperparamters need to be adjusted
#obj.amici_solver.setMaxSteps(10000)
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)

for testCaseIndex in range(0,len(dataFrametestCase)):
    lentestCaseColumns = len(testCaseColumns)
    parameterVector = petabProblem.x_nominal_scaled
    for i in range(6,lentestCaseColumns):
        parameterName = testCaseColumns[i]
        parameterValue = dataFrametestCase[parameterName]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'lin':
            petabProblem.parameter_df.nominalValue[parameterName] = parameterValue[testCaseIndex]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'log10':
            petabProblem.parameter_df.nominalValue[parameterName] = 10**parameterValue[testCaseIndex]
    ret = obj(
        petabProblem.x_nominal_scaled,
        mode="mode_fun",
        sensi_orders=(0, 1, 2),
        return_dict=True
    )
    
    JuliaCost = dataFrametestCase.Cost[testCaseIndex]
    PythonCost = ret['fval']

    PythonGrad = ret['grad']
    lentestCaseGradColumns = len(petabProblem.x_nominal_scaled)
    JuliaGrad = np.zeros(lentestCaseGradColumns)
    for i in petabProblem.x_free_indices:
        parameterName = petabProblem.x_ids[i]
        parameterValue = dataFrametestCaseGrad[parameterName]
        JuliaGrad[i] = parameterValue[testCaseIndex]

    PythonHess = ret['hess']
    lentestCaseGradColumns = len(petabProblem.x_nominal_scaled)
    JuliaHess = np.zeros((lentestCaseGradColumns,lentestCaseGradColumns))
    row = 0
    col = 0
    # The non-free ids should have Hess=0
    for rowid in petabProblem.x_free_ids:
        col = 0
        for colid in petabProblem.x_free_ids:
            parameterName = rowid + colid
            parameterValue = dataFrametestCaseHess[parameterName]
            JuliaHess[row,col] = parameterValue[testCaseIndex]
            col += 1
        row += 1

    # Create true solution given parameters
    testCaseCost = dataFrametestCase.Cost[testCaseIndex]
    alpha = dataFrametestCase.alpha[testCaseIndex]
    beta = dataFrametestCase.beta[testCaseIndex]
    sd_sebastian_rel = dataFrametestCase.sd_sebastian_rel[testCaseIndex]
    sd_damiano_rel = dataFrametestCase.sd_damiano_rel[testCaseIndex]
    sd_sebastian_new = dataFrametestCase.sd_sebastian_new[testCaseIndex]
    sd_damiano_new = dataFrametestCase.sd_damiano_new[testCaseIndex]
    
    expCondPath = os.path.join(folder_base, modelName, "experimentalCondition_" + modelName + ".tsv")
    expCondDF = pd.read_csv(expCondPath, sep='\t')
    expCondColumns = expCondDF.columns
    
    measurementDataPath = os.path.join(folder_base, modelName, "measurementData_" + modelName + ".tsv")
    measurementData = pd.read_csv(measurementDataPath, sep='\t')
    
    truelLik = 0.0
    trueGrad = np.zeros(lentestCaseGradColumns)
    trueHess = np.zeros((lentestCaseGradColumns,lentestCaseGradColumns))        
    for id in expCondDF.conditionId:
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
            truelLik += logLikFun(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            # Calculate gradient
            trueGrad[gradIndPar[i]] += DlogLikFun_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueGrad[gradIndSd[i]] += DlogLikFun_sigma(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            # Calculate hessian
            trueHess[gradIndPar[i], gradIndPar[i]] += DDlogLikFun_par_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndSd[i], gradIndSd[i]] += DDlogLikFun_sigma_sigma(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndPar[i], gradIndSd[i]] += DDlogLikFun_sigma_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])
            trueHess[gradIndSd[i], gradIndPar[i]] += DDlogLikFun_sigma_par(parV[i], sdV[i], c0V[i], time[i], obsData[i])        
    
    #print("PythonCost      = " , PythonCost)
    #print("ManualCost      = " , truelLik)
    #print("JuliaCost       = ", JuliaCost)   
    #print("diffCostPyJu    = ", np.linalg.norm(JuliaCost-PythonCost)/np.linalg.norm(PythonCost))   
    #print("diffCostPyJuMan = ", np.linalg.norm(truelLik-PythonCost)/np.linalg.norm(PythonCost))   
    #print("diffCostJuJuMan = ", np.linalg.norm(truelLik-JuliaCost)/np.linalg.norm(JuliaCost))   

    #print("PythonGrad = " , PythonGrad)
    #print("ManualGrad = " , trueGrad)
    #print("JuliaGrad = " , JuliaGrad)
    #print("diffGradPyJu    = " , np.linalg.norm(JuliaGrad-PythonGrad)/np.linalg.norm(PythonGrad))
    #print("diffGradPyJuMan = " , np.linalg.norm(PythonGrad-trueGrad)/np.linalg.norm(PythonGrad))
    #print("diffGradJuJuMan = " , np.linalg.norm(JuliaGrad-trueGrad)/np.linalg.norm(JuliaGrad))

    #print("PythonHess = " , PythonHess)
    #print("ManualHess = " , trueHess)
    #print("JuliaHess = " , JuliaHess)
    #print("diffHessPyJu = " , np.linalg.norm(JuliaHess-PythonHess)/np.linalg.norm(PythonHess))
    #print("diffHessPyJuMan = " , np.linalg.norm(PythonHess-trueHess)/np.linalg.norm(PythonHess))
    #print("diffHessJuJuMan = " , np.linalg.norm(JuliaHess-trueHess)/np.linalg.norm(JuliaHess))

    print(PythonHess[1])
    print(trueHess[1])
    print(JuliaHess[1])
    print(PythonHess/trueHess)