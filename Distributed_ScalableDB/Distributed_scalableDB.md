# Distributed - Scalable Databases
Cassandra is the the distributed-scalable database of choice. Cassandra is another NoSQL database that was developed initially by Facebook. These are the features of Cassandra:

1. Highly scalable: It can be easily expanded or upgraded on demand.
2. Fault-tolerant: Cassandra was designed to continue operating uninterrupted despite the failure of a component. The same copy of data is stored in multiple locations as a cluster. Data is available on multiple computers at once.
3. High availability (HA): HA refers to the continuous availability of applications and data to authorized users and includes all aspects of a hardware and software environment that could fail, such as disk, CPU, mainframe, physical site, or regional outage.
4. Decentralized: Cassandra can be spread out across many servers while providing highly available service with no single point of failure.
5. Nodes are set up in the form of clusters: A node in Cassandra contains the actual data. A cluster is a collection of nodes that represent a single system. Every node is independent.

In Cassandra, a database or data container is called a keyspace. Each keyspace is a separate entity created for each application within a cluster. In a Cassandra cluster, a keyspace is an outermost object that determines how data replicates on nodes. Keyspaces consist of core objects called column families (which are like tables in RDBMS), rows indexed by keys, datatypes, data center awareness, replication factor, and keyspace strategy.

First, you need to run a Cassandra container in Docker to practice interfacing with the database. To download a Cassandra Docker image and run it, execute the following command from a Windows PowerShell or from a Terminal window on a Mac:

`docker run -p 9042:9042 --name some-cassandra -d cassandra`

Open Docker desktop and verify that the Cassandra image is up and running

You can use Python code to access the Cassandra database. To do so, you will need to install Python libraries for Cassandra:

`pip install cassandra-driver`

The sample code below will create a keyspace, also known as a database, in Cassandra called employees. It will then create a table called employee and insert three employees into the table.

``` python
from cassandra.cluster import Cluster
keyspace = None
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect(keyspace)

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS employees
    WITH REPLICATION = {'class':'SimpleStrategy','replication_factor' :1};
    """)

session.set_keyspace('employees')

session.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        EMPLOYEE_ID int PRIMARY KEY,
        FIRST_NAME text,
        LAST_NAME text,
        AGE int
    );
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (123450, 'John', 'Doe', 33);
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (123678, 'Mary', 'Jane', 21);
""")

session.execute("""
    INSERT INTO employee (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, AGE)
    VALUES (678123, 'Peter', 'Gabriel', 65);
""")
```

The sample code below reads the data from the employees keyspace:
``` python
from cassandra.cluster import Cluster

cluster = Cluster(['localhost'], port=9042)
session = cluster.connect('employees', wait_for_all_pools=True)
session.execute('USE employees')
rows = session.execute('SELECT * FROM EMPLOYEE')
for row in rows:
    print(row)
```

You have now interfaced with Cassandra using a Python client. Another method to do this is to use the cqlsh Terminal command line. To launch cqlsh, open the Docker desktop and select the ???CLI??? option for the Cassandra container. CLI is a command line tool that allows you to communicate with the Docker server

Enter the `cqlsh` command and select the ???Enter??? key.

You are now connected directly to the Cassandra database. There is no need to write Python code to select or insert rows.

Enter `use employees;`. Don???t forget the ???;??? at the end of the command to tell `cqlsh` that you finished the command, and select the ???Enter??? key.

Now enter select * from employee; to get the employees.

For more information on large active datasets in Cassandra, reference the Apache Cassandra Documentation. 