#!/usr/bin/python -tt
# Copyright 2015 Brendan Ferracciolo
# 
# This file is part of SWBFHistoricalStats.
#
# SWBFHistoricalStats is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SWBFHistoricalStats is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SWBFHistoricalStats. If not, see <http://www.gnu.org/licenses/>.

"""<insert man page here>"""

import sys          # for various I/O functions
import urllib2      # URL fetching and handleing
import time         # time support (for .sleep())
import datetime     # datetime support
import json         # JSON parsing
import re           # regular expressions
import os           # for file truncation

def main():
    try: #check to see if the file exists already
        open("output.csv").read()
    except Exception: # create it if it doesn't
        open("output.csv", "w").write("Timestamp (UTC), PC, Xbox One, PS4, Total\n")
    
    getStats("http://api.swbstats.com/api/onlinePlayers")
    # generateJSON()
    
    # while True:
		# time.sleep(300) # sleep for about 5 minutes
		# getStats("http://api.swbstats.com/api/onlinePlayers")
		# generateJSON()
    
def getStats(url):
    try:
        page = urllib2.urlopen(urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        #print page.read()
          
        data = json.load(page)
        
        csvoutputfile = open("output.csv", "a")
        csvoutputfile.write(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S") + ",")
        csvoutputfile.write(str(data['pc']['count']) + ",")
        csvoutputfile.write(str(data['xone']['count']) + ",")
        csvoutputfile.write(str(data['ps4']['count']) + ",")
        csvoutputfile.write(str(data['pc']['count'] + data['xone']['count'] + data['ps4']['count']) + "\n")
        csvoutputfile.close()
        
        log("Successfully recorded stats.")
        
        # from pprint import pprint
        # pprint(data)
        
        # pprint(data['pc'])
        # pprint(data['pc']['count'])
        
    except Exception:
        log('Error: Problem loading stats')
        log('Type: ' + str(sys.exc_info()[0]))
        log('Value: ' + str(sys.exc_info()[1]))
        quit()
        
def generateJSON():
    csvoutputfile = open("output.csv", "r")
    
    jsonoutputfile = open("data.json", "w")
    jsonoutputfile.write("[")
    for line in csvoutputfile:
        values = line.rstrip().split(",")
        if values[0] == "Timestamp (UTC)": # skip the first line
            continue
        dict = {}
        dict['timestamp'] = values[0]
        dict['pc'] = values[1]
        dict['xboxone'] = values[2]
        dict['ps4'] = values[3]
        dict['total'] = values[4]
        jsonoutputfile.write(json.dumps(dict, separators=(',', ': ')) + ",")
    jsonoutputfile.seek(-1, os.SEEK_END)
    jsonoutputfile.truncate()
    jsonoutputfile.write("]")
    jsonoutputfile.close()
	
def log(msg):
	print datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S") + "-" + msg
	

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
