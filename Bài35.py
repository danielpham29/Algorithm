# https://drive.google.com/file/d/10eSYB9dvpj_GvrVqU3IuPHaO4I9cmyJb/view?usp=sharing
# Bài 35 - Dinh Quy Pham
import math
n = int(input("Nhập N : "))
# Sử dụng biến giatri để sau trừ ra mà không làm thay đổi giá trị của n
giatri = n
su = list()

canbac = 0
tongcan = 0
tong = 0
# Cho vòng for a lặp 1 lần vì chỉ cần thêm 1 giá trị canbac vào list su
for a in range(1):
    canbac = math.sqrt(giatri)
    # Thêm giá trị vào list su
    su.append(canbac)
    # Cho vòng for x để thêm tong vào list su
    # Lý do đặt range(n-1) vì chỉ cần lặp n-1 lần là đủ
    for x in range(n-1):
        giatri -= 1
        tongcan = giatri + su[x]
        tong = math.sqrt(tongcan)
        su.append(tong)
# Lúc này, giá trị cuối cùng của list su là đáp án của bài toán
print(su[n-1])






