## Practice Quiz: Automation at Scale
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

What is IaC (Infrastructure as Code)?

* Writing a program from the outside in
* Programs for industrial use
* Hardware-based programming with FPGAs
* **Using a version control system to deploy and manage node configurations**

> IaC goes hand in hand with continuous delivery.

<br>

### Question 2

What is the principle called when you think of networked machines as interchangeable resources instead of individual machines?

* "Flexible deployment"
* The "Borg" principle
* **Treating computers like "cattle instead of pets"**
* The principle of "group operation"

> This means no node is irreplaceable and configuration is automated.

<br>

### Question 3

What benefits can we gain by using automation to manage our configuration? (Check all that apply)

* **Consistency**
* Simplicity
* **Reliability**
* **Scalability**

> When a configuration or process doesn't depend on a human remembering to follow all the necessary steps, the result will always be the same.

> Because automation breeds consistency, when we know a particular process that has been automated works, we can count on it working every time as long as everything remains the same.

> A scalable system is a flexible system that can handle extra tasks or integrate extra resources easily.

<br>

### Question 4

Puppet is a commonly used configuration management system. Which of the following applications are also used for configuration management?

* Valgrind
* **Chef**
* **Ansible**
* **CFEngine**

> Chef is a configuration management system that treats configuration as code.

> Ansible is an open source IT Configuration Management, Deployment & Orchestration tool which aims to provide a wide variety of automation challenges with huge productivity gains.

> CFEngine is an open-source configuration management program that offers automated configuration and maintenance of large-scale computing networks, including centralized cloud, desktop, consumer and industrial application control, embedded networked applications, handheld smartphones, and tablet computers.

<br>

### Question 5

A network administrator is accustomed to manually configuring the 5 nodes on the network he manages. However, the company he works for is quickly growing, and there are plans to expand the network to 200 nodes. What is the most reasonable course of action for the network administrator?

* Prepare to manually configure 200 nodes
* Hire more network techs
* Ask for a reduction in planned nodes to simplify configuration
* **Prepare scripts or download software for automated configuration**

> We can write automation scripts ourselves or we can use some sort of configuration management software to make our network scalable by pushing changes from a control server.