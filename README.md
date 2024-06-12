# Ocean Insights

#### Description
For my final project I created a program for users (beach-goers) to effectevly plan their beach activities (surfing, swimming, diving / scuba, snorkeling, kayaking ) based on ocean data. Ocean data is sythesized by combination of tide / water levels data and Meteorological Data. Ocean data is from the API provided by the National Oceanic and Atmospheric Administration [Tide and Currents API](https://api.tidesandcurrents.noaa.gov/api/prod/) 

For this projects, my valid roles / asserts for the user imput would be activites connected to the API data. In order to run this code, for the user persona of a beginner surfer in Florida, change directories into the directory containing function.py and classes.py in your terminal and run python functions.py.

The use personas this program is designed for is surfers, kayakers/paddleboarders and scuba divers. To make this possible I decided to build my code by creating a class called `Station` that would take in the parameters specific to location of the station. 

I created __six methods__ within the `Station` that provide key metrics and advice to people looking to beach at that station:

* `go_to_beach` : Provides for the user persona based on tide conditions. Specific advice is outputed to the specific role aftet tide direction and height is checked. 


* `fetch_tide_data` : Tide data is fetched from API using the station id. Tide direction (rising or falling) and average tide height is computed. DataFrame showing tide data is outputed. 


* `combine_data` : combine data sources for wind data and tide data (same time inerval for both), results would be an attribute. This functions needs to be run before any other methods for the different users is run.  


* `surfer_skill_level`: Provides advice for surfers based on their skill level and wind conditions. It checks the wind speed and the surfer's skill level and returns applicable advice.


* `fetch_water_temperature`: Uses API to fetch water temp and computes the water temp average. Based on this data, it determines that water quality to be Clear" or "Murky" based on a temp threshold.


* `fetch_water_level_summary`: Computes summary stats (e.g., mean, min, max) of water levels from the combined data. This is then shown to the user in summary DataFrame.


__Inspiration__: This project was orginally sparked from [Mingson Leung's](https://github.com/mingsonleung/terminal-weather-app/) project that was shown in class. As somebody who loves the beach, I want to create something that would be useful for other individual that also love to the beach and ocean activities based on real data from the API. 


---

#### Project Structure

```
├── my_module   
│   ├── classes.py                  # Station Class Code
│   ├── functions.py                # Main function, runner file
│   ├── test_functions.py           # Testing functions
├── ocean-insights-notebook.ipynb   # Notebook format
```
