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
#modelName = "Boehm_JProteomeRes2014"
# modelName = "Fujita_SciSignal2010"
# modelName = "Sneyd_PNAS2002"
# modelName = "Borghans_BiophysChem1997"
# modelName = "Elowitz_Nature2000"
# modelName = "Crauste_CellSystems2017"
# modelName = "Lucarelli_CellSystems2018"
# modelName = "Schwen_PONE2014"
# modelName = "Blasi_CellSystems2016"
modelName = "Test_Cvijoviclab2022simple"
#modelName = "Test_Cvijoviclab2022"

JuliaManGrad=[[-2482.627113403602, -2.699286891072461e-5, 2.3446775200237315, 0.7832201894515517, 7.773450052661612e-5, 0.0005325589743592207]
,[-2482.6336481009866, 3.016334915173502e-8, 2.3445953697121897, 0.7828362555307312, 1.1370615307093601e-6, 5.503551352536995e-6]
,[-2482.627113431598, -6.227111640555449e-6, 2.344677520025619, 0.7832290201625004, 7.773430140289861e-5, 0.0006181678985206496]
,[3.610408612075844e-7, 1.1608136674112757e-9, 2.992825028942814, 0.5812326551804138, -1.5493828442458835e-11, -1.3586909375362666e-12]
,[3.5741894066632085e-7, 1.1407763622628408e-9, 2.9928250289430087, 0.581232655178823, -1.7071455360451182e-11, -2.5049962104617407e-12]
,[-2482.6269622080226, -2.9064414349022627e-5, 2.3446793903741714, 0.7832289268293313, 7.949731863809983e-5, 0.0005446361440686331]
,[-2482.633750576024, -3.843245679036045e-6, 2.344595377178161, 0.7828362913959225, 3.452342758336613e-7, 2.1637558677012336e-6]
,[-2482.626962255227, -6.398575223443004e-6, 2.3446793903788294, 0.7832389899328668, 7.94969467383666e-5, 0.0006389956574283095]
,[3.6104279388382565e-7, 1.1607568239924149e-9, 2.9928250289428444, 0.5812326551806928, -1.5339063352826088e-11, -1.1831646773430293e-12]
,[3.5738844417210203e-7, 1.1708181091307779e-9, 2.9928250289429505, 0.5812326551783767, -1.8883228314336975e-11, -3.443800800084773e-12]
,[-2482.6303012849553, -3.0838270816957447e-6, 2.34463808598466, 0.7830359349805144, 4.0568527053586045e-5, 0.0002777772790959476]
,[-2482.633068058481, -4.372135293806423e-7, 2.3445955140662176, 0.782836930978243, 5.677934773240523e-6, 8.343268874888565e-6]
,[-2482.624189901808, -9.974260748890629e-6, 2.3447136876282118, 0.7834411631393833, 0.00011182202543014164, 0.0011251781215873002]
,[3.573959190816822e-7, 1.1707044222930563e-9, 2.9928250289430474, 0.5812326551791328, -1.8320123196247096e-11, -2.874700477661918e-12]
,[3.610313399349252e-7, 1.1608989325395669e-9, 2.9928250289427982, 0.5812326551803159, -1.6052270623845288e-11, -1.2432277429752503e-12]
,[-2482.6290620285486, -2.726323985768886e-5, 2.3446428135935786, 0.783058127856357, 5.1663244572619504e-5, 0.0003085176075472429]
,[-2482.6337611231993, -6.465042758918571e-6, 2.3445955660448567, 0.7828371755625432, 3.231653972202153e-7, 3.7116767128697603e-6]
,[-2482.6231372602747, -1.1549633157414974e-5, 2.344726710643522, 0.7835322706245458, 0.0001240963196558198, 0.0013689908121813366]
,[3.573962885639048e-7, 1.170832319985493e-9, 2.9928250289429372, 0.581232655178282, -1.8456569605973527e-11, -3.5054181779514693e-12]
,[3.5742613135880674e-7, 1.1406768862798344e-9, 2.9928250289431513, 0.581232655179948, -1.6458168161648246e-11, -1.5631940186722204e-12]
,[-2482.629835457621, -3.7238658023852622e-6, 2.3446438477961014, 0.7830628612370012, 4.599910140279384e-5, 0.0003149505750040804]
,[-2482.63376587363, 5.2316336834223875e-5, 2.3445959633568467, 0.7828390103861299, 4.1183811061440423e-7, 6.320862976361141e-6]
,[-2482.629830282202, -3.5526501278582145e-6, 2.3446438680161057, 0.7830661186871911, 4.6011045613525425e-5, 0.0003404308712403603]
,[3.574384095372807e-7, 1.1410321576477145e-9, 2.992825028942965, 0.5812326551784707, -1.6035284211568523e-11, -2.319255898441952e-12]
,[3.5741661008614756e-7, 1.1407621514081256e-9, 2.9928250289430194, 0.5812326551788939, -1.718736264422205e-11, -2.5049962104617407e-12]
,[-2482.6271134120484, -2.6993997707336348e-5, 2.344677520023728, 0.7832201894520145, 7.773443507097522e-5, 0.0005325589742124492]
,[-2482.633718501351, -4.4428816181607544e-9, 2.3445953697121897, 0.7828362552853386, 5.914641871829218e-7, 3.9010783905446544e-6]
,[-2482.627113459219, -6.228101099736705e-6, 2.3446775200256096, 0.7832290201629111, 7.773408735844978e-5, 0.000618167903475686]
,[2.2502831598103512e-8, 1.0605560873955255e-10, 2.992825028977847, 0.5812326551983205, 2.567945855957987e-12, 1.3732348591588561e-11]
,[1.5940656794555252e-8, 5.5791815611883067e-11, 2.992825028976066, 0.5812326551796412, -4.141131881851834e-13, 4.630740235711528e-13]
,[-2482.6269622181426, -2.9065526874205716e-5, 2.344679390374168, 0.7832289268297795, 7.949724021760751e-5, 0.000544636146377564]
,[-2482.6337867891643, -6.0049739872169994e-5, 2.344595377178155, 0.7828363133810606, 6.458524248742492e-8, 2.5494313716789563e-6]
,[-2482.6269622633095, -6.399655660516146e-6, 2.3446793903788263, 0.7832389899333172, 7.949688410546774e-5, 0.0006389956602845803]
,[5.186731755202345e-8, 1.7912782368512126e-10, 2.9928250289740337, 0.5812326551911103, 3.756328581516755e-12, 8.394729356098196e-12]
,[5.182232598599512e-8, 1.7746515368344262e-10, 2.9928250289757394, 0.5812326552046582, 3.772093748466432e-12, 1.8626877817951026e-11]
,[-2482.628759452764, -4.588336804545179e-5, 2.344638090076251, 0.7830361172242294, 5.251386288107618e-5, 0.0002781927115563798]
,[-2482.6337450639203, -1.132119493263417e-6, 2.3445955140662176, 0.7828369303973413, 4.3119657233692266e-7, 3.070651876102559e-6]
,[-2482.624189911036, -9.975271041184897e-6, 2.3447136876282055, 0.7834411631397314, 0.00011182195392300809, 0.001125178123437709]
,[5.186288376535231e-8, 1.800657400963246e-10, 2.992825028973208, 0.5812326551845267, 2.2631896356983816e-12, 3.739564213844915e-12]
,[2.834943302332249e-8, 9.812595180846984e-11, 2.992825028975294, 0.5812326551809547, -5.424882765225902e-12, 4.947153797729698e-13]
,[-2482.629919291861, -3.4921143452493197e-6, 2.344642811068806, 0.783058016464758, 4.5021834881309175e-5, 0.0003082627447523745]
,[-2482.634126780861, -2.9411261735390326e-5, 2.344595566046426, 0.7828371848574872, -2.5106556178489114e-6, 5.97408706048963e-6]
,[-2482.623137269395, -1.1550634653190173e-5, 2.344726710643515, 0.7835322706249537, 0.00012409624898690463, 0.001368990814777149]
,[3.8377464761651936e-8, 1.510329639131669e-10, 2.992825028974001, 0.5812326551788989, -2.701394663517931e-12, 2.357336548186595e-12]
,[5.1876867246392067e-8, 1.779767444531899e-10, 2.992825028975238, 0.5812326552006756, 6.106226635438361e-12, 1.5650813978140832e-11]
,[-2482.615093199825, -1.963165233576092e-5, 2.3448262429657563, 0.7839142756750942, 0.0002179098806680546, 0.0014892036254154917]
,[-2482.6332850757035, 7.267123481824456e-5, 2.34459596335685, 0.782839002794247, 4.137983894203501e-6, 8.415405635120443e-6]
,[-2482.6298302908435, -3.553631700015103e-6, 2.344643868016102, 0.7830661186876026, 4.601097864354031e-5, 0.0003404308715488913]
,[1.589333464835363e-8, 7.852918315620627e-11, 2.9928250289765668, 0.5812326551836143, -2.334576976181779e-12, 2.822853062411923e-12]
,[2.5304387918367865e-8, 8.733991307963151e-11, 2.992825028975826, 0.5812326551835987, 4.226619054747971e-13, 3.3490987760842472e-12]]


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
    #PythonGrad[PythonGrad<1e-5]=0
    #JuliaGrad[JuliaGrad<1e-5]=0
    
    #print("PythonGrad = " , PythonGrad)
    #print("JuliaGrad = " , JuliaGrad)
    #print("JuliaManGrad = " , JuliaManGrad[testCaseIndex])
    
    print("diffGradPyJu = " ,    np.linalg.norm(JuliaGrad-PythonGrad)/np.linalg.norm(PythonGrad))
    print("diffGradPyJuMan = " , np.linalg.norm(JuliaManGrad[testCaseIndex]-PythonGrad)/np.linalg.norm(PythonGrad))
    print("diffGradJuJuMan = " , np.linalg.norm(JuliaManGrad[testCaseIndex]-JuliaGrad)/np.linalg.norm(JuliaGrad))
    
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
    #print("PythonHess = " , PythonHess)
    #print("JuliaHess = " , JuliaHess)
    #print("diffHess = " , np.linalg.norm(JuliaHess-PythonHess)/np.linalg.norm(PythonHess))

