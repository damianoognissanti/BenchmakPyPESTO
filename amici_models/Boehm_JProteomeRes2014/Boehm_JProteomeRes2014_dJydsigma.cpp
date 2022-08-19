#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_y.h"
#include "Boehm_JProteomeRes2014_sigmay.h"
#include "Boehm_JProteomeRes2014_my.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dJydsigma_Boehm_JProteomeRes2014(realtype *dJydsigma, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydsigma[0] = 1.0/sigma_pSTAT5A_rel - 1.0*std::pow(-mpSTAT5A_rel + pSTAT5A_rel, 2)/std::pow(sigma_pSTAT5A_rel, 3);
            break;
        case 1:
            dJydsigma[1] = 1.0/sigma_pSTAT5B_rel - 1.0*std::pow(-mpSTAT5B_rel + pSTAT5B_rel, 2)/std::pow(sigma_pSTAT5B_rel, 3);
            break;
        case 2:
            dJydsigma[2] = 1.0/sigma_rSTAT5A_rel - 1.0*std::pow(-mrSTAT5A_rel + rSTAT5A_rel, 2)/std::pow(sigma_rSTAT5A_rel, 3);
            break;
    }
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
