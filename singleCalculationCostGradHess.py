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
# modelName = "Test_Cvijoviclab2022simple"
# modelName = "Test_Cvijoviclab2022"
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
obj.amici_solver.setRelativeTolerance(1e-15)
obj.amici_solver.setAbsoluteTolerance(1e-15)
#obj.amici_solver.setSensitivityMethod(2)

numberOfGuesses = len(dataFrametestCase)
inputVector = np.multiply(0.1,[1,2,3,4,5,6,1,7,8,9,1])
#inputVector = [-1.5031824967959286,-3.0095746355871924,5.009999999926782,-1.9240513626801432,-1.904774873182132,3.8358652775802495,1,0.6320160135256181,0.7893288825398606,0.7347892671669879,1]
#inputVector = np.power(10,inputVector)
ratio=0.693
specC17=0.107
inputVector[6] = ratio
inputVector[10] = specC17
#inputVector = np.array(inputVector)
#perInd = np.random.permutation(len(inputVector))
#inputVector = inputVector[perInd]
#print(perInd)
print(inputVector)
ret = obj(
    inputVector,
    mode="mode_fun",
    sensi_orders=(0, 1, 2),
    return_dict=True
)
PythonCost = ret['fval']
PythonGrad = ret['grad']
PythonHess = ret['hess']


print("PythonCost = ", PythonCost)
print("PythonGrad = ", PythonGrad)
print("PythonHess = ", 2*PythonHess)


# PythonCost =  2616.028841095372
# PythonGrad =  [ 2.27701372e-02  5.47773130e-05 -7.51310909e-05  1.17723849e-02
#   3.67359606e-03 -9.09010007e-03  0.00000000e+00 -8.12253355e+03
#  -3.00948644e+03 -1.94398501e+02  0.00000000e+00]
# PythonHess =  [[ 4.16859663e-06  4.62630271e-09 -6.75353277e-09  2.27390139e-06
#    7.11698893e-07 -1.76836596e-06  0.00000000e+00 -9.54638722e-02
#   -8.76045100e-03 -6.36033821e-04  0.00000000e+00]
#  [ 4.62630271e-09  1.79203055e-09 -2.59191998e-09  4.59643738e-09
#   -6.34157058e-10 -2.02994714e-09  0.00000000e+00  3.62651860e-07
#    2.53594129e-08 -2.52646860e-04  0.00000000e+00]
#  [-6.75353277e-09 -2.59191998e-09  3.76144792e-09 -6.70622574e-09
#    9.11261143e-10  2.97230573e-09  0.00000000e+00  5.34771087e-07
#    5.51575131e-08  3.45401531e-04  0.00000000e+00]
#  [ 2.27390139e-06  4.59643738e-09 -6.70622574e-09  1.24740203e-06
#    3.86419456e-07 -9.67553290e-07  0.00000000e+00 -4.97594721e-02
#   -3.85351489e-03 -6.00849096e-04  0.00000000e+00]
#  [ 7.11698893e-07 -6.34157058e-10  9.11261143e-10  3.86419456e-07
#    1.24086959e-07 -3.02773210e-07  0.00000000e+00 -1.50915802e-02
#   -1.91061338e-03  8.46585439e-05  0.00000000e+00]
#  [-1.76836596e-06 -2.02994714e-09  2.97230573e-09 -9.67553290e-07
#   -3.02773210e-07  7.52640273e-07  0.00000000e+00  3.81812168e-02
#    3.41647299e-03  2.63768023e-04  0.00000000e+00]
#  [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
#    0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
#    0.00000000e+00  0.00000000e+00  0.00000000e+00]
#  [-9.54638722e-02  3.62651860e-07  5.34771087e-07 -4.97594721e-02
#   -1.50915802e-02  3.81812168e-02  0.00000000e+00  3.75753101e+04
#    0.00000000e+00  0.00000000e+00  0.00000000e+00]
#  [-8.76045100e-03  2.53594129e-08  5.51575131e-08 -3.85351489e-03
#   -1.91061338e-03  3.41647299e-03  0.00000000e+00  0.00000000e+00
#    1.40288580e+04  0.00000000e+00  0.00000000e+00]
#  [-6.36033821e-04 -2.52646860e-04  3.45401531e-04 -6.00849096e-04
#    8.46585439e-05  2.63768023e-04  0.00000000e+00  0.00000000e+00
#    0.00000000e+00  1.06489892e+03  0.00000000e+00]
#  [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
#    0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
#    0.00000000e+00  0.00000000e+00  0.00000000e+00]]
