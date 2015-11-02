import sys
import argparse
import pandas as pd
from sqlalchemy import create_engine

# main function
if __name__ == "__main__":

	# Define cmd line args
	parser=argparse.ArgumentParser(description='''Import a CSV to Postgresql using Pandas''')
	parser.add_argument('--file', '-f', type=str, help='path to csv file, i.e. /Users/myusername/Documents/input.csv', required=True)
	parser.add_argument('--connection', '-c', type=str, help='database connection string, i.e. postgresql://user:pass@localhost/db_name', required=True)	
	parser.add_argument('--schema', '-s', type=str, help='name of schema, i.e. accounts', required=True)
	parser.add_argument('--table', '-t', type=str, help='name of table to create in database, i.e. payments', required=True)
	args=parser.parse_args()

	# connection
	engine = create_engine(args.connection)
	# read data from sql
	df = pd.read_csv(args.file)
	# column headers to lowercase
	df.columns = map(str.lower, df.columns)
	# data to sql
	df.to_sql(args.table, engine, schema=args.schema, if_exists='replace')

	if df.size:
		print args.table + ' import success!'
