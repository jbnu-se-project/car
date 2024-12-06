from unittest import TestCase

from car import Car
from car_command_executor import CarCommandExecutor
from car_controller import CarController


class TestCarCommandExecutor(TestCase):
    def setUp(self):
        self.car = Car(engine_on=False)
        self.car_controller = CarController(self.car)
        self.car_command_executor = CarCommandExecutor(self.car_controller)

    def test_multiple_commands_with_space(self):
        """공백으로 구분된 여러 명령어가 할 줄로 입력되었을때 개별 명령어로 인식"""
        # Given: 엔진이 꺼진 상태
        self.assertFalse(self.car.engine_on)

        # When: 공백으로 구분된 연러 명령어 실행
        result = self.car_command_executor.execute_command("BRAKE ENGINE_BTN")

        # Then: BRAKE와 ENGINE_BTN 명령어 별도로 인식
        self.assertTrue(result)
        self.assertTrue(self.car.engine_on)
