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








