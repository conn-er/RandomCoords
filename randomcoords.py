from math import cos, sin, sqrt, pi
import random


class RandomCoords:

    def __init__(self, center: list[float, float], diameter: int, units: str = 'km') -> None:

        valid_units = {'m', 'km', 'ft', 'mi'}
        conversion_dict = {
            'm': 0.001,
            'mi': 1.60934,
            'ft': 0.0003048,
            'km': 1
        }

        self.center = center
        self.diameter = diameter
        self.units = units
        self.conversion = conversion_dict[units]

        if self.units not in valid_units:
            raise ValueError(f"Units must be one of {valid_units}.")

    def generate_coords(self, num_coords: int):

        coords = []

        for _ in range(num_coords):

            circle_radius = (self.diameter / 2) * self.conversion

            rand_rad = random.random() * 2 * pi
            rand_decimal = sqrt(random.random())

            pt_lon = ((circle_radius / 115) * rand_decimal) * cos(rand_rad) + self.center[0]
            pt_lat = ((circle_radius / 95) * rand_decimal) * sin(rand_rad) + self.center[1]

            coords.append((pt_lon, pt_lat))

        return coords