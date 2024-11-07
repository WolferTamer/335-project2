# Project 2

Caleb Cassin - cbcassin@csu.fullerton.edu

Keillor Jennings - keillorjennings@csu.fullerton.edu

Luke Arcebal - lukearcebal@csu.fullerton.edu

Jackson Cross - jmcross02@csu.fullerton.edu

## Execution

1. Ensure Python is installed on your machine
2. Modify the Input.txt file. Each use case is seperated by `***CASE***`. Each user's information is seperated by two line breaks. See below for an example

```
***CASE***
person1_Schedule = 7:00-8:30,12:00-13:00,16:00-18:00
person1_DailyAct = 9:00-19:00

person2_Schedule = 9:00-10:30,12:20-13:30,14:00-15:00,16:00,17:00
person2_DailyAct = 9:00-18:30
duration_of_meeting = 30
```
3. Once Input.txt has been configured, run `py project2_starter.py` or `python project2_starter.py` in the command line
4. Open the newly created Output.txt file to see the outputs, seperated by a line break.
``` 
[['10:30', '12:00'], ['13:30', '14:00'], ['15:00', '16:00'], ['18:00', '18:30']]
```