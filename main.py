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
import time         # time support (for .clock())
import datetime     # datetime support
import json         # JSON parsing

def main():
    try: #check to see if the file exists already
        open("output.csv").read()
    except Exception: # create it if it doesn't
        open("output.csv", "w").write("Timestamp (UTC), PC, Xbox One, PS4, Total\n")
    
    getStats("http://api.swbstats.com/api/onlinePlayers")
    
    delay = 300
    lastTime = 0
    time.clock() #Start timer
    while True:
        if time.clock()-lastTime > delay:
            lastTime = time.clock()
            getStats("http://api.swbstats.com/api/onlinePlayers")

    
def getStats(url):
    # try:
        page = urllib2.urlopen(urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
        #print page.read()
          
        data = json.load(page)
        
        outputfile = open("output.csv", "a")
        outputfile.write(datetime.datetime.utcnow().strftime("%Y/%m/%d %H:%M:%S") + ",")
        outputfile.write(str(data['pc']['count']) + ",")
        outputfile.write(str(data['xone']['count']) + ",")
        outputfile.write(str(data['ps4']['count']) + ",")
        outputfile.write(str(data['pc']['count'] + data['xone']['count'] + data['ps4']['count']) + "\n")
        
        print "Recorded stats at " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " UTC -05:00"
        
        # from pprint import pprint
        # pprint(data)
        
        # pprint(data['pc'])
        # pprint(data['pc']['count'])
        
    # except Exception:
        # print 'Error: Problem loading stats'
        # print 'Type: ' + str(sys.exc_info()[0])
        # print 'Value: ' + str(sys.exc_info()[1])
        # quit()

def generateJSON(platform):
    

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
