#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022_p.h"
#include "Test_Cvijoviclab2022_y.h"
#include "Test_Cvijoviclab2022_sigmay.h"
#include "Test_Cvijoviclab2022_my.h"

namespace amici {
namespace model_Test_Cvijoviclab2022 {

void Jy_Test_Cvijoviclab2022(realtype *Jy, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_sebastian_measurement, 2)) + 0.5*std::pow(-msebastian_measurement + sebastian_measurement, 2)/std::pow(sigma_sebastian_measurement, 2);
            break;
        case 1:
            Jy[0] = 0.5*std::log(2*amici::pi*std::pow(sigma_damiano_measurement, 2)) + 0.5*std::pow(damiano_measurement - mdamiano_measurement, 2)/std::pow(sigma_damiano_measurement, 2);
            break;
    }
}

} // namespace model_Test_Cvijoviclab2022
} // namespace amici
