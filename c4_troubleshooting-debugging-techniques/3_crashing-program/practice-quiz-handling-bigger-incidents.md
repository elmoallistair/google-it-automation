## Practice Quiz: Handling Bigger Incidents
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Which of the following would be effective in resolving a large issue if it happens again in the future?

* Incident controller
* **Postmortem**
* Rollbacks
* Load balancers

> A postmortem is a detailed document of an issue which includes the root cause and remediation. It is effective on large, complex issues.

<br>

### Question 2

During peak hours, users have reported issues connecting to a website. The website is hosted by two load balancing servers in the cloud and are connected to an external SQL database. Logs on both servers show an increase in CPU and RAM usage. What may be the most effective way to resolve this issue with a complex set of servers?

* Use threading in the program
* Cache data in memory
* **Automate deployment of additional servers**
* Optimize the database

> Automatically deploying additional servers to handle the loads of requests during peak hours can resolve issues with a complex set of servers.

<br>

### Question 3

It has become increasingly common to use cloud services and virtualization. Which kind of fix, in particular, does virtual cloud deployment speed up and simplify?

* **Deployment of new servers**
* Application code fixes
* Log reviewing
* Postmortems

> Virtualization makes deployment of VM servers in the cloud a fast and relatively simple process.

<br>

### Question 4

What should we include in our postmortem? (Check all that apply)

* **Root cause of the issue**
* **How we diagnosed the problem**
* **How we fixed the problem**
* Who caused the problem

> In order to learn about the problem and how it happens in general, we should include what caused it this time.

> Awesome! By clarifying how we identified the problem, it can be more easily identified in the future.

> In order to share with reviewers how the issue was resolved, it's important to include what we did to solve it this time.

<br>

### Question 5

In general, what is the goal of a postmortem? (Check all that apply)

* To identify who is at fault
* **To allow prevention in the future**
* **To allow speedy remediation of similar issues in the future**
* To analyze all system bugs

> By describing the cause of the problem, we can learn to avoid the same circumstances in the future.

> By describing in detail how we fixed the problem, we can help others or ourselves fix the same problem more quickly in the future.