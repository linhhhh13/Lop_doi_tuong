from abc import ABC, abstractmethod
import re
from datetime import datetime

class Person(ABC):
    def __init__(self, full_name="", age=0):
        self.full_name = full_name
        self.age = age

    @abstractmethod
    def input_info(self): # Hàm ảo để nhập thông tin người
        pass

    @abstractmethod
    def display_info(self): # Hàm ảo để hiển thị thông tin người
        pass

class Reader(Person):
    def __init__(self, full_name="", age=0, reader_id="", class_name="", register_date="", borrowed_books=0):
        super().__init__(full_name, age)
        self.reader_id = reader_id
        self.class_name = class_name
        self.register_date = register_date
        self.borrowed_books = borrowed_books 

    def input_info(self):
        # FullName: Viết hoa chữ cái đầu mỗi từ, không chứa số/ký tự đặc biệt
        while True:
            name = input("Nhập họ tên: ").strip()
            if re.match(r"^[A-ZÀ-Ỹ][a-zà-ỹ]*(\s[A-ZÀ-Ỹ][a-zà-ỹ]*)*$", name):
                self.full_name = name
                break
            print("Họ tên không hợp lệ.")

        # Age: từ 18 đến 30 tuổi
        while True:
            try:
                age = int(input("Nhập tuổi: "))
                if 18 <= age <= 30:
                    self.age = age
                    break
                else:
                    print("Tuổi sinh viên phải từ 18–30.")
            except ValueError:
                print("Tuổi phải là số nguyên!")

        # ReaderID: R[Khóa/Năm][5 số] (VD: R24_00001)
        while True:
            rid = input("Nhập mã độc giả (VD: R24_00001): ").strip()
            if re.match(r"^R\d{2}_\d{5}$", rid):
                self.reader_id = rid
                break
            print("Mã độc giả không hợp lệ.")

        # Class: Không để trống, đúng định dạng (VD: K60S)
        while True:
            class_name = input("Nhập lớp (VD: K60S): ").strip()
            if class_name and re.match(r"^[A-Z]\d{2,3}[A-Z]\d?$", class_name):
                self.class_name = class_name
                break
            print("Lớp không hợp lệ.")

        # RegisterDate: Đúng định dạng ngày, nhỏ hơn hoặc bằng hiện tại
        while True:
            date = input("Nhập ngày đăng ký (DD/MM/YYYY): ").strip()
            try:
                reg_date = datetime.strptime(date, "%d/%m/%Y")
                if reg_date <= datetime.now():
                    self.register_date = date
                    break
                else:
                    print("Ngày đăng ký không được lớn hơn ngày hiện tại.")
            except:
                print("Ngày đăng ký sai định dạng (DD/MM/YYYY).")

        # Số sách mượn
        while True:
            try:
                num = int(input("Nhập số lượng sách đang mượn: "))
                if num >= 0:
                    self.borrowed_books = num
                    break
                else:
                    print("Số lượng phải >= 0.")
            except ValueError:
                print("Số lượng phải là số nguyên!")

    def display_info(self):
        print("\n===== THÔNG TIN ĐỘC GIẢ =====")
        print(f"{'Mã độc giả':<10} | {'Họ tên':<25} | {'Tuổi':<6} | {'Lớp':<6} | {'Ngày đăng ký':<10} | {'Sách mượn':<5}")
        print(f"{self.reader_id:<10} | {self.full_name:<25} | {self.age:<6} | {self.class_name:<6} | {self.register_date:<10} | {self.borrowed_books:<5}")

class Staff(Person):
    def __init__(self, full_name="", age=0, staff_id="", position="",  start_date=""):
        super().__init__(full_name, age)
        self.staff_id = staff_id
        self.position = position
        self.start_date = start_date

    def input_info(self):
        # Họ tên
        while True:
            name = input("Nhập họ tên nhân viên: ").strip()
            if re.match(r"^[A-ZÀ-ỸĐ][a-zà-ỹđ]+(\s[A-ZÀ-ỸĐ][a-zà-ỹđ]+)*$", name):
                self.full_name = name
                break
            print("Họ tên không hợp lệ!")

        # Tuổi nhân viên: 18–65
        while True:
            try:
                age = int(input("Nhập tuổi: "))
                if 18 <= age <= 65:
                    self.age = age
                    break
                else:
                    print("Tuổi nhân viên phải từ 18–65.")
            except ValueError:
                print("Tuổi phải là số nguyên!")

        # Ngày vào làm
        while True:
            date = input("Nhập ngày vào làm (DD/MM/YYYY): ").strip()
            try:
                start_date = datetime.strptime(date, "%d/%m/%Y")
                if start_date <= datetime.now():
                    self.start_date = date
                    break
                else:
                    print("Ngày vào làm không được lớn hơn hiện tại!")
            except ValueError:
                print("Định dạng ngày không hợp lệ!")

        # Mã nhân viên: NV + YYYYMMDD + _ + STT (3 chữ số)
        while True:
            stt = input("Nhập số thứ tự (VD: 001, 002...): ").strip()
            if re.match(r"^\d{3}$", stt):
                date_str = datetime.strptime(self.start_date, "%d/%m/%Y").strftime("%Y%m%d")
                self.staff_id = f"NV{date_str}_{stt}"
                break
            print("Số thứ tự phải gồm 3 chữ số!")

        # Chức vụ
        while True:
            pos = input("Nhập chức vụ (VD: Thủ thư, Quản lý...): ").strip()
            if len(pos) >= 2:
                self.position = pos
                break
            print("Chức vụ không hợp lệ!")

    def display_info(self):
        print("\n--- THÔNG TIN NHÂN VIÊN ---")
        print(f"{'Mã NV':<15} | {'Họ tên':<25} | {'Tuổi':<6} | {'Chức vụ':<15} | {'Ngày vào làm':<10}")
        print(f"{self.staff_id:<15} | {self.full_name:<25} | {self.age:<6} | {self.position:<12} | {self.start_date:<10}")


# =========================
# CHƯƠNG TRÌNH CHẠY THỬ
# =========================
if __name__ == "__main__":
    print("=== THỬ NGHIỆM LỚP BẠN ĐỌC (READER) ===")
    reader = Reader()
    reader.input_info()
    reader.display_info()

    print("\n=== THỬ NGHIỆM LỚP NHÂN VIÊN (STAFF) ===")
    staff = Staff()
    staff.input_info()
    staff.display_info()


