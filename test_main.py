import unittest
from unittest.mock import MagicMock
from car_controller import CarController
from car import Car
from main2 import EngineController


class TestEngineController(unittest.TestCase):
    def setUp(self):
        self.car = Car()
        self.car_controller = CarController(self.car)
        self.engine_controller = EngineController(self.car_controller)

        self.car_controller.get_speed = MagicMock(return_value=0)
        self.car_controller.get_engine_status = MagicMock(return_value=False)
        self.car_controller.toggle_engine = MagicMock()

    def test_engine_off_when_stationary(self):
        self.car_controller.get_speed.return_value = 0
        self.car_controller.get_engine_status.return_value = False

        result = self.engine_controller.handle_engine_control()
        self.car_controller.toggle_engine.assert_called_once()
        self.assertTrue(result)

    def test_engine_on_when_stationary(self):
        self.car_controller.get_speed.return_value = 0
        self.car_controller.get_engine_status.return_value = True

        result = self.engine_controller.handle_engine_control()
        self.car_controller.toggle_engine.assert_called_once()
        self.assertTrue(result)

    def test_engine_toggle_is_ignored_when_driving(self):
        self.car_controller.get_speed.return_value = 50
        self.car_controller.get_engine_status.return_value = True

        result = self.engine_controller.handle_engine_control()
        self.car_controller.toggle_engine.assert_not_called()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()