---
title: "{{< param replacables.brand_name  >}} K8X"
linkTitle: "{{< param replacables.brand_name  >}} K8X"
weight: 102
description: >
  Overview and in-depth introduction to {{< param replacables.brand_name  >}} Event Driven Kubernetes.
---


## What is {{< param replacables.brand_name  >}} K8X?

{{< param replacables.brand_name  >}} K8X brings event driven automation to Kubernetes. 

With K8X you can create service flows which span multiple containers written in different programming languages. K8X takes over the responsibility of launching the right container when an event arrives that is mapped to the container. Further it provides the container with the incoming parameters, the service specific configurations and secrets injected into the container environment.

Since each service or container is invoked upon an event trigger, they (service, container) are dormant and require no compute resources.

The event driven nature of K8X makes it not only easy to use and fast to deploy, it brings unprecedented levels of resources efficiency as well as decreases resource contention to any Kubernetes Cluster.

## How it works
The following is a brief explanation of how K8X works.

* Edge Adapters are responsible for sourcing events from external systems, converting the incoming events into cloud events and forwarding them to the appropriate topic in Kafka. 
* These events are consumed by the K8X Hub which looks up the mapping of the event to the target services.
* The K8X hub then deploys the appropriate service/container and injects the event parameters, service configs and secrets to the container environment.
* The container executes the service.
* The K8X hub collects the logs from the container for monitoring of the container status.




{{< param replacables.brand_name  >}} K8X aims to make it easy to build event-driven microservices in polyglot environments. As such it gives you complete freedom in selecting the language of your choice. 

In order to 'event-enable' a service K8X requires 3 artefacts to be created.
* The manifest.json file: Which describes your service to the platform.
* The deployment.yaml: A standard kubernetes deployment file which defines your Kubernetes deployment.

Optional Files
* The parameters.json file: Which can be used to define UI Forms attached to the service for manaully trigerred runs. Please read the section on parameters.json to understand the structure of this file.
* The configs.json file: Defines configurations of the service.
* The secrets.json file: Any secrets that are to be associated with the service. These will be injected to the container on launch. 


# The manifest.json 
The following is a sample manifest.json file.
```json
{
  "name": "k8s_test_job",
  "type": "k8s_job",
  "description": "Deploying k8 job",
  "allow_manual_triggering": true,
  "active": true,
  "trigger_events": ["ferris.apps.minio.file_uploaded"],
  "tags": ["k8s"]
}
```


The following table describes the attributes of the manifest.json file.


| Attribute               | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| name                    | Name of the service. Spaces will be replaced by underscores. |
| type                    | The type of the service must always be 'k8x_job'             |
| description             | Description of the service which will be displayed in the UI. |
| allow_manual_triggering | Values are either 'true' or 'false' . Defines whether the service may be trigerred manually from the UI. Which normally means the service is either trigerred from a micro-ui or does not expect any event parameters. |
| active                  | Values are either 'true' or 'false' .  Can be used to selectively deactivate the service. |
| trigger_events          | An array of trigger events. The service will be trigerred when any of these events arrive on the platform. |
| tags                    | An array of tags. Tags are used for organising and finding related services easily. |

# The deployment.yaml file
The following is a sample deployment.yaml file

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-world
spec:
  template:
    spec:
      containers:
        - name: hello-alpine
          image: frolvlad/alpine-bash
          command: [ "/bin/bash", "-c" ]
          args: [ "echo BEGIN; env; sleep 5; ls -la /usr/bin; echo DONE!" ]
          env:
            - name: SERVICE_PORT
              value: "80"
      restartPolicy: Never
```

The above is a standard kubernetes job deployment yaml file. As you will note there is nothing special about it. When the above file is processed by K8X it will add the incoming parameters, service secrets and configs into the environment. 