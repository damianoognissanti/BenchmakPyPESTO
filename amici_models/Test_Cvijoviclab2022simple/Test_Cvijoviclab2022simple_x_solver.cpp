#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_x_rdata.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void x_solver_Test_Cvijoviclab2022simple(realtype *x_solver, const realtype *x_rdata){
    x_solver[0] = sebastian;
    x_solver[1] = damiano;
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
