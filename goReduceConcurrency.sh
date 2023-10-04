# # (c) copyright 2023 Martin Lurie - sample code not supported

# 
echo 
echo WARNING - YOU ARE ABOUT TO UPDATE ALL THE PROCESSORS DESCRIBED IN YOUR JSON file
echo 
echo download json from the nifi canvas and name  the file    input.json
echo hit enter when ready
read foo
echo 
echo now extracting processor id and level of concurrency from input.json
echo about to overwrite file called output.json
echo hit control-c and  save your current output.json if you want
echo hit enter when ready
read foo
python3 listPGroupProcessorIdentifierConcurrency.py
echo
echo you can look at the file output.json to see what processors you are about
echo to update
echo 
echo now ready to get the current versions by calling the nifi api - update to your
echo nifi url - look out for extra / in the url
echo we need the current version in case someone else has done edits
echo hit enter when ready
read foo
python3 getRevisionVersion.py
echo now ready to update - check the script for the threshold value and the new value 
echo you want for concurrency
echo defaults are anything above 7 gets changed to 9
echo
echo WARNING - YOU ARE ABOUT TO UPDATE ALL THE PROCESSORS DESCRIBED IN YOUR
echo JSON FILE - ARE YOU REALLY, REALLY SURE YOU WANT TO DO THIS?
echo
echo hit control-c to exit or hit enter to continue
read foo
python3 updateConcurrencyUsingVersionViaNifiAPI.py  > update.$$.log 2>&1
echo 
echo 
tail -2 update.$$.log

