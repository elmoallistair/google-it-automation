# Git Revert Cheat Sheet

[git checkout](https://git-scm.com/docs/git-checkout) is effectively used to switch branches.

[git reset](https://git-scm.com/docs/git-reset#_examples) basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful.

There are some other useful articles online, which discuss more aggressive approaches to [resetting the repo](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html).

[git commit --amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend) is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.

[git revert](https://git-scm.com/docs/git-revert) makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.

There are a [few ways](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things) you can rollback commits in Git.

There are some interesting considerations about how git object data is stored, such as the usage of sha-1.

Feel free to read more here:

* https://en.wikipedia.org/wiki/SHA-1
* https://github.blog/2017-03-20-sha-1-collision-detection-on-github-com/