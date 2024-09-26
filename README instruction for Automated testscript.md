# Automated Testing for Frontend and Backend Integration
- This README file contains instructions on how to set up and run the automated tests script.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Postman](https://www.postman.com/downloads/)

## Installation

1. **Install Docker**:
   - Verify the installation by running the following command in the command prompt:
  
     ```bash
     docker --version  # To check the installed Docker version
     ```
     
2. **Install Minikube**:

- Start Minikube with the following commands using the command prompt:

  ```bash
  minikube start  # This will install Minikube
  minikube status  # To check the status
  minikube dashboard  # To start the Minikube dashboard

## Deploying Services on Kubernetes

- Clone the repository containing your deployment YAML files:
  
  ```bash
  git clone <repository-link>

- Navigate into the cloned repository folder using:

  ```bash
  cd <repository-folder>

- In the Minikube dashboard, go to Workloads > Deployments.
- Click on the + button and select Create from file. Upload your frontend and backend deployment YAML files Monitor the deployment status in the dashboard to ensure both services are running.    
- Click on Services and find the frontend service (run minikube tunnel command if an IP is not assigned to the frontend)
- Click on External endpoint and Verify that accessing the frontend URL displays the greeting message fetched from the backend. 

## Verifying API endpoints
- Use post forwarding to forward a port local machine to the backend service:                                           
  kubectl port-forward service/backend-service 3000:3000
- Open Postman and Add a Get request for the backend API using URL http://localhost:3000/greet
- Send the request and Verify JSON response from the backend                                                   
- Match the message displayed on the frontend to check if the integration is successfull     
                                                  
## Automated test scripts using Postman
- Create a New collection and Add a request for the backend
- In the tests tab add a Script to check the response status is 200 and it contains a message property
- Add another request for the Frotend to check the response status is 200 and the response from the frontend includes the message obtained from the backend.
- Run the entire collection and Verify                                                  
