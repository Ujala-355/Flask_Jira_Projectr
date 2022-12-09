
# Flask_Jira_Projectr
"M26.0406546,5 L14.9983562,5 C14.9983562,6.32163748 15.5233746,7.58914413 16.4579134,8.52368295 C17.3924523,9.45822178 18.6599589,9.98324022 19.9815964,9.98324022 L22.0151159,9.98324022 L22.0151159,11.9465283 C22.0168782,14.6974491 24.2474348,16.9265768 26.9983562,16.9265762 L26.9983562,5.95770152 C26.9983562,5.42877757 26.5695786,5 26.0406546,5 Z"

#  Jira
#  Project management tool.used Jira for bug-tracking and task management.
# In Jira I create API token

# First Task 
# File name jira1_project .

# I am Fetch all tickets from Jira API and save that in the database table.
# this is my Jira API 
## https://ujalasaini.atlassian.net/rest/api/2/search# 
# Number,Name,Description,Reporter,Status,Due Date if any this data i am store in mysql .
# In this task I am useing Request for get the data in url and json use for json formet data . mysql.connector for connect the data .I am useing cursor() for  iterate though the records of a table from a MySQL stored.

# Second Task
# I can  Change the status what I want the status . I am use 11 number to change tha status TO DO .Use 21 number to change the status IN PROGRESS .Use 31 number to change the status DONE.
# This is my URL
# https://ujalasaini.atlassian.net//rest/api/3/issue/TIC-27/transitions
# Third Task
#  I am create a UI to show the tickets from the database.I am install FLask .Flask is a python framework .render_template_string is a  function from the flask .By becoming a template file, we write HTML in it.In html I am useing for loop for start a loop and end for  endfor {% %}.In flask connect the mysql data than I create the UI .
# Fouth task 
# In html I am create a relaod button re-fetch or re-load MYSQL DATA.
