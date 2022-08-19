#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022 {

static constexpr std::array<sunindextype, 3> dwdx_colptrs_Test_Cvijoviclab2022_ = {
    0, 2, 4
};

void dwdx_colptrs_Test_Cvijoviclab2022(SUNMatrixWrapper &dwdx){
    dwdx.set_indexptrs(gsl::make_span(dwdx_colptrs_Test_Cvijoviclab2022_));
}
} // namespace model_Test_Cvijoviclab2022
} // namespace amici
