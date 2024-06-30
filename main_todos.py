import todos
class Todos:
    def add(self,todo):
        lines = todos.get_todos()
        if todo + '\n' not in lines:
            lines.append(todo + '\n')
            todos.write_todos(lines)
            print(f"Added to-do:{todo}")
        else:
            print(f"To-do '{todo}' already exists. ")

    def show(self):
        lines = todos.get_todos()
        for index,item in enumerate(lines):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    def edit(self,index,to_edit):
        lines = todos.get_todos()
        if 0 < index > len(lines):
            lines[index-1] = to_edit + '\n'
            todos.write_todos(lines)
        else:
            print("Invalid index entered")


    def delete(self,index):
        lines = todos.get_todos()
        if 0 < index > len(lines):
            to_remove = lines.pop(index-1)
            todos.write_todos(lines)
        else:
            print("Invalid Index entered")
    def insert(self,index,arg):
        lines = todos.get_todos()
        if arg not in lines:
            if 0<index>len(lines):
                lines.insert(index-1,arg + '\n')
                todos.write_todos(lines)
                print(f"{arg} is inserted at {index} index")
            else:
                print("Index out of range!")
        else:
            print(f"{arg} already exists!")


t1 = Todos()
t1.add("Wake up at 7:00 am")
t1.add("Drink milk")
t1.add("Have BF")
t1.add("Study for 6 hrs")
#t1.edit(1,"Wake up at 7:00 am")
t1.delete(4)
#t1.insert(2,"freshen up")
t1.show()


