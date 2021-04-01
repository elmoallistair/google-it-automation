## Practice Quiz: Introduction to Puppet
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

A Puppet agent inspects /etc/conf.d, determines the OS to be Gentoo Linux, then activates the Portage package manager. What is the provider in this scenario?

* /etc/conf.d
* **Portage**
* Gentoo Linux
* The Puppet agent

> The Portage package manager used by Gentoo Linux is the provider called by the Puppet agent.

<br>

### Question 2

Which of the following examples show proper Puppet syntax? 

```
class AutoConfig {
  package { 'Executable':
    ensure => latest,
  }
  file { 'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  }
  service { 'executable.exe':
    enable  => true,
    ensure  => running,
  }
}
```

> The AutoConfig class has all its resources grouped together using proper Puppet syntax. 

<br>

### Question 3

What is the benefit of grouping resources into classes when using Puppet?

* Providers can be specified
* **Configuration management is simplified**
* The title is changeable
* Packages are not required

> Grouping a collection of related resources into a single class simplifies configuration management by, for one example, allowing us to apply a single class to each host rather than having to specify every resource for each host separately and possibly missing some.

<br>

### Question 4

What defines which provider will be used for a particular resource?

* **Puppet assigns providers based on the resource type and data collected from the system.**
* A menu allows you to choose providers on a case-by-case basis.
* The user is required to define providers in a config file.
* Puppet uses an internet database to decide which provider to use.

> Puppet assigns providers according to predefined rules for the resource type and data collected from the system such as the family of the underlying operating system.

<br>

### Question 5

In Puppet’s file resource type, which attribute overwrites content that already exists?

* Purge
* Overwrite
* **Replace**
* Save

> Puppet has many useful attributes. "Replace" set to True tells Puppet to replace files or symlinks that already exist on the local system but whose content doesn’t match what the source or content attribute specifies.