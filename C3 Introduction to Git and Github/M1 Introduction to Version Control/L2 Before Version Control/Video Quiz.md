# Before Version Control

<br>

## Video: Keeping Historical Copies

What’s the goal of a version control system?

* To make sure that our code has no bugs
* **To keep track of changes made to our files**
* To have backup copies of our code
* To store code, images, configuration, and videos

> A version control system allows us to keep track of when and who did what changes to our files. Those can be code, configuration, images, or whatever else we need to track.

<br>

## Video: Diffing Files

What’s the goal of the diff tool?

* To keep track of changes to our files
* To check if our changes make sense
* To highlight new lines in Python files
* **To show the differences between two files**

> The diff tool shows all the differences between any type of file. By highlighting what’s changed, it helps us understand the changes and see how the files have been modified.

<br>

## Video: Applying Changes

What does the patch command do?

* It generates a file with the differences between two files.
* It shows the changes made in a directory of files.
* It redirects the contents of a file into standard input.
* **It applies the changes contained in a diff file to another file.**

> While diff is the command that generates the difference between two files, patch is the command that applies those differences to the original file.

<br>

## Video: Practical Application of diff and patch

We've prepared a diff file with the changes that need to be applied to the script. What does our colleague need to do now?

* Look at the changes in the diff file and manually modify the original file with those same changes.
* Run diff disk_usage.diff disk_usage.py.
* Ask us to send them the full file, not just the diff file.
* **Run patch disk_usage.py < disk_usage.diff.**

> To automatically apply changes to a file, we need to run the patch command on the file that we want to modify with the diff file as input.