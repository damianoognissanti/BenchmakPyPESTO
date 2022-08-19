#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022_x.h"
#include "Test_Cvijoviclab2022_p.h"
#include "Test_Cvijoviclab2022_w.h"
#include "Test_Cvijoviclab2022_dwdx.h"

namespace amici {
namespace model_Test_Cvijoviclab2022 {

void dydx_Test_Cvijoviclab2022(realtype *dydx, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *dwdx){
    dydx[0] = 1;
    dydx[3] = 1;
}

} // namespace model_Test_Cvijoviclab2022
} // namespace amici
