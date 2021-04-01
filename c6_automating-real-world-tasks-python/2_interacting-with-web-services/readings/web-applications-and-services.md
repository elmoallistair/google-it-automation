## Web Applications and Services

A ***web application*** is an application that you interact with over HTTP. Most of the time when you’re using a website on the Internet, you’re interacting with a web application. So, how does this look behind the scenes?

Your web browser sends an HTTP request to a web server. Then, the web server passes the request along to the web application in charge of deciding what information to show you. The application then generates the website content (in HTML format). The application is also in charge of serving images and any other necessary data so that your web browser can render the website on your computer.

Lots of web applications also have APIs that you can use from your scripts! Web applications that have an API are also known as ***web services***. Instead of browsing to a web page to type and click around, you can use your program to send a message known as an ***API call*** to the web service. The part of the program that listens on the network for API calls is called an ***API endpoint***.

When you interact with a web service like this, you don't even care what language the other application is using. You interact with it using a specified protocol, and the only important constraint is that both the service and your program know how to use this protocol.

So, how does that work? That's coming up!