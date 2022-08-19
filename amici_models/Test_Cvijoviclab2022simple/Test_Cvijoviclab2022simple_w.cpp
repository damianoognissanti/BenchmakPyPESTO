#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_x.h"
#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_w.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void w_Test_Cvijoviclab2022simple(realtype *w, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *tcl){
    flux_v1_v_0 = alpha*sebastian;  // w[0]
    flux_v2_v_1 = beta*damiano;  // w[1]
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
