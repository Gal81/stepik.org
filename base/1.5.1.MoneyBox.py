class MoneyBox:
    # конструктор с аргументом – вместимость копилки
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    # True, если можно добавить v монет, False иначе
    def can_add(self, v):
        if self.amount + v <= self.capacity:
            return True

        return False

    # положить v монет в копилку
    def add(self, v):
        if self.can_add(v):
            self.amount += v
            print('Added')
        else:
            print('Full')

mb = MoneyBox(10)
mb.add(8)
mb.add(4)