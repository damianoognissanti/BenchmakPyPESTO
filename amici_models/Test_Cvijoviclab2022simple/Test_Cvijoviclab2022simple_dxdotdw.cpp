#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_x.h"
#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_w.h"
#include "Test_Cvijoviclab2022simple_dxdotdw.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void dxdotdw_Test_Cvijoviclab2022simple(realtype *dxdotdw, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    dxdot0_dflux_v1_v_0 = 1.0;  // dxdotdw[0]
    dxdot1_dflux_v2_v_1 = 1.0;  // dxdotdw[1]
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
