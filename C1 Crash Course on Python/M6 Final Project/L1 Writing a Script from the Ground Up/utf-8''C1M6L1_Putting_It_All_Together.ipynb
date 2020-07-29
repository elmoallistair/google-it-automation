{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Practice Notebook - Putting It All Together"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hello, coders! Below we have code similar to what we wrote in the last video.  Go ahead and run the following cell that defines our `get_event_date`, `current_users` and `generate_report` methods."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_event_date(event):\n",
    "  return event.date\n",
    "\n",
    "def current_users(events):\n",
    "  events.sort(key=get_event_date)\n",
    "  machines = {}\n",
    "  for event in events:\n",
    "    if event.machine not in machines:\n",
    "      machines[event.machine] = set()\n",
    "    if event.type == \"login\":\n",
    "      machines[event.machine].add(event.user)\n",
    "    elif event.type == \"logout\":\n",
    "      machines[event.machine].remove(event.user)\n",
    "  return machines\n",
    "\n",
    "def generate_report(machines):\n",
    "  for machine, users in machines.items():\n",
    "    if len(users) > 0:\n",
    "      user_list = \", \".join(users)\n",
    "      print(\"{}: {}\".format(machine, user_list))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "No output should be generated from running the custom function definitions above.  To check that our code is doing everything it's supposed to do, we need an `Event` class.  The code in the next cell below initializes our `Event` class.  Go ahead and run this cell next."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Event:\n",
    "  def __init__(self, event_date, event_type, machine_name, user):\n",
    "    self.date = event_date\n",
    "    self.type = event_type\n",
    "    self.machine = machine_name\n",
    "    self.user = user"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ok, we have an `Event` class that has a constructor and sets the necessary attributes.  Next let's create some events and add them to a list by running the following cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "events = [\n",
    "    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),\n",
    "    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),\n",
    "    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),\n",
    "    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),\n",
    "    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),\n",
    "    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),\n",
    "]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we've got a bunch of events.  Let's feed these events into our `custom_users` function and see what happens."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'webserver.local': {'lane'}, 'myworkstation.local': set(), 'mailserver.local': {'chris'}}\n"
     ]
    }
   ],
   "source": [
    "users = current_users(events)\n",
    "print(users)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Uh oh.  The code in the previous cell produces an error message.  This is because we have a user in our `events` list that was logged out of a machine he was not logged into. Do you see which user this is? Make edits to the first cell containing our custom function definitions to see if you can fix this error message. There may be more than one way to do so. \n",
    "<br><br>\n",
    "Remember when you have finished making your edits, rerun that cell as well as the cell that feeds the `events` list into our `custom_users` function to see whether the error message has been fixed. Once the error message has been cleared and you have correctly outputted a dictionary with machine names as keys, your custom functions are properly finished.  Great!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now try generating the report by running the next cell."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "webserver.local: lane\n",
      "mailserver.local: chris\n"
     ]
    }
   ],
   "source": [
    "generate_report(users)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Whoop whoop! Success! The error message has been cleared and the desired output is produced. You are all done with this practice notebook. Way to go!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
