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

void y_Test_Cvijoviclab2022simple(realtype *y, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w){
    y[0] = sebastian;
    y[1] = damiano;
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
