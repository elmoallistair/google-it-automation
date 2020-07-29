# While Loops

<br>

## Video: What is a while loop?

```
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))
```

How many times will "Not there yet" be printed?

> 5

<br>

## Video: More while Loop Examples

Can you work out what this function does? Try passing different parameters to the attempts function to see what it does. 

```
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(3)
```

Output:

```
Attempt 1
Attempt 2
Attempt 3
Done
```

<br>

## Video: Why Initializing Variables Matters

In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?

```
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
```

Output:

```
3
2
1
Zero!
```

<br>

## Video: Infinite Loops and How to Break Them

The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

```
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
        n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
```

Output:

```
1
2
3
4
5
```