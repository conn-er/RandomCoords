# RandomCoords
RandomCoords is a short and sweet Python module that generates a uniform pseudo-random set of points inside of a circle on the surface of a sphere (e.g. the Earth) using only Python's stdlib. Useful for quickly generating test data for mapping solutions.

### Usage
- RandomCoords objects have a few parameters
    - center: a coordinate pair in [lat: float, lon: float] format that represents the center of the circle defined below.
    - diameter (int): diameter of the circle
    - units (str): units used in string format
        - valid input: 'm', 'km', 'ft', 'mi'
- RandomCoords objects have one method you may call:
    - generate_coords(num_coords: int)
        - Generates num_coords amount of random points within the bounds of the RandomCoords object. 
