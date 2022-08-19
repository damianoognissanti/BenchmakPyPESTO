#include "amici/symbolic_functions.h"
#include "amici/defines.h"
#include "sundials/sundials_types.h"

#include <gsl/gsl-lite.hpp>
#include <array>
#include <algorithm>

#include "Boehm_JProteomeRes2014_x.h"
#include "Boehm_JProteomeRes2014_p.h"
#include "Boehm_JProteomeRes2014_w.h"
#include "Boehm_JProteomeRes2014_dwdw.h"

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

void dwdw_Boehm_JProteomeRes2014(realtype *dwdw, const realtype t, const realtype *x, const realtype *p, const realtype *k, const realtype *h, const realtype *w, const realtype *tcl){
    dflux_v1_v_0_dBaF3_Epo = 1.3999999999999999*std::pow(STAT5A, 2)*k_phos;  // dwdw[0]
    dflux_v2_v_1_dBaF3_Epo = 1.3999999999999999*STAT5A*STAT5B*k_phos;  // dwdw[1]
    dflux_v3_v_2_dBaF3_Epo = 1.3999999999999999*std::pow(STAT5B, 2)*k_phos;  // dwdw[2]
}

} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
