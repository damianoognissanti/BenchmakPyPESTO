import os
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pandas as pd

import amici


def setParameters(problem, dataframe, rowindex):
    problem.parameter_df.nominalValue['Epo_degradation_BaF3'] = 10**dataframe['Epo_degradation_BaF3'][rowindex]
    problem.parameter_df.nominalValue['k_exp_hetero'] = 10**dataframe['k_exp_hetero'][rowindex]
    problem.parameter_df.nominalValue['k_exp_homo'] = 10**dataframe['k_exp_homo'][rowindex]
    problem.parameter_df.nominalValue['k_imp_hetero'] = 10**dataframe['k_imp_hetero'][rowindex]
    problem.parameter_df.nominalValue['k_imp_homo'] = 10**dataframe['k_imp_homo'][rowindex]
    problem.parameter_df.nominalValue['k_phos'] = 10**dataframe['k_phos'][rowindex]
    #problem.parameter_df.nominalValue['ratio'] = 0.693
    #problem.parameter_df.nominalValue['specC17'] = 0.107
    problem.parameter_df.nominalValue['sd_pSTAT5A_rel'] = 10**dataframe['sd_pSTAT5A_rel'][rowindex]
    problem.parameter_df.nominalValue['sd_pSTAT5B_rel'] = 10**dataframe['sd_pSTAT5B_rel'][rowindex]
    problem.parameter_df.nominalValue['sd_rSTAT5A_rel'] = 10**dataframe['sd_rSTAT5A_rel'][rowindex]

#def setParameters(problem, dataframe, rowindex, paramvec):
#    numOfParameters = len(problem.x_free_ids)
#    for i in range(0,numOfParameters):
#        parameterName = problem.x_free_ids[i]
#        pIndex = problem.x_free_indices[i]
#        parameterValue = dataframe[parameterName]
#        paramvec[pIndex] = parameterValue[rowindex]

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
longModelName = "model_" + modelName 

# the yaml configuration file links to all needed files
yamlConfig = os.path.join(folder_base, modelName, modelName + ".yaml")

# import the model from yaml-file
importer = pypesto.petab.PetabImporter.from_yaml(yamlConfig)
petabProblem = importer.petab_problem

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
#obj.amici_solver.setRelativeTolerance(1e-15)
#obj.amici_solver.setAbsoluteTolerance(1e-15)

numberOfGuesses = len(dataFrametestCase)
parameterVector = petabProblem.x_nominal_scaled

for testCaseIndex in range(0,numberOfGuesses):
    setParameters(petabProblem, dataFrametestCase, testCaseIndex)
    ret = obj(
            petabProblem.x_nominal_scaled,
            mode="mode_fun",
            sensi_orders=(0, 1, 2),
            return_dict=True
    )
    #setParameters(petabProblem, dataFrametestCase, testCaseIndex, parameterVector)
    #ret = obj(
    #        parameterVector,
    #        mode="mode_fun",
    #        sensi_orders=(0, 1, 2),
    #        return_dict=True
    #)
    PythonCost = ret['fval']
    PythonGrad = ret['grad']
    PythonHess = ret['hess']

    JuliaCost = dataFrametestCase.Cost[testCaseIndex]
    numberOfParameters = len(PythonGrad)
    JuliaGrad = np.zeros(numberOfParameters)
    JuliaHess = np.zeros((numberOfParameters,numberOfParameters))

    getGradHessFromDataFrame(petabProblem, dataFrametestCaseGrad, dataFrametestCaseHess, testCaseIndex, JuliaGrad, JuliaHess)

    # Control python gradient manually
    #problem = importer.create_problem(obj)
    #objective = problem.objective
    #eps = 1e-4
    #
    #def fd(x):
    #    grad = np.zeros_like(x)
    #    j = 0
    #    for i, xi in enumerate(x):
    #        mask = np.zeros_like(x)
    #        mask[i] += eps
    #        valinc, _ = objective(x + mask, sensi_orders=(0, 1))
    #        valdec, _ = objective(x - mask, sensi_orders=(0, 1))
    #        grad[j] = (valinc - valdec) / (2 * eps)
    #        j += 1
    #    return grad
    #
    #fdval = fd(petabProblem.x_nominal_free_scaled)
    #print(fdval)

    #print("PythonCost = ", PythonCost)
    #print("JuliaCost = ", JuliaCost)
    print(PythonCost, JuliaCost)
    #print(PythonCost)
    #print(np.linalg.norm(PythonCost-JuliaCost)/np.linalg.norm(PythonCost))
    #print("")
    #print("PythonGrad = ", PythonGrad)
    #print("JuliaGrad = ", JuliaGrad)
    #print(np.linalg.norm(PythonGrad-JuliaGrad)/np.linalg.norm(PythonGrad))
    #print("")
    #print("PythonHess = ", PythonHess)
    #print("JuliaHess = ", JuliaHess)
    #print(np.linalg.norm(PythonHess-JuliaHess)/np.linalg.norm(PythonHess))
    #print("")
    #print(PythonHess/JuliaGrad)

    