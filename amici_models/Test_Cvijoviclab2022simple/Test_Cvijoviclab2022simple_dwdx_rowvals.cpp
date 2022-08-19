#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

static constexpr std::array<sunindextype, 2> dwdx_rowvals_Test_Cvijoviclab2022simple_ = {
    0, 1
};

void dwdx_rowvals_Test_Cvijoviclab2022simple(SUNMatrixWrapper &dwdx){
    dwdx.set_indexvals(gsl::make_span(dwdx_rowvals_Test_Cvijoviclab2022simple_));
}
} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
