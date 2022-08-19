#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"
#include "Boehm_JProteomeRes2014_dwdx.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dydx_Boehm_JProteomeRes2014(realtype *dydx, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *dwdx){
    dydx[0] = -specC17*(200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 + 2*pApA*specC17 + pApB, 2);
    dydx[2] = -specC17*(100*STAT5A*specC17 + 200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2) + 100*specC17/(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1));
    dydx[4] = -(-100*pApB + 200*pBpB*(specC17 - 1))*(specC17 - 1)/std::pow(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1), 2);
    dydx[5] = -(1 - specC17)*(100*STAT5A*specC17 + 200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2);
    dydx[6] = (-200*pApA*specC17 - 100*pApB)/std::pow(STAT5A*specC17 + 2*pApA*specC17 + pApB, 2) + 100/(STAT5A*specC17 + 2*pApA*specC17 + pApB);
    dydx[7] = (-100*pApB + 200*pBpB*(specC17 - 1))/std::pow(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1), 2) - 100/(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1));
    dydx[8] = (-200*STAT5A*specC17 - 400*pApA*specC17 - 200*pApB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2) + 100/(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1));
    dydx[9] = -2*specC17*(200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 + 2*pApA*specC17 + pApB, 2) + 200*specC17/(STAT5A*specC17 + 2*pApA*specC17 + pApB);
    dydx[11] = -2*specC17*(100*STAT5A*specC17 + 200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2) + 200*specC17/(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1));
    dydx[13] = -(-100*pApB + 200*pBpB*(specC17 - 1))*(2*specC17 - 2)/std::pow(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1), 2) + (200*specC17 - 200)/(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1));
    dydx[14] = -(2 - 2*specC17)*(100*STAT5A*specC17 + 200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2);
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
