#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void sx0_Boehm_JProteomeRes2014(realtype *sx0, const realtype t, const realtype *x, const realtype *p, const realtype *k, const int ip){
    switch(ip) {
        case 6:
            sx0[0] = 207.59999999999999;
            sx0[1] = -207.59999999999999;
            break;
    }
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
