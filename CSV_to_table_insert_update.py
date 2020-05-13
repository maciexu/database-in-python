""" Loading a CSV into a table

One way to do that would be to read a CSV file line by line, create a dictionary from each line, and then use insert().

But there is a faster way using pandas. 
You can read a CSV file into a DataFrame using the read_csv() function 
(this function should be familiar to you, but you can run help(pd.read_csv) in the console to refresh your memory!). 
Then, you can call the .to_sql() method on the DataFrame to load it into a SQL table in a database. 
The columns of the DataFrame should match the columns of the SQL table.

.to_sql() has many parameters, but in this exercise we will use the following:

name is the name of the SQL table (as a string).
con is the connection to the database that you will use to upload the data.
if_exists specifies how to behave if the table already exists in the database; possible values are "fail", "replace", and "append".
index (True or False) specifies whether to write the DataFrame's index as a column.

"""
# import pandas
import pandas as pd

# read census.csv into a dataframe : census_df
census_df = pd.read_csv("census.csv", header=None)

# rename the columns of the census dataframe
census_df.columns = ['state', 'sex', 'age', 'pop2000', 'pop2008']

# append the data from census_df to the "census" table via connection
census_df.to_sql(name='census', con=connection, if_exists='append', index=False)


""" Update """
# Example 1 Updating individual records
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')
results = connection.execute(select_stmt).fetchall()
print(results)
print(results[0]['fips_state'])

update_stmt = update(state_fact).values(fips_state = 36)
update_stmt = update_stmt.where(state_fact.columns.name == 'New York')
update_results = connection.execute(update_stmt)

# Execute select_stmt again and fetch the new results
new_results = connection.execute(select_stmt).fetchall()

# Print the new_results
print(new_results)

# Print the FIPS code for the first row of the new_results
print(results[0]['fips_state'])



# Example 2 Updating multiple records
"""
When appending a where statement to an existing statement, make sure you include the name of the table as well as the name of the column, 
for example 
new_stmt = old_stmt.where(my_tbl.columns.my_col == 15).

On the other hand, you do not need to include the name of the table when referencing a column in an update statement, e.g. 
stmt = update(my_table).values(my_col = 10).

== is a comparison operator ("is equal?"), and = is an assignment operator ("set equal to"). 
Make sure you use an appropriate operator in your calls to where() and values().
"""


# Build a statement to update the notes to 'The Wild West': stmt
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records: stmt_west
stmt_west = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement: results
results = connection.execute(stmt_west)

# Print rowcount
print(results.rowcount)



""" Correlated updates
You can also update records with data from a select statement. This is called a correlated update. 
It works by defining a select statement that returns the value you want to update the record 
with and assigning that select statement as the value in update.
"""
# Build a statement to select name from state_fact: fips_stmt
fips_stmt = select([state_fact.columns.name])

# Append a where clause to match the fips_state to flat_census fips_code: fips_stmt
fips_stmt = fips_stmt.where(
    state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt_where: update_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt: results
results = connection.execute(update_stmt)

# Print rowcount
print(results.rowcount)




