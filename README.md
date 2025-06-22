## 🧰 Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/GCR-F44336?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Google Container Registry"/>
  <img src="https://img.shields.io/badge/GKE-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Google Kubernetes Engine"/>
  <img src="https://img.shields.io/badge/CircleCI-343434?style=for-the-badge&logo=circleci&logoColor=white" alt="CircleCI"/>
</p>

**Summary**
Automated the build, test, and deployment process using CircleCI as the CI/CD tool. Deployed Dockerized ML applications to Google Kubernetes Engine (GKE), managed secrets and service accounts securely, and monitored deployments via GCP.

**Go to MLOPS_project6_results for outputs**

Step 1
Project Setup
1.	Creating virtual Environment in project folder.
2.	Creating required folders and files. (artifacts for outputs, pipeline folder, src where main project code lies, (static , templates for html,css,js and flask automatically finds them in project directory), utils for common functions, requirements and setup file. To make a folder a package we need to create a __init__.py file inside it so that the methods/files can be accessed from other places.
3.	Next, we code for setup, custom exceptions, logger, requirements files (basic things at first like numpy, pandas) .
4.	Then we run setup.py in venv in cmd using pip install -e . This will install all the required dependencies for the project make the project directory ready for next steps. This step automatically created a folder with project name given in the setup.py

Step 2
1.	After jupyter notebook testing we start with Data processing.
2.	Create data_processing.py, code it and test. You should see the artifacts in the project directory.
3.	Now model_training.py in src, code it and test. Should see the model.pkl in the artifacts.

Step 3
User App building using Flask
1.	Create application.py in root , code and test. Make sure flask in requirements.
2.	Create index.html, style.css and code, Run.

Step 4
Training Pipeline, Data and Code versioning
1.	Create training_pipeline.py in pipeline folder, code and run.
2.	Now push all the necessary code to github by creating a repo there.

Step 5
CI-CD using Circle CI and Google Kubernetes
1.	Go to GCP console and enable the API’s for the project.
2.	Kubernetes Engine API, google container registry API, Compute Engine API , cloud build api, cloud storage api, IAM API
3.	Now we need to create a cluster. So go to  kubernetes engine – clusters -create-give name-“enable access using DNS”- create
4.	Now create a service account. Go to IAM-service accounts-create-give name-give permissions (owner, storage object admin, storage object viewer, artifact registry administrator, artifact registry writer)-create.
5.	Now let’s create keys for service account. Go to three dots-manage keys-add key- create key-json-create. A file will be downloaded which has the key.
6.	Upload the key to project root dir in vscode and add the file name to gitignore , if we don’t when we push the changes to github and the key becomes public and then the key will be deactivated automatically in GCP.
7.	Now push the changes so far to github.
8.	Now go to artifact registry and create one repository. give name- select same region as service account-create. We are creating this to store our docker image in gcr.
9.	Now let’s make Dockerfile in project root. Code it.
10.	Create Kubernetes_deployment.yaml and code it from material. Make necessary changes like gcr name, path etc according to your names.
11.	 Now its circle ci part.
12.	Create .circleci folder. It automatically detects the folder. And create config.yml inside it.
13.	We write all our CI-CD code here in this file, push to github , then connect circleci and github, then github checks this config.yml file and do the deployment accordingly.
14.	Push the changes to github.
15.	Now go to circle ci on web and you can login with github or google account.
16.	I did login with github. You will see all the repos in circle ci.
17.	Select our project repo and setup triggers.
18.	 In triggers , we use ALL pushes as default. This means whatever we make changes to github, circle ci will detect and update.
19.	Now go to settings – environment variales- add the variables you mentioned in config.yml.
20.	Now for the GCLOUD_SERVICE_KEY we can’t just do it directly because when it is exposed in public, it will be automatically deactivated as said before.
21.	So go to project and open bash terminal.
22.	We need to convert the key from json to base64 format. Using $ cat key.json | base64 -w 0
23.	You will see a long code in terminal- copy it-paste it in value field in environment variable for GCLOUD_SERVICE_KEY
24.	Next add another variable GOOGLE_PROJECT_ID and give project ID from GCP.
25.	Next add GKE_CLUSTER_NAME, go to cluster name in GKE and copy-paste
26.	 Next add GKE_region, in the same page copy region-paste
27.	Now go to pipelines in circle ci- choose project if not before- click trigger pipeline
28.	Now push the changes to Github and the pipeline in circle ci should run automatically.
29.	Now you should see the run is successful in circle ci.
30.	Now to check whether the deployment is successful, go to cluster in GKE, workloads, you will see status OK and pods 2/2 running. Get inside and go the app running page.
31.	Now you can see the app running in GKE online.
32.	Done
33.	Clean up: remove artifacts repo, GKE clusters

