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
#include "Test_Cvijoviclab2022_dJydy.h"

namespace amici {
namespace model_Test_Cvijoviclab2022 {

void dJydy_Test_Cvijoviclab2022(realtype *dJydy, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydy[0] = (-1.0*msebastian_measurement + 1.0*sebastian_measurement)/std::pow(sigma_sebastian_measurement, 2);
            break;
        case 1:
            dJydy[0] = (1.0*damiano_measurement - 1.0*mdamiano_measurement)/std::pow(sigma_damiano_measurement, 2);
            break;
    }
}

} // namespace model_Test_Cvijoviclab2022
} // namespace amici
