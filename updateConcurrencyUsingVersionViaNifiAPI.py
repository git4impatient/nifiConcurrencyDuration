# (c) copyright 2023 Martin Lurie - sample code not supported

import json
import subprocess
import sys

undo = sys.argv[1]
print ( "we are doing a:  ",  undo ) 

# Default values for variables
threshold = 6
newconcurrency = 8
# desired duration in milliseconds
newduration = 25

# Read JSON input from 'output2.json'
with open('output2.json', 'r') as json_file:
    input_data = json.load(json_file)

# Iterate through each object in the list
numprocessed=0
numchanged=0
for data in input_data:
    numprocessed=numprocessed+1
    # Extract the required values from the object
    instanceIdentifier = data.get('instanceIdentifier', '')
    instance_version = data.get('version', '')
    current_concurrency = data.get('concurrentlySchedulableTaskCount', 0)
    current_duration = data.get ('runDurationMillis', 0 )
    # do not overwrite an existing non zero duration
    if current_duration > newduration:
      newduration = current_duration       
    # Ensure instance_version is not an empty string
    if instance_version == '':
        print(f"Error: 'version' is missing or empty in object {data}.")
    else:
      if undo=="UNDO":
       # force everything to be updated
       threshold=0
       # make the new setting for concurrency and duration equal to what is in the undo.json
       newconcurrency=current_concurrency
       newduration=current_duration
        # Compare current_concurrency with the threshold and update if greater
      if current_concurrency > threshold:
            curl_command = f"""curl 'http://merlin:8080/nifi-api/processors/{instanceIdentifier}' \
             -X 'PUT' \
             -H 'Content-Type: application/json' \
             --data-raw '{{ "component": {{ "id": "{instanceIdentifier}", "config": {{ "concurrentlySchedulableTaskCount": "{newconcurrency}", "runDurationMillis": {newduration} }} }}, "revision": {{ "clientId": "cmdLineConcurrencyUpdater", "version": {instance_version} }} }}' \
             --compressed \
             --insecure"""

#             --data-raw '{{"component":{{"id":"{instanceIdentifier}","name":"UpdateCounter","config":{{"concurrentlySchedulableTaskCount":"{newconcurrency}","schedulingPeriod":"0 sec","executionNode":"ALL","penaltyDuration":"30 sec","yieldDuration":"1 sec","bulletinLevel":"WARN","schedulingStrategy":"TIMER_DRIVEN","comments":"","runDurationMillis":{newduration},"autoTerminatedRelationships":[],"retriedRelationships":[]}},"state":"STOPPED"}},"revision":{{"clientId":"cmdLineConcurrencyUpdater","version":{instance_version}}},"disconnectedNodeAcknowledged":false}}' \

            #print ( " " ) 
            print (curl_command ) 
            #print ( " " ) 
            # Execute the cURL command using subprocess
            try:
                subprocess.run(curl_command, shell=True, check=True)
                print(f"Updated NiFi processor for object {data}.")
                numchanged= numchanged+1
                
            except subprocess.CalledProcessError as e:
                print(f"Error updating NiFi processor for object {data}: {e}")
      else:
            a=1
            # do nothing
            # print(f"Current concurrency in object {data} is not greater than the threshold. No update needed.")
print ( "number of instanceIdentifiers processed:  " , str(numprocessed) ) 
print ( "number of instanceIdentifiers updated:  " , str(numchanged) ) 

