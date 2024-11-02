![database](https://github.com/user-attachments/assets/8ad6a490-8b54-4d60-921b-8ccf6feedde4)

# Databases for ML

After fetching data via APIs, storing them is also really important for training a Machine Learning model.

You have multiple options:

- Relational database
- Non-relational database
- Key-Value storage
- Document storage
- Data Lake
- etc.

In this project, you will touch the first two: relational and non-relational databases.

## Relational Databases

Relational databases are mainly used for applications, not as a source of data for training your ML models, but they can be really useful for data processing, labeling, and injecting data into another data storage. In this project, you will play with basic SQL commands, create automation, and compute data directly in SQL—resulting in less load at your application level since the computing power is dispatched to the database.

## Non-Relational Databases

Non-relational databases, known as NoSQL, will give you flexibility with your data: document storage, versioning, no fixed schema, no validation to improve performance, complex lookups, etc.

## Resources

Read or watch:

### MySQL:
- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
- [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/blog/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

### NoSQL:
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [Building Your First Application: An Introduction to MongoDB](https://www.youtube.com/watch?v=ClAQEARNUoQ)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/manual/reference/mongo/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General:
- What’s a relational database
- What’s a non-relational database
- What is the difference between SQL and NoSQL
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL
- What is ACID
- What is document storage
- What are NoSQL types
- What are the benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### General:
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your SQL files will be executed on Ubuntu 16.04 LTS (or 18.04) using MySQL 5.7 (version 5.7.30)
- All your SQL queries should have a comment just before (i.e., syntax above)
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- All your Mongo files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using MongoDB (version 4.2)
- The first line of all your Mongo files should be a comment: `// my comment`
- All your Python files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using python3 (version 3.5 or 3.7) and PyMongo (version 3.10)
- The first line of all Python files should be exactly `#!/usr/bin/env python3`
- Your Python code should use the pycodestyle style (version 2.5.*)
- All your Python modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your Python functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your Python code should not be executed when imported (by using `if __name__ == "__main__":`)
- All your files should end with a new line
- The length of your files will be tested using `wc`

##### Projects

- Open this [Projects](https://github.com/MohamedAYasin/alu-machine_learning/blob/main/pipeline/databases/Project_%20Databases%20_%20ALU%20Intranet.pdf) to see the Assignments I did.

`©2024 African Leadership University`
