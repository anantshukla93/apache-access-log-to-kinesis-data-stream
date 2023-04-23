#!/bin/bash
#Written by Anant Shukla

while true; do
	echo "Generating Logs"
	sudo python ~/Fake-Apache-Log-Generator/apache-fake-log-gen.py -n 100 -o LOG
	echo "Converting and pushing JSON records to KDS"
	./convert_and_put_records_kds.py
	sleep 5
done
