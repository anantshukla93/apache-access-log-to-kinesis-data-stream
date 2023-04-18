# Access Log Converter and Kinesis Data Stream Producer

This Python script converts the contents of an Apache access log file in the current working directory into JSON format, parses it using a regular expression, and streams the data to an Amazon Kinesis Data Stream using the AWS SDK.

## Prerequisites
- AWS Account
- Python 2.x installed
- Python 3.x installed
- AWS SDK for Python (Boto3) installed
- AWS credentials configured with appropriate permissions to access the Kinesis Data Stream (IAM Role preferred)

## Usage
1. Clone this repository to your local machine.
2. Ensure that you have Python 3.x and Boto3 installed.
3. Place your Apache log file in the same directory as the `convert_and_put_records_kds.py` script.
4. Modify the `convert_and_put_records_kds.py` script with your AWS region and Kinesis stream name.
5. Run the `convert_and_put_records_kds.py` script with Python to generate a JSON output and send it to the specified Kinesis stream.

Clone the repository and navigate to the project directory
Install the required packages by running the command: pip install -r requirements.txt
Add your AWS credentials to the .aws/credentials file. Alternatively, you can set environment variables for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
Run the script by executing python convert_and_put_records_kds.py in the terminal.
The script will prompt you to enter the name of the Kinesis Data Stream you want to write to. Enter the name and press enter.
The script will then read the latest .log file in the current directory, convert its contents into a JSON format, and write it to the Kinesis Data Stream you specified.
Check the AWS console to verify that the records were successfully written to the stream.

##License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
