## Practice Quiz: Automation
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

At a manufacturing plant, an employee spends several minutes each hour noting uptime and downtime for each of the machines they are running. Which of the following ideas would best automate this process?

* Provide a tablet computer to the employee to record uptime and downtime
* Hire an extra employee to track uptime and downtime for each machine
* **Add an analog Internet of Things (IoT) module to each machine, in order to detect their power states, and write a script that records uptime and downtime, reporting hourly**
* Add an analog IoT module to each machine, in order to detect their power states, and attach lights that change color according to the power state of the machine

> This is a practical application of using Python (and some extra hardware, in this case) to automate a task, freeing up a human's time. The solutions can be complex if the return in saved human time warrants it.

<br>

#### Question 2

One important aspect of automation is forensic value. Which of the following statements describes this term correctly?

* **It is important for automated processes to leave extensive logs so when errors occur, they can be properly investigated.**
* It's important to have staff trained on how automation processes work so they can be maintained and fixed when they fail.
* It's important to organize logs in a way that makes debugging easier.
* It's important to remember that 20% of our tasks as system administrators is responsible for 80% of our total workload.

> Forensic value, in relation to automation, is the value we get while debugging from properly logging every action our automation scripts take.

<br>

### Question 3

An employee at a technical support company is required to collate reports into a single file and send that file via email three times a day, five days a week for one month, on top of his other duties. It takes him about 15 minutes each time. He has discovered a way to automate the process, but it will take him at least 10 hours to code the automation script. Which of the following equations will help them decide whether it's worth automating the process?

* `if [10 hours to automate > (15 minutes * 60 times per month)] then automate`
* **`if [10 hours to automate < (15 minutes * 60 times per month)] then automate`**
* `if [(10 hours to automate + 15 minutes) > 60 times per month)] then automate`
* `[(10 hours to automate / 60 times per month) < 15 minutes]`

> With 10 hours to automate, the employee will start saving time before the month is over.

<br>

### Question 4

A company is looking at automating one of their internal processes and wants to determine if automating a process would save labor time this year. The company uses the formula [time_to_automate < (time_to_perform * amount_of_times_done) to decide whether automation is worthwhile. The process normally takes about 10 minutes every week. The automation process itself will take 40 hours total to complete. Using the formula, how many weeks will it be before the company starts saving time on the process?

* 6 weeks
* 2 weeks
* 24 weeks
* **240 weeks**

> It's safe to say that the company won't find it worth it's time to automate.

<br>

### Question 5

Which of the following are valid methods to prevent silent automation errors? (Check all that apply)

* **Email notifications about errors**
* **Internal issue tracker entries**
* Constant human oversight
* **Regular consistency checks**

> Email notifications for errors or task completions can help keep track of automated processes.

> Internal issue tracker entries are created as part of reporting on errors in our automation script in this lesson.

> Automated consistency checks, such as hash checks on backups, can help identify problems ahead of time.