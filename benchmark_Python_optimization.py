import os
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pandas as pd


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

# import the model from yaml-file
importer = pypesto.petab.PetabImporter.from_yaml(yamlConfig)


# open the CSV-file with the parameter values
longModelName = "model_" + modelName 
testCasePath = os.path.join(test_folder_base, longModelName, "CubeOpt.csv")
dataFrametestCase = pd.read_csv(testCasePath)

# initialize the guessMatrix by copying the scaled variables over and over 
# (so that the fixed parameters are stored in the correct positions)
numberOfGuesses = len(dataFrametestCase)
guessMatrix = np.array(importer.petab_problem.x_nominal_scaled)
guessMatrix = np.tile(guessMatrix,(numberOfGuesses,1))

# The dataframe does not contain fixed parameters, only free
# so add the imported parameters to the free column indices
freeIndices = importer.petab_problem.x_free_indices
guessMatrix[:,freeIndices] = dataFrametestCase.values

# create and set options for the objective function
obj = importer.create_objective()
#obj.amici_solver.setMaxSteps(10000)
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)

# select single or multiprocess engine
engine = pypesto.engine.SingleCoreEngine()
#engine = pypesto.engine.MultiProcessEngine()

# Create problem and add all guesses to problem
problem = importer.create_problem(obj)
problem.set_x_guesses(guessMatrix)

# select an optimizer, you will probably need to add them with `pip install ...`
# I had to install these (for ipopt I first had to do  sudo apt install coinor-libipopt-dev)
#pip install pyswarm
#pip install dlib
#pip install fides
#pip install cma
#pip install nlopt
#pip install ipopt

optimizerVector = [
    optimize.CmaesOptimizer(), 
    optimize.DlibOptimizer(), 
    optimize.FidesOptimizer(), 
    optimize.IpoptOptimizer(), 
    optimize.NLoptOptimizer(), 
    optimize.PyswarmOptimizer(), 
    optimize.PyswarmsOptimizer(), 
    optimize.ScipyDifferentialEvolutionOptimizer(), 
    optimize.ScipyOptimizer()]

# If n_starts > numberOfGuesses it will create guesses itself.
# This also works if there are no guesses at all.
#result = optimize.minimize(
#    problem=problem, optimizer=optimizer, n_starts=100, engine=engine
#)

# TEST ALL THE OPTIMIZERS!!!!
for optimizer in optimizerVector:

    result = optimize.minimize(
        problem=problem, optimizer=optimizer, n_starts=numberOfGuesses, engine=engine
    )
    # There is probably a cleaner way of extracting the name of the optimizer
    nameOfOptimizer = str(type(optimizer))[35:-2]
    resultDF = result.optimize_result.as_dataframe()
    outputPath = os.path.join(test_folder_base, longModelName, "optRun" + nameOfOptimizer + ".csv")
    resultDF.to_csv(outputPath, header=resultDF.columns, index=None, sep=',', mode='a')
    #print(resultDF.fval)
    #print(resultDF.x)
    #print(resultDF.grad)

