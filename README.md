# vdjProjectComparison
# 8-20-15
The main script (comparison.py) runs comparisons for the percent of correct gene calls on VDJ Alignment projects packaged into bioboxes. 
========
The current possible actions of comparison include:
-add new biobox: add a new biobox to the list for comparisons
-compare current bioboxes: output comparisons of current bioboxes into a csv file
========
Standards necessary for biobox comparison:
In addition to the standards mentioned on http://bioboxes.org/ all bioboxes must have the following:
-Input yaml file generator 
-Shell script to automate the docker commands as well as writing to dataFile.txt
Projects partis and mixcr contain example scripts. 
