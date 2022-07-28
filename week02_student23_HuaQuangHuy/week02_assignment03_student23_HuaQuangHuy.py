#  Câu 3: Viết một hàm nhận vào tên học viên (kiểu string), số thứ tự tuần học (kiểu nguyên), số thứ tự bài tập (kiểu nguyên) và trả về tên file .py tương ứng.

# hàm thực hiện trả về tên file
def getFileName(nameStudent, week, assingment):
    if type(nameStudent) is str and type(week) is int and type(assingment) is int:
        nameStudent = nameStudent.replace(" ", "")
        return 'week' + f"{week:02d}" + '_assingment' + f"{assingment:02d}" + '_' + nameStudent + '.py'
    else:
        print('Chưa nhập đúng kiểu dữ liệu')

    # format string : print(f"{1:02}")


# main
if __name__ == '__main__':
    # week03_assingment04_HuaQuangHuy.py
    print(getFileName(' Hua Quang Huy ', 3, 4))
    # week10_assingment11_HuaQuangHuy.py
    print(getFileName(' Hua Quang Huy ', 10, 11))
    # Chưa nhập đúng kiểu dữ liệu
    print(getFileName(' Hua Quang Huy ', 3.5, 4))
