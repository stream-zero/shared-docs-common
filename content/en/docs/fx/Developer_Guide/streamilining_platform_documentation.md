---
title: "Streamlining Platform Documentation"
linkTitle: "Streamlining Platform Documentation"
tags: [quickstart, integration, documentation]
categories: ["Knowledge Base"]
weight: 221
description: >-
  Streamlining Service Documentation and Discoverability : A Dynamic Approach with AsyncAPI
---

## Streamlining Service Documentation and Discoverability: A Dynamic Approach with AsyncAPI

The FX platform employs CloudEvents as the foundational format for event transmission across its internal Kafka bus, demonstrating our dedication to leveraging industry standards and specifications to achieve superior interoperability and efficiency. Our commitment to standards, however, extends beyond just CloudEvents. We also embrace OpenAPI and AsyncAPI, two critical standards that significantly contribute to our ecosystem's robustness. By integrating OpenAPI and AsyncAPI with the platform's internal Schema Registry, we not only adhere to well-recognized standards but also enhance the platform's discoverability.

Moreover, as detailed in the following sections of this article, our platform employs a 'dynamic documentation' strategy. This innovative approach significantly reduces the burden on developers and architects to manually update extensive API documentation. Through this method, we aim to streamline the documentation process, ensuring it remains current with minimal effort, a practice that sets a new standard in the industry for maintaining API documentation.

## OpenAPI Integration

The FX Event Bridge API embraces OpenAPI to facilitate seamless integration with external systems through a standardized HTTP-based API. This adoption simplifies the process for external applications to connect with our platform, ensuring a smooth and consistent integration experience. 

Enhancing this integration framework, the FX platform repositories are equipped with a master template designed for the creation of new OpenAPI-based servers. This template leverages Swagger code generation tools, streamlining the development of API servers that are fully compliant with the OpenAPI specification. 

To further support the deployment and operational security of these APIs, the integration pipeline has been designed to automate the launching of servers into the cluster and secure the APIs with token-based authentication, supported by Keycloak. Additionally, this pipeline includes steps for running unit and integration tests to ensure code quality and functionality before deployment. It also handles the building of the container image, which is a necessary step prior to launching on the platform. 

This approach ensures that APIs are not only deployed efficiently but are also tested and secured according to predefined standards, facilitating a more streamlined and reliable integration process within the FX platform environment.

## AsyncAPI Integration

On the other hand, AsyncAPI is instrumental in documenting the platform's event and service definitions. This serves multiple purposes: 

* it acts as a comprehensive reference for understanding platform capabilities
* enables the export of definitions to other systems
* enhances visibility through catalog-based discovery. 

Beyond documentation, AsyncAPI is can be leveraged for code generation and schema validation within services, streamlining the development process and ensuring adherence to defined schemas.

In the context of avoiding the cumbersome task of writing API specifications, which can impede development velocity, it's crucial to note that AsyncAPI is not employed within the core workflow of our platform. Instead, we opt for an internal `manifest.json` method for outlining service interactions with the platform. This strategic choice is made to prioritize development speed, ensuring that our core development processes stay agile and efficient. This approach allows for a more streamlined development cycle, reducing the overhead associated with the manual crafting of API specifications and thereby maintaining a focus on rapid, iterative development.

In this article, we will delve deeper into the role of AsyncAPI within the FX platform. We'll explore how it is utilized to capture the current state of the platform, how the published AsyncAPIs can be employed to validate message payloads, and how they facilitate code generation. This discussion aims to provide a clearer understanding of AsyncAPI's value and its strategic application within our ecosystem, reinforcing our commitment to standardization and specification-first development.

This article assumes that the reader possesses a basic understanding of AsyncAPI and its associated terminology. For those seeking to enhance their knowledge or clarify specific concepts, we recommend visiting the official AsyncAPI website. This resource provides comprehensive information and guidance on AsyncAPI, facilitating a better grasp of the subject matter discussed herein.

## Events and Services

The core elements of an event-driven platform are the events themselves and the services that either consume or publish these events. For events, our main concern is to verify the integrity and validity of their payloads. On the other hand, for services, our focus is on accurately documenting the events they consume and publish. 

The FX platform employs a `manifest.json` file for each service to outline the interactions between services and the platform. This file specifies `trigger_events` and `output_events` to delineate these interactions clearly.

