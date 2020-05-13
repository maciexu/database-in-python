"""
Automatic joins with an established relationship
If you have two tables that already have an established relationship, 
you can automatically use that relationship by just adding the columns we want from each table to the select statement. 

stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])

in order to join the census and state_fact tables and select the pop2008 column from the first and the abbreviation column from the second.
In this case, the census and state_fact tables had a pre-defined relationship: 
the state column of the former corresponded to the name column of the latter.
"""
# Build a statement to join census and state_fact tables: stmt
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result: result
result = connection.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(resu
 
 
   
""" Joins
stmt = stmt.select_from(
    census.join(
        state_fact, census.columns.state == 
        state_fact.columns.name)
"""






