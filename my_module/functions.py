"""A collection of function for doing my project."""

from classes import *

# This is for the user persona of a beginner surfer in Florida 
def main():
    florida_station = Station()
    
    print('Beach recommendation:')
    print(florida_station.go_to_beach() + '\n')
    
    print('Surf recommendation:')
    print(florida_station.surfer_skill_level() + '\n')
    
    print('Water temperature:')
    print(florida_station.fetch_water_temperature() + '\n')
    
    # Fetch water level summary
    print('Water level summary:')
    print(florida_station.fetch_water_level_summary())

if __name__ == "__main__":
    main()