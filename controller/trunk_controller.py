class TrunkController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def handle_trunk_open_controller(self):
        """
        트렁크 열기 시도하는 메서드

        차량의 현재 정차하고 있고 트렁크가 닫혀있다면 트렁크를 연다.
        그렇지 않다면 메시지를 출력하고 무시한다.
        차량이 움직이고 있다면 메시지 출력하고 무시한다
        
        return:
        트렁크 열기 성공시 True
        트렁크 열기 실패시 False
        """
        try_case = "트렁크 열기 시도"

        current_speed = self.car_controller.get_speed()

        if current_speed == 0:
            if self.car_controller.get_trunk_status():
                self.car_controller.open_trunk()
                success(try_case)
                return True
            else:
                fail(try_case, "트렁크가 이미 열려 있음")
                return False
        elif current_speed > 0:
            fail(try_case, "차량이 주행 중임으로 트렁크를 열 수 없음")
            return False

    def handle_trunk_closed_controller(self):
        """
        트렁크 닫기 시도하는 메서드

        트렁크가 열려있다면 트렁크를 닫는다.
        그렇지 않다면 메시지 출력하고 무시한다.

        return:
        트렁크 닫기 성공시 True
        트렁크 닫기 실패시 False
        """
        try_case = "트렁크 닫기 시도"

        if not self.car_controller.get_trunk_status():
            self.car_controller.close_trunk()
            success(try_case)
            return True
        else:
            fail(try_case, "트렁크가 이미 닫혀 있음")
            return False


def success(try_case):
    print("\n[{} - 성공]".format(try_case))


def fail(try_case, fail_reason):
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))