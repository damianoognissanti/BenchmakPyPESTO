#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022 {

static constexpr std::array<sunindextype, 7> dwdp_colptrs_Test_Cvijoviclab2022_ = {
    0, 1, 2, 3, 4, 4, 4
};

void dwdp_colptrs_Test_Cvijoviclab2022(SUNMatrixWrapper &dwdp){
    dwdp.set_indexptrs(gsl::make_span(dwdp_colptrs_Test_Cvijoviclab2022_));
}
} // namespace model_Test_Cvijoviclab2022
} // namespace amici
