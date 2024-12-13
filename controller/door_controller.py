class OpenDoorController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def handle_right_door_open_controller(self):
        """
        오른쪽 문 열기 시도 하는 메서드

        오른쪽 문이 닫혀있고 문이 잠겨있지 않다면 문을 열고
        그렇지 않다면 메시지 출력후 무시한다.
        만약 이미 문이 열려있다면 메시지 출력후 무시한다.
        """
        try_case = "오른쪽 문 열기 시도"

        current_right_door_status = self.car_controller.get_right_door_status()
        current_right_door_lock = self.car_controller.get_right_door_lock()

        if current_right_door_status == "CLOSED":
            if current_right_door_lock == "LOCKED":
                fail(try_case, "오른쪽 문이 잠겨 있어 문 닫힘 상태 유지")
                return False
            elif current_right_door_lock == "UNLOCKED":
                self.car_controller.open_right_door()
                success(try_case)
                return True
        elif current_right_door_status == "OPEN":
            fail(try_case, "오른쪽 문이 이미 열려 있음")
            return False

    def handle_left_door_open_controller(self):
        """
        왼쪽 문 열기 시도 하는 메서드

        왼쪽 문이 닫혀있고 문이 잠겨있지 않다면 문을 열고
        그렇지 않다면 메시지 출력후 무시한다.
        만약 이미 문이 열려있다면 메시지 출력후 무시한다.
        """
        try_case = "왼쪽 문 열기 시도"

        current_left_door_status = self.car_controller.get_left_door_status()
        current_left_door_lock = self.car_controller.get_left_door_lock()

        if current_left_door_status == "CLOSED":
            if current_left_door_lock == "LOCKED":
                fail(try_case, "왼쪽 문이 잠겨 있어 문 닫힘 상태 유지")
                return False
            elif current_left_door_lock == "UNLOCKED":
                self.car_controller.open_left_door()
                success(try_case)
                return True
        elif current_left_door_status == "OPEN":
            fail(try_case, "왼쪽 문이 이미 열려 있음")
            return False


class ClosedDoorController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def handle_right_door_closed_controller(self):
        """
        오른쪽 문 닫기 시도 하는 메서드

        오른쪽 문이 열려있다면 문을 닫고
        그렇지 않다면 메시지 출력후 무시한다.
        만약 이미 문이 닫혀 있다면 메시지 출력후 무시한다.
        """
        try_case = "오른쪽 문 닫기 시도"

        current_right_door_status = self.car_controller.get_right_door_status()

        if current_right_door_status == "OPEN":
            self.car_controller.close_right_door()
            success(try_case)
            return True
        elif current_right_door_status == "CLOSED":
            fail(try_case, "오른쪽 문이 이미 닫혀 있음")
            return False

    def handle_left_door_closed_controller(self):
        """
        왼쪽 문 닫기 시도 하는 메서드

        왼쪽 문이 열려있다면 문을 닫고
        그렇지 않다면 메시지 출력후 무시한다.
        만약 이미 문이 닫혀 있다면 메시지 출력후 무시한다.
        """
        try_case = "왼쪽 문 닫기 시도"

        current_left_door_status = self.car_controller.get_left_door_status()

        if current_left_door_status == "OPEN":
            self.car_controller.close_left_door()
            success(try_case)
            return True
        elif current_left_door_status == "CLOSED":
            fail(try_case, "왼쪽 문이 이미 닫혀 있음")
            return False

def success(try_case):
    print("\n[{} - 성공]".format(try_case))


def fail(try_case, fail_reason):
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))