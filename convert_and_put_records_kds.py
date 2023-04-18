#!/usr/bin/python3
# written by Anant Shukla

import os
import boto3
import json
import re

# Set up the Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Name of the Kinesis data stream
stream_name = 'demo'

# Get the path of the current working directory
cwd = os.getcwd()

# Get the path of the latest log file in the directory
log_file = max([f for f in os.listdir(cwd) if f.endswith('.log')], key=os.path.getctime)

# Parse the log file using a regular expression
regex = r'(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>[^\]]+)\] "(?P<httpstatus>GET|POST) (?P<path>.+?) HTTP/\d+\.\d+" (?P<returnstatus>\d{3}) (?P<bytes>\d+) "(?P<referrer>.+?)" "(?P<useragent>.+?)"'

result = []
with open(log_file) as f:
    for line in f:
        match = re.match(regex, line)
        if match:
            result.append({
                'IP address': match.group('ipaddress'),
                'Time Stamp': match.group('dateandtime'),
                'HTTP method': match.group('httpstatus'),
                'Path': match.group('path'),
                'Return status': match.group('returnstatus'),
                'Bytes': match.group('bytes'),
                'Referrer': match.group('referrer'),
                'User agent': match.group('useragent')
            })

# Write the parsed data to a JSON file
with open(os.path.join(cwd, 'data.json'), 'w') as fp:
    json.dump(result, fp, indent=2)

# Send the data to the Kinesis data stream
for item in result:
    # Convert each dictionary item to a JSON string
    item_json = json.dumps(item)

    # Put the record to the Kinesis stream
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=item_json,
        PartitionKey=item['User agent']  # Use user agent as the partition key
    )

    print(f"Put record to Kinesis stream {stream_name}, partition key: {item['User agent']}, response: {response}")

