class Buffer:
    # конструктор без аргументов
    def __init__(self):
        self.buffer = []

    def get_sum_of5(self):
        self.buffer.reverse()

        i = 0
        sum = 0
        while i < 5:
            i += 1
            sum += self.buffer.pop()

        self.buffer.reverse()
        print(sum)

    # добавить следующую часть последовательности
    def add(self, *a):
        for x in a:
            self.buffer.append(x)

        while len(self.buffer) >= 5:
            self.get_sum_of5()

    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
    def get_current_part(self):
        return self.buffer

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]