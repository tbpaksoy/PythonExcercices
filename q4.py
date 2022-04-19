class BackToBackNums():
    n : int
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self.n
    def __next__(self):
        self.n += 1
        return self.n + (self.n-1)
a = BackToBackNums(6)
print(next(a))#7+6
print(next(a))#8+7
print(next(a))#9+8
print(next(a))#10+9
print(next(a))#11+10
b = BackToBackNums(5)