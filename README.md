
# Flask_Jira_Projectr
# # https://www.google.com/url?sa=i&url=https%3A%2F%2Fworldvectorlogo.com%2Flogo%2Fjira-1&psig=AOvVaw0VDmO5Z6ZmeRZ1AnkHR2CO&ust=1670680049598000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJDlk6rW7PsCFQAAAAAdAAAAABAD
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
