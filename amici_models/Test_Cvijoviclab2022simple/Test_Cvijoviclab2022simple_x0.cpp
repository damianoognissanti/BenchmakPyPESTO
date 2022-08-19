#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_p.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void x0_Test_Cvijoviclab2022simple(realtype *x0, const realtype t, const realtype *p, const realtype *k){
    x0[0] = 8.0;
    x0[1] = 4.0;
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
