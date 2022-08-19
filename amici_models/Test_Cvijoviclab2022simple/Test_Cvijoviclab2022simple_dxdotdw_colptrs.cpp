#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

static constexpr std::array<sunindextype, 3> dxdotdw_colptrs_Test_Cvijoviclab2022simple_ = {
    0, 1, 2
};

void dxdotdw_colptrs_Test_Cvijoviclab2022simple(SUNMatrixWrapper &dxdotdw){
    dxdotdw.set_indexptrs(gsl::make_span(dxdotdw_colptrs_Test_Cvijoviclab2022simple_));
}
} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
