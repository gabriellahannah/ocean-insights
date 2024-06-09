"""Classes used throughout project"""

import requests
import pandas as pd

# station represents where ocean data is being monitored, like what specific beach etc.

class Station:
    
    def __init__(self, station_id=8724580):
        
        # Floria (default)
        self.station_id = station_id
        self.tide_height = None
        self.tide_direction = None
        self.wind = None
        self.water_temperature = None
        
        # Get tide data and Combine data sources
        self.tide_data = self.fetch_tide_data()
        self.combined_data = self.combine_data()
       
    def fetch_tide_data(self):
        
        # Fetch tide data from the API
        request = requests.get(f'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20240609&end_date=20240609&station={self.station_id}&product=water_level&datum=MLLW&time_zone=gmt&units=english&application=DataAPI_Sample&format=json')
        tide_data = pd.DataFrame(request.json()['data'])[['t', 'v']]
        tide_data.columns = ['time', 'water_level']

        # Extract tide height and direction
        tide_data['water_level'] = tide_data['water_level'].astype(float)
        self.tide_height = tide_data['water_level'].mean()
        temp = tide_data['water_level'].iloc[int(len(tide_data) / 2)] - tide_data['water_level'].iloc[0]
        
        if temp > 0:
            self.tide_direction = 'Rising' 
            
        if temp <= 0:
            self.tide_direction = 'Falling'
     
        return tide_data
            
   
    def combine_data(self):
        
        # Fetch wind data
        wind_request = requests.get(f'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20240609&end_date=20240609&&station={self.station_id}&product=wind&time_zone=lst_ldt&units=english&interval=m&application=DataAPI_Sample&format=json')
        wind_data = pd.DataFrame(wind_request.json()['data'])[['t', 's']]
        wind_data.columns = ['time', 'wind_speed']
        wind_data['wind_speed'] = wind_data['wind_speed'].astype(float)

        
        temp = wind_data['wind_speed'].mean()
        if temp > 4:
            self.wind = 'Windy' 
            
        if temp <= 4:
            self.wind = 'Not windy'

        
        # Combine data sources
        return pd.merge(self.tide_data, wind_data, on='time', how='left')

     
    def go_to_beach(self, role='surfer'):
        
        '''
        This function takes in a user persona and provides insight as 
        to whether or not this person may want to go to the beach
        
        params:
            - role: The user persona 
        returns:
            - A printed statement of advice for the user
            
        '''
        
        assert role.lower() in ['surfer', 'scuba diver', 'kayaker', 'paddle_boarder']

        # These conditionals determine output based on the tide for each activity
        if role == 'surfer':
            
            if self.tide_height > 3 and self.tide_direction == 'Rising':
                return "The tide is rising, which often leads to better waves. It's a good time to surf."
            elif self.tide_height > 3 and self.tide_direction == 'Falling':
                return "The tide is falling. Wave conditions might change."
            else:
                return "Tide conditions are not optimal for surfing right now."
        
        elif role == 'kayaker':
            
            if self.tide_height >= 2 and self.tide_height <= 4:
                return "Tide conditions are suitable for kayaking."
            else:
                return "Tide conditions are not suitable for kayaking right now."
        
        elif role == 'paddle_boarder':
            
            if self.tide_height >= 1.5 and self.tide_height <= 3:
                return "Tide conditions are suitable for paddle boarding."
            else:
                return "Tide conditions are not suitable for paddle boarding right now."
        
        elif role == 'scuba diver':
            
            if self.tide_height >= 3 and self.tide_height <= 5:
                return "Tide conditions are suitable for scuba diving."
            else:
                return "Tide conditions are not suitable for scuba diving right now."
            
            
    def surfer_skill_level(self, skill_level='beginner', wind='windy'):
        
        '''
        This function provides advice for surfers based on their skill level and wind conditions
        
        params:
            - skill_level: The surfer's skill level. Options are 'beginner', 'intermediate', or 'advanced'
            - wind: Wind conditions. Options are 'windy' or 'not windy'
        returns:
            - A printed statement of advice for the surfer
            
        '''
        
        assert skill_level.lower() in ['beginner', 'intermediate', 'advanced']
        assert self.wind.lower() in ['windy', 'not windy']
        
        if skill_level.lower() == 'beginner':
            if self.wind.lower() == 'windy':
                return "As a beginner surfer, it's recommended to avoid surfing in windy conditions."
            else:
                return "As a beginner surfer, you can enjoy surfing in calm conditions!"
        
        elif skill_level.lower() == 'intermediate':
            if self.wind.lower() == 'windy':
                return "Intermediate surfers can handle some wind!"
            else:
                return "Intermediate surfers can enjoy surfing in various conditions!"
        
        elif skill_level.lower() == 'advanced':
            if self.wind.lower() == 'windy':
                return "Advanced surfers have the skills to handle windy conditions, stay safe!"
            else:
                return "For advanced surfers, ideal surfing conditions have moderate winds or calm seas!"
            
    def fetch_water_temperature(self):
        
        # Fetch water temps data from the API
        water_temperature_request = requests.get(f'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20240609&end_date=20240609&&station={self.station_id}&product=water_temperature&datum=MLLW&time_zone=gmt&units=english&application=DataAPI_Sample&format=json')
        temperature_data = pd.DataFrame(water_temperature_request.json()['data'])[['t', 'v']]
        temperature_data.columns = ['time', 'temperature']
        temperature_data['temperature'] = temperature_data['temperature'].astype(float)
        
        self.water_temperature = temperature_data['temperature'].mean()
        water_quality = "Clear" if self.water_temperature > 75 else "Murky"
        
        return water_quality
    
    def fetch_water_level_summary(self):
        
        water_level_summary = self.combined_data['water_level'].describe()
        
        return water_level_summary
