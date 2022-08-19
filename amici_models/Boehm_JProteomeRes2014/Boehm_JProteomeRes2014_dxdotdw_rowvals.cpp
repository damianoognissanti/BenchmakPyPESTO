#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 20> dxdotdw_rowvals_Boehm_JProteomeRes2014_ = {
    0, 3, 0, 1, 2, 1, 4, 3, 5, 2, 6, 4, 7, 0, 5, 0, 1, 6, 1, 7
};

void dxdotdw_rowvals_Boehm_JProteomeRes2014(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexvals(gsl::make_span(dxdotdw_rowvals_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
