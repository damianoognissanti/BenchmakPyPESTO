#include "Test_Cvijoviclab2022simple.h"
#include <array>

namespace amici {

namespace model_Test_Cvijoviclab2022simple {

std::array<const char*, 4> parameterNames = {
    "alpha", // p[0]
"beta", // p[1]
"noiseParameter1_sebastian_measurement", // p[2]
"noiseParameter1_damiano_measurement", // p[3]
};

std::array<const char*, 0> fixedParameterNames = {
    
};

std::array<const char*, 2> stateNames = {
    "sebastian", // x_rdata[0]
"damiano", // x_rdata[1]
};

std::array<const char*, 2> observableNames = {
    "", // y[0]
"", // y[1]
};

std::array<const ObservableScaling, 2> observableScalings = {
    ObservableScaling::lin, // y[0]
ObservableScaling::lin, // y[1]
};

std::array<const char*, 2> expressionNames = {
    "flux_v1_v_0", // w[0]
"flux_v2_v_1", // w[1]
};

std::array<const char*, 4> parameterIds = {
    "alpha", // p[0]
"beta", // p[1]
"noiseParameter1_sebastian_measurement", // p[2]
"noiseParameter1_damiano_measurement", // p[3]
};

std::array<const char*, 0> fixedParameterIds = {
    
};

std::array<const char*, 2> stateIds = {
    "sebastian", // x_rdata[0]
"damiano", // x_rdata[1]
};

std::array<const char*, 2> observableIds = {
    "sebastian_measurement", // y[0]
"damiano_measurement", // y[1]
};

std::array<const char*, 2> expressionIds = {
    "flux_v1_v_0", // w[0]
"flux_v2_v_1", // w[1]
};

std::array<int, 2> stateIdxsSolver = {
    0, 1
};

std::array<bool, 0> rootInitialValues = {
    
};

} // namespace model_Test_Cvijoviclab2022simple

} // namespace amici
