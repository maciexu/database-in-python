# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

# Create a select query: stmt
stmt = select([census])

# Add a where clause to filter the results to only those for New York : stmt_filtered
stmt = stmt.where(census.columns.state=='New York')

# Execute the query to retrieve all the data returned: results
results = engine.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2000
for result in results:
    print(result.age, result.sex, result.pop2000)

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for x in connection.execute(stmt):
    print(x.state, x.pop2000)
    

# Import and_
from sqlalchemy import and_

# Build a query for the census table: stmt
stmt = select([census])

# Append a where clause to select only non-male records from California using and_
# it can also be done with normal SQl query !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
stmt = stmt.where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M'
         )
)

# Loop over the ResultProxy printing the age and sex
for result in connection.execute(stmt):
    print(result.age, result.sex)



# Build a query to select state and age: stmt
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])





""" Counting, summing and grouping data   """

"""
func.sum() to get a sum of the pop2008 column of census as shown below:

select([func.sum(census.columns.pop2008)])
If instead you want to count the number of values in pop2008, you could use func.count() like this:

select([func.count(census.columns.pop2008)])
Furthermore, if you only want to count the distinct values of pop2008, you can use the .distinct() method:

select([func.count(census.columns.pop2008.distinct())])

.fetchall(), .fetchmany(), and .first() used on a ResultProxy to get the results. 
The ResultProxy also has a method called .scalar() for getting just the value of a query that returns only one row and column.
"""

# Build a query to count the distinct states values: stmt
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result: distinct_state_count
distinct_state_count = connection.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)


"""
Count of records by state
Often, we want to get a count for each record with a particular value in another column. 
The .group_by() method helps answer this type of query. 
You can pass a column to the .group_by() method and use in an aggregate function like sum() or count(). 
Much like the .order_by() method, .group_by() can take multiple columns as arguments.
"""
# Import func
from sqlalchemy import func

# Build a query to select the state and count of ages by state: stmt
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())


"""
Determining the population sum by state
To avoid confusion with query result column names like count_1, 
we can use the .label() method to provide a name for the resulting column. 
This gets appended to the function method we are using, and its argument is the name we want to use.

We can pair func.sum() with .group_by() to get a sum of the population by State and use the label() method to name the output.

We can also create the func.sum() expression before using it in the select statement. 
We do it the same way we would inside the select statement and store it in a variable. 
Then we use that variable in the select statement where the func.sum() would normally be.
"""
# Import func
from sqlalchemy import func

# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008: stmt
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())


""" SQLAlchemy, pandas and matplotlib to visualize our data
# import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the results: df
df = pd.DataFrame(results)

# Set column names
df.columns = results[0].keys()

# Print the Dataframe
print(df)

# Plot the DataFrame
df.plot.bar()
plt.show()



