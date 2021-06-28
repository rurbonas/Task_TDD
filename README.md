**TDD Task**
- Create a new Repo on gihub
- Create a new project in pycharm
- name tdd_test_task
- create a TDD diagram
- create a file to write tests
- create a file to write code
- implement sudo coding
- create a README to document the steps to successfully achieve the task

![TDD](https://developer.ibm.com/developer/default/articles/5-steps-of-test-driven-development/images/tdd-red-green-refactoring-v3.png)

- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test
- create a test case to calculate % and code to pass the test
- create a test to check if the given values are positive 
- create a method in the class to pass the test

**Testing**
```python
import unittest
import pytest

from tdd_code import SimpleCode

class Calctest(unittest.TestCase):
    calc = SimpleCode()

# create a test to check is the number divisible/remainder 0 if True pass the test if False fail
    def test_is_div_int(self):
        self.assertEqual(self.calc.is_div_int(4,2) ,0)

# create a test case to calculate % and code to pass the test
    def test_percent(self):
        self.assertEqual(self.calc.percent(150,20) ,30)

# create a test to check if the given values are positive
    def test_positive(self):
        self.assertEqual(self.calc.positive(15), True)
```
**Code**
```python
# create a class and method to write code to pass the test
# create a method in the class to pass the test

class SimpleCode:
    def is_div_int(self, num1, num2):
        return num1 % num2

    def percent(self, num1, num2):
        return (num1 / 100) * num2

    def positive(self, num1):
        return num1 > 0
```
