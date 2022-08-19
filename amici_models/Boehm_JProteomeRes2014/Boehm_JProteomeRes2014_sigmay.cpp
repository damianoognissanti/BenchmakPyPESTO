#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_y.h"
#include "Boehm_JProteomeRes2014_sigmay.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void sigmay_Boehm_JProteomeRes2014(realtype *sigmay, const realtype t, const realtype *p, const realtype *k, const realtype *y){
    sigma_pSTAT5A_rel = noiseParameter1_pSTAT5A_rel;  // sigmay[0]
    sigma_pSTAT5B_rel = noiseParameter1_pSTAT5B_rel;  // sigmay[1]
    sigma_rSTAT5A_rel = noiseParameter1_rSTAT5A_rel;  // sigmay[2]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
