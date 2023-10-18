class Student:
    """
    Класс для представления студента в БД
    """

    def __init__(self, name, age, fav_subj, grade):
        self.name = name
        self.age = age
        self.fav_subj = fav_subj
        self.grade = grade
        self.is_dumb_boy = False
        self.cringe_boy = False
        self.friendship = False
        self.enemies = False
        """
        Инициализация
        """


    def says_hello(self):   #Начало конфликта
        print('Ты странный')

    def hit(self, other):

        if self.is_dumb_boy:
            print(f'{self.name}, ты кринж')
            self.enemies = True

        if other.cringe_boy:
            print(f'{other.name}, это шутка, бро')
            other.friendship = True

        self.is_dumb_boy = True
        other.cringe_boy = True

print(f'{__name__=}')

student1 = Student('Ушак', 19, 'IT', 13)
student2 = Student('Женя', 19, 'math', 13)

student1.says_hello()
student2.hit(student1)
student2.hit(student1)

