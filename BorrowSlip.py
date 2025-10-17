import re
from datetime import datetime

class BorrowSlip:
    def __init__(self, borrow_id="", book_id="", reader_id="", borrow_date="", return_date=""):
        self.borrow_id = borrow_id
        self.book_id = book_id
        self.reader_id = reader_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def input_info(self):
        # BorrowID: P[YYYYMMDD]_[4 số]
        while True:
            bid = input("Nhập mã phiếu mượn (VD: P20251009_0001): ").strip()
            if re.match(r"^P\d{8}_\d{4}$", bid):
                self.borrow_id = bid
                break
            print("Mã phiếu mượn không hợp lệ.")

        # BookID: 1 chữ in hoa + 4 số
        while True:
            bookid = input("Nhập mã sách mượn (VD: A0001): ").strip()
            if re.match(r"^[A-Z]\d{4}$", bookid):
                self.book_id = bookid
                break
            print("Mã sách không hợp lệ.")

        # ReaderID: R[Khóa/Năm]_[5 số]
        while True:
            rid = input("Nhập mã độc giả (VD: R24_00001): ").strip()
            if re.match(r"^R\d{2}_\d{5}$", rid):
                self.reader_id = rid
                break
            print("Mã độc giả không hợp lệ")

        # BorrowDate: Đúng định dạng ngày, nhỏ hơn hoặc bằng hôm nay
        while True:
            date = input("Nhập ngày mượn (DD/MM/YYYY): ").strip()
            try:
                borrow_date = datetime.strptime(date, "%d/%m/%Y")
                if borrow_date <= datetime.now():
                    self.borrow_date = date
                    break
                else:
                    print("Ngày mượn không được lớn hơn ngày hiện tại.")
            except:
                print("Ngày mượn sai định dạng (DD/MM/YYYY).")

        # ReturnDate: Có thể để trống, nếu nhập thì phải lớn hơn ngày mượn
        while True:
            rdate = input("Nhập ngày trả (DD/MM/YYYY, có thể bỏ trống): ").strip()
            if rdate == "":
                self.return_date = ""
                break
            try:
                return_date = datetime.strptime(rdate, "%d/%m/%Y")
                borrow_date = datetime.strptime(self.borrow_date, "%d/%m/%Y")
                if return_date > borrow_date:
                    self.return_date = rdate
                    break
                else:
                    print("Ngày trả phải lớn hơn ngày mượn.")
            except:
                print("Ngày trả sai định dạng (DD/MM/YYYY), hoặc lớn hơn ngày mượn.")

    def display_info(self):
        print("\n===== THÔNG TIN PHIẾU MƯỢN =====")
        print(f"{'Mã phiếu':<15} | {'Mã sách':<8} | {'Mã độc giả':<10} | {'Ngày mượn':<10} | {'Ngày trả':<10}")
        print(f"{self.borrow_id:<15} | {self.book_id:<8} | {self.reader_id:<10} | {self.borrow_date:<10} | {self.return_date if self.return_date else 'Chưa trả':<10}")

