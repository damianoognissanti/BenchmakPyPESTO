#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_x.h"
#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_w.h"
#include "Test_Cvijoviclab2022simple_dwdp.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void dwdp_Test_Cvijoviclab2022simple(realtype *dwdp, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *tcl, const realtype *dtcldp){
    dflux_v1_v_0_dalpha = sebastian;  // dwdp[0]
    dflux_v2_v_1_dbeta = damiano;  // dwdp[1]
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
