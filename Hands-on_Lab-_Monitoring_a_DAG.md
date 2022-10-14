---
markdown-version: 
title: labs/Apache Airflow/Monitoring a DAG/Hands-on_Lab-_Monitoring_a_DAG
branch: lab-435-instruction
version-history-start-date: 2022-04-08T08:45:28Z
---

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Hands-on Lab: Monitoring a DAG

Estimated time needed: **20** minutes

## Objectives

After completing this lab you will be able to:

*   Search for a DAG.
*   Pause/Unpause a DAG.
*   Get the Details of a DAG.
*   Explore tree view of a DAG.
*   Explore graph view of a DAG.
*   Explore Calendar view of a DAG.
*   Explore Task Duration view of a DAG.
*   Explore Details view of a DAG.
*   View the source code of a DAG.
*   Delete a DAG.

# About Skills Network Cloud IDE

Skills Network Cloud IDE (based on Theia and Docker) provides an environment for hands on labs for course and project related labs. Theia is an open source IDE (Integrated Development Environment), that can be run on desktop or on the cloud. to complete this lab, we will be using the Cloud IDE based on Theia running in a Docker container.

## Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.

# Exercise 1 - Getting the environment ready

Step 1.1. Open a new terminal by clicking on the menu bar and selecting **Terminal**->**New Terminal**, as shown in the image below.

![Screenshot highlighting New Terminal in menu bar](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/new-terminal.png)

This will open a new terminal at the bottom of the screen.

![Screenshot highlighting new terminal at bottom of screen](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/terminal_bottom_screen.png)

Run the commands below on the newly opened terminal. (You can copy the code by clicking on the little copy button on the bottom right of the codeblock below and then paste it, wherever you wish.)

Start Apache Airflow in the lab environment.

```
start_airflow
```

{: codeblock}

Please be patient, it will take a few minutes for airflow to get started.

When airflow starts successfully, you should see an output similar to the one below:

![Screenshot highlighting UI URL, Username, and Password](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/start_airflow.png)

Step 1.2. Open the Airflow Web UI

Copy the Web-UI URL and paste it on a new browser tab. Or your can click on the URL by holding the control key (Command key in case of a Mac).

You should land at a page that looks like this:

![Screenshot of Skills Network Airflow](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/airflow_webui.png)

# Exercise 2 - Submit a dummy DAG

For the purpose of monitoring, let's create a dummy DAG with three tasks.

Task1 does nothing but sleep for 1 second.

Task2 sleeps for 2 seconds.

Task3 sleeps for 3 seconds.

This DAG is scheduled to run every 1 minute.

Step 2.1. Using Menu->`File`->`New File` create a new file named `dummy_dag.py`.

Step 2.2. Copy and paste the code below into it and save the file.

```
# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG
dag = DAG(
    'dummy_dag',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(minutes=1),
)

# define the tasks

# define the first task

task1 = BashOperator(
    task_id='task1',
    bash_command='sleep 1',
    dag=dag,
)


# define the second task
task2 = BashOperator(
    task_id='task2',
    bash_command='sleep 2',
    dag=dag,
)

# define the third task
task3 = BashOperator(
    task_id='task3',
    bash_command='sleep 3',
    dag=dag,
)

# task pipeline
task1 >> task2 >> task3

```

{: codeblock}

Submitting a DAG is as simple as copying the DAG python file into `dags` folder in the `AIRFLOW_HOME` directory.

Step 2.3. Open a terminal and run the command below to submit the DAG that was created in the previous exercise.

```
cp dummy_dag.py $AIRFLOW_HOME/dags
```

{: codeblock}

Step 2.4. Verify that our DAG actually got submitted.

Run the command below to list out all the existing DAGs.

```
airflow dags list
```

{: codeblock}

Verify that `dummy_dag` is a part of the output.

Step 2.5. Run the command below to list out all the tasks in `dummy_dag`.

```
airflow tasks list dummy_dag
```

{: codeblock}

You should see 3 tasks in the output.

# Exercise 3 - Search for a DAG

In the Web-UI, identify the `Search DAGs` text box as shown in the image below.

![Screenshot highlighting Search DAGs textbox, dummy_dag typed in text box, and dummy-dag toggle button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/search_dags.png)

Type `dummy_dag` in the text box and press enter.

Note: It may take a couple of minutes for the dag to appear here. If you do not see your DAG, please give it a minute and try again.

You should see the `dummy_dag` listed as seen in the image below:

![Screenshot highlighting the dummy_dag toggle button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/search_dags2.png)

# Exercise 4 - Pause/Unpause a DAG

Unpause the DAG using the Pause/Unpause button.

![Screenshot highlighting the Pause/Unpause DAG button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/pauseunpause1.png)

You should see the status as shown in the image below after you unpause the DAG.

![Screenshot showing the status of the dummy_dag](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_listing.png)

You can see the following details in this view.

*   Owner of the DAG
*   How many times this DAG has run.
*   Schedule of the DAG
*   Last run time of the DAG
*   Recent task status.

# Exercise 5 - DAG - Detailed view

Click on the DAG name as shown in the image below to see the detailed view of the DAG.

![Screenshot highlighting the dummy_dag tag name](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_click.png)

You will land a page that looks like this.

![Screenshot of the page for the dummy_dag](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_detailed_view.png)

# Exercise 6 - Explore tree view of DAG

Click on the `Tree View` button to open the Tree view.

![Screenshot highlighting the Tree View button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_tree_view.png)

Click on the `Auto Refresh` button to switch on the auto refresh feature.

The tree view shows your DAG tasks in the form of a tree as seen in the image above.

It also shows the DAG run and task run status as seen below.

![Screenshot highlighting task run status](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_tree_view2.png)

The circles in the image below represent a single DAG run and the color indicates the status of the DAG run. Place your mouse on any circle to see the details.

![Screenshot showing details of DAG run](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_status.png)

The squares in the image below represent a single task within a DAG run and the color indicates its status. Place your mouse on any square to see the task details.

![Screenshot showing details of task](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/task_status.png)

# Exercise 7 - Explore graph view of DAG

Click on the `Graph View` button to open the graph view.

Click on the `Auto Refresh` button to switch on the auto refresh feature.

The graph view shows the tasks in a form of a graph. With the auto refresh on, each task status is also indicated with the color code.

![Screenshot of tasks in graph form](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_graph_view.png)

# Exercise 8 - Calender view

The calender view gives you an overview of all the dates when this DAG was run along with its status as a color code.

![Screenshot highlighting Calendar veiw button and the detailed information for a specific date](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_calendar_view.png)

# Exercise 9 - Task Duration view

The Task Duration view gives you an overview of how much time each task took to execute, over a period of time.

![Screenshot of overview for duration of each task](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_task_times.png)

# Exercise 10 - Details view

The Details view give you all the details of the DAG as specified in the code of the DAG.

![Screenshot of DAG details view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_details_view.png)

# Exercise 11 - Code view

The Code view lets you view the code of the DAG.

![Screenshot of Code view](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_code.png)

# Exercise 12 - Delete a DAG

To delete a DAG click on the delete button.

![Screenshot highlighting delete button](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/delete_a_dag.png)

You will get a confirmation pop up as shown in the image below. Click `OK` to delete the DAG.

![Screenshot of confirmation pop up](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Monitoring%20a%20DAG/images/dag_delete_confirm.png)

# Practice exercises

1.  Problem:

> *Unpause any existing DAG and monitor it.*

## Authors

Ramesh Sannareddy

### Other Contributors

Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2021-07-05        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |

Copyright (c) 2021 IBM Corporation. All rights reserved.
