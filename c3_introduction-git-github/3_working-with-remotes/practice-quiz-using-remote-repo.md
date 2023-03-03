## Practice Quiz: Using a Remote Repository
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

In order to get the contents of a remote branch without automatically merging, which of these commands should we use?

* git pull
* **git remote update**
* git checkout
* git log -p -1

> git remote update will fetch the contents of all remote branches and allow us to merge the contents ourselves.

<br>

### Question 2

If we need to find more information about a remote branch, which command will help us?

* git fetch
* git checkout
* git remote update
* **git remote show origin**

> If you want to see more information about a particular remote branch, you can use the git remote show command. Don't forget the commit ID!

<br>

### Question 3

What command will download remote branches from remote repositories without merging the content with your current workspace automatically?

* git checkout
* git pull
* **git fetch**
* git remote update

> git fetch will download remote updates, such as objects and refs, from the remote branch.

<br>

### Question 4

What type of merge creates a new merge commit?

* Fast-forward merge
* Implicit merge
* **Explicit merge**
* Squash on merge

> An explicit merge creates a new merge commit. This alters the commit history and explicitly shows where a merge was executed.

<br>

### Question 5

What method of getting remote contents will automatically merge the remote branch with the current local branch?

* git fetch
* git checkout
* git remote update
* **git pull**

> git pull automatically merges the remote branch with the current branch.
