from controller.door_controller import OpenDoorController, ClosedDoorController
from controller.door_lock_controller import DoorLockController
from controller.engin_controller import EngineController
from controller.movement_controller import MovementController
from controller.sos_controller import SOSController
from controller.trunk_controller import TrunkController


class CarCommandExecutor:
    def __init__(self, car_controller):
        self.car_controller = car_controller
        self._initialize_controllers()
        self.current_frame_commands = []

    def _initialize_controllers(self):
        self.engin_controller = EngineController(self.car_controller)
        self.door_lock_controller = DoorLockController(self.car_controller)
        self.movement_controller = MovementController(self.car_controller, self.door_lock_controller)
        self.trunk_controller = TrunkController(self.car_controller)
        self.door_open_controller = OpenDoorController(self.car_controller)
        self.door_closed_controller = ClosedDoorController(self.car_controller)
        self.sos_controller = SOSController(
            self.car_controller,
            self.movement_controller,
            self.door_lock_controller,
            self.door_open_controller,
            self.trunk_controller,
            self.engin_controller
        )

    def execute_command(self, command):
        """
        공백으로 구분된 명령어들 처리
        """
        commands = command.split()
        
        self.current_frame_commands.clear()
        self.current_frame_commands.extend(commands)

        if self._is_engine_control_commands():
            return self._handle_engine_control()
        return self._handle_single_command(command)

    def _is_engine_control_commands(self):
        """현재 프레임의 명령어들이 엔진 제어와 관련되었는지 판단"""
        command_set = set(self.current_frame_commands)
        return command_set >= {"BRAKE", "ENGINE_BTN"}

    def _handle_engine_control(self):
        """엔진제어 관련 명령어 처리"""
        result = self.engin_controller.process_simultaneous_commands(self.current_frame_commands)
        self.current_frame_commands.clear()
        return result

    def _handle_single_command(self, command):
        """단일 명령어 처리"""
        result = False

        if command == "ENGINE_BTN":
            result =  self.engin_controller.handle_engine_control()
        elif command == "ACCELERATE":
            result = self.movement_controller.handle_acceleration()
        elif command == "BRAKE":
            result = self.movement_controller.handle_brake()
        elif command == "LOCK":
            result =  self.door_lock_controller.handle_all_door_lock()
        elif command == "UNLOCK":
            result =  self.door_lock_controller.handle_all_door_unlock()
        elif command == "LEFT_DOOR_LOCK":
            result =  self.door_lock_controller.handle_left_door_lock()
        elif command == "LEFT_DOOR_UNLOCK":
            result =  self.door_lock_controller.handle_left_door_unlock()
        elif command == "RIGHT_DOOR_LOCK":
            result =  self.door_lock_controller.handle_right_door_lock()
        elif command == "RIGHT_DOOR_UNLOCK":
            result =  self.door_lock_controller.handle_right_door_unlock()
        elif command == "LEFT_DOOR_OPEN":
            result =  self.door_open_controller.handle_left_door_open_controller()
        elif command == "LEFT_DOOR_CLOSE":
            result =  self.door_closed_controller.handle_left_door_closed_controller()
        elif command == "RIGHT_DOOR_OPEN":
            result =  self.door_open_controller.handle_right_door_open_controller()
        elif command == "RIGHT_DOOR_CLOSE":
            result =  self.door_closed_controller.handle_right_door_closed_controller()
        elif command == "TRUNK_OPEN":
            result =  self.trunk_controller.handle_trunk_open_controller()
        elif command == "TRUNK_CLOSE":
            result =  self.trunk_controller.handle_trunk_closed_controller()
        elif command == "SOS":
            result =  self.sos_controller.activate_sos()
        else:
            print("잘못된 입력입니다.")

        self.current_frame_commands.clear()
        return result