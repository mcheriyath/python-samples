import json
import argparse
import sys

# Loading the config file based on the argument passed
data = ''
env = ''
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--environment", choices=["uatdev","prod"])
args = parser.parse_args()
# Dumb method
if args.environment == "uatdev":
    with open('config/uatdev.json', 'r') as data_file:
        data = json.load(data_file)
        env = 'UATDEV'
elif args.environment == "prod":
    with open('config/prod.json', 'r') as data_file:
        data = json.load(data_file)
        env = 'PROD'
else:
    print 'Usage: python main.py -e {uatdev,prod}'

print data['EnvInfo']['Name']

for i in data['PublicSubnetsData']:
    print i['Name']
