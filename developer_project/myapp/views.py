# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import asyncio
import aiohttp
import random
from django.shortcuts import render
from services.services import google_sheet
from django.template.defaulttags import register
# from myapp.models import Location

#dictionary for icons
d = {
    'thunderstorm': '11d',
    'snow': '13d',
    'rain': '10d',
    'clear': '01d',
    'drizzle': '09d',
    'atmosphere': '50d',
    'clouds': '02d' 
}

atmosphere = ['Mist', 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Dust', 'Ash', 'Squall', 'Tornado']
# api_key = "ea28a5f31255e50647af6bcf50377941"
# api_key = "2ec45f60e91ca112feaa654baf6764cc"
api_key ="a5ecef3ba4c08c8a0fc220cdf34aa40e"

locations = google_sheet()

@register.filter
def get_range(value):
    return range(value)

@register.filter
def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def home(request):
    # Call google sheet api services and display all 250 locations on home page
    locations.sort(key=lambda x: x['City'])
    context = {'locations': locations}    
    return render(request, "myapp/home.html", context)

# session calling api to retrieve data
async def get_location(session, url):
    async with session.get(url) as response:
        location_data = await response.json()
        return location_data

# responsible for search functionalities logic 
async def search(request):
    res = []
    actions = []
    city_state = []
    search = ""

    # get searched weather
    if request.method == "GET":
        search = request.GET['searched']

    # Async function with session to communicate with api 
    async with aiohttp.ClientSession() as session:
        for location in locations:
            city = location['City']
            state = location['State']
            city_state.append((city,state))
            url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}".format(city, state, api_key)
            actions.append(asyncio.ensure_future(get_location(session, url)))

        # return event loop to get all location weather information from api
        location_res = await asyncio.gather(*actions)

        # Iterate through location information that correspondings to searched weather
        for location, data in zip(city_state[:60], location_res[:60]):
            #If api calls exceeds limit of 60 then api key will potentially be suspended and location_res returns 404 status code
            if data['cod'] == '404':
                continue
            if data['cod'] == '424':
                return render(request, "myapp/error.html")
            #Check if searched string equals api response main weather
            elif data['weather'][0]['main'].lower() == search.lower():
                weathers = {
                    'city': location[0],
                    'state': location[1],
                    'temperature': data['main']['temp'],
                    'wind': data['wind']['speed'],
                }
                res.append(weathers)
            #Check if search equals atmosphere and get current location weather in atmosphere
            elif search.lower() == 'atmosphere' and data['weather'][0]['main'] in atmosphere:
                weathers = {
                    'city': location[0],
                    'state': location[1],
                    'temperature': data['main']['temp'],
                    'wind': data['wind']['speed'],
                }
                res.append(weathers)

    icon = d[search.lower()]
    context = {'weathers': res, 'search': search, 'icon': icon}
    return render(request, "myapp/search.html", context)
