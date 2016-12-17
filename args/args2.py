import json
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as file:
    data = json.load(file)

print data['EnvInfo']['Name']

for i in data['PublicSubnetsData']:
    print i['Name']
