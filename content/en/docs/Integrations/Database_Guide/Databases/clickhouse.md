---
title: Clickhouse
hide_title: true
sidebar_position: 15
version: 1
---

## Clickhouse

To use Clickhouse with {{< param replacables.brand_name  >}} you will need to add the following Python libraries:

```
clickhouse-driver==0.2.0
clickhouse-sqlalchemy==0.1.6
```

If running {{< param replacables.brand_name  >}} using Docker Compose, add the following to your `./docker/requirements-local.txt` file:

```
clickhouse-driver>=0.2.0
clickhouse-sqlalchemy>=0.1.6
```

The recommended connector library for Clickhouse is
[sqlalchemy-clickhouse](https://github.com/cloudflare/sqlalchemy-clickhouse).

The expected connection string is formatted as follows:

```
clickhouse+native://<user>:<password>@<host>:<port>/<database>[?options…]clickhouse://{username}:{password}@{hostname}:{port}/{database}
```

Here's a concrete example of a real connection string:

```
clickhouse+native://demo:demo@github.demo.trial.altinity.cloud/default?secure=true
```

If you're using Clickhouse locally on your computer, you can get away with using a native protocol URL that
uses the default user without a password (and doesn't encrypt the connection):

```
clickhouse+native://localhost/default
```
