# MTAtimes
Made by Ethan Friedman. (etfriedman@packer.edu) In 2 days!
---
Customizable train times for Borough Hall made in python.

Includes Customizable GUI through tkinter

### How it works (simple):
1. scrapes mta info site for json dict
2. removes junk, now able to parse dict in python
3. picks pieces of the dict and puts them together
4. updates every determined number of miliseconds (can be changed in the main app)

## IMPORTANT:
### Always keep the mainApp.py and times.py in the same directory, otherwise this will not run
This can be changed if you know what you're doing though, through the mainApp

### dependencies:
- tkinter (updated version if you want to add cool stuff to GUI)
- beautifulsoup
- requests (pip install requests)
- os

### Photo of GUI:

![alt text](https://raw.githubusercontent.com/etfriedman/MTAtimes/master/Screen%20Shot%202019-12-04%20at%203.52.00%20PM.png)
