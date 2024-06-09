"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

#from functions import my_func, my_other_func
from classes import *
##
##
florida_station = Station()

def test_fetch_tide_data():
    assert florida_station.fetch_tide_data().iloc[0]['water_level'] == 0.418
    
def test_combine_data():
    assert florida_station.fetch_tide_data().iloc[1]['wind_speed'] == 10.50
    
def test_go_to_beach():
    assert florida_station.go_to_beach('kayaker') == 'Tide conditions are not suitable for kayaking right now.'

def test_surfer_skill_level():
    assert florida_station.surfer_skill_level('advanced') == 'Advanced surfers have the skills to handle windy conditions, stay safe!'

def test_fetch_water_temperature():
    assert florida_station.fetch_water_temperature() == 'Clear'
    
def test_water_level_summary():
    assert florida_station.water_level_summary().iloc[-1] == 2.38



 