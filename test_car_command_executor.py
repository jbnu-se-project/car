import unittest
from car import Car
from car_command_executor import CarCommandExecutor
from car_controller import CarController
from unittest.mock import patch
from io import StringIO

class TestCarCommandExecutor(unittest.TestCase):
    def setUp(self):
        self.car = Car(engine_on=False)
        self.car_controller = CarController(self.car)
        self.car_command_executor = CarCommandExecutor(self.car_controller)

    # def test_multiple_commands_with_space(self):
    #     """공백으로 구분된 여러 명령어가 할 줄로 입력되었을때 개별 명령어로 인식"""
    #     # Given: 엔진이 꺼진 상태
    #     self.assertFalse(self.car.engine_on)

    #     # When: 공백으로 구분된 연러 명령어 실행
    #     result = self.car_command_executor.execute_command("BRAKE ENGINE_BTN")

    #     # Then: BRAKE와 ENGINE_BTN 명령어 별도로 인식
    #     self.assertTrue(result)
    #     self.assertTrue(self.car.engine_on)
    
    def test_multiple_invalid_commands(self):
        """
        다양한 커맨드 조합으로 시동 동작 테스트.
        """
        fail_message = "유효하지 않은 입력입니다.\n\n[엔진 제어 시도 - 실패] : 브레이크와 엔진 버튼을 동시에 눌러야 시동이 걸립니다."
        test_cases = [
            # 커맨드 조합, 예상 결과 및 출력 메시지
            ("BRAKE ENGINE_BTN INVALID_INPUT", False, fail_message),  # TC2-1
            ("INVALID_INPUT BRAKE ENGINE_BTN", False, fail_message),  # TC2-2
            ("BRAKE NVALID_INPUT ENGINE_BTN", False, fail_message),  # TC2-3

            ("ENGINE_BTN BRAKE", False, fail_message),  # 기본 조건 (잘못된 순서)
            ("BRAKE ENGINE_BTN", True, "[엔진 제어 시도 - 성공]"),  # 기본 조건 (올바른 순서)
        ]

        for commands, expected, output in test_cases:
            with self.subTest(commands=commands), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Given: 초기 상태
                self.assertFalse(self.car.engine_on)

                # When: 커맨드 실행
                result = self.car_command_executor.execute_command(commands)
                printed_output = mock_stdout.getvalue().strip()

                # Then: 결과 확인
                self.assertEqual(result, expected)
                self.assertEqual(printed_output, output)

                # 엔진 상태 확인 및 초기화
                self.assertEqual(self.car.engine_on, expected)
                if self.car.engine_on:
                    self.car_controller.toggle_engine()

if __name__ == '__main__':
    unittest.main()
