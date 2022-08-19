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

void x_rdata_Boehm_JProteomeRes2014(realtype *x_rdata, const realtype *x, const realtype *tcl, const realtype *p, const realtype *k){
    x_rdata[0] = STAT5A;
    x_rdata[1] = STAT5B;
    x_rdata[2] = pApB;
    x_rdata[3] = pApA;
    x_rdata[4] = pBpB;
    x_rdata[5] = nucpApA;
    x_rdata[6] = nucpApB;
    x_rdata[7] = nucpBpB;
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
