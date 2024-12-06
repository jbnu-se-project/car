class EngineController:
    def __init__(self, car_controller):
        self.car_controller = car_controller
        self.current_frame_commands = []

    def process_command(self, command):
        """단일 커맨드를 현재 프레임에 추가한다."""
        self.current_frame_commands.append(command)

    def process_simultaneous_commands(self, commands):
        """여러 커맨드를 동시에 처리한다."""
        self.current_frame_commands = commands

        result = self.handle_engine_control()

        self.current_frame_commands.clear()
        return result

    def handle_brake_command(self):
        """브레이크 커멘드 처리"""
        self.process_command("BRAKE")
        return False # 브레이크만으로는 시동이 걸리지 않음

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
            self.current_frame_commands.clear()
            return False

        # 엔진이 꺼진 상태에서 시동을 걸 때
        if not current_engine_status:
            if not self._check_valid_start_condition():
                fail(try_case, "브레이크와 엔진 버튼을 동시에 눌러야 시동이 걸립니다.")
                self.current_frame_commands.clear()
                return False

        # 정차 중이거나 엔진이 꺼져 있을 때만 엔진 상태 토글
        self.car_controller.toggle_engine()
        success(try_case)
        return True

    def _check_valid_start_condition(self):
        """
        시동을 걸기 위한 유효한 조건 체크
        마지막 두 명령어가 순서대로 BRAKE, ENGINE_BTN인지 확인
        """
        last_commands = self.current_frame_commands[-2:]
        return last_commands == ["BRAKE", "ENGINE_BTN"]


def success(try_case):
    print("\n[{} - 성공]".format(try_case))

def fail(try_case, fail_reason):
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))