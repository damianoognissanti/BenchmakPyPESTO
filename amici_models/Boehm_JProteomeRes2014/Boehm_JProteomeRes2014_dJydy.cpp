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
#include "Boehm_JProteomeRes2014_dJydy.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dJydy_Boehm_JProteomeRes2014(realtype *dJydy, const int iy, const realtype *p, const realtype *k, const realtype *y, const realtype *sigmay, const realtype *my){
    switch(iy) {
        case 0:
            dJydy[0] = (-1.0*mpSTAT5A_rel + 1.0*pSTAT5A_rel)/std::pow(sigma_pSTAT5A_rel, 2);
            break;
        case 1:
            dJydy[0] = (-1.0*mpSTAT5B_rel + 1.0*pSTAT5B_rel)/std::pow(sigma_pSTAT5B_rel, 2);
            break;
        case 2:
            dJydy[0] = (-1.0*mrSTAT5A_rel + 1.0*rSTAT5A_rel)/std::pow(sigma_rSTAT5A_rel, 2);
            break;
    }
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