Regarding event handling, our approach is somewhat flexible; it is not mandatory to define or register an event's schema before sending an event through the system. The platform continuously monitors the event stream, dynamically updating a schema registry in the background. These schemas are subsequently made accessible through the user interface. Payload validation is delegated to the consuming service, a decision made to preserve both development momentum and the routing mechanism's efficiency. 

When the platform detects a 'new event type'—characterized by a schema not yet recorded in the schema registry—it automatically adds this new schema. This action marks the initial update to the schema registry, triggered by the identification of an event type previously unknown to the system. This automation significantly simplifies the workflow for developers and architects by eliminating the need to manually define asynchronous schemas from the outset. Consequently, the development process is streamlined, allowing the focus to shift towards service development and enhancement rather than the labor-intensive management of event schemas. 

Once an event's schema is detected for the first time and recorded in the registry, it is considered 'frozen.' Any subsequent modifications to this event's schema require direct management within the registry. This approach strikes a careful balance between maintaining system flexibility and ensuring the consistency and reliability of event handling, providing a structured yet adaptable framework for event schema management.

## An Event AsyncAPI Specification Sample

The definition of event schemas within our system follows a structured yet flexible approach. To illustrate, consider a typical event schema example. Notably, in this schema, the message payload is not assigned to a specific channel. This design choice is intentional and serves two primary purposes:

1. **Unified Channel Strategy**: By routing all messages through a single channel in Kafka, we avoid the complexity and overhead associated with managing thousands of Kafka topics. This streamlined approach enhances the efficiency of message processing and simplifies the architecture of our event-driven system.

2. **Centralized Schema Catalog**: The platform maintains a centralized catalog of messages, adopting an 'uber specification' model. This model aggregates the definitions of various events and references the payload schemas, which are maintained separately. This centralized approach facilitates easier management and discovery of schemas, ensuring that the system remains organized and that schemas are easily accessible for validation and other purposes.

```yaml
asyncapi: 3.0.0
info:
  title: Git Repository Events
  version: 1.0.0
  description: This specification covers events related to Git repository operations.
components:
  messages:
    'fx.container.repo.update': # Use quotes to clearly define the name
      summary: An event indicating an update to a git repository.
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

## A Service AsyncAPI Specification Sample

The `manifest.json` file, integral to each service within the FX platform, is structured as a JSON document incorporating FX-specific attributes. Key among these attributes are `trigger_events` and `output_events`, which orchestrate the service's publish/subscribe mechanisms. The design and periodic updates of the `manifest.json` are executed with AsyncAPI compatibility as a guiding principle. However, this process adopts a streamlined approach, aiming to enhance development speed and the clarity of the document. This efficiency-focused strategy ensures that the `manifest.json` remains straightforward to use and modify, facilitating a smoother development workflow.

The `manifest.json` is structured in such a way that it can be directly transformed into AsyncAPI definitions. This transformation process allows for a seamless integration of service-specific configurations into the broader AsyncAPI ecosystem, ensuring that services can be easily documented and understood within the context of event-driven architecture. 

The generation of AsyncAPI documentation for a service is dynamically handled by the platform at the time of service creation, and it is subsequently updated whenever changes are made to the `manifest.json` file by the service. This dynamically generated AsyncAPI documentation, in YAML format, is then registered within the platform's schema registry, specifically APICurio. This process facilitates platform developers in maintaining a comprehensive overview of the services operational on the platform. Additionally, it simplifies the task of keeping the service documentation current and reflective of the actual service functionalities and interfaces. This dynamic approach to documentation ensures that the information available to developers is always accurate, aiding in better service integration and collaboration across the platform.

For attributes that do not directly relate to the event types a service publishes or subscribes to, they are incorporated into the `info` section of the AsyncAPI document. To maintain clarity and avoid conflicts with standard AsyncAPI attributes, these additional attributes are prefixed with `x-fx`. This naming convention signifies that the attributes are extensions specific to the FX platform, providing additional context or metadata that enhances the understanding or functionality of the service without cluttering the core AsyncAPI definitions.

This method of extending the AsyncAPI specifications with `x-fx` prefixed attributes in the `info` section allows for a flexible yet organized way to include FX-specific information. It ensures that all necessary details are captured and conveyed in the service documentation, while also adhering to the best practices of specification extension and customization.

```yaml
asyncapi: 3.0.0
info:
  title: Account Service
  version: '1.0.0'
  description: |
    Manages user accounts in the system.
  x-fx-schedule: '* * * * *'
  x-fx-active: true
  

servers:
  production:
    host: kafka://broker.core
    protocol: kafka
    description: Kafka broker

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

