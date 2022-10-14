---
markdown-version: 
title: labs/Apache Airflow/Getting Started with Apache Airflow/Getting started with Apache Airflow
branch: lab-433-instruction
version-history-start-date: 2022-04-08T08:44:58Z
---

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Hands-on Lab: Getting started with Apache Airflow

Estimated time needed: **20** minutes

## Objectives

After completing this lab you will be able to:

*   Start Apache Airflow.
*   Open the Airflow UI in a browser.
*   List all the DAGs.
*   List the tasks in a DAG.
*   Explore a DAG in the UI.

# About Skills Network Cloud IDE

Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.

# Exercise 1 - Start Apache Airflow

Open a new terminal by clicking on the menu bar and selecting **Terminal**->**New Terminal**, as shown in the image below.

![Screenshot highlighting New Terminal in dropdown menu](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/new-terminal.png)

This will open a new terminal at the bottom of the screen as in the image below.

![Screenshot highlighting new terminal at the bottom of the screen](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/terminal_bottom_screen.png)

Run the commands below on the newly opened terminal. (You can copy the code by clicking on the little copy button on the bottom right of the codeblock below and paste it wherever you wish.)

Run the command below in the terminal to start Apache Airflow.

```
start_airflow
```

{: codeblock}

Please be patient, it may take upto 5 minutes for airflow to get started.

When airflow starts successfully, you should see an output similar to the one below.

![Screenshot highlighting UI URL, Username, and Password](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/start_airflow.png)

# Exercise 2 - Open the Airflow Web UI

Copy the Web-UI URL and paste it on a new browser tab. You can also click on the URL by holding the control key (Command key in case of a Mac).

You should land at a page that looks like this:

![Screenshot of Skills Network Airflow](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_webui.png)

You can Unpause/Pause a DAG using the Unpause/Pause toggle button.

![Screenshot highlighting Unpause/Pause toggle button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_pause_unpause.png)

An unpaused DAG looks like this:

![Screenshot of Unpaused button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_unpaused_dag.png)

Click on a DAG to explore more about the DAG.

![Screenshot highlighting ETL DAG tutorial](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_dag_click.png)

Click on the Tree View button to see the tree view of the DAG.

![Screenshot highlighting Tree View button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_tree_view.png)

Click on the Graph View button to see the graph view of the DAG.

![Screenshot highlighting Graph view button and graph view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Getting%20Started%20with%20Apache%20Airflow/images/airflow_graph_view.png)

# Exercise 3 - List all DAGs

Apache airflow gives us some handy command line options to work with.

Run the command below in the terminal to list out all the existing DAGs.

```
airflow dags list
```

{: codeblock}

# Exercise 4 - List tasks in a DAG

Run the command below in the terminal to list out all the tasks in the DAG named `example_bash_operator`.

```
airflow tasks list example_bash_operator
```

Here `example_bash_operator` is the name of the DAG.

Try listing out the tasks for the DAG `tutorial`.

# Exercise 5 - Pause/Unpause a DAG

Run the command below in the terminal to unpause a DAG.

```
airflow dags unpause tutorial
```

{: codeblock}

Here ` tutorial  ` is the name of the DAG.

Pause a DAG.

```
airflow dags pause tutorial
```

{: codeblock}

Try to unpause the DAG named `example_branch_operator`.

# Practice exercises

1.  Problem:

> *List tasks for the DAG `example_branch_labels`.*

<details>
<summary>Click here for Hint</summary>

> Use `list` option.

</details>

<details>
<summary>Click here for Solution</summary>

```
airflow tasks list example_branch_labels
```

{: codeblock}

</details>

2.  Problem:

> *Unpause the DAG `example_branch_labels`.*

<details>
<summary>Click here for Hint</summary>

> Use the unpause option.

</details>

<details>
<summary>Click here for Solution</summary>

```
airflow dags unpause example_branch_labels

```

{: codeblock}

</details>

3.  Problem:

> *Pause the DAG `example_branch_labels`.*

<details>
<summary>Click here for Hint</summary>

> Use the pause option.

</details>

<details>
<summary>Click here for Solution</summary>

```
airflow dags pause example_branch_labels

```

{: codeblock}

</details>

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2021-07-05        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright (c) 2021 IBM Corporation. All rights reserved.
