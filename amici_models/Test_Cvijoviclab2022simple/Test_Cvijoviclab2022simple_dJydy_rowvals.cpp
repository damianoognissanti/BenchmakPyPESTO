#include "amici/sundials_matrix_wrapper.h"
#include "sundials/sundials_types.h"

#include <array>
#include <algorithm>

namespace amici {
namespace model_Test_Cvijoviclab2022simple {

static constexpr std::array<std::array<sunindextype, 1>, 2> dJydy_rowvals_Test_Cvijoviclab2022simple_ = {{
    {0}, 
    {0}, 
}};

void dJydy_rowvals_Test_Cvijoviclab2022simple(SUNMatrixWrapper &dJydy, int index){
    dJydy.set_indexvals(gsl::make_span(dJydy_rowvals_Test_Cvijoviclab2022simple_[index]));
}
} // namespace model_Test_Cvijoviclab2022simple
} // namespace amici
