# DeveloperProject

*************************
# Overview:

A simple website that allows a user to search up certain weather conditions. The website consumes data from the openweathermap API and thus the search will return a list of locations that are experiencing the weather condition that the user searched.

Notes: All keys to openweathermap.org and google sheet api are hardcoded into the program; did not separate keys to these API in a different file (not the best practice).

*************************
# Preview:

Home Page: Displays dropdown search bar and the top 250 us cities from the google sheet.
<img width="600" alt="Screen Shot 2021-08-17 at 11 04 36 PM" src="https://user-images.githubusercontent.com/22754752/129831212-166bd6f6-2034-4e58-a32b-c8054f68ba87.png">

Search Page: Displays locations that match the weather conditions searched.
<img width="600" alt="Screen Shot 2021-08-17 at 11 08 29 PM" src="https://user-images.githubusercontent.com/22754752/129831245-2c429b3f-9088-4829-97be-598ba23a2b32.png">


*************************
# How to run the website:
- Clone project repository by running: ```git clone <repository-name>``` into a local machine with your github credentials.
- Install Python3 into local machine: https://www.python.org/downloads/ or run ```brew install python3``` on Macos if you have brew installed. 
- Go into developer_project directory and create a file called api_key.py and add your api key like so: API_KEY = <Your-API-KEY>
- Create a virtual environment for the project folder by running this command: ```python3 -m venv <myenvname>``` or ```py -m venv <myenvname>```.
- Once you have your virtual environment created, activate virtual env by running: ```source /<myenvname>/bin/activate``` in terminal or ```<myenvname>\Scripts\activate``` on windows cmd.
- Download dependencies in the requirement.txt file by running this command: ```pip3 install -r requirements.txt```
- Go to project folder and run ```python3 manage.py runserver``` or ```python manage.py runserver``` or ```py3 manage.py runserver``` to run program
- Finally, go your browser and type http://127.0.0.1:8000/ in the address field.
 
*************************
# Future Considerations:

1. What features should be implemented in future versions?
- I was thinking of implementing single pages for separate city in case a user just wanted to check information for only one city and not have the page too busy.
- Adding different search inquiries such as searching by city, state, temperature, timezone, etc.
- Making the search functionalities asynchronous if I decide to search by city and state to speed up page load up. Meaning as I am searching, I am making requests to the API and thus display data on the frontend as I am typing the city or state out.
- A cool thing we can do with this API is if someone was on a road trip, they could save the locations that they were visiting and the API could respond back with the current forecast for that road trip and update a user if there is any changes to a weather in a certain location.
- Adding pagination to home page; 250 items one page not really ideal in a design standpoint.

2. What are potential optimization opportunities?
- Making a 250 requests required me to search weather asynchronously but imagine if there was over 10000 requests. I would have to split up my requests load and load items by batches instead of all at once. It also kind of makes sense in a design standpoint since no one is going to scroll through 10000 items quickly. This way allows users to read the current loaded items and scroll down if they want to look up more data.
- We could store openweathermap or google sheet api data into database and query database in the backend to the frontend which could possibly speed up the overall website; although if one decides to change google sheet data by deleting or adding locations then those changes will not reflect in the frontend unless added to the database.
 
3. What could break this current version?
- A requests of 10000 api calls at a time may slow down or program or even break it. 
- The current free API version only allows 60 calls a min, so this could potentially break program by making key unusable for a certain period of time. This also can make my program susceptibles to errors since a non-working api key will cause of a lot of my values to be length 0 or None, which would cause website to display nothing or show error page.
- API are always changing therefore a change in the structure of the openweathermap API json response can cause my website to break because of the way I iterated through the response.
