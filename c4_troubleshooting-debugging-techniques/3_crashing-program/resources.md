## Resources for Understanding Crashes

There's a ton of different reasons why a computer might crash. This [Scientific American article](https://www.scientificamerican.com/article/why-do-computers-crash/) discusses many of the possible reasons, including hardware problems and issues with the overall operating system or the applications on top. 

On Linux or MacOS, the worst kind of crash is called a Kernel Panic. On Windows, it's known as the [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_Screen_of_Death). These are situations where the computer completely stops responding and only a reboot can make it work again. They don't happen often, but it's good to understand what they mean: the whole OS encountered an error and it can't recover.

We called out that reading logs is super important. You should know how to read logs on the operating system that you're using. Here are some resources for this:

* [How to find logs on Windows 10](https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/) (Digital Masters Magazine)
* [How to view the System Log on a Mac](https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/) (How-to Geek)
* [How to check system logs on Linux](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm) (FOSS Linux) 

You also need to be familiar with the tools available in your OS to diagnose problems. These are the tools we called out, but you don't need to limit yourself to them:

* [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) for Windows (Microsoft)
* [Linux strace command tutorial for beginners](https://www.howtoforge.com/linux-strace-command/) (HowtoForge)
* [How to trace your system calls on Mac OS](https://etcnotes.com/posts/system-call/) (/etc/notes)

<br><hr><br>

## Resources for Debugging Crashes

Check out the following links for more information:

* https://realpython.com/python-concurrency/
* https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
* https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults
* https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

Readable Python code on GitHub:

* https://github.com/fogleman/Minecraft
* https://github.com/cherrypy/cherrypy
* https://github.com/pallets/flask
* https://github.com/tornadoweb/tornado
* https://github.com/gleitz/howdoi
* https://github.com/bottlepy/bottle/blob/master/bottle.py
* https://github.com/sqlalchemy/sqlalchemy