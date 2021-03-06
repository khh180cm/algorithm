"""
출석하지 않은 학생 찾기
"""

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# 방법 1
def get_absent_student_1(all_students, present_students):
    student_presented = {}
    # 전체 수강생
    for student in all_students:
        student_presented[student] = False

    # 참석한 수강생
    for student in present_students:
        student_presented[student] = True

    # 미참석 수강생 구하기
    for key, value in student_presented.items():
        if value is False:
            return key
    return "All student participated!"


print(get_absent_student_1(all_students, present_students))


all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["채영", "쯔위", "사나", "나연", "미나", "다현"]


# 방법 2
def get_absent_student_2(all_students, present_students):
    student_presented = {}
    # 전체 수강생
    for student in all_students:
        student_presented[student] = None

    # 미참석 수강생 구하기
    for student in present_students:
        del student_presented[student]
    absented = []
    for key in student_presented.keys():
        absented.append(key)
    return absented


print(get_absent_student_2(all_students, present_students))
