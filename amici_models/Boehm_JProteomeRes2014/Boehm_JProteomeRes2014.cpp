#include "Boehm_JProteomeRes2014.h"
#include <array>

namespace amici {

namespace model_Boehm_JProteomeRes2014 {

std::array<const char*, 11> parameterNames = {
    "Epo_degradation_BaF3", // p[0]
"k_exp_hetero", // p[1]
"k_exp_homo", // p[2]
"k_imp_hetero", // p[3]
"k_imp_homo", // p[4]
"k_phos", // p[5]
"ratio", // p[6]
"specC17", // p[7]
"noiseParameter1_pSTAT5A_rel", // p[8]
"noiseParameter1_pSTAT5B_rel", // p[9]
"noiseParameter1_rSTAT5A_rel", // p[10]
};

std::array<const char*, 0> fixedParameterNames = {
    
};

std::array<const char*, 8> stateNames = {
    "STAT5A", // x_rdata[0]
"STAT5B", // x_rdata[1]
"pApB", // x_rdata[2]
"pApA", // x_rdata[3]
"pBpB", // x_rdata[4]
"nucpApA", // x_rdata[5]
"nucpApB", // x_rdata[6]
"nucpBpB", // x_rdata[7]
};

std::array<const char*, 3> observableNames = {
    "", // y[0]
"", // y[1]
"", // y[2]
};

std::array<const ObservableScaling, 3> observableScalings = {
    ObservableScaling::lin, // y[0]
ObservableScaling::lin, // y[1]
ObservableScaling::lin, // y[2]
};

std::array<const char*, 10> expressionNames = {
    "BaF3_Epo", // w[0]
"flux_v1_v_0", // w[1]
"flux_v2_v_1", // w[2]
"flux_v3_v_2", // w[3]
"flux_v4_v_3", // w[4]
"flux_v5_v_4", // w[5]
"flux_v6_v_5", // w[6]
"flux_v7_v_6", // w[7]
"flux_v8_v_7", // w[8]
"flux_v9_v_8", // w[9]
};

std::array<const char*, 11> parameterIds = {
    "Epo_degradation_BaF3", // p[0]
"k_exp_hetero", // p[1]
"k_exp_homo", // p[2]
"k_imp_hetero", // p[3]
"k_imp_homo", // p[4]
"k_phos", // p[5]
"ratio", // p[6]
"specC17", // p[7]
"noiseParameter1_pSTAT5A_rel", // p[8]
"noiseParameter1_pSTAT5B_rel", // p[9]
"noiseParameter1_rSTAT5A_rel", // p[10]
};

std::array<const char*, 0> fixedParameterIds = {
    
};

std::array<const char*, 8> stateIds = {
    "STAT5A", // x_rdata[0]
"STAT5B", // x_rdata[1]
"pApB", // x_rdata[2]
"pApA", // x_rdata[3]
"pBpB", // x_rdata[4]
"nucpApA", // x_rdata[5]
"nucpApB", // x_rdata[6]
"nucpBpB", // x_rdata[7]
};

std::array<const char*, 3> observableIds = {
    "pSTAT5A_rel", // y[0]
"pSTAT5B_rel", // y[1]
"rSTAT5A_rel", // y[2]
};

std::array<const char*, 10> expressionIds = {
    "BaF3_Epo", // w[0]
"flux_v1_v_0", // w[1]
"flux_v2_v_1", // w[2]
"flux_v3_v_2", // w[3]
"flux_v4_v_3", // w[4]
"flux_v5_v_4", // w[5]
"flux_v6_v_5", // w[6]
"flux_v7_v_6", // w[7]
"flux_v8_v_7", // w[8]
"flux_v9_v_8", // w[9]
};

std::array<int, 8> stateIdxsSolver = {
    0, 1, 2, 3, 4, 5, 6, 7
};

std::array<bool, 0> rootInitialValues = {
    
};

} // namespace model_Boehm_JProteomeRes2014

} // namespace amici
