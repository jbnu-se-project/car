import unittest

from car import Car
from car_controller import CarController
from controller.door_lock_controller import DoorLockController


class TestDoorLockController(unittest.TestCase):

    def setUp(self):
        self.car = Car(engine_on=True, speed=0, lock=True, trunk_status=True)
        self.car_controller = CarController(self.car)
        self.door_lock_controller = DoorLockController(self.car_controller)

    def test_all_door_lock_all_doors_closed_and_locked(self):
        # 모든 문이 닫히고 이미 잠긴 상태에서 모든 문을 잠그는 시도
        self.door_lock_controller.all_door_lock()
        self.assertEqual(self.car.left_door_lock, "LOCKED")
        self.assertEqual(self.car.right_door_lock, "LOCKED")

    def test_all_door_lock_all_doors_open(self):
        # 모든 문이 열린 상태에서 모든 문을 잠그는 시도
        self.car.open_left_door()
        self.car.open_right_door()

        self.door_lock_controller.all_door_lock()
        self.assertEqual(self.car.left_door_lock, "LOCKED")
        self.assertEqual(self.car.right_door_lock, "LOCKED")

    def test_all_door_unlock_while_driving(self):
        # 주행 중에 모든 문을 잠금 해제하는 시도
        self.car.accelerate()
        self.door_lock_controller.all_door_unlock()

        self.assertEqual(self.car.left_door_lock, "LOCKED")
        self.assertEqual(self.car.right_door_lock, "LOCKED")

    def test_all_door_unlock_when_already_unlocked(self):
        # 모든 문이 이미 잠김 해제 상태에서 모든 문을 잠금 해제하는 시도
        self.car.unlock_left_door()
        self.car.unlock_right_door()
        self.car.unlock_vehicle()

        self.door_lock_controller.all_door_unlock()
        self.assertEqual(self.car.left_door_lock, "UNLOCKED")
        self.assertEqual(self.car.right_door_lock, "UNLOCKED")

    def test_left_door_lock_when_already_locked(self):
        # 왼쪽 문이 이미 잠긴 상태에서 왼쪽 문을 잠그는 시도
        self.door_lock_controller.left_door_lock()
        self.assertEqual(self.car.left_door_lock, "LOCKED")

    def test_left_door_unlock_while_driving(self):
        # 주행 중에 왼쪽 문을 잠금 해제하는 시도
        self.car.accelerate()

        self.door_lock_controller.left_door_unlock()
        self.assertEqual(self.car.left_door_lock, "LOCKED")

    def test_left_door_unlock_when_already_unlocked(self):
        # 왼쪽 문이 이미 잠김 해제 상태에서 왼쪽 문을 잠금 해제하는 시도
        self.car.unlock_left_door()

        self.door_lock_controller.left_door_unlock()
        self.assertEqual(self.car.left_door_lock, "UNLOCKED")

    def test_right_door_lock_when_already_locked(self):
        # 오른쪽 문이 이미 잠긴 상태에서 오른쪽 문을 잠그는 시도
        self.door_lock_controller.right_door_lock()
        self.assertEqual(self.car.right_door_lock, "LOCKED")

    def test_right_door_unlock_while_driving(self):
        # 주행 중에 오른쪽 문을 잠금 해제하는 시도
        self.car.accelerate()
        self.door_lock_controller.right_door_unlock()

        self.assertEqual(self.car.right_door_lock, "LOCKED")

    def test_right_door_unlock_when_already_unlocked(self):
        # 오른쪽 문이 이미 잠김 해제 상태에서 오른쪽 문을 잠금 해제하는 시도
        self.car.unlock_right_door()

        self.door_lock_controller.right_door_unlock()
        self.assertEqual(self.car.right_door_lock, "UNLOCKED")

if __name__ == '__main__':
    unittest.main()