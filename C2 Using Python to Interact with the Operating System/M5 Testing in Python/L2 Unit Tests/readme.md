# Unit Test Cheat-Sheet

Frankly, the unit testing library for Python is fairly well documented, but it can be a bit of a dry read. Instead, we suggest covering the core module concepts, and then reading in more detail later.

## Best of Unit Testing Standard Library Module

### Understand a Basic Example:

* https://docs.python.org/3/library/unittest.html#basic-example

### Understand how to run the tests using the Command Line:

* https://docs.python.org/3/library/unittest.html#command-line-interface

### Understand various Unit Test Design Patterns:

* https://docs.python.org/3/library/unittest.html#organizing-test-code
* Understand the uses of setUp, tearDown; setUpModule and tearDownModule

### Understand basic assertions:

|           Method          |      Checks that     | New in |
|:-------------------------:|:--------------------:|:------:|
| assertEqual(a, b)         | a == b               |        |
| assertNotEqual(a, b)      | a != b               |        |
| assertTrue(x)             | bool(x) is True      |        |
| assertFalse(x)            | bool(x) is False     |        |
| assertIs(a, b)            | a is b               | 3.1    |
| assertIsNot(a, b)         | a is not b           | 3.1    |
| assertIsNone(x)           | x is None            | 3.1    |
| assertIsNotNone(x)        | x is not None        | 3.1    |
| assertIn(a, b)            | a in b               | 3.1    |
| assertNotIn(a, b)         | a not in b           | 3.1    |
| assertIsInstance(a, b)    | isinstance(a, b)     | 3.2    |
| assertNotIsInstance(a, b) | not isinstance(a, b) | 3.2    |

### Understand more specific assertions such as assertRaises

* https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises