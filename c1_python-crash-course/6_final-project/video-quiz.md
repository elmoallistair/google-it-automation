## Writing a Script from the Ground Up

<br>

### Video: Problem Statement

Restate the problem statement from the video example.

* Each login event is an instance of the Event class.
* The attributes of the Event class are date, user, machine, and type.
* The company manager wants to know which users are currently connected to which machines.
* **We need to process a list of Event objects using their attributes to generate a report that lists all users currently logged in to the machines.**

> This problem statement defines the problem in specific terms and provides a direction and goal.

<br>

### Video: Research

There are two standard methods to sort a list in Python, sort and sorted. What is the difference between these two methods?

* sort returns a new list, while sorted returns the same list reorganized.
* sort lists alphabetically, while sorted lists by word length.
* **sorted returns a new list, while sort returns the same list reorganized.**

> Knowing the difference between these two methods is not nearly as important as the ability to research the tools we have available to us.

<br>

### Video: Planning

Having a plan is half the battle. When planning out your program, why is it often a good idea to separate functions?

* It simplifies making changes and fixing bugs.
* It allows us to use the same function for multiple purposes.
* It makes list sorting easier.
* **Both A and B.**
  
> Separating functions is helpful when debugging or making other changes, as it keeps functions from getting ‘tangled’. It also makes it easier to adapt functions for other uses.

<br>

### Video: Writing the Script

It’s important to know why we’ve written a function. In the example used in the video (shown here), what is the purpose of “if len(users) > 0:” ?

```
def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
```

* **Ensure that we don't print any machines where nobody is currently logged in**
* Generates a string of logged-in users for a given machine
* Sorts the list of users
* Iterate over the keys and values in the dictionary

> Generating the string underneath this check prevents lists with zero users from being printed.

<br>

### Video: Putting It All Together

Which line from the program we just wrote combines each logged-in user attribute into one variable?

* events.sort(key=get_event_date)
* self.user = user
* user_list = ", ".join(users)
* machines[event.machine].add(event.user)

> The join() function of str gathers the user attributes (which is a string) into a single string, with commas separating the users.
