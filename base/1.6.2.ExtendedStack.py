class ExtendedStack(list):
    def sum(self):
        num1 = self.pop()
        num2 = self.pop()
        self.append(num1 + num2)

    def sub(self):
        num1 = self.pop()
        num2 = self.pop()
        self.append(num1 - num2)

    def mul(self):
        num1 = self.pop()
        num2 = self.pop()
        self.append(num1 * num2)

    def div(self):
        num1 = self.pop()
        num2 = self.pop()
        self.append(num1 // num2)

stack = ExtendedStack()
stack.append(2)
stack.append(3)
stack.sum()

print(stack)
