# bài tập 12
def getMark(diemchuyencan, diemgiuaky, diemcuoiky):
    checkValidMark = diemchuyencan < 0 or diemchuyencan > 10 or diemgiuaky < 0 or diemgiuaky > 10 or diemcuoiky < 0 or diemcuoiky > 10

    if checkValidMark:
        print("invalid input")
        return
    return 0.2 * diemchuyencan + 0.2 * diemgiuaky + 0.6 * diemcuoiky


def getRank(mark):
    if mark < 4:
        return 'F'
    elif mark >= 0 and mark < 5:
        return 'D'
    elif mark >= 5 and mark < 6:
        return 'D+'
    elif mark >= 6 and mark < 6.5:
        return 'C'
    elif mark >= 6.5 and mark < 7:
        return 'C+'
    elif mark >= 7 and mark < 8:
        return 'B'
    elif mark >= 8 and mark < 8.5:
        return 'B+'
    elif mark >= 8.5 and mark < 9.0:
        return 'A'
    else:
        return 'A+'
