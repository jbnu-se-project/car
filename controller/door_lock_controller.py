class DoorLockController:
    def __init__(self, car_controller):
        self.car_controller = car_controller

    def door_open_status(self, try_case):
        if self.car_controller.get_left_door_status() == "OPEN" and self.car_controller.get_right_door_status() == "OPEN":
            fail(try_case, "모든 문이 열려있습니다")
            return False
        elif self.car_controller.get_left_door_status() == "OPEN":
            fail(try_case, "왼쪽 문이 열려있습니다")
            return False
        elif self.car_controller.get_right_door_status() == "OPEN":
            fail(try_case, "오른쪽 문이 열려있습니다")
            return False

    def are_all_doors_closed(self):
        return self.car_controller.get_left_door_status() == "CLOSED" and self.car_controller.get_right_door_status() == "CLOSED"

    def vehicle_status_checking(self):
        if self.car_controller.get_left_door_lock() == "LOCKED" and self.car_controller.get_right_door_lock() == "LOCKED":
            self.car_controller.lock_vehicle()
        else:
            self.car_controller.unlock_vehicle()

    def handle_all_door_lock(self):
        """
        모든 차량 문을 잠금 시도하는 메서드
        모든 문의 현재 상태를 확인하여 아직 잠겨 있지 않은 경우에는 잠근다.
        작업 결과에 따라 상태 메시지를 출력합니다.
        
        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "모든 문 잠금 시도"

        if self.are_all_doors_closed():
            if self.car_controller.get_left_door_lock() == "LOCKED" and self.car_controller.get_right_door_lock() == "LOCKED":
                fail(try_case, "이미 모든 문이 잠긴 상태입니다.")
                return False
            else:
                self.car_controller.lock_left_door()
                self.car_controller.lock_right_door()
                self.car_controller.lock_vehicle()
                success(try_case)
        else:
            self.door_open_status(try_case)
            return False
        
        self.vehicle_status_checking()
        return True

    def handle_all_door_unlock(self):
        """
        모든 차량 문을 잠금 해제 시도하는 메서드

        차량이 움직이고 있다면 적절한 메시지와 함께 문을 잠금 해제 신호를 무시합니다.
        모든 문이 모두 이미 잠금 해제된 경우 잠금 해제 작업을 수행하지 않고
        그렇지 않으면 왼쪽과 오른쪽 문이 모두 잠금 해제됩니다.

        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "모든 문 잠금 해제 시도"

        if self.car_controller.get_speed() != 0:
            fail(try_case, "차량이 주행 중입니다.")
            return False
        elif self.are_all_doors_closed():
            if self.car_controller.get_left_door_lock() == "UNLOCKED" and self.car_controller.get_right_door_lock() == "UNLOCKED":
                fail(try_case, "이미 모든 문이 잠금 해제된 상태입니다.")
                return False
            else:
                success(try_case)
                self.car_controller.unlock_left_door()
                self.car_controller.unlock_right_door()
        else:
            self.door_open_status(try_case)
            return False
        
        self.vehicle_status_checking()
        return True

    def handle_left_door_lock(self):
        """
        왼쪽 문을 잠금 시도하는 메서드

        문이 닫혀있고 문이 잠겨있지 않은 상태라면 왼쪽 문을 잠금.
        그렇지 않다면 메시지를 출력하고 무시한다.

        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "왼쪽 문 잠금 시도"

        if self.are_all_doors_closed():
            if self.car_controller.get_left_door_lock() == "LOCKED":
                fail(try_case, "이미 왼쪽 문이 잠긴 상태입니다.")
                return False
            else:
                success(try_case)
                self.car_controller.lock_left_door()
        else:
            self.door_open_status(try_case)
            return False
        
        self.vehicle_status_checking()
        return True

    def handle_left_door_unlock(self):
        """
        왼쪽 문을 잠금 해제 시도하는 메서드

        문이 닫혀있고 문이 잠겨있지 않은 상태라면 왼쪽 문을 잠금.
        그렇지 않다면 메시지를 출력하고 무시한다.

        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "왼쪽 문 잠금 해제 시도"

        if self.car_controller.get_speed() != 0:
            fail(try_case, "차량이 주행 중입니다.")
            return False
        elif self.are_all_doors_closed():
            if self.car_controller.get_left_door_lock() == "UNLOCKED":
                fail(try_case, "이미 왼쪽 문이 잠금 해제된 상태입니다.")
                return False
            else:
                success(try_case)
                self.car_controller.unlock_left_door()
        else:
            self.door_open_status(try_case) 
            return False
          
        self.vehicle_status_checking()
        return True


    def handle_right_door_lock(self):
        """
        오른쪽 문을 잠금 시도하는 메서드

        문이 닫혀있고 문이 잠겨있지 않은 상태라면 오른쪽 문을 잠금.
        그렇지 않다면 메시지를 출력하고 무시한다.

        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "오른쪽 문 잠금 시도"
        
        if self.are_all_doors_closed():
            if self.car_controller.get_right_door_lock() == "LOCKED":
                fail(try_case, "이미 오른쪽 문이 잠긴 상태입니다.")
                return False
            else:
                success(try_case)
                self.car_controller.lock_right_door()
        else:
            self.door_open_status(try_case)
            return False
        
        self.vehicle_status_checking()
        return True

    def handle_right_door_unlock(self):
        """
        오른쪽 문을 잠금 해제 시도하는 메서드

        문이 닫혀있고 문이 잠겨있지 않은 상태라면 오른쪽 문을 잠금.
        그렇지 않다면 메시지를 출력하고 무시한다.

        return :
        - 잠금 성공 시 True
        - 잠금 실패 시 False
        """
        try_case = "오른쪽 문 잠금 해제 시도"

        if self.car_controller.get_speed() != 0:
            fail(try_case, "차량이 주행 중입니다.")
            return False
        elif self.are_all_doors_closed():
            if self.car_controller.get_right_door_lock() == "UNLOCKED":
                fail(try_case, "이미 오른쪽 문이 잠금 해제된 상태입니다.")
                return False
            else:
                success(try_case)
                self.car_controller.unlock_right_door()
        else:
            self.door_open_status(try_case)
            return False
        
        self.vehicle_status_checking()
        return True


def success(try_case):
    "Case가 성공했음을 출력합니다."
    print("\n[{} - 성공]".format(try_case))

def fail(try_case, fail_reason):
    "Case가 실패했음을 출력합니다."
    print("\n[{} - 실패] : {}".format(try_case, fail_reason))