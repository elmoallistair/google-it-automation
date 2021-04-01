#!/usr/bin/env python3

import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted(fruit.items())
# Output: sorted(fruit.items())

sorted(fruit.items(), key=operator.itemgetter(0))
# Output: [('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

sorted(fruit.items(), key=operator.itemgetter(1))
# Output: [('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)
# Output: [('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]