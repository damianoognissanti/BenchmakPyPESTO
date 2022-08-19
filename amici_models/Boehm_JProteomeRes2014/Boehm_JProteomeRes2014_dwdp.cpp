#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"
#include "Boehm_JProteomeRes2014_dwdp.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dwdp_Boehm_JProteomeRes2014(realtype *dwdp, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *tcl, const realtype *dtcldp){
    dBaF3_Epo_dEpo_degradation_BaF3 = -1.2499999999999999e-7*t*std::exp(-Epo_degradation_BaF3*t);  // dwdp[0]
    dflux_v8_v_7_dk_exp_hetero = 0.45000000000000001*nucpApB;  // dwdp[1]
    dflux_v7_v_6_dk_exp_homo = 0.45000000000000001*nucpApA;  // dwdp[2]
    dflux_v9_v_8_dk_exp_homo = 0.45000000000000001*nucpBpB;  // dwdp[3]
    dflux_v5_v_4_dk_imp_hetero = 1.3999999999999999*pApB;  // dwdp[4]
    dflux_v4_v_3_dk_imp_homo = 1.3999999999999999*pApA;  // dwdp[5]
    dflux_v6_v_5_dk_imp_homo = 1.3999999999999999*pBpB;  // dwdp[6]
    dflux_v1_v_0_dk_phos = 1.3999999999999999*BaF3_Epo*std::pow(STAT5A, 2);  // dwdp[7]
    dflux_v2_v_1_dk_phos = 1.3999999999999999*BaF3_Epo*STAT5A*STAT5B;  // dwdp[8]
    dflux_v3_v_2_dk_phos = 1.3999999999999999*BaF3_Epo*std::pow(STAT5B, 2);  // dwdp[9]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
