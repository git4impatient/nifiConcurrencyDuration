# (c) copyright 2023 Martin Lurie - sample code not supported

import json

import sys

# Check if a file name is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python read_file.py <file_name>")
    sys.exit(1)

# Get the file name from the command line argument
file_name = sys.argv[1]

# Load the provided JSON data
try:
    # Open the file for reading
    with open(file_name, 'r') as input_file:
        data = json.load(input_file)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Initialize a list to store the extracted information
extracted_data = []

# counter for instanceIdentifier and processors over 10
numprocessed=0
numgreedy=0
# Extract the information from the JSON structure
for process_group in data['flowContents']['processGroups']:
    for processor in process_group['processors']:
        extracted_data.append({
            'processGroup': process_group['name'],
            'processor': processor['name'],
            'instanceIdentifier': processor['instanceIdentifier'],
            'concurrentlySchedulableTaskCount': processor['concurrentlySchedulableTaskCount'],
            'runDurationMillis': processor['runDurationMillis']
        })
        numprocessed=numprocessed+1
        #print ( int( processor['concurrentlySchedulableTaskCount'] ) -20 )
        if int( processor['concurrentlySchedulableTaskCount']) > 10:
            numgreedy=numgreedy+1

# Create a new JSON file with the extracted data
with open('output.json', 'w') as output_file:
    json.dump(extracted_data, output_file, indent=2)

print("Data extraction and JSON creation completed.")
print ( " " )
print ( " " )

print ( "  ########################################################## " ) 
print ( "  ##############  Summary of current settings ############## " ) 
print ( "number of instanceIdentifiers processed:  " , str(numprocessed) ) 
print ( "number of instanceIdentifier with more than 10  concurrentlySchedulableTaskCount: " , str(numgreedy) ) 
print ( " " )
print ( " " )

