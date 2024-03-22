---
title: "FX Event Bridge API"
linkTitle: "FX Event Bridge API"
tags: [quickstart, integration]
categories: ["Knowledge Base"]
weight: 220
description: >-
  How to send events to the {{< param replacables.brand_name  >}} Platform using the FX Event Bridge API
---

# FX Event Bridge API 

## Overview

The FX Event Bridge API provides a set of webhook endpoints for receiving out-of-cluster events. These events are converted to CloudEvents and routed into the FX platform for triggering executions. This API is essential for external applications that need to interact with the FX platform by sending trigger events.

## Authentication

To use the FX Event Bridge API, an access token must be provided in the request header. There are two types of authentication supported:

- **API Key Authentication**: Requires an access token to be included in the `X-API-KEY` header.
- **Secret Key Authentication**: Requires a secret key to be included in the `X-Hub-Signature-256` header.

Access tokens and secret keys must be created in the management UI of the FX platform and provided by the submitter of the request.

## API Endpoints

### Event Submission

- **POST /fx/events**

  Submits a new event to be processed by the FX platform.

  **Request Body**:
  - `event_source`: Source of the event.
  - `event_type`: Type of the event.
  - `payload`: Event data in JSON format.

  **Response**:
  - Returns a `CreateEventResponse` object containing the `cid` (Correlation ID) and `eventType`.

- **POST /fx/events/generic**

  Submits a new generic event to be processed.

  **Request Body**:
  - Generic event data in JSON format.

  **Response**:
  - Similar to the `/fx/events` endpoint, returns a `CreateEventResponse` object.

- **POST /fx/events/webhook**

  Submits a new generic event from a webhook.

  **Request Body**:
  - Generic event data in JSON format.

  **Response**:
  - Similar to the `/fx/events` and `/fx/events/generic` endpoints, returns a `CreateEventResponse` object.

### Event and Execution Status

- **GET /fx/cid/{cid}**

  Retrieves the status of executions for a given Correlation ID (CID).

  **Parameters**:
  - `cid`: CorrelationID of the event.

  **Response**:
  - Returns a `CIDResult` object containing the CID and an array of `ExecutionResult` objects detailing each execution's status.

- **GET /fx/executions/{execution_id}**

  Retrieves the status of a specific execution by its ID.

  **Parameters**:
  - `execution_id`: The ID of the execution to retrieve.

  **Response**:
  - Returns an `ExecutionResult` object containing details about the execution, such as data, datetime, execution time, service, and status.

## Data Models

### CIDResult

- `cid`: String representing the Correlation ID.
- `executions`: Array of `ExecutionResult` objects.

### CreateEventResponse

- `cid`: Correlation ID of the created event.
- `eventType`: Type of the event.

### EventRequest

- `event_source`: Source of the event.
- `event_type`: Type of the event.
- `payload`: Event data.

### ExecutionResult

- `data`: Data saved within the execution.
- `datetime`: Date and time of the execution.
- `execution_id`: Execution ID.
- `execution_time`: Total time for the execution.
- `service`: Name of the service.
- `status`: Status of the execution (e.g., pending, in progress, completed, failed, skipped).

### GenericEventRequest

- Represents generic event data in JSON format.

## Security Schemes

- **ApiKeyAuth**: Authentication via `X-API-KEY` header.
- **SecretKeyAuth**: Authentication via `X-Hub-Signature-256` header.

For further assistance or to report issues, please contact the FX platform support team.
