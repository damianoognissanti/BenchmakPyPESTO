#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"
#include "Boehm_JProteomeRes2014_xdot.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void xdot_Boehm_JProteomeRes2014(realtype *xdot, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    xdot0 = -1.4285714285714286*flux_v1_v_0 - 0.7142857142857143*flux_v2_v_1 + 1.4285714285714286*flux_v7_v_6 + 0.7142857142857143*flux_v8_v_7;  // xdot[0]
    xdot1 = -0.7142857142857143*flux_v2_v_1 - 1.4285714285714286*flux_v3_v_2 + 0.7142857142857143*flux_v8_v_7 + 1.4285714285714286*flux_v9_v_8;  // xdot[1]
    xdot2 = 0.7142857142857143*flux_v2_v_1 - 0.7142857142857143*flux_v5_v_4;  // xdot[2]
    xdot3 = 0.7142857142857143*flux_v1_v_0 - 0.7142857142857143*flux_v4_v_3;  // xdot[3]
    xdot4 = 0.7142857142857143*flux_v3_v_2 - 0.7142857142857143*flux_v6_v_5;  // xdot[4]
    xdot5 = 2.2222222222222223*flux_v4_v_3 - 2.2222222222222223*flux_v7_v_6;  // xdot[5]
    xdot6 = 2.2222222222222223*flux_v5_v_4 - 2.2222222222222223*flux_v8_v_7;  // xdot[6]
    xdot7 = 2.2222222222222223*flux_v6_v_5 - 2.2222222222222223*flux_v9_v_8;  // xdot[7]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
