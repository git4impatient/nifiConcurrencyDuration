# # (c) copyright 2023 Martin Lurie - sample code not supported

# 
echo 
echo WARNING - YOU ARE ABOUT TO UPDATE ALL THE PROCESSORS DESCRIBED IN YOUR JSON file
echo THIS SCRIPT WILL REVERT THE SETTINGS TO A PRIOR STATE.
echo 
echo here are the last 5 saved input files, please enter the input file you 
echo want to revert
echo hit enter when ready
# saved.input.136477.json
ls -latr saved.input.*.json | tail -5 
echo
echo please enter file name
echo
read revert2thisfile
echo 
echo about to revert to values contained in  hit cntl-c to stop
echo $revert2thisfile
read foo
echo now extracting values to revert
echo hit enter when ready
python3 listPGroupProcessorIdentifierConcurrency.py $revert2thisfile
echo
echo output.json contains the values we will revert
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
python3 updateConcurrencyUsingVersionViaNifiAPI.py UNDO  > update.$$.log 2>&1
echo 
echo 
tail -2 update.$$.log

