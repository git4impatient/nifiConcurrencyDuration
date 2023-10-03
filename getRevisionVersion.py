# (c) copyright 2023 Martin Lurie - sample code not supported

import json
import requests

# Define the NiFi API base URL and endpoint to fetch processor details.
#nifi_api_base_url = "http://your-nifi-server:port/nifi-api"
nifi_api_base_url = "http://nifihost:8080/nifi-api"
nifi_processor_endpoint = "/processors/"

# Specify the input JSON file path
input_json_file = "input2.json"

# Function to fetch processor version from NiFi API
def get_processor_version(instance_identifier):
    url = f"{nifi_api_base_url}{nifi_processor_endpoint}{instance_identifier}"
    #print ( url )
    response = requests.get(url)
    if response.status_code == 200:
        processor_data = response.json()
        return processor_data["revision"]["version"]
    else:
        print (" no version returned " ) 
        print ( response.status_code )
        return None

# Load input JSON data from the file
with open(input_json_file, "r") as infile:
    input_json = json.load(infile)

# Iterate through input JSON, fetch versions, and add to output JSON
output_json = []
for item in input_json:
    instance_identifier = item["instanceIdentifier"]
    version = get_processor_version(instance_identifier)
    if version is not None:
        item["version"] = version
    output_json.append(item)

# Specify the output JSON file path
output_json_file = "output2.json"

# Save the output JSON to a file
with open(output_json_file, "w") as outfile:
    json.dump(output_json, outfile, indent=2)

print("Output JSON file created:", output_json_file)

