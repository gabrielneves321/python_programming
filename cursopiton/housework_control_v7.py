from datetime import datetime, timedelta
from housework_control_v5 import Task

class Task_not_found(Exception):
    pass

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def __iadd__(self, task):
        task.owner = self
        self._add_task(task)
        return self 

    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, description, **kwargs):
        self.tasks.append(Task(description, kwargs.get('due_date', None)))

    def add(self, task, due_date=None, **kwargs):
        chosen_function = self._add_task if isinstance(task, Task) \
            else self._add_new_task  
        kwargs['expired'] = due_date
        chosen_function(task, **kwargs)

    def pending(self, ):
        return [task for task in self.tasks if not task.done]

    def search_for(self, description):
        try:
            return [task for task in self.tasks if task.description == description] [0]
        except IndexError as e:
            raise Task_not_found(str(e))
    
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
               status.append('(expired)')
           else:
               days = (self.due_date - datetime.now()).days
               status.append(f'(expired in {days} days)')

        return f'{self.description} ' + ' '.join(status)

class Recurring_task(Task):
    def __init__(self, description, due_date, days=7):
        super().__init__(description, due_date)
        self.days = days
        self.owner = None

    def conclude(self):
        super().conclude()
        new_due_date = datetime.now() + timedelta(days=self.days)
        new_task = Recurring_task(self.description, new_due_date, self.days)
        if self.owner:
            self.owner += new_task
        return new_task 

def main():
    house = Project('houseworks')
    house.add('cleam the floor', datetime.now())
    house.add('wash dishes')
    house += Recurring_task('change sheets', datetime.now(), 7)
    house.search_for('change sheets').conclude()
    print(house)

    try:
        house.search_for('wash dishes   - ERROR').conclude()
    except Task_not_found as e:
        print(f'the cause was "{str(e)}"!')

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



