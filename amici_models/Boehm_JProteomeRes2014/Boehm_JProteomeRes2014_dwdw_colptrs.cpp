#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Boehm_JProteomeRes2014 {

static constexpr std::array<sunindextype, 11> dwdw_colptrs_Boehm_JProteomeRes2014_ = {
    0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
};

void dwdw_colptrs_Boehm_JProteomeRes2014(SUNMatrixWrapper &dwdw){
    dwdw.set_indexptrs(gsl::make_span(dwdw_colptrs_Boehm_JProteomeRes2014_));
}
} // namespace model_Boehm_JProteomeRes2014
} // namespace amici
