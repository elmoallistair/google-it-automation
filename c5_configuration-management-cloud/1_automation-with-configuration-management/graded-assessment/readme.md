## Qwiklabs Assessment: Debugging Puppet Installation

### Introduction

You're a member of the IT team at your company. One of your coworkers has recently set up a Puppet installation, but it doesn't seem to be doing its job. So, you're asked to debug the profile class, which is supposed to append a path to the environment variable $PATH. But it's somehow misbehaving and causing the $PATH variable to be broken. You'll need to locate the issue and fix it with the knowledge that you learned in this module.

### What you'll do

* Check out what Puppet rules look like
* Run the Puppet agent locally
* Understand how file permissions are represented by numbers
* Learn how scripts under /etc/profile.d/ perform startup tasks, including setting up your own environment variables
* Append a string to an environment variable