#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x_rdata.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void x_solver_Boehm_JProteomeRes2014(realtype *x_solver, const realtype *x_rdata){
    x_solver[0] = STAT5A;
    x_solver[1] = STAT5B;
    x_solver[2] = pApB;
    x_solver[3] = pApA;
    x_solver[4] = pBpB;
    x_solver[5] = nucpApA;
    x_solver[6] = nucpApB;
    x_solver[7] = nucpBpB;
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
