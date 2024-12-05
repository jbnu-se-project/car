class EngineController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def handle_brake_command(self):
        """브레이크 커멘드 처리"""
        pass

    def handle_simultaneous_commands(self, commands):
        """동시 입력된 커맨드들 처리"""
        pass

    def handle_engine_control(self) -> bool:
        """
        자동차의 엔진 상태를 전환하는 메서드
        자동차가 움직이고 엔진이 켜져 있으면 엔진 상태를 전환하는 명령이 무시됩니다.
        자동차가 정지해 있거나 엔진이 꺼져 있으면 엔진 상태가 전환됩니다.

        :return: 엔진 제어 명령이 실행 된다면 True, 아니라면 False.
        """
        try_case = "엔진 제어 시도"
        current_speed = self.car_controller.get_speed()
        current_engine_status = self.car_controller.get_engine_status()
        # 주행 중이고 엔진이 켜져 있을 때 엔진 끄기 명령을 무시
        if current_speed > 0 and current_engine_status:
            fail(try_case, "주행 중이고 엔진이 켜져 있습니다.")
            return False
        # 정차 중이거나 엔진이 꺼져 있을 때만 엔진 상태 토글
        self.car_controller.toggle_engine()
        success(try_case)
        return True




def success(try_case):
    print("\n[{} - 성공]".format(try_case))

def fail(try_case, fail_reason):
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))