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

## Prerequisites

Ensure your system is prepared with:

- **OpenJDK (version specified by the FX platform requirements)** installed and the `JAVA_HOME` environment variable correctly set.
- **Docker** installed for local image building and testing.

## Steps for Deployment

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

## Automated Pipeline

Upon pushing changes to the repository, an automated pipeline is triggered. The pipeline is customised for your implementation of the FX Platform.

This pipeline performs several actions:

- **Builds the Application**: Compiles your code, ensuring it's ready for deployment.
- **Runs Tests**: Executes predefined tests to verify the functionality of your application.
- **Builds and Pushes Docker Image**: Creates a Docker image of your application and pushes it to a configured Docker registry.

Following the successful execution of these steps, the pipeline communicates with the FX platform to deploy your application. This involves:

- **Launching the Container**: Your application's container is launched into the 'fx-k8x' namespace.
- **Route Creation**: A route is created in APISix to make your application accessible.
- **Security Measures**: If specified, routes are secured according to the configurations detailed in subsequent sections of the documentation.


## Building Image for Local Testing of the Server

After successfully generating your server code stubs from the OpenAPI specification, the next step involves creating a local Docker image. This image facilitates testing your server in an environment that closely mimics the production setup. To accomplish this, you need to utilize the Dockerfile provided in your server directory. Follow these steps to build your Docker image:

1. **Navigate to the Server Directory**: First, ensure you are in the directory where your server code and the Dockerfile reside. This is typically the `server` directory created during the code generation process.

   Open a terminal or command prompt, and change to the server directory using the `cd` command. For example:
   ```bash
   cd path/to/your/server
   ```
   Replace `path/to/your/server` with the actual path to your server directory.

2. **Build the Docker Image**: With the Dockerfile in place, you can now build your Docker image. Use the Docker `build` command followed by the `-t` option to tag your image, making it easier to identify and manage. For instance, to tag and build the image as `test`, run:
   ```bash
   docker build -t test .
   ```
   Here, `-t test` assigns the tag `test` to your Docker image, and the `.` specifies that Docker should look for the Dockerfile in the current directory.

3. **Verify the Image Creation**: After the build process completes, you can verify that your Docker image has been created and tagged correctly by listing all Docker images:
   ```bash
   docker images
   ```
   Look for the `test` tag in the output list to confirm your image is ready.

4. **Run Your Docker Image**: To start a container from your newly created image, use the Docker `run` command. For example:
   ```bash
   docker run -d -p 8080:8080 test
   ```
   This command runs your Docker container in detached mode (`-d`), maps port 8080 of the container to port 8080 on your host (assuming your server listens on port 8080), and uses the `test` image.

By following these steps, you've built a Docker image from your server code stubs and can proceed with local testing. This approach ensures that your server behaves as expected in a controlled environment before deploying it to production.

## The Swagger UI
Integrating Swagger UI into your server provides a convenient and interactive documentation interface for your API. Swagger UI allows developers and users to visualize and interact with the API's resources without having any of the implementation logic in place. It's particularly useful for understanding the capabilities of your API and for testing purposes. If your server is set up to serve Swagger UI, accessing it is straightforward.

### Accessing Swagger UI

Once your server is running, you can access the Swagger UI by navigating to the `/ui` endpoint in your web browser. Here's how:

1. **Start Your Server**: Ensure your server is running. If you're using Docker, as mentioned previously, you might have started your server using a command similar to:
   ```bash
   docker run -d -p 8080:8080 your_image_name
   ```
   Replace `your_image_name` with the actual name of your Docker image.

2. **Open Swagger UI**:
   - Open a web browser of your choice.
   - In the address bar, type the URL that points to the `/ui` endpoint of your server. Assuming your server is accessible locally and uses port `8080`, the URL would be:
     ```
     http://localhost:8080/ui
     ```
   - Press Enter to navigate to the URL.

3. **Interact with Your API**: Once the Swagger UI loads, you'll see a list of all the endpoints defined in your OpenAPI specification. You can:
   - Expand each endpoint to view its documentation, including the HTTP method, parameters, request body schema, and response models.
   - Try out the endpoints directly from the browser by filling in the required parameters and executing the requests. Swagger UI will display the request as it's sent to the server and the response received.

### Tips for Using Swagger UI

- **Security**: If your API includes endpoints that require authentication, Swagger UI typically provides a way to authenticate (e.g., entering an API key or JWT token) so you can test protected endpoints.
- **Customization**: Swagger UI can be customized to match your branding or to enhance its functionality. Check the Swagger UI documentation for customization options.
- **Feedback and Testing**: Use Swagger UI as a tool for gathering feedback from potential API users and for preliminary testing of your API's functionality.

By visiting the `/ui` endpoint, you leverage Swagger UI as an effective tool for exploring and testing your API in a user-friendly manner. This not only aids in development and testing but also improves the overall developer experience for those consuming your API.

## Securing Endpoints

To secure endpoints, refer to the detailed instructions provided in the documentation. This typically involves specifying security schemes in your `openapi.yaml` and configuring the necessary authentication and authorization mechanisms within the FX platform's deployment settings.

## Conclusion

By following these steps, developers can efficiently deploy OpenAPI compliant servers using the FX platform. This process not only automates the deployment pipeline but also ensures that applications are scalable, secure, and ready for production environments.