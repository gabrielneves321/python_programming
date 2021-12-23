from datetime import datetime
from housework_control_v1 import Task


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self, description):
        self.tasks.append(Task(description))

    def pending(self, ):
        return [task for task in self.tasks if not task.done]

    def search_for(self, description):
        return [task for task in self.tasks if task.description == description] [0]
    
    def __str__(self):
        return f'{self.name} ({len(self.pending())} task(s) pending(s))'



class Task: 
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()

    def conclude(self):
        self.done = True

    def __str__(self):
        return self.description + (' (completed)' if self.done else '')


def main():
    house = Project('housework')
    house.add('clean the floor')
    house.add('wash dishes')
    print(house)

    house.search_for('wash dishes').conclude()
    for task in house.tasks:
        print(f'-{task}')
    print(house)

    market = Project('market shopping')
    market.add('meet')
    market.add('dry fruits')
    market.add('tomato')
    print(market)

    buy_tomato = market.search_for('tomato')
    buy_tomato.conclude()
    buy_meet = market.search_for('meet')
    buy_meet.conclude()
    for task in market.tasks:
        print(f'- {task}')
    print(market)

        
if __name__ == '__main__':
    main()

