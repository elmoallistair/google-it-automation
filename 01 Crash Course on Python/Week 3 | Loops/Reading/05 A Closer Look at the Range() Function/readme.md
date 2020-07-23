# A Closer Look at the Range() Function

Previously we had used the *range()* function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. But the *range()* function can do much more than that. We can pass in two parameters: the first specifying our starting point, the second specifying the end point. Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified.

The *range()* function can take a third parameter, too. This third parameter lets you  alter the size of each step. So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5.

To quickly recap the *range()* function when passing one, two, or three parameters:

* One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
* Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
* Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.