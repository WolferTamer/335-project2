# Schedules is a 2D array, with the value of a 2 string array.
def scheduler(schedules,start_hours,duration):
    
    #Merging every schedule into one list
    string_list = list()
    for schedule in schedules:
        for event in schedule:
            string_list.append(event)
    
    #Convert the schedule list into number of minutes
    master_list = list()
    for event in string_list:
      new_event = list()
      for value in event:
        broken = value.split(':')
        new_event.append(int(broken[0])*60+int(broken[1]))
      master_list.append(new_event)
    
    #Sort the minute list
    master_list.sort(key=sort_by_start)

    #Convert the working hours into minutes
    minute_starts = list()
    for person in start_hours:
      new_person = list()
      for value in person:
        broken = value.split(':')
        new_person.append(int(broken[0])*60+int(broken[1]))
      minute_starts.append(new_person)

    #Get the latest start time and earliest end time
    bestStart = 0
    bestEnd = 1440
    for person in minute_starts:
        if bestStart < person[0]:
            bestStart = person[0]
        if bestEnd > person[1]:
            bestEnd = person[1]
    
    #Code to combine the values in master_list to create all available blocks.
    timeslots = list()
    timeslots.append([bestStart,bestEnd])
    for event in master_list:
        n = len(timeslots)-1
        if event[0] >= timeslots[n][0]+duration:
            # Current Timeslot is 9:00 - 18:00
            # Current event is 10:00 - 11:30
            # New timeslots are 9:00-10:00, 11:30 - 18:00

            #Never gonna run, just for clarity
            if bestStart > event[0]:
                continue
            if bestEnd < event[1]:
                continue
            timeslots[n][1] = event[0]
            timeslots.append([event[1],bestEnd])
        elif event[1] > timeslots[n][0]:
          # Current Timeslot is 9:00-18:00
          # Current event is 8:00-9:30
          # New timeslot is 9:30-18:00
          timeslots[n][0] = event[1]  
          if timeslots[n][0] >= bestEnd:
             # Current Timeslot is 17:00-18:00
             # Current event is 17:00-18:00
             # Last timeslot is removed, loop ends
             timeslots.pop()
             break
        # Current Timeslot is 9:00-18:00
        # Current event is 8:00-8:30
        # No changes made
    formatted = list()
    for slot in timeslots:
        newslot = list()
        for time in slot:
          newslot.append("%02d:%02d" % (divmod(time,60)))
        formatted.append(newslot)
    return formatted    
def sort_by_start(x):
    return x[0]
  
  
  
### pre-file testing
'''schedule1 = [ ['7:00', '8:30'], ['12:00', '13:00'], ['16:00', '18:00']]
schedule2 = [ ['9:00', '10:30'], ['12:20', '13:30'], ['14:00', '15:00'], ['16:00', '17:00' ]]
compschedule = [schedule1,schedule2]
hours1 = ['9:00','18:30']
hours2 = ['9:00','19:00']
comphours = [hours1,hours2]
duration = 30
print(schedule(schedules=compschedule,start_hours=comphours,duration=duration))'''


### import from Input.txt
file = open('Input.txt', 'r', encoding="utf-8")
file.readline()
out = open("Output.txt", "w")

done = False
while not done:
  schedules = list()
  working_hours = list()
  while True:
    # parse out schedule
    schedule : str = file.readline()
    person_schedule = list()
    schedule_times = schedule.split(' = ')[1].strip('\n')
    events = schedule_times.split(',')
    for event in events:
      split = event.split('-')
      person_schedule.append([split[0], split[1]])
    schedules.append(person_schedule)
    
    # parse working hours
    hours : str = file.readline()
    hours = hours.split(' = ')[1].strip('\n')
    hours = hours.split(',')
    for time in hours:
      split = time.split('-')
      working_hours.append([split[0], split[1]])
    next_line : str = file.readline()
    if next_line == '\n':
      # we are still looking at the same day
      continue
    elif 'duration_of_meeting' in next_line:
      meeting_duration = int(next_line.split(' = ')[1])
      # Write to the file
      out.write(str(scheduler(schedules=schedules, start_hours=working_hours, duration=meeting_duration)))
      out.write("\n")
      if not file.readline():
        done = True
        break
      else:
        schedules.clear()
        working_hours.clear()
    else:
      break
    
    

file.close()
out.close()
