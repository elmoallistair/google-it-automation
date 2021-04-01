## Practice Quiz: Introduction to GitHub
* **Total points: 4**
* **Score: 100%**

<br>

### Question 1

When we want to update our local repository to reflect changes made in the remote repository, which command would we use?

* git clone <URL>
* git push
* **git pull**
* git commit -a -m

> git pull updates the local repository by applying changes made in the remote repository.

<br>

### Question 2

git config --global credential.helper cache allows us to configure the credential helper, which is used for ...what?

* Troubleshooting the login process
* Dynamically suggesting commit messages
* Allowing configuration of automatic repository pulling
* **Allowing automated login to GitHub**

> By configuring the credential helper, we can avoid having to type in our username and password repeatedly.

<br>

### Question 3

Name two ways to avoid having to enter our password when retrieving and when pushing changes to the repo. (Check all that apply)

* Implement a post-receive hook
* **Use a credential helper**
* **Create an SSH key-pair**
* Use the git commit -a -m command.

> The credential helper caches our credentials for a time window, so that we don't need to enter our password with every interaction.

> Great job! We can create an SSH key-pair and store the public key in our profile, so that GitHub recognizes our computer.

<br>

### Question 4

Before we have a local copy of a commit, we should download one using which command?

* git commit -a -m
* git push
* git pull
* **git clone <URL>**

> If the repository already exists locally, this may raise an error.