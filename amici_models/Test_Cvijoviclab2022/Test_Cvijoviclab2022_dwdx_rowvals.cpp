#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022 {

static constexpr std::array<sunindextype, 4> dwdx_rowvals_Test_Cvijoviclab2022_ = {
    0, 1, 0, 1
};

void dwdx_rowvals_Test_Cvijoviclab2022(SUNMatrixWrapper &dwdx){
    dwdx.set_indexvals(gsl::make_span(dwdx_rowvals_Test_Cvijoviclab2022_));
}
} // namespace model_Test_Cvijoviclab2022
} // namespace amici
