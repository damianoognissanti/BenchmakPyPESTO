#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Test_Cvijoviclab2022simple_p.h"
#include "Test_Cvijoviclab2022simple_y.h"
#include "Test_Cvijoviclab2022simple_sigmay.h"

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

void sigmay_Test_Cvijoviclab2022simple(realtype *sigmay, const realtype t, const realtype *p, const realtype *k, const realtype *y){
    sigma_sebastian_measurement = noiseParameter1_sebastian_measurement;  // sigmay[0]
    sigma_damiano_measurement = noiseParameter1_damiano_measurement;  // sigmay[1]
}

} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
