import time as t
import json


class Task:
    def __init__(self, name: str, start: str= None, end: str= None, description: str= None, todo: list[str]= None) -> None:
        self.name= name
        self.desc= description
        self.start= start
        self.end= end
        self.st= "New Task"
        self.todo= todo
        self.aux= todo

        new= t.localtime()
        hour, minutes= new[3], new[4]
        if self.start and self.end:
            hold_srt= self.start.split(':')
            hold_end= self.end.split(':')

            if int(hold_srt[1]) < minutes or self.todo:
                self.st= 'in-progress'
            elif minutes > int(hold_end[1]) or not self.todo:
                self.st= "Task Done"

    def name_change(self, new_name: str) -> None:
        self.name= new_name

    def desc(self, new_description: str) -> None:
        self.desc= new_description
    
    def __str__(self) -> str:
        res= f"Task: {self.name}:\n"
        res+= f"Start at: {self.start}\n"
        res+= f"End at: {self.end}\n\n"
        res+= f"Description:\n{self.desc:^6}\n"
        
        if self.aux:
            res+= f"Todo list:\n"
            if not self.st == "Task Done":
                for i, e in enumerate(self.aux, 1):
                    res+= f"{i}. {e}\n"
            else:
                res+= f"You completed all your todo list"

        return res


class TaskHolder:
    def __init__(self) -> None:
        self.tks= []

    def save_to_json(self, filename: str = "tasks.json") -> None:
        """Converts all tracking tasks into structural JSON data format."""
        exported_data = []
        
        if self.tks:
            for task in self.tks:
                task_dict = {
                    "name": task.name,
                    "description": task.desc,
                    "start": task.start,
                    "end": task.end,
                    "status": task.st,
                    "todo_live": task.todo,
                    "todo_original": task.aux
                }
                exported_data.append(task_dict)
            
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(exported_data, file, indent=4)
            print(f" Data successfully backed up to {filename}!")

    def show_tasks(self) -> str:
        new= t.localtime()
        year, month, day, hours, minutes, secs= new[0], new[1], new[2], new[3], new[4], new[5]
        
        res= 'My Tasks:\n\n'

        if self.tks:
            for i, k in enumerate(self.tks, 1):
                res+= f"{i}. {k.name:22}{k.st}\n"
        else:
            empty= "No Tasks are set."
            res+= f"{empty:^22}\n\n"

        res+= f'{day}/{month}/{year} {hour}:{minutes}:{secs}'

        return res
        
class User:
    def __init__(self, name: str) -> None:
        self.name= name
        self.th= TaskHolder()

    def add_task(self, task: Task) -> None:
        self.th.tks.append(task)
    
    def remove_task(self, task: Task) -> None:
        if self.th.tks:
            self.th.tks.remove(task)

    def access_task(self, s: int) -> str:
        return print(self.th.tks[s-1])

    def Tasks(self) -> str:
        return self.th.show_tasks()
    
    def check_todolist(self, task: Task, num: int) -> None:
        if self.th.tks and self.th.tks[task].todo:
            self.th.tks[task].todo.remove(self.th.tks[task].todo[num-1])




user1 = User("Marwan")


study_list = ["Complete HTML layout module", "Review CSS Grid rules"]
new_task = Task("Study Web Dev", description="freeCodeCamp modules", todo=study_list)

user1.add_task(new_task)

user1.th.save_to_json()