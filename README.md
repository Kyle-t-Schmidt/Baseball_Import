# Baseball_Import

## Introduction
This program downloads a zip file containing 28 csv files with historical baseball data and imports the data into Postgresql, creating a separate table for each csv file. The data can be downloaded here: https://github.com/chadwickbureau/baseballdatabank/archive/master.zip

## Using the program
The program was written and designed to be run on Ubuntu Linux. You need to have a postgresql database available and you need to have the pgfutter utility:
postgresql: https://www.postgresql.org/download/linux/ubuntu/
pgfutter: https://github.com/lukasmartinelli/pgfutter

Before running the program you need to insert your postgresql information and path to where the downloaded and extracted files will be located.
