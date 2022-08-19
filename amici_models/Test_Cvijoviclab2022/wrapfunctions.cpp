#include "amici/model.h"
#include "wrapfunctions.h"
#include "Test_Cvijoviclab2022.h"

namespace amici {
namespace generic_model {

std::unique_ptr<amici::Model> getModel() {
    return std::unique_ptr<amici::Model>(
        new amici::model_Test_Cvijoviclab2022::Model_Test_Cvijoviclab2022());
}


} // namespace generic_model

} // namespace amici
