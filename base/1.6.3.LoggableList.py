import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, data):
        self.log(data)
        return super().append(data)

testList = LoggableList()
testList.append('zzz')