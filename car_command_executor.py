from controller.door_controller import OpenDoorController, ClosedDoorController
from controller.door_lock_controller import DoorLockController
from controller.engin_controller import EngineController
from controller.movement_controller import MovementController
from controller.sos_controller import SOSController
from controller.trunk_controller import TrunkController


class CarCommandExecutor:
    def __init__(self, car_controller):
        self.car_controller = car_controller
        self.engin_controller = EngineController(car_controller)
        self.door_lock_controller = DoorLockController(car_controller)
        self.movement_controller = MovementController(car_controller, self.door_lock_controller)
        self.trunk_controller = TrunkController(car_controller)
        self.door_open_controller = OpenDoorController(car_controller)
        self.door_closed_controller = ClosedDoorController(car_controller)
        self.sos_controller = SOSController(
            self.car_controller,
            self.movement_controller,
            self.door_lock_controller,
            self.door_open_controller,
            self.trunk_controller,
            self.engin_controller
        )

    def execute_command(self, command):
        if command == "ENGINE_BTN":
            return self.engin_controller.handle_engine_control()
        elif command == "ACCELERATE":
            return self.movement_controller.handle_acceleration()
        elif command == "BRAKE":
            return self.movement_controller.handle_brake()
        elif command == "LOCK":
            return self.door_lock_controller.all_door_lock()
        elif command == "UNLOCK":
            return self.door_lock_controller.all_door_unlock()
        elif command == "LEFT_DOOR_LOCK":
            return self.door_lock_controller.left_door_lock()
        elif command == "LEFT_DOOR_UNLOCK":
            return self.door_lock_controller.left_door_unlock()
        elif command == "RIGHT_DOOR_LOCK":
            return self.door_lock_controller.right_door_lock()
        elif command == "RIGHT_DOOR_UNLOCK":
            return self.door_lock_controller.right_door_unlock()
        elif command == "LEFT_DOOR_OPEN":
            return self.door_open_controller.handle_left_door_open_controller()
        elif command == "LEFT_DOOR_CLOSE":
            return self.door_closed_controller.handle_left_door_closed_controller()
        elif command == "RIGHT_DOOR_OPEN":
            return self.door_open_controller.handle_right_door_open_controller()
        elif command == "RIGHT_DOOR_CLOSE":
            return self.door_closed_controller.handle_right_door_closed_controller()
        elif command == "TRUNK_OPEN":
            return self.trunk_controller.handle_trunk_open_controller()
        elif command == "TRUNK_CLOSE":
            return self.trunk_controller.handle_trunk_closed_controller()
        elif command == "SOS":
            return self.sos_controller.activate_sos()
        else:
            print("잘못된 입력입니다.")