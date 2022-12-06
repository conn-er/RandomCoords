from math import cos, sin, sqrt, pi
import random


class RandomCoords:

    def __init__(self, center: list[float, float], diameter: int, units: str = 'km') -> None:

        valid_units = {'m', 'km', 'ft', 'mi'}
        self.center = center
        self.diameter = diameter
        self.units = units

        if self.units not in valid_units:
            raise ValueError(f"Units must be one of {valid_units}.")

    def __str__(self) -> str:

        return f'Center point: {self.center}\nDiameter ({self.units}): {self.diameter}\nUnits: {self.units}'

    def generate_coords(self, num_coords: int):

        if num_coords == 0:
            return self.__generate_coord()

        coords_list = []
        for _ in range(num_coords):
            coords_list.append(self.__generate_coord())

        return coords_list

    def __generate_coord(self) -> list[float, float]:

        conversion = {
            'm': 0.001,
            'mi': 1.60934,
            'ft': 0.0003048,
            'km': 1,
        }

        circle_lon_position, circle_lat_position = self.center[0], self.center[1]
        circle_radius = (self.diameter / 2) * conversion[self.units]

        random_radians = random.random() * 2 * pi
        random_decimal = sqrt(random.random())

        point_lon_position = ((circle_radius / 115) * random_decimal) * cos(random_radians) + circle_lon_position
        point_lat_position = ((circle_radius / 95) * random_decimal) * sin(random_radians) + circle_lat_position

        return [point_lon_position, point_lat_position]