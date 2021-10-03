# Percolation


This is a project based on a very simple percolation process. Percolation is the process of a liquid slowly passing through a filter. 
This is how coffee is usually made. This is a program which mimics this concept. A dynamic grid with 2 digits random numbers will be created. 
The grid will have some empty slots with no numbers, which again randomly generated. This program will check each column for possible percolations.


• The percolation is not possible for a column if the column consists of one or more empty spaces
from top to bottom.

• The percolation is possible for a column if the entire column consists numbers from top to bottom
This program is showing state weather percolation of a column is possible or not at the end of each column.
If it possible this program show “OK” under the column and if it’s not possible this program show “NO” under the column.
The grid size is dynamically passed as a command-line argument to the program. If no dimensions are passed, the default 
dimension for the grid is 5x5. The lowest dimension is 3x3 while
the highest dimension is 9x9. Some possible commands would be,

• C:\>perc 3x4
  1. The above creates a 3x4 grid
• C:\>perc
  1. The above creates a 5x5 default grid
  The resulting answer has written to a text file so the result can be viewed later via notepad
• Each result is going to a different text file
This program is generating the grid and saving the result in an HTML file so you can see the answer in a web browser.
