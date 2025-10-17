import re

class Book:
    def __init__(self, book_id="", title="", author="", publisher="", status="", importer="", quantity=0):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.status = status
        self.importer = importer  
        self.quantity = quantity 

    def input_info(self):
        # BookID: 1 ký tự in hoa + 4 số, duy nhất
        while True:
            bid = input("Nhập mã sách (VD: A0001): ").strip()
            if re.match(r"^[A-Z]\d{4}$", bid):
                self.book_id = bid
                break
            print("Mã sách không hợp lệ.")

        # Title: Ít nhất 2 ký tự, chữ cái đầu viết hoa
        while True:
            title = input("Nhập tên sách: ").strip()
            if len(title) >= 2 and re.match(r"^[A-ZÀ-Ỹ][A-Za-zÀ-ỹ\s]*$", title):
                self.title = title
                break
            print("Tên sách không hợp lệ.")

        # Author: Viết hoa chữ cái đầu, không chứa số/ký tự đặc biệt
        while True:
            author = input("Nhập tác giả: ").strip()
            if author and author[0].isupper() and re.match(r"^[A-ZÀ-Ỹ][A-Za-zÀ-ỹ\s]*$", author):
                self.author = author
                break
            print("Tác giả không hợp lệ.")

        # Publisher: Không để trống
        while True:
            publisher = input("Nhập nhà xuất bản: ").strip()
            if publisher != "":
                self.publisher = publisher
                break
            print("Nhà xuất bản không được để trống.")

        # Status: Chỉ nhận 1 trong các giá trị cho phép
        while True:
            status = input("Nhập tình trạng (Còn/Đã mượn/Hư hỏng/Mất):").strip()
            if status in ["Còn","Đã mượn","Hư hỏng","Mất"]:
                self.status = status
                break
            print("Tình trạng không hợp lệ.")


        # Nhập số lượng
        while True:
            try:
                q = int(input("Nhập số lượng sách: "))
                if q > 0:
                    self.quantity = q
                    break
                print("Số lượng phải > 0.")
            except ValueError:
                print("Số lượng phải là số nguyên!")

    def display_info(self):
        print("\n===== THÔNG TIN SÁCH =====")    
        print(f"Mã sách: {self.book_id}")
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Nhà xuất bản: {self.publisher}")
        print(f"Tình trạng: {self.status}")



