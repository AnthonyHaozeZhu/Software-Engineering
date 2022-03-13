import numpy as np


class MSA:
    ls = []
    result = 0

    def __init__(self, ls):
        self.ls = np.array(ls)

    def Calc(self):
        while self.ls.shape != (0,):
            max_index = np.argmax(self.ls)
            if self.ls[max_index] < 0:
                break
            else:
                self.result += self.ls[max_index]
                self.ls = np.delete(self.ls, max_index)
        return self.result


a = MSA([-1, -1, 1, 2, 3])
print(a.Calc())
