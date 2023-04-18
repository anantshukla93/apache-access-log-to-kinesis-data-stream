# Access Log Converter and Kinesis Data Stream Producer

This Python script converts the contents of an Apache access log file in the current working directory into JSON format, parses it using a regular expression, and streams the data to an Amazon Kinesis Data Stream using the AWS SDK.

## Prerequisites
- AWS Account
- Python 2.x installed
- Python 3.x installed
- AWS SDK for Python (Boto3) installed
- AWS credentials configured with appropriate permissions to access the Kinesis Data Stream (IAM Role preferred)

## Usage
0. Spin up an EC2 Instance (t2.micro) in us-east-1 (North Virginia) Region and connect to the instance over ssh.
1. AMI Description - Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type | North Virginia AMI ID - ami-069aabeee6f53e7bf
2. Clone the repository and navigate to the project directory.
3. Run the following commands
4. chmod u+x ./log-generator-install.sh
5. ./log-generator-install.sh
6. cd /tmp/logs
7. sudo python ~/Fake-Apache-Log-Generator/apache-fake-log-gen.py -n 100 -o LOG
8. Create kinesis stream with name demo in North Virginia DC - Provisioned - 1 shard
9. create IAM role for EC2 role giving put-record api access to kinesis stream and assign it to the ec2 instance.
10. mv ./convert_and_put_records_kds.py /tmp/logs/convert_and_put_records_kds.py
11. chmod u+x ./convert_and_put_records_kds.py
12. ./convert_and_put_records_kds.py
13. Check the AWS console to verify that the records were successfully written to the stream.
<img width="1578" alt="Screenshot 2023-04-19 at 12 21 57 AM" src="https://user-images.githubusercontent.com/47002135/232876214-4ec45a5f-9da3-4fe3-a369-a914945abaeb.png">

The script will then read the latest .log file in the current directory, convert its contents into a JSON format, and write it to the Kinesis Data Stream you specified.

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Credits
The Fake Log Generator used in this project is the work of @kiritbasu in their [Fake Apache Log Generator](https://github.com/kiritbasu/Fake-Apache-Log-Generator). Thank you
