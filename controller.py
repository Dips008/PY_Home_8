import view
main = {}
subject = []


def start():
    i = 1
    while i:
        print('Сделайте выбор:')
        print('1 - Добавить нового студента')
        print('2 - Добавить предмет')
        print('3 - Добавление оценки ученику по предмету')
        print('4 - Показать список учеников')
        print('5 - Показать лист оценок конкретного ученика')
        print('0 - выход из справочника')
        k = int(input('Введите: '))
        if k == 1:
            name = view.new_student()
            main[name] = {}
            for i in subject:
                main[name][i] = []
            print(main)
        elif k == 2:
            les = view.new_lesson()
            subject.append(les)
            for key, value in main.items():
                value[les] = []
            print(main)
        elif k == 3:
            st = view.receiw_st(main)
            subj = view.receiw_subj(subject)
            est = view.estimation()
            main[st][subj].append(est)
            print(main)
        elif k == 4:
            for k in main.keys():
                print(k)
        elif k == 5:
            view.student_estimate(main, subject)
        i = k
