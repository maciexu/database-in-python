""" 
delete_stmt = delete(extra_employees)
result_proxy = connection.execute(delete_stmt)
Do be careful, though, as deleting cannot be undone!
"""
# Import delete, select
from sqlalchemy import delete, select

# Build a statement to empty the census table: stmt
delete_stmt = delete(census)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table : select_stmt
select_stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(connection.execute(select_stmt).fetchall())



# Deleting specific records

# Build a statement to count records using the sex column for Men ('M') age 36: count_stmt
count_stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = connection.execute(count_stmt).scalar()

# Build a statement to delete records from the census table: delete_stmt
delete_stmt = delete(census)

# Append a where clause to target Men ('M') age 36: delete_stmt
delete_stmt = delete_stmt.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = connection.execute(delete_stmt)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)



""" Deleting a table completely
You're now going to practice dropping individual tables from a database with the .drop() method, 
as well as all tables in a database with the .drop_all() method!
 you can check to see if a table exists on an engine with the .exists(engine) method.
 
 """# Drop the state_fact tables
state_fact.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))



