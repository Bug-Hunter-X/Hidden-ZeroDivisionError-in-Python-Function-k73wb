# Hidden ZeroDivisionError Bug
This repository demonstrates a subtle bug involving a ZeroDivisionError that is not immediately obvious in a Python function. The issue arises from the order of conditional statements and the way zero values are handled. 

The `bug.py` file contains the erroneous code, while `bugSolution.py` provides a corrected version.

The problem is particularly tricky because the typical expectation is that a division-by-zero error will always occur when dividing by zero. However, the conditional logic masks the error in a specific case.