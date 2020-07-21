# Reading and Writing Files

## Reading Files

What is the difference between the readline() and read() methods?

* The readline() method starts from the current position, while the read() method reads the whole file.
* The read() method reads a single line, the readline() method reads the whole file.
* The readline() method reads the first line of the file, the read() method reads the whole file.
* **The readline() method reads a single line from the current position, the read() method reads from the current position until the end of the file.**

> Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.

## Iterating through Files

Can you identify which code snippet will correctly open a file and print lines one by one without whitespace?

<ul>
    <li><pre>with open("hello_world.txt") as text:
        for line in text:
            print(line)</pre></li>
    <li><pre>with open("hello_world.txt") as text:
        for line in text:
            print(text)</pre></li>
    <li><pre>with open("hello_world.txt") as text:
        print(line)</pre></li>
    <li><pre><b>with open("hello_world.txt") as text:
        for line in text:
            print(line.strip())</b></pre></li>
</ul>

> Here, we are iterating line by line, and the strip() command is used to remove extra whitespace.

## Writing Files

What happens to the previous contents of a file when we open it using "w" ("write" mode)?

* The new contents get added after the old contents.
* A new file is created and the old contents are kept in a copy.
* **The old contents get deleted as soon as we open the file.**
* The old contents get deleted after we close the file.

> When using write mode, the old contents get deleted as soon as the file is opened.