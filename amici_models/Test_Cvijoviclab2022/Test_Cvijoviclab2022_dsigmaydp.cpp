#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022_p.h"
#include "Test_Cvijoviclab2022_y.h"

namespace amici {
namespace model_Test_Cvijoviclab2022 {

void dsigmaydp_Test_Cvijoviclab2022(realtype *dsigmaydp, const realtype t, const realtype *p, const realtype *k, const realtype *y, const int ip){
    switch(ip) {
        case 4:
            dsigmaydp[0] = 1;
            break;
        case 5:
            dsigmaydp[1] = 1;
            break;
    }
}

} // namespace model_Test_Cvijoviclab2022
} // namespace amici
