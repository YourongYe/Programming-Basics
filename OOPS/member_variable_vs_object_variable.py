class figure:
    name = ''
    gender = ''
    age = 0
    fightAbility = 0
    status = 'youngster'

    def __init__(self,name,gender,age,fightAbility):
        self.name = name
        self.gender = gender
        self.age = age
        self.fightAbility = fightAbility

figure1 = figure('yoyo','f',18,1000)
figure2 = figure('mumu','m',20,1800)
figure3 = figure('duoduo','f',19,2500)

figure1.title = 'winner'
figure2.status = 'elderly'
print(figure1.status)
print(figure1.__dict__)#print属于只figure1（object）的变量
print(figure2.__dict__)#print属于只figure2（object）的变量
print(figure.__dict__)#print属于只figure（class）的变量

# 类的变量和实例的变量是分开的，实例属于某一类之后仍然可以创建只属于这个实例的变量，则该实例会同时拥有自己的变量和属于的类的变量
