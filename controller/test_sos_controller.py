import unittest

from car import Car
from car_controller import CarController
from controller.sos_controller import SOSController


class TestSOSController(unittest.TestCase):

    def setUp(self):
        # 기본 설정: 엔진이 꺼져있고, 차량은 정지 상태, 잠겨있으며, 트렁크는 닫혀 있는 상태
        self.car = Car(engine_on=False, speed=0, lock=True, trunk_status=True)
        self.car_controller = CarController(self.car)
        self.sos_controller = SOSController(self.car_controller)

    def test_activate_sos_engine_on_speed_above_zero(self):
        # 초기 상태 설정: 엔진이 켜져 있고,
        # 차량이 움직이고 있으며, 잠겨있고, 트렁크가 닫혀 있는 상태
        self.car.__engine_on = True
        self.car.__speed = 10

        self.sos_controller.activate_sos()

        # 차량이 정지했는지 확인
        self.assertEqual(self.car.speed, 0)

        # 모든 문 잠금 해제 확인
        self.assertFalse(self.car.lock)
        self.assertEqual(self.car.left_door_status, "OPEN")
        self.assertEqual(self.car.right_door_status, "OPEN")

        # 트렁크가 열렸는지 확인
        self.assertFalse(self.car.trunk_status)

        # 엔진이 꺼졌는지 확인
        self.assertFalse(self.car.engine_on)

    def test_activate_sos_engine_off_speed_zero(self):
        # 초기 상태 설정: 엔진이 꺼져 있고, 정지한 상태, 잠겨있고, 트렁크가 닫혀 있는 상태
        self.car._engine_on = False
        self.car._speed = 0

        self.sos_controller.activate_sos()

        # 차는 이미 정지 상태이므로 스피드 0 확인
        self.assertEqual(self.car.speed, 0)

        # 모든 문 잠금 해제 확인
        self.assertFalse(self.car.lock)
        self.assertEqual(self.car.left_door_status, "OPEN")
        self.assertEqual(self.car.right_door_status, "OPEN")

        # 트렁크가 열렸는지 확인
        self.assertFalse(self.car.trunk_status)

        # 엔진이 꺼져 있는지 확인 (변화가 없음)
        self.assertFalse(self.car.engine_on)

    def test_activate_sos_trunk_already_open(self):
        # 초기 상태 설정: 트렁크가 이미 열려있는 상태
        self.car._trunk_status = False

        self.sos_controller.activate_sos()

        # 차량이 정지했는지 확인
        self.assertEqual(self.car.speed, 0)

        # 모든 문 잠금 해제 확인
        self.assertFalse(self.car.lock)
        self.assertEqual(self.car.left_door_status, "OPEN")
        self.assertEqual(self.car.right_door_status, "OPEN")

        # 트렁크가 이미 열려있으므로 상태가 그대로인지 확인
        self.assertFalse(self.car.trunk_status)

        # 엔진이 꺼져 있는지 확인
        self.assertFalse(self.car.engine_on)

    def test_activate_sos_doors_already_unlocked(self):
        # 초기 상태 설정: 문이 이미 열려있는 상태
        self.car.__lock = False
        self.car.__left_door_status = "OPEN"
        self.car.__right_door_status = "OPEN"

        self.sos_controller.activate_sos()

        # 차량이 정지했는지 확인
        self.assertEqual(self.car.speed, 0)

        # 문이 이미 열려있으므로 상태가 그대로인지 확인
        self.assertFalse(self.car.lock)
        self.assertEqual(self.car.left_door_status, "OPEN")
        self.assertEqual(self.car.right_door_status, "OPEN")

        # 트렁크가 열렸는지 확인
        self.assertFalse(self.car.trunk_status)

        # 엔진이 꺼져 있는지 확인
        self.assertFalse(self.car.engine_on)


if __name__ == '__main__':
    unittest.main()