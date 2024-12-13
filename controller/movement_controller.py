class MovementController:
    def __init__(self, car_controller, doorLock_controller):
        self.car_controller = car_controller
        self.doorLock_controller = doorLock_controller
        self.min_speed = 0
        self.max_speed = 200
        self.auto_lock_speed = 15

    def auto_lock_by_speed(self):
        """속도 감응식 자동 문 잠금 처리"""
        try_case = "속도 감응식 자동 잠금"

        if not self.car_controller.get_lock_status():
            if self.doorLock_controller.all_door_lock():
                success(try_case)
            else:
                fail(try_case, "문이 열려있습니다")

    def handle_acceleration(self) -> bool:
        """
        가속 처리

        현재 자동차의 속도를 확인하고, 속도가 최고 속도 이하일 경우 가속한다.
        가속 중 속도가 자동 잠금 속도에 도달하거나 초과하면 속도에 따라 자동 잠금 메커니즘이 작동됩니다.

        :return: 차량이 가속할 수 있다면 True , 아니라면 False .
        """
        try_case = "가속"
        
        if not self.car_controller.get_engine_status():
            fail(try_case, "엔진이 꺼져 있는 상태로 가속할 수 없습니다.")
            return False
        
        if self.car_controller.get_speed() >= self.max_speed:
            fail("가속", "속도가 최대값에 도달하여 가속할 수 없습니다.")
            return False
        
        self.car_controller.accelerate()

        if self.car_controller.get_speed() >= self.auto_lock_speed:
            self.auto_lock_by_speed()

        return True

    def handle_brake(self) -> bool:
        """
        브레이크 처리
        자동차의 현재 속도가 최소 속도 보다 높으면 브레이크를 활성화하고
        자동차가 이미 정지한 경우 IGNORE 메시지를 출력하고 무시한다.

        :return: 차량이 브레이크할 수 있다면 True, 아니라면 False
        """
        try_case = "브레이크"

        if self.car_controller.get_speed() > self.min_speed:
            self.car_controller.brake()
            return True
            
        fail(try_case, "차량이 정차 중임")
        return False

def success(try_case):
    print("\n[{} - 성공]".format(try_case))


def fail(try_case, fail_reason):
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))