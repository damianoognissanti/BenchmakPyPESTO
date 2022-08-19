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

void dydp_Boehm_JProteomeRes2014(realtype *dydp, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const int ip, const realtype *w, const realtype *tcl, const realtype *dtcldp){
    switch(ip) {
        case 7:
            dydp[0] = 200*pApA/(STAT5A*specC17 + 2*pApA*specC17 + pApB) - (STAT5A + 2*pApA)*(200*pApA*specC17 + 100*pApB)/std::pow(STAT5A*specC17 + 2*pApA*specC17 + pApB, 2);
            dydp[1] = 200*pBpB/(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1)) - (STAT5B + 2*pBpB)*(-100*pApB + 200*pBpB*(specC17 - 1))/std::pow(STAT5B*(specC17 - 1) - pApB + 2*pBpB*(specC17 - 1), 2);
            dydp[2] = (100*STAT5A + 200*pApA)/(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1)) - (100*STAT5A*specC17 + 200*pApA*specC17 + 100*pApB)*(STAT5A - STAT5B + 2*pApA - 2*pBpB)/std::pow(STAT5A*specC17 - STAT5B*(specC17 - 1) + 2*pApA*specC17 + 2*pApB - 2*pBpB*(specC17 - 1), 2);
            break;
    }
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
