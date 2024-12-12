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
        result = self.engine_controller.handle_engine_control()

        # Then: 시동이 걸리지 않아야 함
        self.assertFalse(result)
        self.assertFalse(self.car.engine_on)

    def test_engine_start_with_sequential_input(self):
        """
        브레이크 신호를 보내고 엔진 버튼을 순차적으로 눌렀을 때는 시동이 걸리지 않는다
        ex)
        BREAK
        ENGINE_BTN
        """
        # Given: 엔진이 꺼진 상태
        self.assertFalse(self.car.engine_on)

        # When: 브레이크 신호를 보내고 나서 엔진 버튼을 누름
        self.engine_controller.handle_brake_command()
        result = self.engine_controller.handle_engine_control()

        # Then: 시동이 걸리지 않아야 함
        self.assertFalse(result)
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
        result = self.engine_controller.process_simultaneous_commands(["BRAKE", "ENGINE_BTN"])

        # Then: 시동이 걸려야함
        self.assertTrue(result)
        self.assertTrue(self.car.engine_on)

    def test_engine_start_with_various_commands(self):
        """
        다양한 커맨드 조합으로 시동 동작 테스트.
        """

        test_cases = [
            # 커맨드 조합, 예상 결과                            # TC1: 3개 이상의 다중 명령어
            (["BRAKE", "ENGINE_BTN", "ACCELERATE"], False),     # TC1-1
            (["ACCELERATE", "BRAKE", "ENGINE_BTN"], False),     # TC1-2
            (["BRAKE", "ACCELERATE", "BRAKE"], False),          # TC1-3
            (["UNLOCK", "BRAKE", "ENGINE_BTN"], False),         # TC1-4
            (["LEFT_DOOR_OPEN", "BRAKE", "ENGINE_BTN"], False), # TC1-5
            (["TRUNK_OPEN", "BRAKE", "ENGINE_BTN"], False),     # TC1-6
            
            (["ENGINE_BTN", "BRAKE"], False),                   # 기본 조건
            (["BRAKE", "ENGINE_BTN"], True),                    # 기본 조건
        ]

        for commands, expected in test_cases:
            with self.subTest(commands=commands):
                # Given: 초기 상태
                self.assertFalse(self.car.engine_on)
                
                # When: 커맨드 실행
                result = self.engine_controller.process_simultaneous_commands(commands)

                # Then: 결과 확인
                self.assertEqual(result, expected)
                self.assertEqual(self.car.engine_on, expected)

                # 엔진 상태 초기화
            if self.car.engine_on:
                self.car_controller.toggle_engine()

if __name__ == '__main__':
    unittest.main()
