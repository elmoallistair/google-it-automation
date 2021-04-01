## Practice Quiz: Troubleshooting & Debugging
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Which of the following are valid strategies for recovery after encountering service failure? (Select all that apply.)

* **Switching to a secondary instance.**
* Setting up monitoring and alerts.
* **Restoring from backup.**
* **Performing a rollback to a previous version.**

> A quick way to recover is to have a secondary instance of the VM running your service that you can quickly switch to.

> As long as you've been keeping frequent backups, restoring a previous VM image will often get you where you need to be.

> If the problem is related to recent changes or updates, rolling back to a previous working version of the service or supporting software will give the time to investigate further.

<br>

### Question 2

Which of the following concepts provide redundancy? (Select all that apply.)

* **Having a secondary instance of a VM.**
* **Having a secondary Cloud vendor.**
* Having automatic backups configured.
* Performing a rollback.


> If your primary VM instance running your service fails, having a secondary instance running in the background ready to take over can provide instant failover.

> Having a secondary Cloud service provider on hand with your data in case of the first provider having large-scale outages can provide redundancy for a worst-case scenario.

<br>

### Question 3

If you operate a service that stores any kind of data, what are some critical steps to ensure disaster recovery? (Select all that apply)

* **Implement automated backups**
* Use redundant systems wherever possible
* **Test backups by restoring**
* Never delete old backups

> As long as we have viable backup images, we can restore the VM running our service.
> It's important to know that our backup process is working correctly. It would not do to be in a recovery situation and not have backups.

<br>

### Question 4

What is the correct term for packaged applications that are shipped with all needed libraries and dependencies, and allows the application to run in isolation?

* Rollback
* Secondary instance
* **Containers**
* Disk Image

> Containerization ensures that our software runs the same way every time.

<br>

### Question 5

Using a large variety of containerized applications can get complicated and messy. What are some important tips for solving problems when using containers? (Select all that apply)

* **Use extensive logging in all parts**
* Reduce the number of containers
* Reuse container configurations
* **Use test instances**

> As long as we have the right logs in the right places, we can tell where our problems are.

> We should take every opportunity to test and retest that our configuration is working properly.
