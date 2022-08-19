#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void w_Boehm_JProteomeRes2014(realtype *w, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *tcl){
    BaF3_Epo = 1.2499999999999999e-7*std::exp(-Epo_degradation_BaF3*t);  // w[0]
    flux_v1_v_0 = 1.3999999999999999*BaF3_Epo*std::pow(STAT5A, 2)*k_phos;  // w[1]
    flux_v2_v_1 = 1.3999999999999999*BaF3_Epo*STAT5A*STAT5B*k_phos;  // w[2]
    flux_v3_v_2 = 1.3999999999999999*BaF3_Epo*std::pow(STAT5B, 2)*k_phos;  // w[3]
    flux_v4_v_3 = 1.3999999999999999*k_imp_homo*pApA;  // w[4]
    flux_v5_v_4 = 1.3999999999999999*k_imp_hetero*pApB;  // w[5]
    flux_v6_v_5 = 1.3999999999999999*k_imp_homo*pBpB;  // w[6]
    flux_v7_v_6 = 0.45000000000000001*k_exp_homo*nucpApA;  // w[7]
    flux_v8_v_7 = 0.45000000000000001*k_exp_hetero*nucpApB;  // w[8]
    flux_v9_v_8 = 0.45000000000000001*k_exp_homo*nucpBpB;  // w[9]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
