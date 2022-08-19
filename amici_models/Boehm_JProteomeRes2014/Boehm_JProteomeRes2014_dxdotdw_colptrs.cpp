#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 11> dxdotdw_colptrs_Boehm_JProteomeRes2014_ = {
    0, 0, 2, 5, 7, 9, 11, 13, 15, 18, 20
};

void dxdotdw_colptrs_Boehm_JProteomeRes2014(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexptrs(gsl::make_span(dxdotdw_colptrs_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
