# Fibonacci API

## Project Overview

This project involves developing a REST API that computes the nth Fibonacci number. As a Senior DevOps/SRE Engineer, I followed a structured approach to ensure that the API could be efficiently deployed and managed in a production environment. This includes writing the API, containerizing the application, deploying it to a Kubernetes cluster, and setting up horizontal pod autoscaling (HPA).

## Table of Contents

1. Fibonacci API Overview.
2. Process Workflow.
  - 2.1. Writing the Fibonacci API.
  - 2.2. Dockerizing the Project.
  - 2.3. Kubernetes Deployment.
  - 2.4. Setting Up HPA.
  - 2.5. CI/CD Pipeline.
  - 2.6. Monitoring and Logging.
  - 2.7. Scaling Considerations.
3.	Future Work.
4.	Operational Considerations.
5.  Conclusion.

## Fibonacci API Overview

The Fibonacci API computes the nth Fibonacci number provided as an input. It is implemented using Python's Flask framework for simplicity and rapid development. 

The API accepts multiple HTTP requests, including:

1. GET /get: Accepts a query parameter n to calculate the Fibonacci sequence up to the given number n.
2. GET /health: Returns the health status of the API.
3. GET /metrics: Provides metrics for monitoring the performance of the API, compatible with Prometheus..

## Process Workflow

### 2.1. Writing the Fibonacci API:

I wrote the REST API using Python and Flask. The endpoint accepts a GET request with the input n and returns the nth Fibonacci number as a JSON response. The logic is optimized for performance and includes basic input validation to handle edge cases, such as negative numbers or non-integer inputs.

### 2.2. Dockerizing the Project:

I built the Docker image for the API to enable consistent and reproducible deployments. 

The Dockerfile is optimized for production with a multi-stage build:

-	Stage 1: Uses a lightweight Python image to install dependencies.
  
-	Stage 2: Uses a minimal base image to run the application, reducing the overall image size.
  
This approach helps in minimizing the attack surface and reducing start-up time, critical for production deployments.

### 2.3. Kubernetes Deployment:

I wrote the Kubernetes manifests to deploy the Dockerized API to a Kubernetes cluster. 

The deployment includes:

- Deployment Manifest: Specifies the desired number of replicas and the container image to be used.

### 2.4. Setting Up HPA:

I set up Horizontal Pod Autoscaling (HPA) using a Kubernetes manifest. The HPA automatically scales the number of pods based on CPU utilization to ensure that the service can handle varying levels of load efficiently. 

The following configurations were considered:

-	Target CPU Utilization: Set to 50% to maintain a balance between resource usage and response time.
  
-	Minimum/Maximum Replicas: Configured to scale between 3 and 10 replicas depending on the load.
  
It is important to note that vertical scaling was not implemented in this project. Only horizontal scaling through HPA was configured.

### 2.5. CI/CD Pipeline:

Although a CI/CD pipeline was not implemented due to time constraints, another reason was the absence of a specified cloud provider where the CI/CD pipeline could be deployed. If a cloud provider were provided, I would have used a tool like Jenkins, GitHub Actions, or GitLab CI/CD to automate the build, test, and deployment process. 

This would include:

- Automated Build: Triggered on code changes to build the Docker image.
  
-	Automated Tests: Runs unit tests to ensure API correctness.
  
-	Automated Deployment: Uses kubectl or Helm charts to deploy the updated images to the Kubernetes cluster.

### 2.6. Monitoring and Logging:

I did not use any monitoring or logging tools in this project. However, I would have proposed a combination of Prometheus and Grafana for monitoring and ELK (Elasticsearch, Logstash, Kibana) or Datadog for centralized logging to ensure observability and quick incident response.

### 2.7. Scaling Considerations:

The API is designed to scale horizontally. For handling high request rates:

- Horizontal Scaling: Implemented through Kubernetes' HPA, allowing the API to automatically adjust the number of replicas based on CPU utilization, ensuring it can handle spikes in request volume while optimizing resource use.

## Future Work

Given more time, I would have expanded the project with the following:

- API Rate Limiting: Using an API Gateway like Kong or AWS API Gateway to prevent abuse.
  
-	Automated Backups: Set up a backup mechanism for configuration and data (if persisted).

-	Blue-Green Deployments: To ensure zero-downtime deployments and facilitate testing of new changes in production.
  
-	Advanced Security Measures: Implement network policies in Kubernetes and enable TLS termination using Cert-Manager.

## Operational Considerations

This section covers how the service can be deployed and run in a production environment:

-	Containerization: I used Docker for packaging the API, making it easier to run in different environments without compatibility issues.
  
-	CI/CD Processes: Would have leveraged GitHub Actions to automate build, testing, and deployment, ensuring faster and more reliable releases.
  
-	Monitoring/Logging Strategies: I would have proposed a combination of Prometheus and Grafana for monitoring and ELK/Datadog for centralized logging.
  
-	Scaling the Service: The HPA setup allows the API to automatically adjust the number of replicas based on CPU utilization, ensuring it can handle spikes in request volume while optimizing resource use.


## Conclusion

The project demonstrates a scalable, containerized API that can be deployed in a Kubernetes environment. While certain enhancements and workflows were not fully implemented due to time constraints, this README outlines the approach and considerations for taking the service to production. Thank you for reviewing my submission.