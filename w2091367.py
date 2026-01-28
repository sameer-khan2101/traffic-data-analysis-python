
"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2091367
 4. Date: 21/11/2024
****************************************************************************

"""

from graphics import *
import csv
import math



#To calculate percentages
def Percentage(portion,total):
   percentage = (portion / total)*100
   return percentage

#To change graph label sizes
def Graph_labels_size_styling(labelSizeToStyle):
   labelSizeToStyle.setSize(10)

#To change axis label sizes
def axis_labels(axis_number):
   axis_number.setSize(18)
   
#To style Elm avenue Elements
def Elm_avenue_Elements_styling(Elm_Avenue_TextToStyle, Elm_Avenue_BoxToStyle):
   Elm_Avenue_TextToStyle.setTextColor("orange")
   Elm_Avenue_BoxToStyle.setFill("orange")
   
#To style Hanley Elements
def Hanley_Elements_styling(Hanley_TextToStyle, Hanley_BoxToStyle):
   Hanley_TextToStyle.setTextColor("grey")
   Hanley_BoxToStyle.setFill("grey")


end_loop = False
#Program will not loop again if end_loop = True and program will end and vice versa
while not end_loop:
   #Asking the user to input the specific date so the program will be able to select the csv dateset file for that day
   valid_day_input = False
   valid_month_input = False
   valid_year_input = False
   #Obtain valid date from the user to select the dataset for that date
   #try block used if user doesn't enter an integar, which would result in ValueError
   while not valid_day_input:
      try:
         day = int(input("Please enter the day of the survey in the format dd: "))
         if 1 <= day <= 31:#there can't be less than 1 or more than 31 days in a month
            valid_day_input = True
         else:
               print("Out of range - values must be in the range 1 and 31")
      except ValueError:
            print("Integar required")

   while not valid_month_input:
      try:
         month = int(input("Please enter the month of the survey in the format MM:  "))
         if 1 <= month <= 12:# there can't be a month above 12 or less than 1
            valid_month_input = True
         else:
            print("Out of range - values must be in the range 1 to 12")
      except ValueError:
         print("Integar required")

   while not valid_year_input:
      try:
         year = int(input("Please enter the year of the survey in the format YYYY: "))
         if 2000 <= year <= 2024:#only dates allowed are from 2000 to 2004
            valid_year_input = True
         else:
            print("Out of range - values must range from 2000 and 2024")
      except ValueError:
         print("Integar required")
   
   data_list = []   #An empty list to load and hold data from csv file

   data_file_required=f"traffic_data{day:02}{month:02}{year}.csv" #The name of the csv dataset file that program will use

   #Code to load the csv file into data_list
   try:
      with open(data_file_required, 'r') as file:
          csvreader = csv.reader(file)
          header = next(csvreader)
          for row in csvreader:
              data_list.append(row) #data_list will be a nested list, where each individual list will be about infomation of an individual vehicle
   except FileNotFoundError:
      print("File does not exist")
      break  # Exit the program
   

   #Below will be code that will be used to analyse dataset and output the analysis
   print("***************************")
   selected_data_result = (f'data file selected is {data_file_required}')
   print(selected_data_result)
   print("***************************")

   #Calculate amount of vehicles 
   total_vehicle_count = len(data_list)#Will calculate the amount of individual lists(vehicles)
   total_vehicle_result = (f"The total number of vehicles recorded for this date is {total_vehicle_count}")
   print(total_vehicle_result)

   #Calculate amount of trucks 
   total_truck_count = 0
   for i in range(total_vehicle_count):
      if data_list[i][8] == "Truck":#will check every row's 8th index, to see if it's vehicle type is "Truck"
         total_truck_count += 1
      else:
         continue
   total_truck_count_result = (f"The total number of trucks recorded for this date is {total_truck_count}")
   print(total_truck_count_result)

   #Calculate amount of electric vehicles 
   electric_vehicles_count = 0
   for i in range(total_vehicle_count):
      if data_list[i][9].upper() == "TRUE":#the reason for using .upper() is because in csv file it says "TRUE",but python thought it says "True", just to be sure i use .upper()
         electric_vehicles_count += 1
      else:
         continue
   electric_vehicles_count_result = (f"The total number of electric vehicles for this date is {electric_vehicles_count}")
   print(electric_vehicles_count_result)

   #Calculate amount of two wheeled vehicles 
   two_wheeled_vehicles = ["Bicycle", "Motorcycle", "Scooter"]
   two_wheeled_vehicles_count = 0
   for i in range(total_vehicle_count):
      if data_list[i][8] in two_wheeled_vehicles:
         two_wheeled_vehicles_count += 1
      else:
         continue
   two_wheeled_vehicles_count_result = (f"The total number of two-wheeled vehicles for this date is {two_wheeled_vehicles_count}")
   print(two_wheeled_vehicles_count_result)

   #Calculate amount of busses heading north 
   busses_heading_north = 0
   for i in range(total_vehicle_count):
      if data_list[i][8] == "Buss" and data_list[i][4] == "N":
         busses_heading_north += 1
      else:
         continue
   busses_heading_north_result = (f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {busses_heading_north}")
   print(busses_heading_north_result)

   #Calculate amount of vehicles travelling straight
   vehicles_travelling_staight = 0
   for i in range(total_vehicle_count):
      if data_list[i][3] == data_list[i][4]:#vehicle will be striaght if the direction they travelled in is the same as the direction it travelled out the junction 
         vehicles_travelling_staight +=1
      else:
         continue    
   vehicles_travelling_staight_result = (f"The total number of Vehicles through both junctions not turning left or right is {vehicles_travelling_staight}")
   print(vehicles_travelling_staight_result)

   #Calculate percentage of trucks 
   truck_percentage = round(Percentage(total_truck_count, total_vehicle_count))    
   truck_percentage_result = (f"The percentage of total vehicles recorded that are trucks for this date is {truck_percentage}%")
   print(truck_percentage_result)

   #Calculate average of number of bicycle 
   bike_count = 0
   for i in range(total_vehicle_count):
      if data_list[i][8] == "Bicycle":
         bike_count += 1
      else:
         continue
   bike_average = round(bike_count / 24)    
   bike_average_result = (f"The average number of Bikes per hour for this date is {bike_average}")
   print(bike_average_result)

   #Calculate amount of speeding vehicles 
   speeding_vehicles = 0
   for i in range(total_vehicle_count):
      if int(data_list[i][7]) > int(data_list[i][6]):
         speeding_vehicles += 1
      else:
         continue
   speeding_vehicles_result = (f"The total number of vehicles recorded as over the speed limit for this date is {speeding_vehicles}")
   print(speeding_vehicles_result)

   #Calculate amount of vehicles recorded through Elm Avenue/Rabbit Road junction 
   elm_avenue_junction_vehicles = 0
   for i in range(total_vehicle_count):
      if data_list[i][0] == "Elm Avenue/Rabbit Road":
         elm_avenue_junction_vehicles += 1
      else:
         continue
   elm_avenue_junction_vehicles_result = (f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {elm_avenue_junction_vehicles}")
   print(elm_avenue_junction_vehicles_result)

   #Calculate amount of vehicles recorded through Hanley Highway/Westway junction
   hanley_highway_junction_vehicles = 0
   for i in range(total_vehicle_count):
      if data_list[i][0] == "Hanley Highway/Westway":
         hanley_highway_junction_vehicles += 1
      else:
         continue
   hanley_highway_junction_vehicles_result = (f"The total number of vehicles recorded through Hanley Highway/Westway junction is {hanley_highway_junction_vehicles}")
   print(hanley_highway_junction_vehicles_result)

   #Calculate percentage of vehicles recorded through Elm Avenue/Rabbit Road are scooters
   elm_avenue_scooters = 0
   for i in range(total_vehicle_count):
      if data_list[i][0] == "Elm Avenue/Rabbit Road" and data_list[i][8] == "Scooter":
         elm_avenue_scooters +=1
      else:
         continue
   elm_avenue_scooters_percentage = round(Percentage(elm_avenue_scooters, elm_avenue_junction_vehicles)) 
   elm_avenue_scooters_percentage_result = (f"{elm_avenue_scooters_percentage}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.") 
   print(elm_avenue_scooters_percentage_result)

   #Calculate the highest number of vehicles in an hour on Hanley Highway/Westway
   #list to store numbers of things recorded in an hour
   hour_list = [0, 0,0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   #lists to store numbers of vehicles recored in an hour
   hanley_vehicles_in_hour_list = list(hour_list)#used to list for number of vehicles per hour in hanley
   elm_vehicles_in_hour_list = list(hour_list)#used to make list for number of vehicles per hour in elm, needed for task C histogram
   for i in range(24):
      for j in range(total_vehicle_count):
         if data_list[j][0] == "Hanley Highway/Westway" and int(data_list[j][2][0:2]) == i:#the inner loop will not move out to outer loop and move to the counting for next hour, unless there is no longer anymore vehicles recored for that hour  
            hanley_vehicles_in_hour_list[i] += 1       
         elif data_list[j][0] == "Elm Avenue/Rabbit Road" and int(data_list[j][2][0:2]) == i:
            elm_vehicles_in_hour_list[i] += 1
         else:
            continue
   peak_hour_vehicle_count = max(hanley_vehicles_in_hour_list)      
   peak_hour_vehicle_count_result = (f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_hour_vehicle_count}")
   print(peak_hour_vehicle_count_result) 

   #Calculate hours between which the most numbers of vehicles through Hanley Highway/Westway were recorded
   peak_hour_start = hanley_vehicles_in_hour_list.index(peak_hour_vehicle_count)
   peak_hour_end = peak_hour_start + 1
   peak_hour_results =(f"The most vehicles through Hanley Highway/Westway were recorded between {peak_hour_start}:00 and {peak_hour_end}:00")
   print(peak_hour_results)

   #Calculate number of hours of rain
   hours_of_rain_list = list(hour_list)#copy hour list to not alter original hour list
   for i in range(24):
      for j in range(total_vehicle_count):
         if "Rain" in data_list[j][5] and int(data_list[j][2][0:2]) == i:
            hours_of_rain_list[i] += 1
         else:
            continue
   #this loop below goes through the hours of rain list to see whether it has rained in that hour
   number_of_hours_rain = 0
   for i in range(len(hours_of_rain_list)):
      if hours_of_rain_list[i] != 0:
         number_of_hours_rain += 1
      else:
         continue
   number_of_hours_rain_result = (f"The number of hours of rain for this date is {number_of_hours_rain}")
   print(number_of_hours_rain_result)

   #Created list for results so it is to put results in text file
   data_results = [selected_data_result, total_vehicle_result, total_truck_count_result, electric_vehicles_count_result, two_wheeled_vehicles_count_result, busses_heading_north_result, vehicles_travelling_staight_result, truck_percentage_result, bike_average_result, speeding_vehicles_result, elm_avenue_junction_vehicles_result, hanley_highway_junction_vehicles_result, elm_avenue_scooters_percentage_result, peak_hour_vehicle_count_result,peak_hour_results, number_of_hours_rain_result]

   #Create text file
   with open("results.txt", 'a') as f:
      for results in data_results: 
         f.write(str(results) + "\n")#writes every data results in the text file on a new line
      f.write("*" * 90 + "\n")#just a line to seperate new appended output data 

   #Create Histogram
   #reference for video i used for help, making histogram is below
   win = GraphWin("Histogram", 1100, 600)#opens window for histogram

   #Create title 
   title = Text(Point(260, 30), f"Histogram of Vehicle Frequency per Hour ({day:02}/{month:02}/{year})")
   title.draw(win)#puts title on window
   title.setSize(12)

   #create colour legends(one for Elm and one for Hanley)
   elm_colour_label = Text(Point(190 , 60), "Elm Avenue/Rabbit Road")
   elm_colour_label.draw(win)
   elm_colour = Rectangle(Point(70, 50), Point(90, 70))
   elm_colour.draw(win)
   Elm_avenue_Elements_styling(elm_colour_label, elm_colour)#changes colour of labels to colour legend 

   hanley_colour_label = Text(Point(190 , 90), "Hanley Highway/Westway")  
   hanley_colour_label.draw(win)
   hanley_colour = Rectangle(Point(70, 80), Point(90, 100))
   hanley_colour.draw(win)
   Hanley_Elements_styling(hanley_colour_label, hanley_colour)

   #create x axis line
   x_axis_line = Line(Point(75, 530), Point(1025, 530))
   x_axis_line.draw(win)
   x_axis_label = Text(Point(550 , 570), "Hours 00:00 to 24:00")#x axis heading
   axis_labels(x_axis_label)
   x_axis_label.draw(win)
   x_hours_labels = ("0  01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23")
   hour_labels_starting_xposition = 114
   hour_starting_xposition_label = Text(Point(550 , 545), x_hours_labels)  
   hour_starting_xposition_label.draw(win)
   axis_labels(hour_starting_xposition_label)
   elm_vehicles_bars_xpos1 = 75#starting x position of first Elm bar
   hanley_vehicles_bars_xpos1 = 90##starting x position of first Hanley bar                                                                                                         
   highest_volume_both_junctions = max([max(elm_vehicles_in_hour_list), max(hanley_vehicles_in_hour_list)])
   max_height = 410# this is the maximum height i wanted the bar to go up by from the x axis
   #the reason for variable scaling factor was because some csv had large number of vehicles per hour,as a result some bars would go out the window, when i had a fixed scaling factor 
   scaling_factor = max_height / int(highest_volume_both_junctions)#this is so the highest volume of vehicles in a hour, for both junctions in a dataset, will not go beyond the max height when multiplied by the scaling factor
   fixed_ypos = 530#this is the ypos of the bar which will always stay the same as this will be touching the x axis line and have same ypos of x axis
   try:
      for i in range(24):
         actual_volume = int(elm_vehicles_in_hour_list[i])#volume of Elm vehicles per hour
         adjusted_frequency = actual_volume * scaling_factor#volume is adjusted so it better fits the window
         variable_ypos = fixed_ypos - adjusted_frequency#to get the second y position of the bar, minus the adjusted frequency from the fixed ypos of bar, to get the second ypos of the bar upwards from xaxis,relative to the actual volume
         elm_vehicles_bars_xpos2 = elm_vehicles_bars_xpos1 + 15#all bars are 15 units in the x direction(width)
         elm_vehicles_bar = Rectangle(Point(elm_vehicles_bars_xpos1, 530), Point(elm_vehicles_bars_xpos2, variable_ypos))#put all these variables in rectangle function
         elm_vehicles_bar.draw(win)#draw bar
         elm_vehicles_bars_xpos1 += 40#space between each bar is 40 units(15 for Elm bar, 15 for Hanley bar and 10 for space between the bars for one hour and the next)
         elm_count_label_xpos = elm_vehicles_bars_xpos2 - 8#the centre of the label for actual volume needs to be 8 from xpos2 to be in centre of its bar
         elm_count_label = Text(Point(elm_count_label_xpos, (variable_ypos-10)), elm_vehicles_in_hour_list[i])#subtract variable ypos by 10 so label is above its bar
         elm_count_label.draw(win)#draw label
         Graph_labels_size_styling(elm_count_label)#style elm label size
         Elm_avenue_Elements_styling(elm_count_label, elm_vehicles_bar)#style elm elements colour
         #repeat for Hanley
         actual_volume = int(hanley_vehicles_in_hour_list[i])#volume of Hanley vehicles per hour
         adjusted_frequency = actual_volume * scaling_factor                                                                                                                
         variable_ypos = fixed_ypos - adjusted_frequency
         hanley_vehicles_bars_xpos2 = hanley_vehicles_bars_xpos1 + 15
         hanley_vehicles_bar = Rectangle(Point(hanley_vehicles_bars_xpos1, 530), Point(hanley_vehicles_bars_xpos2, variable_ypos))
         hanley_vehicles_bar.draw(win)
         hanley_vehicles_bars_xpos1 += 40
         hanley_count_label_xpos = hanley_vehicles_bars_xpos2 - 8
         hanley_count_label = Text(Point(hanley_count_label_xpos, (variable_ypos-10)), hanley_vehicles_in_hour_list[i])
         hanley_count_label.draw(win)
         Graph_labels_size_styling(hanley_count_label)
         Hanley_Elements_styling(hanley_count_label, hanley_vehicles_bar)
      win.getMouse()
      win.close()
   except GraphicsError:#reason for try/except was because whenever user clicks x the close window containg histogram an error would occur
      print("To close the window containing the histogram, click on the window not the x button")
   
   #ask user if they want to selct another date and therefore start loop again
   while not end_loop:
      loop_again = input("Do you want to select another data file for a different date? \nyes or no:  ")
      if loop_again.lower() == "yes":
         break #break out of this loop and the restart the main loop 
      elif loop_again.lower() == "no":
         end_loop = True#the main loop is broken so no relooping and out of code
      else:
         print("Please enter yes or no")

#loop has been broken
print("End of run")

#references:
#For help in making the histogram rectangles and lines i adapted the codes found in videos in the Python | Graphics.py playlist, from the compineering youtube channel, links are below
#for making lines, i adapted code from this video: https://www.youtube.com/watch?v=GLl8CkOGwEg&list=PL5FKO8x2yHG-UM-6otrJ0aqyg_wWsfb0B&index=5
#for making rectangles, i adapted code from this video: https://www.youtube.com/watch?v=P70A9E3D_SA&list=PL5FKO8x2yHG-UM-6otrJ0aqyg_wWsfb0B&index=7

