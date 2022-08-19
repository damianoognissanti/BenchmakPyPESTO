#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022_x.h"
#include "Test_Cvijoviclab2022_p.h"

namespace amici {
namespace model_Test_Cvijoviclab2022 {

void x_rdata_Test_Cvijoviclab2022(realtype *x_rdata, const realtype *x, const realtype *tcl, const realtype *p, const realtype *k){
    x_rdata[0] = sebastian;
    x_rdata[1] = damiano;
}

} // namespace model_Test_Cvijoviclab2022
} // namespace amici
