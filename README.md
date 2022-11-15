# Manipulating Azure Storage Blobs with CDE

## Objective

CDE is the Cloudera Data Engineering Service, a containerized managed service for Large Scale Batch Pipelines with Spark featuring Airflow and Iceberg.
A CDE Resource in Cloudera Data Engineering (CDE) is a named collection of files used by a job. They can include application code, configuration files, custom Docker images (Private Cloud only), and Python virtual environment specifications.

Overall, CDE Resources simplify the management of files and dependencies associated with complex pipelines. Dependencies and environments are more quickly reproducible and reusable by other pipelines.

This tutorial shows how to create two ADLS Containers and move files between them using a CDE Job and CDE Resources. The pattern provides an example integration between CDE and 3rd party orchestration systems or an example use of a standard python library.


## Requirements

The following requirements are needed to run through the tutorial:

* CDP Public Cloud: A CDE Virtual Cluster associated with an Azure CDP Instance (A similar example in AWS S3 would require using the boto3 library).
* Spark 2 or Spark 3 CDE Virtual Clusters  ok.
* Azure: The Storage Account Name and the Storage Account Key associated with the ADLS target destination for the file transfer.
* Basic familiarity with Python (no code changes required).


## Instructions

#### Step 0: Project setup

##### Clone the Project

Clone this GitHub repository to your local computer.

```
mkdir ~/Documents/abs_containers_cde
cd ~/Documents/abs_containers_cde
git clone https://github.com/pdefusco/ASB_Containers_CDE.git
```

Alternatively, if you don't have GitHub create a folder on your local computer; navigate to [this URL](https://github.com/pdefusco/ASB_Containers_CDE.git) and download the files.

##### Add your ADLS Storage Info to cde_job_move_file.py

Open "cde_job_move_file.py" in any editor of your choice. Add your Azure Connection string at line 8 and your Azure Account Name at line 28.
Please reach out to your Azure admin if you need help obtaining them.


#### Step 1: Create a CDE Resource of Type Files

In this step you will upload the provided Python scripts to a CDE Resource of type "File" so you can more easily create a CDE Job with its dependencies.

Navigate to your CDE Virtual Cluster and Open the Jobs page.

![alt text](img/step1.png)

From the left tab, select Resources and create a CDE Resource of type "File".

![alt text](img/step2.png)

![alt text](img/step3.png)

Next, upload the "cde_job_move_file.py" and "myfile_1.py" files via the "Upload" icon.

![alt text](img/step4.png)


#### Step 2: Create a CDE Resource of Type Python Environment

In this step you will create a Python Environment so you can pip install the "azure-storage-fblob" library and use it with your CDE Job.

Navigate back to the CDE Resources tab and create a CDE Resource of type "Python Environment". Select Python 3 and leave the PyPi mirror field blank.

![alt text](img/step5.png)

Upload "requirements.txt" from your local machine and allow a few seconds for the Python environment to build.

![alt text](img/step6A.png)

When the build is complete, exit to the Resources page and validate that you now see two entries. One of type "Files" and one of type "Python".

![alt text](img/step6.png)


#### Step 3: Create a CDE Job

In this step you will create the CDE Job with the uploaded scripts and Python environment.

Navigate to the Jobs tab on the left pane. Select the "Create Job" blue icon on the right side.

![alt text](img/step7.png)

Next, select the Spark Job Type from the Toggle Bar (Spark 2.4 or 3.2 ok). If you are curious to learn more about Airflow jobs, please visit [this related tutorial](https://github.com/pdefusco/Using_CDE_Airflow).

Under "Application Files" select "File" and then "Select from Resource". Select file "cde_job_move_file.py". This will be the base script for the CDE Job.

![alt text](img/step8.png)

![alt text](img/step9.png)

Immediately below, choose Python 3 and select the Python Environment you created earlier.

![alt text](img/step10.png)

![alt text](img/step11.png)

Expand the "Advanced Options" section. No changes are required but notice the CDE Resource of type file has been associated with the CDE Job for you automatically. This will allow you to mount in the "myfile_1.py" script to the CDE Kubernetes pod from the "cde_job_move_file.py" script.

![alt text](img/step12.png)

Finally, click on the "Create and Run" blue icon at the bottom of the page.

![alt text](img/step13.png)


## Conclusions & Next Steps

CDE is the Cloudera Data Engineering Service, a containerized managed service for Spark and Airflow. With Resources, CDE users can more easily track and reuse dependencies including simple python scripts, jars, as well as Python environments and more.

In this tutorial we uploaded a file from a CDE Resource to an ADLS folder. This pattern can be as an integration point between CDE Jobs/Resources and 3rd party orchestration systems.

If you are exploring CDE you may find the following tutorials relevant:

* [Spark 3 & Iceberg](https://github.com/pdefusco/Spark3_Iceberg_CML): A quick intro of Time Travel Capabilities with Spark 3.

* [Simple Intro to the CDE CLI](https://github.com/pdefusco/CDE_CLI_Simple): An introduction to the CDE CLI for the CDE beginner.

* [CDE CLI Demo](https://github.com/pdefusco/CDE_CLI_demo): A more advanced CDE CLI reference with additional details for the CDE user who wants to move beyond the basics.

* [Using CDE Airflow](https://github.com/pdefusco/Using_CDE_Airflow): A guide to Airflow in CDE including examples to integrate with 3rd party systems via Airflow Operators such as BashOperator, HttpOperator, PythonOperator, and more.

* [GitLab2CDE](https://github.com/pdefusco/Gitlab2CDE): a CI/CD pipeline to orchestrate Cross-Cluster Workflows for Hybrid/Multicloud Data Engineering.

* [CML2CDE](https://github.com/pdefusco/cml2cde_api_example): an API to create and orchestrate CDE Jobs from any Python based environment including CML. Relevant for ML Ops or any Python Users who want to leverage the power of Spark in CDE via Python requests.

* [Postman2CDE](https://github.com/pdefusco/Postman2CDE): An example of the Postman API to bootstrap CDE Services with the CDE API.

* [Oozie2CDEAirflow API](https://github.com/pdefusco/Oozie2CDE_Migration): An API to programmatically convert Oozie workflows and dependencies into CDE Airflow and CDE Jobs. This API is designed to easily migrate from Oozie to CDE Airflow and not just Open Source Airflow.
