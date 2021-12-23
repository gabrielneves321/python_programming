from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def add(self, description, due_date=None):
        self.tasks.append(Task(description, due_date))

    def pending(self, ):
        return [task for task in self.tasks if not task.done]

    def search_for(self, description):
        return [task for task in self.tasks if task.description==description] [0]
    
    def __str__(self):
        return f'{self.name} ({len(self.pending())} task(s) pending(s))'



class Task: 
    def __init__(self, description, due_date=None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.due_date = due_date

    def conclude(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
           status.append('(completed)')
        elif self.due_date:
           if datetime.now() > self.due_date:
               status.append('(expired product)')
           else:
               days = (self.due_date - datetime.now()).days
               status.append(f'( expired in {days} days)')

        return f'{self.description} ' + ' '.join(status)

class Recurring_task(Task):
    def __init__(self, description, due_date, days=7):
        super().__init__(description, due_date)
        self.days = days
    def conclude(self):
        super().conclude()
        new_due_date = datetime.now() + timedelta(days=self.days)
        return Recurring_task(self.description, new_due_date, self.days)

def main():
    house = Project('housework')
    house.add('clean the floor', datetime.now())
    house.add('wash dishes')
    house.tasks.append(Recurring_task('change sheets', datetime.now(), 7))
    house.tasks.append(house.search_for('change sheets').conclude())
    print(house)

    house.search_for('wash dishes').conclude()
    for task in house:
        print(f'-{task}')
    print(house)

    market = Project('market shopping')
    market.add('meet')
    market.add('dry fruits')
    market.add('tomato', datetime.now() + timedelta(days=3, minutes=12))
    print(market)

   
    buy_meet = market.search_for('meet')
    buy_meet.conclude()
    for task in market:
        print(f'- {task}')
    print(market)

        
if __name__ == '__main__':
    main()



