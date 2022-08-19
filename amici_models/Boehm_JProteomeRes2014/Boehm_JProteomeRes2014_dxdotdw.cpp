#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"
#include "Boehm_JProteomeRes2014_dxdotdw.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dxdotdw_Boehm_JProteomeRes2014(realtype *dxdotdw, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    dxdot0_dflux_v1_v_0 = -1.4285714285714286;  // dxdotdw[0]
    dxdot3_dflux_v1_v_0 = 0.7142857142857143;  // dxdotdw[1]
    dxdot0_dflux_v2_v_1 = -0.7142857142857143;  // dxdotdw[2]
    dxdot1_dflux_v2_v_1 = -0.7142857142857143;  // dxdotdw[3]
    dxdot2_dflux_v2_v_1 = 0.7142857142857143;  // dxdotdw[4]
    dxdot1_dflux_v3_v_2 = -1.4285714285714286;  // dxdotdw[5]
    dxdot4_dflux_v3_v_2 = 0.7142857142857143;  // dxdotdw[6]
    dxdot3_dflux_v4_v_3 = -0.7142857142857143;  // dxdotdw[7]
    dxdot5_dflux_v4_v_3 = 2.2222222222222223;  // dxdotdw[8]
    dxdot2_dflux_v5_v_4 = -0.7142857142857143;  // dxdotdw[9]
    dxdot6_dflux_v5_v_4 = 2.2222222222222223;  // dxdotdw[10]
    dxdot4_dflux_v6_v_5 = -0.7142857142857143;  // dxdotdw[11]
    dxdot7_dflux_v6_v_5 = 2.2222222222222223;  // dxdotdw[12]
    dxdot0_dflux_v7_v_6 = 1.4285714285714286;  // dxdotdw[13]
    dxdot5_dflux_v7_v_6 = -2.2222222222222223;  // dxdotdw[14]
    dxdot0_dflux_v8_v_7 = 0.7142857142857143;  // dxdotdw[15]
    dxdot1_dflux_v8_v_7 = 0.7142857142857143;  // dxdotdw[16]
    dxdot6_dflux_v8_v_7 = -2.2222222222222223;  // dxdotdw[17]
    dxdot1_dflux_v9_v_8 = 1.4285714285714286;  // dxdotdw[18]
    dxdot7_dflux_v9_v_8 = -2.2222222222222223;  // dxdotdw[19]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
