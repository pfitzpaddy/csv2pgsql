import sys
import argparse
import pandas as pd
from sqlalchemy import create_engine

# main function
if __name__ == "__main__":

	# Define cmd line args
	parser=argparse.ArgumentParser(description='''Import a CSV to Postgresql using Pandas''')
	parser.add_argument('--connection', '-c', type=str, help='database connection string, i.e. postgresql://user:pass@localhost/db_name', required=True)
	parser.add_argument('--file', '-f', type=str, help='path to csv file, i.e. /Users/myusername/Documents/input.csv', required=True)
	parser.add_argument('--table', '-t', type=str, help='name of table to create in database, i.e. accounts', required=True)
	args=parser.parse_args()

	engine = create_engine(args.connection)
	df = pd.read_csv(args.file)
	df.to_sql(args.table, engine, if_exists='replace')

	if df.size:
		print args.table + ' import success!'
