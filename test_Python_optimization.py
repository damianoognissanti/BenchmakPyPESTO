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
#modelName = "Test_Cvijoviclab2022"

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
testCasePath = os.path.join(test_folder_base, longModelName, "CubeOpt.csv")

dataFrametestCase = pd.read_csv(testCasePath)
testCaseColumns = dataFrametestCase.columns

obj = importer.create_objective()
# for some models, hyperparamters need to be adjusted
#obj.amici_solver.setMaxSteps(10000)
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)

#optimizer = optimize.CmaesOptimizer()
#optimizer = optimize.DlibOptimizer()
#optimizer = optimize.FidesOptimizer()
optimizer = optimize.IpoptOptimizer()
#optimizer = optimize.NLoptOptimizer()
#optimizer = optimize.PyswarmOptimizer()
#optimizer = optimize.PyswarmsOptimizer()
#optimizer = optimize.ScipyDifferentialEvolutionOptimizer()
#optimizer = optimize.ScipyOptimizer()
# engine = pypesto.engine.SingleCoreEngine()
engine = pypesto.engine.MultiProcessEngine()


for testCaseIndex in range(0,len(dataFrametestCase)):
    lentestCaseColumns = len(testCaseColumns)
    parameterVector = petabProblem.x_nominal_scaled
    for i in range(0,lentestCaseColumns):
        parameterName = petabProblem.parameter_df.index[i]
        parameterValue = dataFrametestCase[testCaseColumns[i]]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'lin':
            petabProblem.parameter_df.nominalValue[parameterName] = parameterValue[testCaseIndex]
        if petabProblem.parameter_df.parameterScale[parameterName] == 'log10':
            petabProblem.parameter_df.nominalValue[parameterName] = 10**parameterValue[testCaseIndex]
    ret = obj(
        petabProblem.x_nominal_scaled,
        mode="mode_fun",
        sensi_orders=(0, 1, 2),
        return_dict=True,
    )
    problem = importer.create_problem(obj)
    #print(problem.x_fixed_indices, problem.x_free_indices)
    objective = problem.objective
    ret = objective(petabProblem.x_nominal_free_scaled, sensi_orders=(0, 1))
    #print(ret)
    # perform the optimization
    result = optimize.minimize(
        problem=problem, optimizer=optimizer, n_starts=10, engine=engine
    )
    resultDF = result.optimize_result.as_dataframe()
    outputPath = os.path.join(test_folder_base, longModelName, "optRun" + str(testCaseIndex) + ".csv")
    resultDF.to_csv(outputPath, header=resultDF.columns, index=None, sep=',', mode='a')
    print(resultDF.fval)
    print(resultDF.x)
    print(resultDF.grad)