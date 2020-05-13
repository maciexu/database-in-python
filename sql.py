"""
Connecting to a MySQL database
Before you jump into the calculation exercises, let's begin by connecting to our database. 
Recall that in the last chapter you connected to a PostgreSQL database. 
Now, you'll connect to a MySQL database, for which many prefer to use the pymysql database driver, which, like psycopg2 for PostgreSQL, you have to install prior to use.

This connection string is going to start with 'mysql+pymysql://', 
indicating which dialect and driver you're using to establish the connection. 

The dialect block is followed by the 'username:password' combo. 

Next, you specify the host and port with the following '@host:port/'. 

Finally, you wrap up the connection string with the 'database_name

Create an engine to the census database by concatenating the following strings and passing them to create_engine():
'mysql+pymysql://' (the dialect and driver).
'student:datacamp' (the username and password).
'@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/' (the host and port).
'census' (the database name).

"""
# Import create_engine function
from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Print the table names
print(engine.table_names())

# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt_grouped
stmt_grouped = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt_ordered
stmt_ordered = stmt_grouped.order_by(desc('pop_change'))

# Return only 5 results: stmt_top5
stmt_top5 = stmt_ordered.limit(5)

# Use connection to execute stmt_top5 and fetch all results
results = connection.execute(stmt_top5).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
    

""" The case() expression accepts a list of conditions to match and the column to return if the condition matches, 
followed by an else_ if none of the conditions match. 

Often when performing integer division, we want to get a float back. While some databases will do this automatically, 
you can use the cast() function to convert an expression to a particular type.
"""
# import case, cast and Float from sqlalchemy
from sqlalchemy import case, cast, Float

# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of women in 2000: stmt
stmt = select([female_pop2000 / total_pop2000 * 100])

# Execute the query and store the scalar result: percent_female
percent_female = connection.execute(stmt).scalar()

# Print the percentage
print(percent_female)




""" SQL relationships """




