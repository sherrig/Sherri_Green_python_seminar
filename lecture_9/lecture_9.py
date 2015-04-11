#################################
# Title: Lecture 9              #
# Lesson: Input/Output #
# Filename: lecture_9.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 2/8/2015	#
# Last Editor: Joe Griffin	#
#################################

# To extract the data from the text file, this script will read a line of the file and then
#   separate it into the useful data for plotting. VPython functions can be used from there.

path = '/Users/joegriffin/Documents/Work/python_seminar/group_lectures/lecture_9/traj.txt'

extract = []

with open(path, 'r', 0) as traj:                # `with` will close the file after use
    line = traj.readline()                      # Data was entered line-by-line
    
    while line:
        raw_numbers = line.split(', ')          # Print data is separated by comma-space
        data = []
        
        for val in raw_numbers:                 # Convert all strings to floats
            data.append(float(val.strip('])([\n')))# Remove non-float characters from data
            
        line = traj.readline()

extract.append(data)
