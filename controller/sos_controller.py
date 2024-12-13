class SOSController:
    def __init__(self, car_controller, movement_controller, doorLock_controller, door_open_controller, trunk_controller, engin_controller):
        self.car_controller = car_controller
        self.movement_controller = movement_controller
        self.doorLock_controller = doorLock_controller
        self.door_open_controller = door_open_controller
        self.trunk_controller = trunk_controller
        self.engin_controller = engin_controller

    def activate_sos(self):
        """
        SOS mode 활성화 하는 메서드
        차량의 속도를 정지 시키고 모든 문 잠금 해제후 열고
        트렁크를 열고 엔진을 종료.
        """
        try_case = "SOS 활성화"
        # 차량 정지
        while self.car_controller.get_speed() > 0:
            self.movement_controller.handle_brake()

        # 모든 문 잠금 해제 및 열기
        self.doorLock_controller.all_door_unlock()
        self.door_open_controller.handle_left_door_open_controller()
        self.door_open_controller.handle_right_door_open_controller()

        # 트렁크 열기
        self.trunk_controller.handle_trunk_open_controller()

        # 엔진 끄기
        if self.car_controller.get_engine_status():
            self.engin_controller.handle_engine_control()

        success(try_case)

def success(try_case):
    "Case가 성공했음을 출력합니다."
    print("\n[{} - 성공]".format(try_case))