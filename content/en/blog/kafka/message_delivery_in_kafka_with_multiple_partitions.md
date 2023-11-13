---
title: "Understanding Message Delivery in Kafka with Multiple Partitions"
linkTitle: "Understanding Message Delivery in Kafka with Multiple Partitions"
tags: [kafka, microservices, distributed systems, integration] 
categories: ["kafka"]
weight: 101
description: >-
     Understanding Message Delivery in Kafka with Multiple Partitions
---

This is part of an ongoing series on Apache Kafka examining various aspects related to developing applications on Apache Kafka.

In this post we take a look at how we can ensure ‘nearly even’ distribution of messages across consumers which are part of a consumer group. A challenge which we often face with event driven microservices.

One of Apache Kafka’s core concepts is the topic, a category or feed name to which records are published. Topics in Kafka are divided into partitions, which allow for the parallel processing of data.

However, the presence of multiple partitions raises questions about how messages are delivered and consumed. This article will explore how Kafka manages message distribution across partitions and how consumers are assigned messages.

## Kafka Partitions and Message Ordering

A Kafka topic can be split into multiple partitions, each of which is an ordered, immutable sequence of records. Partitions are distributed across different brokers in the Kafka cluster to ensure load balancing. The key benefits of partitions are scalability and parallelism, as multiple consumers can read from multiple partitions simultaneously.

## Message Ordering

Within a partition, messages are guaranteed to be in the order they were written. However, if a topic has multiple partitions, there is no guarantee of ordering across the entire topic-only within each partition.

## Producer Configuration for Message Distribution

When a producer sends a message to a Kafka topic, it can specify a key for the message. The producer uses a partitioner to decide which partition to send the message to. By default, Kafka provides a partitioner that hashes the message key and maps it to a specific partition. If no key is specified, the producer round-robins the messages across all partitions.

## Partitioner Configuration

Producers can use custom partitioners if specific distribution logic is required. For example, a custom partitioner could ensure that messages with certain attributes always go to the same partition.

## Consumer Message Assignment

Kafka consumers read messages from the partitions of a topic. Consumers can be grouped together into a consumer group for a topic, and each consumer in the group reads from exclusive partitions of the topic.

## Consumer Groups and Partition Assignment

When multiple consumers are part of a single consumer group, Kafka ensures that each partition is only consumed by one consumer from that group. **If there are more consumers than partitions, some consumers will be idle. If there are more partitions than consumers, consumers will be assigned multiple partitions.**

## Partition Assignment Strategies

Kafka provides several assignment strategies that can be leveraged according to the specific needs of the application:

- **Range Assignor** (`org.apache.kafka.clients.consumer.RangeAssignor`): This strategy assigns partitions on a per-topic basis. It works by dividing the sorted list of partitions by the number of consumers and assigning each consumer a contiguous segment of partitions for each topic. This can lead to an uneven distribution if the number of partitions is not a multiple of the number of consumers.
- **Round Robin Assignor** (`org.apache.kafka.clients.consumer.RoundRobinAssignor`): This strategy assigns partitions to consumers in a round-robin fashion, regardless of the topic. It ensures a uniform distribution of partitions across consumers, which can be beneficial when the workload is relatively uniform and the processing time for each message is similar.
- **Sticky Assignor** (`org.apache.kafka.clients.consumer.StickyAssignor`): The Sticky Assignor aims to achieve a balanced distribution while also minimizing the movement of partitions between consumers during rebalances. This strategy tries to preserve the existing assignment as much as possible, which can be useful to maintain locality and cache warmth, leading to more efficient processing.
- **Cooperative Sticky Assignor** (`org.apache.kafka.clients.consumer.CooperativeStickyAssignor`): This strategy extends the Sticky Assignor logic by allowing for cooperative rebalancing. Unlike the eager rebalancing strategy where consumers have to stop processing messages during a rebalance, the Cooperative Sticky Assignor allows consumers to continue processing messages for partitions that they retain throughout the rebalance. This can lead to less disruption and more even distribution as the assignment shifts incrementally.

## Rebalancing and Consumer Coordination

Kafka uses a group coordinator and a consumer coordinator to manage the members of a consumer group and their partition assignments. When a consumer joins or leaves a group, or when the partitions of a topic change, a rebalance is triggered. During a rebalance, consumers temporarily stop reading messages and wait until the new partition assignment is received.

## Configuration Settings for Distribution Management

Kafka provides several configuration settings that control message distribution and consumption:

- `partition.assignment.strategy`: Determines the partition assignment strategy used by the consumer.
- `max.poll.records`: Controls the maximum number of records a consumer can fetch in a single poll. This is a consumer setting.
- `session.timeout.ms`: The timeout used to detect consumer failures. If a consumer doesn't send a heartbeat within this interval, a rebalance will be triggered.
- `heartbeat.interval.ms`: Specifies the expected time between heartbeats to the consumer coordinator.

## Rebalancing and Consumer Coordination

To enable a nearly even distribution of messages across consumers in a consumer group, Kafka offers several mechanisms and configurations that can be fine-tuned. One of the most important is the partition assignment strategy.

To enable a nearly even distribution of messages across consumers, the `StickyAssignor` or `CooperativeStickyAssignor` are often preferred. They not only balance the partition assignment across consumers but also reduce the churn of partitions moving between consumers during rebalances, which can be particularly disruptive. By maintaining a stable partition assignment, these strategies can help ensure that each consumer is processing a roughly equal share of the message load.

In addition to choosing the right assignor, it’s important to configure the number of partitions appropriately. Having a higher number of partitions than consumers can allow for more granular balancing and can accommodate an increase in the number of consumers without requiring a change to the topic configuration.

Lastly, monitoring the consumer lag and throughput can help identify imbalances in the message distribution. If certain consumers are consistently lagging behind others, it may indicate a need to adjust the partition assignment strategy or reevaluate the partitioning of the topic itself.

Additionally, it’s crucial to ensure that the number of partitions for a topic is at least as great as the number of consumers in the consumer group to avoid idle consumers. If the consumers have varying processing capabilities, you might consider implementing a custom partition assignment strategy that takes into account the consumer’s capacity or current load.

Another factor that can affect the distribution of messages is the use of message keys. If keys are used, ensure that they are well-distributed themselves, as Kafka will use these keys to distribute messages to partitions. A poorly chosen key, such as one that always hashes to the same partition, can lead to an uneven load.

On the consumer side, the `max.poll.records` configuration controls the maximum number of records a consumer can fetch in a single poll. By tuning this number, you can prevent a single consumer from being overwhelmed with too many messages while others remain idle.

Lastly, monitoring and adjusting the consumer’s `session.timeout.ms` and `heartbeat.interval.ms` settings can help maintain a stable consumer group membership, which is essential for consistent message distribution. Frequent rebalancing caused by timeouts can disrupt the even distribution of messages, as consumers may spend more time coordinating than processing messages.

By carefully managing these configurations and strategies, you can achieve a nearly even distribution of messages across consumers in a Kafka consumer group, leading to more efficient processing and better overall performance of your streaming application.