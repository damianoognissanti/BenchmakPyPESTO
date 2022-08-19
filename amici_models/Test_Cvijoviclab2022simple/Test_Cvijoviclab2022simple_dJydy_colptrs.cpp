#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

static constexpr std::array<std::array<sunindextype, 3>, 2> dJydy_colptrs_Test_Cvijoviclab2022simple_ = {{
    {0, 1, 1}, 
    {0, 0, 1}, 
}};

void dJydy_colptrs_Test_Cvijoviclab2022simple(SUNMatrixWrapper &dJydy, int index){
    dJydy.set_indexptrs(gsl::make_span(dJydy_colptrs_Test_Cvijoviclab2022simple_[index]));
}
} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
