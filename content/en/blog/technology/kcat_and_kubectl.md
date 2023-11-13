---
title: "Using `kcat` with `kubectl` for Kafka Diagnostics in Kubernetes"
linkTitle: "Kafka Diagnostics in Kubernetes"
tags: [kafka, devops, kubectl, kcat] 
categories: ["technology"]
weight: 102
description: >-
     When diagnosing issues with Kafka running in a Kubernetes cluster, it can be useful to run diagnostic tools directly within the cluster.
---

### Using `kcat` with `kubectl` for Kafka Diagnostics in Kubernetes

When diagnosing issues with Kafka running in a Kubernetes cluster, it can be useful to run diagnostic tools directly within the cluster. One such tool is `kcat` (formerly known as `kafkacat`), a versatile command-line utility to produce and consume Kafka messages. In this article, we'll explain how to run `kcat` as a temporary pod in a Kubernetes cluster using the `kubectl` command. The kcat repo is here:  https://github.com/edenhill/kcat 

#### The Command:

```bash
kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -L -b fx-kafka.core -G test2 minio
```

#### Breaking it Down:

1. **`kubectl run`**: This is the primary command to run a particular container in a Kubernetes cluster. It creates a new pod with the specified container and runs it.

2. **`-it`**: These flags stand for "interactive" and "tty". They allow you to interact with the container (in this case, `kcat`) directly from the terminal.

3. **`-n fx-fx`**: This specifies the namespace in which the pod will be created. Here, the namespace is `fx-fx`.

4. **`kcat`**: This is the name of the pod that will be created.

5. **`--image=edenhill/kcat:1.7.1`**: This specifies the Docker image to use for the pod. In this case, we're using the `kcat` image version `1.7.1` from the `edenhill` repository.

6. **`--rm`**: This flag ensures that the pod is automatically deleted once it's terminated. This is useful for temporary diagnostic tasks as it cleans up resources after the task is completed.

7. **`--`**: This delimiter is used to separate the `kubectl run` parameters from the arguments that will be passed to the `kcat` tool.

8. **`-L`**: This is a `kcat` flag that lists all topics, partitions, and brokers in the cluster.

9. **`-b fx-kafka.core`**: The `-b` flag specifies the broker (or brokers) to connect to. Here, `kcat` will connect to the broker at `fx-kafka.core`.

10. **`-G test2 minio`**: The `-G` flag is used to specify a consumer group. In this case, `kcat` will join the consumer group `test2` and consume messages from the `minio` topic.

---

By running the above command, you'll be able to interactively use `kcat` within your Kubernetes cluster to diagnose issues with your Kafka setup. This approach is particularly useful because it allows you to run diagnostic tools without needing to install them on your local machine or modify existing pods in the cluster.



### More examples - Mileage can vary

The following are samples from the kcat page adapted to kubectl. Not all commands work as expected, but this could be due to me running a non-standard Kafka on a k3s cluster.



1. **Balanced KafkaConsumer for Multiple Topics**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -b mybroker -G minio ferris.events
   ```

2. **Produce Messages from System Logs with Compression**:
   ```bash
   kubectl exec -it [YOUR_LOG_POD_NAME] -- tail -f /var/log/syslog | 
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -b mybroker -t syslog -z snappy
   ```

3. **Read Messages from Kafka 'syslog' Topic**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -b mybroker -t syslog
   ```

4. **Produce Messages from File**:
   *First, you'd need to copy the file to the pod or have it available via a shared volume.* This requires pod to b
   
   ```bash
   kubectl cp myfile1.bin kcat-pod:/tmp/
   kubectl exec -it kcat-pod -- kcat -P -b mybroker -t filedrop -p 0 /tmp/myfile1.bin
   ```
   
5. **Output Consumed Messages in JSON Envelope**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -b mybroker -t syslog -J
   ```

6. **Decode Avro Message and Extract "age" Field**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- 
   -b mybroker -t ledger -s value=avro -r http://schema-registry-url:8080 | jq .payload.age
   ```

7. **Output Consumed Messages According to Format String**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- 
   -b mybroker -t syslog -f 'Topic %t[%p], offset: %o, key: %k, payload: %S bytes: %s\n'
   ```

8. **Metadata Listing**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- -L -b mybroker
   ```

9. **JSON Metadata Listing**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- 
   -b mybroker -L -J | jq .
   ```

10. **Consume Messages Between Two Timestamps**:
   ```bash
   kubectl run -it -n fx-fx kcat --image=edenhill/kcat:1.7.1 --rm -- 
   -b fx-kafka.core -C -t minio -o s@1568276612443 -o e@1568276617901
   ```

---

Remember, when using `kubectl` with `kcat` in this manner, you're creating temporary pods to run these commands. Ensure you have the necessary permissions and resources in your Kubernetes cluster to execute these commands.