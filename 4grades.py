from Students import Student


class Grade8(Student):
    def __init__(self, name, age, fav_subj):
        super().__init__(name, age, fav_subj, 8)

    def says_hello(self):
        print('Привет, старшеклассники!')


class Grade9(Student):
    def __init__(self, name, age, fav_subj):
        super().__init__(name, age, fav_subj, 9)

    def answer(self):
        print('И тебе привет!')


class Grade10(Student):
    def __init__(self, name, age, fav_subj):
        super().__init__(name, age, fav_subj, 10)

    def answer(self):
        print('Привет!')



class Grade11(Student):
    def __init__(self, name, age, fav_subj):
        super().__init__(name, age, fav_subj, 11)
    def answer(self):
        print('Здравствуй!')




grade8 = Grade8('Sofi', 14, 'PE')
grade9 = Grade9('Alek', 15, 'math')
grade10 = Grade10('Daniel', 16, 'germany')
grade11 = Grade11('Frenie', 17, 'english')

grade8.says_hello()
grade9.answer()
grade10.answer()
grade11.answer()
