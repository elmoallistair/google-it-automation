## Notes

* If you're a project maintaner, it's important that you reply promptly to pull requests and don't let them stagnate.
* It's important that you understand any changes you accept.
* When it comes to coordination who does what and when, a common strategy for active software project is to use an **issue tracker**.
* **Continous integration system (CI)** Will build and test our code every time there's a cange
* Once we have our code automatically built and tested, the next automation step is  **countinous deployment**, which is sometimes **called countinous delivery (CD)**.
* **Pipelines** specify the steps that need to run to get the result you want.
* **Artifacts** is the name used to describe any files that are generated as part of the pipeline.
* Make sure the authorized entities for the test servers are not the same entities authorized to deploy on the production servers.
* Always have a plan to recover your access in case your pipeline gets compromised.