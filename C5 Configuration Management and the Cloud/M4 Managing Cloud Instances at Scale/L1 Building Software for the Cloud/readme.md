## Notes

* **Persistent storage**: Used for instances that are long lived and need to keep data across reboot and upgrades
* **Ephemeral storage**: Used for instances that are only temporary and only need to keep local data while they're running
* **Object storage**: Lets you place and retrieve objects in a storage bucket
* **Throughput**: The amount of data that you can read and write in a given amount of time
* **Input/Output Operations Per Second (IOPS)**: Measures how many reads or writes you can do in one second, no matter how much data you're accessing
* **Latency**: The amount of time it takes to complete a read or write operation
* **Hot data** is accessed frequently and stored in hot storage
* **Cold data** is acessed infrequently and stored in cold storage
* **Sticky sessions**: All requests from the same client always go to the same backend server
* **Content Delivery Networks (CDNs)** make up a network of physical hosts that are geographically located as close to the end users as possible
* **Continous integration system** will build and test our code every time there's a change
* **Environment**: Everything needed to run the service
* **A/B testing**: Some requests are served using one set of code and configuration (A) and other requests are served using different set of code and configuration (B)
* **Rate limits**: Prevent one service from overloading the whole system
* **Utilization limits**: Cap the total amount of a certain resource that you can provision