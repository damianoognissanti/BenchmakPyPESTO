#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_y.h"
#include "Test_Cvijoviclab2022simple_sigmay.h"
#include "Test_Cvijoviclab2022simple_my.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void dJydsigma_Test_Cvijoviclab2022simple(realtype *dJydsigma, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydsigma[0] = 1.0/sigma_sebastian_measurement - 1.0*std::pow(-msebastian_measurement + sebastian_measurement, 2)/std::pow(sigma_sebastian_measurement, 3);
            break;
        case 1:
            dJydsigma[1] = 1.0/sigma_damiano_measurement - 1.0*std::pow(damiano_measurement - mdamiano_measurement, 2)/std::pow(sigma_damiano_measurement, 3);
            break;
    }
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
