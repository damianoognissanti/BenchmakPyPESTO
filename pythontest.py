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
# modelName = "Zheng_PNAS2012"
modelName = "Boehm_JProteomeRes2014"
# modelName = "Fujita_SciSignal2010"
# modelName = "Sneyd_PNAS2002"
# modelName = "Borghans_BiophysChem1997"
# modelName = "Elowitz_Nature2000"
# modelName = "Crauste_CellSystems2017"
# modelName = "Lucarelli_CellSystems2018"
# modelName = "Schwen_PONE2014"
# modelName = "Blasi_CellSystems2016"
# modelName = "Test_Cvijoviclab2022simple"
modelName = "Test_Cvijoviclab2022"

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
#obj.amici_solver.setRelativeTolerance(1e-7)
#obj.amici_solver.setAbsoluteTolerance(1e-7)
    
for testCaseIndex in range(0,len(dataFrametestCase)):
    lentestCaseColumns = len(testCaseColumns)
    parameterVector = petabProblem.x_nominal_scaled
    for i in range(6,lentestCaseColumns):
        parameterName = testCaseColumns[i]
        parameterValue = dataFrametestCase[parameterName]
        #parameterIndex = petabProblem.x_ids.index(parameterName)
        #parameterVector[parameterIndex] = parameterValue[testCaseIndex]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'lin':
            petabProblem.parameter_df.nominalValue[parameterName] = parameterValue[testCaseIndex]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'log10':
            petabProblem.parameter_df.nominalValue[parameterName] = 10**parameterValue[testCaseIndex]
        #print(petabProblem.parameter_df)
    ret = obj(
        petabProblem.x_nominal_scaled, #parameterVector,
        mode="mode_fun",
        sensi_orders=(0, 1, 2),
        return_dict=True,
    )
    JuliaCost = dataFrametestCase.Cost[testCaseIndex]
    PythonCost = ret['fval']
    #print("PythonCost = " , PythonCost)
    #print("JuliaCost  = ", JuliaCost)   
    #print("diffCost   = ", np.linalg.norm(JuliaCost-PythonCost)/np.linalg.norm(PythonCost))   
    PythonGrad = ret['grad']
    lentestCaseGradColumns = len(petabProblem.x_nominal_scaled)
    JuliaGrad = np.zeros(lentestCaseGradColumns)
    for i in petabProblem.x_free_indices:
        parameterName = petabProblem.x_ids[i]
        parameterValue = dataFrametestCaseGrad[parameterName]
        JuliaGrad[i] = parameterValue[testCaseIndex]
    #PythonGrad[PythonGrad<1e-7]=0
    #JuliaGrad[JuliaGrad<1e-7]=0
    #print("PythonGrad = " , PythonGrad)
    #print("JuliaGrad = " , JuliaGrad)
    print("diffGrad = " , np.linalg.norm(JuliaGrad-PythonGrad)/np.linalg.norm(PythonGrad))
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
    print("PythonHess = " , PythonHess)
    print("JuliaHess = " , JuliaHess)
    print("diffHess = " , np.linalg.norm(JuliaHess-PythonHess)/np.linalg.norm(PythonHess))
