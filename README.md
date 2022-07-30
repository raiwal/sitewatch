# Sitewatch
Simple configurable sitewatch for text patterns


# Introduction
sw.py is python script that read configuration information from sitewatch.ini 
file and writes polling log.

# How to run program
There are two two things that must be taken into account.
1. You must create subdirectory for the logs. 
eg. if you run this on linux machine straigh from your home directory there 
must be directory ~/logs
2. sitewatch.ini MUST be in the same directory where sw.py is located

when above conditions are met you just simply run python src/hw.py from command 
line 

# Sitewatch.ini
* Only one recognition pattern supported
* if no custom timeout is set then DEFAUL Timeout is used.

# Logfile information
INFO is used when everything is OK
WARNING is given if pattern is not found
CRITICAL is logged if there site is not responding

# Hints
Linux tail -f <file> like functionality is possible in Windows (in powershell) with Get-Content <file> –Wait