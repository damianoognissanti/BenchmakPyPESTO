#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 3> dwdw_rowvals_Boehm_JProteomeRes2014_ = {
    1, 2, 3
};

void dwdw_rowvals_Boehm_JProteomeRes2014(SUNMatrixWrapper &dwdw){
    dwdw.set_indexvals(gsl::make_span(dwdw_rowvals_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
