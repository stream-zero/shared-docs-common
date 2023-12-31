---
title: Apache Drill
hide_title: true
sidebar_position: 6
version: 1
---

## Apache Drill

### SQLAlchemy

The recommended way to connect to Apache Drill is through SQLAlchemy. You can use the
[sqlalchemy-drill](https://github.com/JohnOmernik/sqlalchemy-drill) package.

Once that is done, you can connect to Drill in two ways, either via the REST interface or by JDBC.
If you are connecting via JDBC, you must have the Drill JDBC Driver installed.

The basic connection string for Drill looks like this:

```
drill+sadrill://<username>:<password>@<host>:<port>/<storage_plugin>?use_ssl=True
```

To connect to Drill running on a local machine running in embedded mode you can use the following
connection string:

```
drill+sadrill://localhost:8047/dfs?use_ssl=False
```

### JDBC

Connecting to Drill through JDBC is more complicated and we recommend following
[this tutorial](https://drill.apache.org/docs/using-the-jdbc-driver/).

The connection string looks like:

```
drill+jdbc://<username>:<passsword>@<host>:<port>
```

### ODBC

We recommend reading the
[Apache Drill documentation](https://drill.apache.org/docs/installing-the-driver-on-linux/) and read
the [Github README](https://github.com/JohnOmernik/sqlalchemy-drill#usage-with-odbc) to learn how to
work with Drill through ODBC.
