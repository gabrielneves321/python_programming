from datetime import datetime

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
    house=[]
    house.append(Task('iron the clothes'))
    house.append(Task('wash dishes'))
    house.append(Task('clean the floor'))

    [task.conclude() for task in house if task.description == 'clean the floor']
    for task in house:
        print(f'- {task}')
        
if __name__ == '__main__':
    main()

