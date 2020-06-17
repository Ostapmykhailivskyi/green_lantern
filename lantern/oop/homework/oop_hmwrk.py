class Cat:

    def __init__(self, age):
        self.saturation_level = 50
        self.age = age
        self.average_speed = self._set_average_speed()

    def _reduce_saturation_level(self, value):
        self.saturation_level = self.saturation_level - value
        if self.saturation_level < 0:
            return 0

    def _increase_saturation_level(self, value):
        self.saturation_level = self.saturation_level + value
        if self.saturation_level >= 100:
            return 100

    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        elif self.age in range(8, 11):
            return 9
        elif self.age > 10:
            return 6

    def eat(self, product):
        if product == "fodder":
            self._increase_saturation_level(10)
        elif product == "apple":
            self._increase_saturation_level(5)
        elif product == "milk":
            self._increase_saturation_level(2)
        return self.eat

    def run(self, hours):
        ran_km = self.average_speed * hours
        if ran_km <= 25:
            self._reduce_saturation_level(2)
        elif ran_km in range(26, 51):
            self._reduce_saturation_level(5)
        elif ran_km in range(51, 101):
            self._reduce_saturation_level(15)
        elif ran_km in range(101, 201):
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)
        return f"Your cat ran {ran_km} kilometers"

    def get_saturation_level(self):
        return 'Your cat is died :(' if self.saturation_level == 0 else self.saturation_level

    def get_average_speed(self):
        return self.average_speed


class Cheetah (Cat):
    def eat(self, product):
        if product == "gazelle":
            self._increase_saturation_level(value=30)
        elif product == "rabbit":
            self._increase_saturation_level(value=15)
            return self.eat

    def _set_average_speed(self):
        if self.age <= 5:
            return 90
        elif self.age in range(6, 16):
            return 75
        elif self.age > 15:
            return 40


class Wall:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.height * self.width

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        count_of_lines_in_roll = roll_length_m // self.height
        count_of_lines = self.width // roll_width_m
        number_of_rolls_of_wallpaper = count_of_lines / count_of_lines_in_roll
        return number_of_rolls_of_wallpaper


class Roof:
    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == "gable":
            square_of_the_roof = (self.height * self.width) * 2
        elif self.roof_type == "single-pitch":
            square_of_the_roof = (self.height * self.width)
        else:
            raise ValueError("Sorry there is only two types of roofs")
        return square_of_the_roof


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.metal_price = 3
        self.wood_price = 10

    def door_square(self):
        door_square = self.height * self.width
        return door_square

    def door_price(self, material):
        if material == "wood":
            return self.wood_price * self.door_square()
        elif material == "metal":
            return self.metal_price * self.door_square()
        else:
            raise ValueError("Sorry we don't have such material")

    def update_metal_price(self, new_price):
        self.metal_price = new_price
        return self.update_metal_price

    def update_wood_price(self, new_price):
        self.wood_price = new_price
        return self.update_wood_price


class House:
    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):
        try:
            if self.__walls.__len__() == 4:
                raise ValueError("Our house can not have more than 4 walls")
            elif not width or not height:
                raise ValueError('Value must be not 0')
        except ValueError:
            raise
        self.__walls.append(Wall(width, height))

    def create_roof(self, width, height, roof_type):
        if self.__roof:
            raise ValueError("The house can not have two roofs")
        elif width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            self.__windows.append(Window(width, height))

    def create_door(self, width, height):
        try:
            if self.__door:
                raise ValueError('The house can not have two doors')
            elif not width or not height:
                raise ValueError('Value must be not 0')
        except ValueError:
            raise
        else:
            self.__door = Door(width, height)

    def get_count_of_walls(self):
        return self.__walls.__len__()

    def get_count_of_windows(self):
        return self.__windows.__len__()

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, new_wood_price):
        self.__door.wood_price = new_wood_price

    def update_metal_price(self, new_metal_price):
        self.__door.metal_price = new_metal_price

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        sum_of_all_walls_square = 0
        for wall in self.__walls:
            sum_of_all_walls_square += wall.wall_square()
        return sum_of_all_walls_square

    def get_windows_square(self):
        sum_of_all_windows_square = 0
        for window in self.__windows:
            sum_of_all_windows_square += window.window_square()
        return sum_of_all_windows_square

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        try:
            if not roll_width_m or not roll_length_m:
                raise ValueError('Sorry length must be not 0')
        except ValueError:
            raise
        else:
            rolls_for_all_our_walls = 0
            for wall in self.__walls:
                rolls_of_wallpaper_for_current_wall = wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m)
                rolls_for_all_our_walls += rolls_of_wallpaper_for_current_wall
            return rolls_for_all_our_walls

    def get_room_square(self):
        return self.get_walls_square() - self.get_windows_square() - self.get_door_square()