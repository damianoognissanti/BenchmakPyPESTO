#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022 {

static constexpr std::array<sunindextype, 3> dxdotdw_colptrs_Test_Cvijoviclab2022_ = {
    0, 1, 2
};

void dxdotdw_colptrs_Test_Cvijoviclab2022(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexptrs(gsl::make_span(dxdotdw_colptrs_Test_Cvijoviclab2022_));
}
} // namespace model_Test_Cvijoviclab2022
} // namespace amici
