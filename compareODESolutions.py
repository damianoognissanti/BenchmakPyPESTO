import os
import numpy as np
import petab
import pypesto
import pypesto.optimize as optimize
import pypesto.petab
import pandas as pd

import amici
import amici.plotting
import matplotlib.pyplot as plt


def setParametersForAmici(model, problem, dataframe, rowindex, paramvec):
    parameterIds = model.getParameterIds()
    numOfParameters = len(parameterIds)-5 # amici keeps fixed parameters together with free
    for i in range(0,numOfParameters):
        parameterName = parameterIds[i]
        parameterValue = dataframe[parameterName]
        paramvec[i] = parameterValue[rowindex]
        if problem.parameter_df.parameterScale[parameterName] == 'log10':
            paramvec[i] = 10**paramvec[i]
    paramvec[i+1:i+3]=np.array(petabProblem.x_nominal)[petabProblem.x_fixed_indices]

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
dataFrametestCase = pd.read_csv(testCasePath)

# Path to sol.csv-folder
csvWritePath = os.path.join(test_folder_base, longModelName, "PythonSols/")
# Path to Plot-folder
plotWritePath = os.path.join(test_folder_base, longModelName, "PythonPlots/")

# create and set options for the objective function
obj = importer.create_objective()
#obj.amici_solver.setMaxSteps(10000)
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)
#obj.amici_solver.setSensitivityMethod(2)

model = obj.amici_model

numberOfGuesses = len(dataFrametestCase)
parameterVector = np.zeros(len(model.getParameterIds()))
for testCaseIndex in range(0,numberOfGuesses):
    setParametersForAmici(model, petabProblem, dataFrametestCase, testCaseIndex, parameterVector)
    timeVec = np.array([0,2.5,5,10,15,20,30,40,50,60,80,100,120,160,200,240])
    model.setTimepoints(amici.DoubleVector(timeVec))
    #model.setParameters(
    #    amici.DoubleVector(parameterVector)
    #)
    
    model.setParameterByName('Epo_degradation_BaF3', 10**dataFrametestCase['Epo_degradation_BaF3'][testCaseIndex])
    model.setParameterByName('k_exp_hetero', 10**dataFrametestCase['k_exp_hetero'][testCaseIndex])
    model.setParameterByName('k_exp_homo', 10**dataFrametestCase['k_exp_homo'][testCaseIndex])
    model.setParameterByName('k_imp_hetero', 10**dataFrametestCase['k_imp_hetero'][testCaseIndex])
    model.setParameterByName('k_imp_homo', 10**dataFrametestCase['k_imp_homo'][testCaseIndex])
    model.setParameterByName('k_phos', 10**dataFrametestCase['k_phos'][testCaseIndex])
    model.setParameterByName('ratio', 0.693)
    model.setParameterByName('specC17', 0.107)
    model.setParameterByName('noiseParameter1_pSTAT5A_rel', 10**dataFrametestCase['sd_pSTAT5A_rel'][testCaseIndex])
    model.setParameterByName('noiseParameter1_pSTAT5B_rel', 10**dataFrametestCase['sd_pSTAT5B_rel'][testCaseIndex])
    model.setParameterByName('noiseParameter1_rSTAT5A_rel', 10**dataFrametestCase['sd_rSTAT5A_rel'][testCaseIndex])
    #print(model.getParameterNames())
    #print(model.getParameters())
    
    # Create solver instance
    solver = model.getSolver()
    # Run simulation using model parameters from the benchmark collection and default solver options
    rdata = amici.runAmiciSimulation(model, solver)

    fileName = "sol"+str(testCaseIndex+1)+".csv"
    xoutData = np.array(rdata['x'])
    timeoutData = np.array(rdata['ts'])
    outData = np.c_[timeoutData,xoutData]
    headerString = ','.join(model.getStateIds())
    headerString = 'time,'+headerString
    np.savetxt(csvWritePath + fileName, outData, delimiter=",",header=headerString, comments='')
    
    plt.plot(rdata['ts'],rdata['x'][:,0])
    plt.plot(rdata['ts'],rdata['x'][:,1])
    plt.plot(rdata['ts'],rdata['x'][:,2])
    plt.plot(rdata['ts'],rdata['x'][:,3])
    plt.plot(rdata['ts'],rdata['x'][:,4])
    plt.plot(rdata['ts'],rdata['x'][:,5])
    plt.plot(rdata['ts'],rdata['x'][:,6])
    plt.plot(rdata['ts'],rdata['x'][:,7])

    plt.legend(model.getStateIds())
    #plt.show()
    plt.savefig(plotWritePath + 'Figure' +str(testCaseIndex+1) + '.png')
    plt.clf()


###amici.plotting.plotObservableTrajectories(rdata)
###amici.plotting.plotStateTrajectories(rdata)
###plt.show()
##
##for key, value in rdata.items():
##    print('%12s: ' % key, value)
##
##
