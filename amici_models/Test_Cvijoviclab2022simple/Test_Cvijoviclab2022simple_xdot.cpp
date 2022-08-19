#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_x.h"
#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_w.h"
#include "Test_Cvijoviclab2022simple_xdot.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void xdot_Test_Cvijoviclab2022simple(realtype *xdot, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    xdot0 = 1.0*flux_v1_v_0;  // xdot[0]
    xdot1 = 1.0*flux_v2_v_1;  // xdot[1]
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
