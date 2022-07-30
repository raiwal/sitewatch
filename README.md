# Sitewatch
Simple configurable sitewatch for text patterns


# Introduction
sw.py is python script that read configuration information from sitewatch.ini 
file and writes polling log.

# How to run program

```
$ git clone git@github.com:raiwal/sitewatch.git
$ cd sitewatch
$ mkdir logs
$ python src/sw.py
```
1. You must create subdirectory for the logs if it does not exist
2. sitewatch.ini must be in the same directory where sw.py is located.

# Sitewatch.ini
* Only one recognition pattern supported
* if no custom timeout is set then DEFAUL Timeout is used.

# Logfile information
INFO is used when everything is OK
WARNING is given if pattern is not found
CRITICAL is logged if there site is not responding

# Hints
Linux tail -f <file> like functionality is possible in Windows (in powershell) with Get-Content <file> –Wait
