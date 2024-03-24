---
title: "Specification-First Development"
linkTitle: "Specification-First Development"
tags: [basic, development, design]
categories: ["Knowledge Base"]
weight: 222
description: >-
     Specification-First Development on the FX Platform.
---
# Embracing Specification-First Development on the FX Platform: A Comprehensive Guide

Specification-first development is a methodology where the design of software applications starts with specifying what the application will do and how it will interact with other systems before any code is written. This approach is particularly beneficial in environments where clear communication between teams (such as frontend and backend teams) or between services is crucial. In the context of the FX platform, which supports both code-first and specification-first development, this article focuses on how to implement the latter, leveraging AsyncAPI for defining platform services and event specifications.

### Why Specification First?

Before diving into the how-to, it's worth understanding why a specification-first approach can be advantageous:

- **Clarity and Contract**: It ensures all stakeholders have a clear understanding of the system's functionalities and interactions before development begins.
- **Parallel Development**: Frontend and backend teams can work in parallel, as the specifications act as a contract between different parts of the system.
- **Tooling Support**: Tools can generate documentation, mock servers, and even skeleton code from the specifications, speeding up development and ensuring consistency.

### Implementing Specification First on the FX Platform

The FX platform uses AsyncAPI specifications to describe asynchronous events and services. These specifications are managed within APICurio, making them easily discoverable and manageable. Here’s how to get started with creating and applying these specifications:

#### 1. Create a Directory Structure

First, organize your specifications within a specific directory structure. This structure helps in maintaining a clear separation between different components of your system, such as events and services.

```
project-root/
├── components/
│   └── schemas/
│       └── messages/
└── services/
    ├── ServiceA/
    └── ServiceB/
```

- **components/schemas/messages/**: This directory will contain individual AsyncAPI specification files for each event your system can publish or subscribe to.
- **services/**: This directory contains subdirectories for each service, each of which will have its own AsyncAPI specification file.

#### 2. Create the YAML Files for Events and Services

For each event and service, create a YAML file that describes its specification. AsyncAPI offers a rich syntax for describing asynchronous events and the structure of the messages they carry.

##### Event Specification Sample:

```yaml
asyncapi: 3.0.0
info:
  title: Git Repository Events
  version: 1.0.0
  description: This specification covers events related to Git repository operations.
components:
  messages:
    'fx.git.repo.delete': # Use quotes to clearly define the name
      summary: An event indicating an delete of a git repository.
      contentType: application/json
      payload:
        type: object
        properties:
          image_name:
            type: string
            description: The name of the Docker image built from the updated repository.
          app_name:
            type: string
            description: The name of the application associated with the updated repository.
        required:
          - image_name
          - app_name
```

##### Service Specification Sample:

Note how except for the manifest.json attributes 'trigger_events' and 'output_events' all other attributes are added to the info section of the file along with 'x-fx' prefix.

```yaml
asyncapi: 3.0.0
info:
  title: account_service
  version: '1.0.0'
  description: |
    Manages user accounts in the system.
  x-fx-schedule: '5 * * * *'
  x-fx-active: true
  x-fx-allow_manual_triggering : true
  x-fx-entrypoint: 'app.py'
  x-fx-tags:
      - accounts
      - users

servers:
  production:
    host: kafka://fx-kafka:9093
    protocol: kafka
    description: FX Kafka broker

channels:
  'fx.events':
    address: 'fx.events'
    messages:
      userSignedUp:
        $ref: '../components/messages/userSignedUp'
      userStoredInDB:
        $ref: '../components/messages/userStoredInDB'

operations:
  userSignedUp:
    action: receive
    channel:
      $ref: "#/channels/fx.events"
  userStoredInDB:
    action: send
    channel:
      $ref: "#/channels/fx.events"
```

#### 3. Create a Zip Archive of the File

Once all your YAML files are ready and properly organized within the directory structure, create a zip archive of the entire structure. This makes it easier to upload and manage the specifications as a single unit.

#### 4. Upload the File to the UI

The FX platform provides a user interface for uploading your zip archive. This step integrates your specifications into the platform, making them part of the system's overall architecture.

#### 5. The Platform Creates Code Stubs

Upon uploading your specifications, the FX platform processes them and automatically generates code stubs for the required services. This significantly accelerates the development process by providing a solid foundation on which to build.

#### 6. Download the Code Stubs

Finally, download the generated code stubs from the platform. These stubs serve as the starting point for developing the actual logic of your services, already structured according to the specifications you defined.

### Conclusion

The specification-first approach, supported by the FX platform, offers a structured and efficient way to design and develop software systems. By defining clear specifications using AsyncAPI and organizing them within a well-structured directory system, teams can ensure consistency, facilitate parallel development, and leverage tools for automatic code generation. This methodology not only streamlines the development process but also enhances collaboration across different teams by establishing a clear contract for system interactions.