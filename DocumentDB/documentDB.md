# Document Databases

# What Is MongoDB?

MongoDB is a NoSQL database, which means that the data is not modeled in the tabular relationships used in relational databases. MongoDB is a document-oriented database that stores information in several document collections. A document collection in MongoDB would be the equivalent of a table in a relational database. MongoDB stores documents, the equivalent of MySQL records, in JSON format, and it does not need the structure or the schema of a relational database.

Documents are organized into collections where they can be queried. Data that is frequently accessed together is stored in the same place so read operations are extremely fast because no joins are required.

MongoDB knows how to coordinate multiple servers to store data. That makes MongoDB what is called a distributed database, which provides fault tolerance by keeping redundant copies of the same data in different servers, so a single server failure does not affect the application. MongoDB also scales across multiple servers to store data so, as data volume increases and performance requirements grow, you can just add more servers.

MongoDB is a widely used open-source document database. In fact, you will be taking advantage of containers to run MongoDB in order to install it and then run it on your machine.

# Creating a Database Using MongoDB

Python can be used in database applications. MongoDB is one of the most popular NoSQL database tools. In this mini-lesson, you will learn about how to use MongoDB to create databases.

As you saw in Video 12.6, the first thing you need to do in order to connect to MongoDB using a Python driver is to install it on your machine. To accomplish this run the following command in your Terminal window:

`pip3 install pymongo`

To create a database in MongoDB, start by creating a Python file in your code editor of choice (e.g., VS Code).

Next, you need to create a MongoClient object, then specify a connection URL with the correct IP address and the name of the database you want to create. See the code below:

```Python 
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
```

To check whether a database exists by listing all databases in your system, you can run the following code:

``` python 
print(myclient.list_database_names())
```

In MongoDB, tables are called collections. To create a collection in MongoDB, use the database object you created previously and specify the name of the collection you want to create.

The code below shows how to create a collection named customers in the mydatabase database defined above.

``` python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]
```

You can check whether a collection exists in a database by listing all collections. To do so, add the following line to your Python script:

``` python
print(mydb.list_collection_names())
```

In MongoDB, records are called documents. To insert a document into a collection, you can use the insert_one() method.

The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document that you want to insert. See the example below:

``` python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
```

To insert multiple documents, you will need to use the insert_many() method.

``` python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mylist = [

  { "name": "Amy", "address": "Apple st 652"},

  { "name": "Hannah", "address": "Mountain 21"},

  { "name": "Michael", "address": "Valley 345"}

]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
```