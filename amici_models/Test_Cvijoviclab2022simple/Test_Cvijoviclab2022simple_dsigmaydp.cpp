#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_y.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void dsigmaydp_Test_Cvijoviclab2022simple(realtype *dsigmaydp, const realtype t, const realtype *p, const realtype *k, const realtype *y, const int ip){
    switch(ip) {
        case 2:
            dsigmaydp[0] = 1;
            break;
        case 3:
            dsigmaydp[1] = 1;
            break;
    }
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
