# Key - Value Databases
The key-value database of choice is Redis. 
What Is Redis?

Redis is an in-memory, key-value data store. A key-value data store is a type of NoSQL database where keys serve as unique identifiers for their values. A Redis instance can include various databases, all containing different datatypes.

Redis can be installed on your machine via writing the following command in your Terminal window:

`pip3 install redis`

Start a Redis Container Using Docker

There are many ways to initialize a Redis database. However, the one you will see in this course uses Docker containers. To initialize your Docker container for Redis, run the following command in your Terminal window:

`docker run -p 6379:6379 --name name_of_the_container -d redis`

After opening Docker and running the command above, you should see a Docker container running with the same name defined above.

# Using Python to Define Redis Databases

Redis stands for Remote Dictionary Service. This definition may make you think of Python dictionaries and, in some sense, this is true. Remember that Redis databases are defined using key-value pairs, like Python dictionaries.

The main differences between Redis and Python dictionaries are:

- Redis dictionaries support a variety of methods, such as GET, SEL, and DEL. Python dictionaries do not support these methods, but instead use different ones, such as copy(), clear(), and pop(), as you saw in Module 1.
- Redis keys are always strings. In Python, keys can be of any datatype.
- Redis values may contain different datatypes. In Python, all datatypes must be the same.

# How to Define a Database in Redis

A general Redis database can be initialized using the following code:
```python
#imports

import redis

# connect to server

r = redis.Redis(host='localhost', port=6379, db=0)

# write to server

t = python_code_to_define_your_key_value_pairs

r.rpush('entries',t)
```

Note that in the code above, d=0 initializes the database 0. In Redis, by default, there are 16 available databases numbered from 0 to 15.

After defining the database and its entries, you may want to read those entries to ensure everything is defined correctly. You can do so using the following code:
``` python
# imports

import redis

# connect to server

r = redis.Redis(host='localhost', port=6379, db=0)

# read items

for item in r.lrange('items', 0, -1):

    print(item)
```

# Methods in Redis

The table below explains the most common Redis methods that can be used to access and modify database entries.

Redis Methods:

*** GET ***

Use the GET (Links to an external site.) method to get the value of a key. If the key does not exist, the special value nil is returned. An error is returned if the value stored as key is not a string because the GET method only handles string values.

***SET***

Use the SET (Links to an external site.) method to set the key to hold the string value. If a key already holds a value, it is overwritten, regardless of its type. Any previous time to live associated with the key is discarded on successful SET method.

***DEL***

Use the DEL (Links to an external site.) method to remove specified keys. A key is ignored if it does not exist.