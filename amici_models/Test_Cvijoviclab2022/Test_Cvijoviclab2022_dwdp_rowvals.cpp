#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022 {

static constexpr std::array<sunindextype, 4> dwdp_rowvals_Test_Cvijoviclab2022_ = {
    0, 0, 1, 1
};

void dwdp_rowvals_Test_Cvijoviclab2022(SUNMatrixWrapper &dwdp){
    dwdp.set_indexvals(gsl::make_span(dwdp_rowvals_Test_Cvijoviclab2022_));
}
} // namespace model_Test_Cvijoviclab2022
} // namespace amici
