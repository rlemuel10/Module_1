
# The Calculator Package 

This project creates a 5-function calculator, which can add, subtract, multiply, divide, and the nth-root of a given number.  

## About

The calculator module can be initialized either with a number in memory, or zero as the default value. From there, each of of its methods can be called in order to add, subtract, multiply, or take the root of the number in memory. 
Upon completing each of these operations, the new number will be added to memory. If you'd like to clear the calculator's memory to start over with new numbers, you can simply use the reset_memory method and do whichever operations you choose. 

## Installation

Use the package manager [pip] (https://test.pypi.org/project/calculator-package-LR/0.0.1/) to install calculator

```bash
pip install pip install -i https://test.pypi.org/simple/ calculator-package-LR==0.0.1
```

## Usage

```python
from calculator import calculator

#initializes Calculator class. Defaults to zero, any number can be an arg
instance=Calculator()

# returns sum when given integer/float n
instance.add(n)

# returns difference when given integer/float n
instance.subtract(n)

# returns multiplication when given integer/float n 
instance.multiply(n)

#returns division when given when given integer/float n
instance.divide(n)

#returns n-th root when given when given integer/float n
instance.root(n)

#resets number in memory from last calculation
instance.reset_memory()

 
