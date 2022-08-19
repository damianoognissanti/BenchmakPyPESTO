"""AMICI-generated module for model Test_Cvijoviclab2022simple"""

import amici
from pathlib import Path

# Ensure we are binary-compatible, see #556
if '0.11.32' != amici.__version__:
    raise amici.AmiciVersionError(
        f'Cannot use model `Test_Cvijoviclab2022simple` in {Path(__file__).parent}, '
        'generated with amici==0.11.32, '
        f'together with amici=={amici.__version__} '
        'which is currently installed. To use this model, install '
        'amici==0.11.32 or re-import the model with the amici '
        'version currently installed.'
    )

from Test_Cvijoviclab2022simple._Test_Cvijoviclab2022simple import *

__version__ = '0.1.0'
