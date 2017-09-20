# ComputerLocatingScripts
A script and associated package designed to associate computers with a locations from a given list.
Save the new reports in the Unsorted folder (script will generate if not present)
Run the script
Look at the results in ogs, Located, and Unlocated, as well the console output.

Right now a lot of aspects of the script are hardcoded which would ideally be setup in a config file later.
Some of these include
-The actual field names read from both computer reports and location files
-The order of the fields by which the script attempts to sort computers (right now: Domain->Name->IP)
-the actual bounds of the naming convention (currently checks first 5 characters, why not more/less?)
-The behaviour of log files (should be built bit by bit, not in one go.)
-The behaviour of the "prefix report" that occurs at the end of the script (could vary prefix length, and minimum count)
-the conventions for writing files (similar to reading)
-the number of folders that can be searched for new reports (fixed, poorly coded)
