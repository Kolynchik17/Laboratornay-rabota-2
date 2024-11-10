import csv
import json
with open('input.csv') as f:
    lines = [line for line in csv.DictReader(f)]
    print(json.dumps(lines, indent = 4))


