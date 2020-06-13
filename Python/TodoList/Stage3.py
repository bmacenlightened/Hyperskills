from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date, timedelta

Base = declarative_base()
Engine = create_engine('sqlite:///todo.db?check_same_thread=False')

class Task(Base):
    """The database model of a task"""
    # noinspection SpellCheckingInspection
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Unnamed task')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return f'{self.id}. {self.task}'

class ToDo:
    def __init__(self, session):
        self.session = session
        self.menu_choice = ''

    def menu(self):
        """Prints menu items and accepts user choice"""
        print('1) Today\'s tasks')
        print('2) Week\'s tasks')
        print('3) All tasks')
        print('4) Add task')
        print('0) Exit')
        self.menu_choice = input()

    def show_tasks(self):
        """Shows tasks from the database"""
        tasks = self.session.query(Task).all()
        print('Today:')
        if tasks:
            for task in tasks:
                print(f'{task}')
        else:
            print('Nothing to do!')

    def show_today_tasks(self):
        tasks = self.session.query(Task).filter(Task.deadline == datetime.today()).all()
        mon = datetime.today().strftime('%b')
        day = datetime.today().day
        print(f'\nToday {mon} {day}:')
        if tasks:
            for task in tasks:
                print(f'{task}')
        else:
            print('Nothing to do!')

    def show_week_tasks(self):
        day = datetime.today()
        for i in range(7):
            weekdict = {
                0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"
            }
            tasks = self.session.query(Task).filter(Task.deadline == day.date()).all()
            print(f"\n{day.strftime('%A %d %b')}:")
            if tasks:
                for task in tasks:
                    print(f'{task}')
                print()
            else:
                print('Nothing to do!\n')
            day = day + timedelta(days=1)

    def add_task(self):
        """Add a task to the database"""
        print('\nEnter task')
        t = input()
        print("Enter deadline")
        d = input()
        format_ = "%Y-%m-%d"
        deadl = datetime.strptime(d, format_)
        new_task = Task(task=t, deadline=deadl)  # strftime('%m-%d-%Y')
        self.session.add(new_task)
        self.session.commit()
        print('The task has been added!\n')

    def run(self):
        """Main logic of the program"""
        while True:
            self.menu()
            if self.menu_choice == '1':
                self.show_today_tasks()
            elif self.menu_choice == '2':
                self.show_week_tasks()
            elif self.menu_choice == '3':
                self.show_tasks()
            elif self.menu_choice == '4':
                self.add_task()
            else:
                print('\nBye!')
                break

def main():
    Base.metadata.create_all(Engine)
    Session = sessionmaker(bind=Engine)
    session = Session()
    todo = ToDo(session)
    todo.run()

if __name__ == '__main__':
    main()
