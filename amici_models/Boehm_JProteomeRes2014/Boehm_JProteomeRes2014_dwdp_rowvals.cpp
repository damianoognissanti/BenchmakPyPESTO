#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 10> dwdp_rowvals_Boehm_JProteomeRes2014_ = {
    0, 8, 7, 9, 5, 4, 6, 1, 2, 3
};

void dwdp_rowvals_Boehm_JProteomeRes2014(SUNMatrixWrapper &dwdp){
    dwdp.set_indexvals(gsl::make_span(dwdp_rowvals_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
