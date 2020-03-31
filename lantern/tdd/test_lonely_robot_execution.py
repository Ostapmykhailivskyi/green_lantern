import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = "E"
        asteroid = Asteroid(x, y)
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestTurns:
    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(self.x * 2, self.y * 2)

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N"),
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "E"),
                ("E", "S"),
                ("S", "W"),
                ("W", "N"),
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,steps,expect_pos",
        (
                ("N", 2, (10, 17)),
                ("W", 5, (10, 10)),
                ("S", 8, (2, 15)),
                ("E", 4, (14, 15)),
        )
    )
    def test_move_forward(self, current_direction, steps, expect_pos):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.move_forward(steps)
        assert robot.x, robot.y == expect_pos

    @pytest.mark.parametrize(
        "current_direction, steps, expect_pos",
        (
            ("E", 6, (4, 15)),
            ("N", 1, (10, 16)),
            ("W", 4, (10, 11)),
            ("S", 3, (8, 15)),
        )
    )
    def test_move_backward(self, current_direction, steps, expect_pos):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.move_backward(steps)
        assert robot.x, robot.y == expect_pos

    def test_if_robot_fell(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, "E")
        with pytest.raises(ValueError):
            robot.move_forward(100)
        with pytest.raises(ValueError):
            robot.move_backward(100)