# Author: Kyle Schmidt
# Date 8/17/2020
# Description: This program imports baseball statistics in CSV format from
# https://github.com/chadwickbureau/baseballdatabank/archive/master.zip and creates tables in a Postgres
# server.

from urllib.request import urlopen
import os
import zipfile


def download_data(download_url, extraction_location):
    """ Function that downloads a zip file from the given URL and extracts it to the given location"""
    # Download the file
    res = urlopen(download_url)

    # Create a zip file to write the downloaded file to
    tmp_zip = open(os.path.join(extraction_location, 'download.zip'), 'wb')

    # Write the download to the zip file
    tmp_zip.write(res.read())

    # Close the temporary zip file
    tmp_zip.close()

    # Open the zip file with zipfile so it can be extracted
    zf = zipfile.ZipFile(os.path.join(extraction_location, 'download.zip'))

    # Extract to the project location
    zf.extractall(path=extraction_location)

    # Close the zip file
    zf.close()


def data_to_postgres(directory_path, database, schema, port, user, password):
    """Function takes a directory with one or more csv files and creates a postgresql table using the given database,
    port, username and password"""
    # Create list of files in the directory
    f = os.listdir(directory_path)

    # creates a new postgresql table for each csv in the directory. Requires the pgfutter command line utility
    for file in f:
        os.system('pgfutter --db ' + database + ' --schema ' + schema + ' --port ' + port + ' --user ' + user +
                  ' --pw ' + password + ' csv ' + os.path.join(directory_path, file))


# location of data download and the directory where you want to extract the zip file
baseball_URL = r'https://github.com/chadwickbureau/baseballdatabank/archive/master.zip'
project_loc = r'/home/kyle/Documents/Baseball_Project'

# The directory where the csv files where extracted to nad connection information for the postgresql database
directory = r'/home/kyle/Documents/Baseball_Project/baseballdatabank-master/core'
db = "Baseball"
schma = "public"
prt = "5432"
usr = "postgres"
pswrd = "4261176"

# Download and extract the baseball data.
download_data(baseball_URL, project_loc)

# Create a postgresql table for each csv file.
data_to_postgres(directory, db, schma, prt, usr, pswrd)
