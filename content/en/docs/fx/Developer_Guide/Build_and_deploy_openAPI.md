---
title: "Deploying OpenAPI Compliant Servers"
linkTitle: "OpenAPI Compliant Servers"
tags: [quickstart, integration, openapi]
categories: ["Knowledge Base"]
weight: 220
description: >-
  To utilize the FX platform for creating and deploying OpenAPI compliant servers, follow the structured steps below.
---

# Step-by-Step Guide to Deploying OpenAPI Compliant Servers with the FX Platform

To utilize the FX platform for creating and deploying OpenAPI compliant servers, follow the structured steps below. This guide assumes you have a basic understanding of OpenAPI, Docker, and Java environments.

### Prerequisites

Ensure your system is prepared with:

- **OpenJDK (version specified by the FX platform requirements)** installed and the `JAVA_HOME` environment variable correctly set.
- **Docker** installed for local image building and testing.

### Steps for Deployment

1. **Repository Setup**:

   - Either copy the provided repository to another GitHub repository or use it as a template.

2. **Local Preparation**:

   - Clone the repository to your local machine.

3. **OpenAPI Specification Update**:

   - Navigate to the root directory of your local repository and update the `openapi.yaml` file to reflect your API design.
   - **Important**: When editing the `openapi.yaml`, ensure you introduce the `tag` attribute for each endpoint. This attribute is mandatory and specifies the name of the controller that should handle the endpoint. A sample

   ```yaml
   openapi: 3.0.0
    info:
    title: Hello API
    version: 1.0.0
    paths:
    /hello-world:
        get:
        tags:
            - "codegen"
        summary: Get Hello
        description: Retrieve "OK" message
        responses:
            '200':
    ```


4. **Code Generation**:

   - Execute the command:

     ```bash
     
     java -jar swagger-codegen-cli.jar generate -l python-flask -i openapi.yaml -o server -c server/sg_config.json
     ```

     This command generates the server code based on your openapi.yaml specification.


5. **Implement Controller Functions**:

   - With the generated code, you'll need to fill in the logic for the controller functions in the specified locations.

6. **Initialization Files**:

   - Ensure that the `__init__.py` files in `server/{app_name}` and `server/{app_name}/controllers` are empty.

7. **Repository Update**:

   - Commit and push your changes back to the repository.

### Automated Pipeline

Upon pushing changes to the repository, an automated pipeline is triggered. The pipeline is customised for your implementation of the FX Platform.

This pipeline performs several actions:

- **Builds the Application**: Compiles your code, ensuring it's ready for deployment.
- **Runs Tests**: Executes predefined tests to verify the functionality of your application.
- **Builds and Pushes Docker Image**: Creates a Docker image of your application and pushes it to a configured Docker registry.

Following the successful execution of these steps, the pipeline communicates with the FX platform to deploy your application. This involves:

- **Launching the Container**: Your application's container is launched into the 'fx-k8x' namespace.
- **Route Creation**: A route is created in APISix to make your application accessible.
- **Security Measures**: If specified, routes are secured according to the configurations detailed in subsequent sections of the documentation.

### Securing Endpoints

To secure endpoints, refer to the detailed instructions provided in the documentation. This typically involves specifying security schemes in your `openapi.yaml` and configuring the necessary authentication and authorization mechanisms within the FX platform's deployment settings.

### Conclusion

By following these steps, developers can efficiently deploy OpenAPI compliant servers using the FX platform. This process not only automates the deployment pipeline but also ensures that applications are scalable, secure, and ready for production environments.