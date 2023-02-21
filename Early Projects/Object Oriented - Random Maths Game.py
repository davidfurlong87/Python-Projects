from random import randint, choice

class Matta:
    def __init__(self, x, operator, y):
        self.x = x
        self.y = y
        self.operator = operator
        
    def create_problem(self):
        self.problem = str(self.x) + ' ' + self.operator + ' ' + str(self.y)
        return(self.problem)
    
    def create_solution(self):
        self.solution = eval(str(self.problem))
        return(self.solution)
    

l = ['*', '-', '+', '/']
m = []
n = []
while len(m)<10:
    generator = Matta(randint(1,20), choice(l), randint(1,20))
    m.append(generator.create_problem())
    n.append(generator.create_solution())
for i in range(len(m)):
    print(m[i])
    x = eval(input('Whats the solution? '))
    if x == n[i]:
        print('Correct')
    else:
        print(f'WRON! {n[i]}')
    print()
    
