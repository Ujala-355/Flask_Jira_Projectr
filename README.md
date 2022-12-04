# Flask_Jira_Projectr
# This is my Project
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
