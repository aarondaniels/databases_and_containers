# Containers

A docker requires an image. This can be built from the ground up; however, in the case of database containers the images are already created and available for download. DockerHub(https://hub.docker.com) contains a registry of several images of databases that can be pulled and ran in a local environment. 

For example, search for MySQL docker image. Downloading the official docker image is acheieved by executing `docker pull mysql` into the terminal. 

Loading images from a registry is accomplished via a run command, `docker run [OPTIONS] IMAGE[:TAG| @DIGEST] [COMMAND] [ARG...]` At a minimum, running `docker run` and the name of an image should be satisfied. 

In the case of MySQL, the following command can be used, `docker run -p3306:3306--name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql`. In this case, a port is specified, then the container name, an environment variable that sets the password, and indication that it is detached, and finally an image. Of mention, the port mapping part of this command can be adjusted. Given the format XXXX:YYYY, X is the local port and Y is the docker port. 

To confirm connection with the MySQL database, use this file (show_databases.py). Alternatively, connect to it from MySQL workbench by creating an instance with the port and hostname. 

# Document Databases
*** MongoDB ***  is the document DB of choice and can be launched in docker with the following command, `docker run -p 27017:27017 --name some-mongo -d mongo` This follows the same naming convention as the MySQL container. 

Before running code against this container, the driver needs to be installed by `pip3 install pymongo`

Test read and write to this database by executing the python scripts, `write.py` and `read.py`, respectively. Additional CRUD operations can be executed, as well. There are several GUI's for navigating a Document DB, as well (Consider, Robo 3T). 

# Key-Value Databases
*** redis *** is an in-memory key-value pair database. Data goes into memory (not down to disk) so it has the advantage of speed. It is frequently used as an additional layer on top of other databases. 
The container can be established with the following command, `docker run -p 6379:6379 --name some-redis -d redis`. 

Before running code against this container, the driver needs to be installed by `pip3 install redis`

Test read and write to this database by executing the python scripts, `write.py` and `read.py`, respectively. Additional CRUD operations can be executed, as well. There are several GUI's for navigating a Key-Value database, including Redis Insight. 

# Distributed-Scalable Databases
Cassandra is the distributed-scalable database of choice. Advantage lies in it's scalability. Intent is to use large volumes of data in a distributed fashion. The container can be established with the following command, `docker run -p 9042:9042 --name some-cassandra -d cassandra`. 

Before running code against this container, the driver needs to be installed with `pip3 install cassandra-driver`.

Test read and write to this database by executing the python scripts, `write.py` and `read.py`, respectively. Additional CRUD operations can be executed, as well. The database can also be accessed via SQLSH using the command line interface (CLI). Once in the CLI, enter cqlsh to enter the sql interface and navigate the DB accordingly. 
