#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 10> dwdx_rowvals_Boehm_JProteomeRes2014_ = {
    1, 2, 2, 3, 5, 4, 6, 7, 8, 9
};

void dwdx_rowvals_Boehm_JProteomeRes2014(SUNMatrixWrapper &dwdx){
    dwdx.set_indexvals(gsl::make_span(dwdx_rowvals_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
