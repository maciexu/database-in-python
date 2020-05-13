# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())

"""
Autoloading Tables from a database
SQLAlchemy can be used to automatically load tables from a database using something called reflection. 
Reflection is the process of reading the database and building the metadata based on that information. 
It's the opposite of creating a Table by hand and is very useful for working with existing databases.

To perform reflection, you will first need to import and initialize a MetaData object. 
MetaData objects contain information about tables stored in a database. 
During reflection, the MetaData object will be populated with information about the reflected table automatically, 
so we only need to initialize it before reflecting by calling MetaData().

You will also need to import the Table object from the SQLAlchemy package. 
Then, you use this Table object to read your table from the engine, autoload the columns, and populate the metadata. 
This can be done with a single call to Table(): using the Table object in this manner is a lot like passing arguments to a function. 
For example, to autoload the columns with the engine, you have to specify the keyword arguments
autoload=True and autoload_with=engine to Table().

Finally, to view information about the object you just created, you will use the repr() function. 
For any Python object, repr() returns a text representation of that object. 
For SQLAlchemy Table objects, it will return the information about that table contained in the metadata.
"""
# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, MetaData, Table

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Print a list of column names of the census table by applying the .keys() method to census.columns.
print(census.columns.keys())

# Print full metadata of census,  information about the table objects are stored in the metadata.tables dictionary, 
# so you can get the metadata of your census table with metadata.tables['census']
print(repr(metadata.tables['census']))


""" The object returned by the .execute() method is a ResultProxy. 
On this ResultProxy, we can then use the .fetchall() method to get our results - that is, the ResultSet.
"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'select * from census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)


""" Another way """
# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: results
results = connection.execute(stmt).fetchmany(size=10)

# Execute the statement and print the results
print(results)


""" the differences between a ResultProxy and a ResultSet:

ResultProxy: The object returned by the .execute() method. It can be used in a variety of ways to get the data returned by the query.
ResultSet: The actual data asked for in the query when using a fetch method such as .fetchall() on a ResultProxy.
"""
# Get the first row of the results by using an index: first_row
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])
