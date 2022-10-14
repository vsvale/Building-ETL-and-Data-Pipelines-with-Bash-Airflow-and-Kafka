# Hands-on Lab: Working with streaming data using Kafka

<center>
    <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

Estimated time needed: **20** minutes

## Objectives

After completing this lab you will be able to:

*   Download and install Kafka
*   Start the Zookeeper server for Kafka metadata management
*   Start the Kafka message broker service
*   Create a topic
*   Start a producer
*   Start a consumer

# About Skills Network Cloud IDE

Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. to complete this lab, we will be using the Cloud IDE based on Theia running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.

# Exercise 1 - Download and extract Kafka

Open a new terminal, by clicking on the menu bar and selecting **Terminal**->**New Terminal**, as shown in the image below.

![Screenshot highlighting New Terminal in menu](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/new-terminal.png)

This will open a new terminal at the bottom of the screen.

![Screenshot highlighting new terminal at bottom of screen](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/terminal_bottom_screen.png)

Run the commands below on the newly opened terminal. (You can copy the code by clicking on the little copy button on the bottom right of the codeblock below and then paste it, wherever you wish.)

Download Kafka, by running the command below:

```
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
```

{: codeblock}

Extract kafka from the zip file by running the command below.

```
tar -xzf kafka_2.12-2.8.0.tgz
```

{: codeblock}

This creates a new directory 'kafka\_2.12-2.8.0' in the current directory.

# Exercise 2 - start ZooKeeper

ZooKeeper is required for Kafka to work. Start the ZooKeeper server.

```
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

{: codeblock}

When ZooKeeper starts you should see an output like this:

![Screenshot of output](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/zookeeper1.png)

You can sure it has started when you see an output like this:

![Screenshot of output](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/zookeeper2.png)

ZooKeeper, as of this version, is required for Kafka to work. ZooKeeper is responsible for the overall management of Kafka cluster. It monitors the Kafka brokers and notifies Kafka if any broker or partition goes down, or if a new broker or partition goes up.

# Exercise 3 - Start the Kafka broker service

Start a new terminal. <br>
Run the commands below. This will start the Kafka message broker service.

```
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties
```

{: codeblock}

When Kafka starts, you should see an output like this:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/kafka1.png)

You can be sure it has started when you see an output like this:

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Streaming/images/kafka2.png)

# Exercise 4 - Create a topic

You need to create a topic before you can start to post messages.

To create a topic named `news`, start a new terminal and run the command below.

```
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092
```

{: codeblock}

You will see the message: 'Created topic news.'

# Exercise 5 - Start Producer

You need a producer to send messages to Kafka. Run the command below to start a producer.

```
bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
```

{: codeblock}

Once the producer starts, and you get the '>' prompt, type any text message and press enter. Or you can copy the text below and paste. The below text sends three messages to kafka.

```
Good morning
Good day
Enjoy the Kafka lab
```

{: codeblock}

# Exercise 6 - Start Consumer

You need a consumer to read messages from kafka.

Open a new terminal.

Run the command below to listen to the messages in the topic `news`.

```
cd kafka_2.12-2.8.0
bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092
```

{: codeblock}

You should see all the messages you sent from the producer appear here.

You can go back to the producer terminal and type some more messages, one message per line, and you will see them appear here.

# Exercise 7 - Explore Kafka directories.

Kafka uses the directory /tmp/kakfa-logs to store the messages.

Explore the folder news-0 inside /tmp/kakfa-logs.

This is where all the messages are stored.

Explore the folder /home/project/kafka\_2.12-2.8.0

This folder has the below 3 sub directories.

| Directory | Contents                                     |
| --------- | -------------------------------------------- |
| bin       | shell scripts to control kafka and zookeeper |
| config    | configuration files                          |
| logs      | log files forkafka and zookeeper             |

# Exercise 8 - Clean up

Delete the kafka installation file.

```
rm kafka_2.12-2.8.0.tgz
```

{: codeblock}

# Practice exercises

1.  Problem:

> *Create a new topic named `weather`.*

<details>
<summary>Click here for Hint</summary>

> Use `kafka-topics.sh` command with the `create` option.

</details>

<details>
<summary>Click here for Solution</summary>

Make sure that you are in the 'kafka\_2.12-2.8.0' directory. Run the following command:

```
bin/kafka-topics.sh --create --topic weather --bootstrap-server localhost:9092
```

{: codeblock}

</details>

2.  Problem:

> *Post messages to the topic `weather`.*

<details>
<summary>Click here for Hint</summary>

> Use `kafka-console-producer.sh` and point to topic `weather`.

</details>

<details>
<summary>Click here for Solution</summary>

Make sure that you are in the 'kafka\_2.12-2.8.0' directory. Run the following command:

```
bin/kafka-console-producer.sh --topic weather --bootstrap-server localhost:9092

```

{: codeblock}

Post some test messages.

</details>

3.  Problem:

> *Read the messages from the topic `weather`.*

<details>
<summary>Click here for Hint</summary>

> Use `kafka-console-consumer.sh` and read from the topic 'weather'

</details>

<details>
<summary>Click here for Solution</summary>

```
bin/kafka-console-consumer.sh --topic weather --from-beginning --bootstrap-server localhost:9092
```

{: codeblock}

Make sure that the messages you sent from the producer appear here.

</details>

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2021-08-24        | 0.2     | Ramesh Sannareddy | Incorporated feedback from Yan     |
| 2021-06-22        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright (c) 2021 IBM Corporation. All rights reserved.
