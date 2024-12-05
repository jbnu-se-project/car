import unittest

from car import Car
from car_controller import CarController
from controller.engin_controller import EngineController

class TestEngineStartController(unittest.TestCase):
    def setUp(self):
        self.car = Car(engine_on=False)
        self.car_controller = CarController(self.car)
        self.engine_controller = EngineController(self.car_controller)

    def test_engine_start_with_only_engine_button(self):
        """
        엔진 버튼만 눌렀을 때는 시동이 걸리지 않는다.
        ex)
        ENGINE_BTN
        """
        # Given: 엔진이 꺼진 상태
        self.assertFalse(self.car.engine_on)

        # When: 엔진 버튼 신호만 보냄
        self.engine_controller.handle_engine_control()

        # Then: 시동이 걸리지 않아야 함
        self.assertFalse(self.car.engine_on)

    def test_engine_start_with_sequential_input(self):
        """브레이크 신호를 보내고 엔진 버튼을 순차적으로 눌렀을 때는 시동이 걸리지 않는다"""
        # Given: 엔진이 꺼진 상태
        self.assertFalse(self.car.engine_on)

        # When: 브레이크 신호를 보내고 나서 엔진 버튼을 누름
        self.engine_controller.handle_brake_command()
        self.engine_controller.handle_engine_control()

        # Then: 시동이 걸리지 않아야 함
        self.assertFalse(self.car.engine_on)

    def test_engine_start_with_break_and_engine_button(self):
        """
        브레이크와 엔진 버튼 신호가 동시에 들어올 때만 시동이 걸린다.
        ex)
        BREAK ENGINE_BTN
        """
        # Given: 엔진이 꺼진 상태에서 시작
        self.assertFalse(self.car.engine_on)

        # When: 브레이크와 엔진 버튼 신호가 동시에 들어옴
        self.engine_controller.handle_simultaneous_commands(["BRAKE", "ENGINE_BTN"])

        # Then: 시동이 걸려야함
        self.assertTrue(self.car.engine_on)

if __name__ == '__main__':
    unittest.main()
