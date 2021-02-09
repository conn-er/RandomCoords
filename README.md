# RandomCoords
RandomCoords is a Python project that generates a uniform pseudo-random set of points and/or paths inside of a circle without the use of outside libraries. Useful for quickly generating test data for mapping solutions.

### Dependencies
- I made this using Python 3.9. You could probably go as old as Python 3.6, but YMMV.
- Note: The python script titled "test" uses folium to create maps based on the output.
    - This script is not essential to the runtime randomcoords, it is just a test script that utilizes randomcoords.

### Installation
- Currently, you have to download the script locally.
- In the future, this will be added to PyPi so I can use it at work. 
    - You could use this too, if you want, I guess. It is unlikely to break.

### Usage
- RandomCoords objects have a few parameters
    - center: a coordinate pair in [lat: float, lng: float] format that represents the center of the circle defined below.
    - diameter (int): diameter of the circle
    - units: units used in string format
        - valid input: 'm', 'km', 'ft', 'mi'
- RandomCoords objects have two methods you may call:
    - generate_coords(num_coords: int)
        - Generates num_coords amount of random points within the bounds of the RandomCoords object. 
    - generate_paths(num_paths: int, num_points_range: (int, int) = (10, 50), circle_radius_range: (int, int) = (15, 25))
        - Generates num_paths amount of random paths within the bounds of the RandomCoords object.
        - You probably don't want to change anything other than num_paths, but be my guest.
            - num_points_range defines the range of points per path. Higher numbers for larger paths, lower numbers for shorter paths.
            - circle_radius_range defines how small of a fraction you want the circle for the next point to be in.
                - For example, circle_radius_range=(15, 25) means the next point will be generated in a circle 1/15-1/25 as small as the RandomCoords circle.

### Todo
- Let user define a polygonal geofence if they don't want a circle.
    - However, it would not be difficult for a user to remove points from the output based on a geofence. 
- It may be good to return tuples instead of lists for increased speed.
    - The user can also convert the list to a tuple on their own end.
    - In my tests, runtime only went into the few-seconds range which IMO is acceptable for the use-case of this script. Increases in speed would probably be negligible.
