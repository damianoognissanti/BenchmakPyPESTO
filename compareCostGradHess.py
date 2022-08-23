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

folder_base = "Benchmark-Models/"
test_folder_base = "Small_Tests/"
modelName = "Boehm_JProteomeRes2014"
#modelName = "Test_Cvijoviclab2022simple"
#modelName = "Test_Cvijoviclab2022"

# the yaml configuration file links to all needed files
yamlConfig = os.path.join(folder_base, modelName, modelName + ".yaml")

# import the model from yaml-file
importer = pypesto.petab.PetabImporter.from_yaml(yamlConfig)
petabProblem = importer.petab_problem

# open the CSV-file with the parameter values
longModelName = "model_" + modelName 
testCasePath = os.path.join(test_folder_base, longModelName, "CubeOpt.csv")
dataFrametestCase = pd.read_csv(testCasePath)

# open CSV-files with the Cost, Grad and Hess from Julia
testCasePath = os.path.join(test_folder_base, longModelName, "TestCase.csv")
testCaseGradPath = os.path.join(test_folder_base, longModelName, "TestCaseGrad.csv")
testCaseHessPath = os.path.join(test_folder_base, longModelName, "TestCaseHess.csv")

dataFrametestCase = pd.read_csv(testCasePath)
dataFrametestCaseGrad = pd.read_csv(testCaseGradPath)
dataFrametestCaseHess = pd.read_csv(testCaseHessPath)

# create and set options for the objective function
obj = importer.create_objective()
#obj.amici_solver.setMaxSteps(10000)
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)
#obj.amici_solver.setSensitivityMethod(2)

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

    getGradHessFromDataFrame(petabProblem, dataFrametestCaseGrad, dataFrametestCaseHess, testCaseIndex, JuliaGrad, JuliaHess)

    print(PythonCost)
    print(JuliaCost)
    print(np.linalg.norm(PythonCost-JuliaCost)/np.linalg.norm(PythonCost))
    print("")
    #print(PythonGrad)
    #print(JuliaGrad)
    print(np.linalg.norm(PythonGrad-JuliaGrad)/np.linalg.norm(PythonGrad))
    print("")
    #print(PythonHess)
    #print(JuliaHess)
    print(np.linalg.norm(PythonHess-JuliaHess)/np.linalg.norm(PythonHess))
    print("")
    