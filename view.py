def new_student():
    name = input('Введите Имя и Фамилию через пробел: ')
    return name


def new_lesson():
    in_lesson = input('Введите учебный предмет: ')
    return in_lesson


def receiw_st(x):
    print('Выбери ученика:')
    for k in x.keys():
        print(k)
    st = input('Введите Имя и Фамилию через пробел: ')
    return st


def receiw_subj(x):
    print('Выбери предмет:')
    for j in x:
        print(j)
    subj = input('Введите название предмета: ')
    return subj


def estimation():
    estimation = input('Введите оценку: ')
    return estimation


def student_estimate(x, y):
    name = receiw_st(x)
    subj = receiw_subj(y)
    print(x[name][subj])
