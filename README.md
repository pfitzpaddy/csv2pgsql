## csv2pgsql
Import CSV to Postgresql using Pandas

### Requirements
* Python 2.7
* Pandas
* sqlalchemy

### Arguments

    --connection, -c: Postgresql database connection string, i.e. postgresql://user:pass@localhost/db_name
    --file, -f: path to csv file, i.e. /Users/myusername/Documents/input.csv
    --table, -t: name of table to create in database, i.e. shipping
    
### Usage

    python csv2pgsql.py -f /Users/fitzpaddy/Documents/data/input.csv  -t shipping -c postgresql://user:pass@localhost/accounts

