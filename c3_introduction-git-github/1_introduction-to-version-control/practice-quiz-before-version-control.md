## Practice Quiz: Before Version Control
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Your colleague sent you a patch called fix_names.patch, which fixes a config file called fix_names.conf. What command do you need to run to apply the patch to the config file?
1 / 1 point

* diff names.conf fix_names.conf
* patch fix_names.conf names.conf
* **patch fix_names.conf < fix_names.patch**
* diff names.conf_orig names.conf_fixed > fix_names.conf

> The patch command with the file to be patched, followed by the filename of the patch, will apply it.

<br>

### Question 2

You're helping a friend with a bug in a script called fix_permissions.py, which fixes the permissions of a bunch of files. To work on the file, you make a copy and call it fix_permissions_modified.py. What command do you need to run after solving the bug to send the patch to your friend?

* **diff fix_permissions.py fix_permissions_modified.py > fix_permissions.patch**
* patch fix_permissions.py < fix_permissions_modified.py
* patch fix_permissions.py > fix_permissions.patch
* diff fix_permissions.py fix_permissions.diff

> The diff command will allow us to compare and apply the differences between the files.

<br>

### Question 3

The _____ commandhighlights the words that changed in a file instead of working line by line.

* diff
* diff -u
* **wdiff**
* patch

> The vimdiff commandhighlights the words that changed in a file by color, in addition to working line by line.

<br>

### Question 4

How can we choose the return value our script returns when it finishes?

* **Using the exit command from the sys module**
* Use the patch command
* Use the diff command
* Use meld

> A script can use sys.exit to finish processing and return the number passed as an argument as the script's return code.

<br>

### Question 5

In addition to the original files, what else do we need before we can use the patch command?

* **Diff file**
* exit command of the sys module
* Version control
* Full copy of the new files

> We need to use the patch command with the diff file to apply new changes to the original file.
