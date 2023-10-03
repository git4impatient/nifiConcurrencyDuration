# (c) copyright 2023 Martin Lurie - sample code not supported

import json
import subprocess

# Default values for variables
threshold = 6
newconcurrency = 13
newduration = 25

# Read JSON input from 'output2.json'
with open('output2.json', 'r') as json_file:
    input_data = json.load(json_file)

# Iterate through each object in the list
for data in input_data:
    # Extract the required values from the object
    instanceIdentifier = data.get('instanceIdentifier', '')
    instance_version = data.get('version', '')
    current_concurrency = data.get('concurrentlySchedulableTaskCount', 0)

    # Ensure instance_version is not an empty string
    if instance_version == '':
        print(f"Error: 'version' is missing or empty in object {data}.")
    else:
        # Compare current_concurrency with the threshold and update if greater
        if current_concurrency > threshold:
            # Create the cURL command with the updated concurrency value
            curl_command = f"""curl 'http://merlin:8080/nifi-api/processors/{instanceIdentifier}' \
            -X 'PUT' \
            -H 'Content-Type: application/json' \
            --data-raw '{{"component":{{"id":"{instanceIdentifier}","name":"UpdateCounter","config":{{"concurrentlySchedulableTaskCount":"{newconcurrency}","schedulingPeriod":"0 sec","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","schedulingStrategy":"TIMER_DRIVEN","comments":"","runDurationMillis":{newduration},"autoTerminatedRelationships":[],"retriedRelationships":[]}},"state":"STOPPED"}},"revision":{{"clientId":"cmdLineConcurrencyUpdater","version":{instance_version}}},"disconnectedNodeAcknowledged":false}}' \
            --compressed \
            --insecure"""

            #print ( " " ) 
            #print (curl_command ) 
            #print ( " " ) 
            # Execute the cURL command using subprocess
            try:
                subprocess.run(curl_command, shell=True, check=True)
                print(f"Updated NiFi processor for object {data}.")
            except subprocess.CalledProcessError as e:
                print(f"Error updating NiFi processor for object {data}: {e}")
        else:
            a=1
            # do nothing
            # print(f"Current concurrency in object {data} is not greater than the threshold. No update needed.")

