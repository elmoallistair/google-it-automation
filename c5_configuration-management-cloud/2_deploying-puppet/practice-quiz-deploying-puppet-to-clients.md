## Practice Quiz: Deploying Puppet to Clients
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

When defining nodes, how do we identify a specific node that we want to set rules for?

* By using the machine’s MAC address
* **By specifying the node's Fully Qualified Domain Names (FQDNs)**
* User-defined names
* Using XML tags

> A FQDN is a complete domain name for a specific machine that contains both the hostname and the domain name.

<br>

### Question 2

When a Puppet agent evaluates the state of each component in the manifest, it uses gathered facts about the system to decide which rules to apply. What tool can these facts be "plugged into" in order to simplify management of the content of our Puppet configuration files?

* Node definitions
* Certificates
* **Templates**
* Modules

> Templates are documents that combine code, system facts, and text to render a configuration output fitting predefined rules.

<br>

### Question 3

What is the first thing that happens after a node connects to the Puppet master for the first time?

* The node identifies an open port.
* The Puppet-master requests third-party authentication.
* **The node requests a certificate.**
* The user can immediately add modules.

> After receiving a certificate, the node will reuse it for subsequent logins.

<br>

### Question 4

What does FQDN stand for, and what is it?

* Feedback Query Download Noise, which is extraneous data in feedback queries
* Far Quantum Data Node, which is a server node utilizing quantum entanglement
* Fairly Quantized Directory Network, which is a network consisting of equitable counted folders
* **Fully Qualified Domain Name, which is the full address for a node**

> A fully qualified domain name (FQDN) is the unabbreviated name for a particular computer, or server. There are two elements of the FQDN: the hostname and the domain name.

<br>

### Question 5

What type of cryptographic security framework does Puppet use to authenticate individual nodes?

* Single Sign On (SSO)
* **Public Key Infrastructure (PKI)**
* Fully Qualified Domain Name (FQDN)
* Token authentication

> Puppet uses an Secure Sockets Layer (SSL) Public Key Infrastructure to authenticate both nodes and masters.