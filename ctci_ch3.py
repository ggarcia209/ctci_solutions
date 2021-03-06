""" Answers clipped from scratch_stacks.py """

# 3.1 - Use single array to implement 3 stacks - see Stack from scratch_stacks

def split_array(self, array):
    stack_1 = Stack()
    stack_2 = Stack()
    stack_3 = Stack()
    count = 1
    for element in array:
        if count == 4:
            count = 1
        if count == 1:
            stack_1.push(element)
        elif count == 2:
            stack_2.push(element)
        else:
            stack_3.push(element)
        count += 1
    print("Stack 1: {}".format(stack_1.items))
    print("Stack 2: {}".format(stack_2.items))
    print("Stack 3: {}".format(stack_3.items))

# 3.2 - Design stack with function to find min element in O(1) time

class Stack:
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        self.items.append(item)
        self.update_min_push(item)

    def pop(self):
        self.update_min_pop()
        return self.items.pop()

    def update_min_push(self, item):
        if not self.min:
            self.min = item
        if self.min and item < self.min:
            self.min = item

    def update_min_pop(self):
        if self.items[-1] == self.min:
            list_copy = copy(self.items)
            list_copy.pop()
            self.min = min(list_copy)

    def find_min(self):
        return self.min

# 3.3 - Create Set Of Stacks that behaves like Stack (pop/push/min) Follow Up: pop at sub stack

class SetOfStacks(Stack):
    def __init__(self, limit=None):
        self.limit = limit
        self.stacks = []
        self.current_stack = Stack()

    def new_stack(self):
        new_stack = Stack()
        self.current_stack = new_stack
        self.stacks.append(self.current_stack)

    def push(self, item):
        if len(self.current_stack.items) == 0:
            self.new_stack()
        elif len(self.current_stack.items) == self.limit:
            self.new_stack()
        self.current_stack.push(item)

    def pop(self):
        self.current_stack.pop()
        if len(self.current_stack.items) == 0:
            self.stacks.pop()
            self.current_stack = self.stacks[-1]

    def pop_at(self, index):
        try:
            selected_stack = self.stacks[index]
            selected_stack.pop()
        except IndexError:
            print("Stack does not exist")

    def view_stacks(self):
        print([stack.items for stack in self.stacks])

    def min_of_set(self):
        return min([stack.min for stack in self.stacks])

# 3.4 - Implement a queue using 2 stacks

class MyQueue():  # coupled with Stack() class
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def add_to_queue(self, data):
        if len(self.stack_1.items) == 0:
            self.stack_1.push(data)
        else:
            while len(self.stack_1.items) > 0:
                self.stack_2.push(self.stack_1.pop())
            self.stack_1.push(data)
            while len(self.stack_2.items) > 0:
                self.stack_1.push(self.stack_2.pop())

    def pop_from_queue(self):
        return self.stack_1.pop()

# 3.6 - Animal Shelter Queues

class Animal:
    def __init__(self, name="Name", kind="Unspecified"):
        self.name = name
        self.kind = kind
        self.availability = True

    def __str__(self):
        return str((self.name, self.kind))

    def __repr__(self):
        return str((self.name, self.kind))


class AnimalShelter:
    def __init__(self):
        self.cats = MyQueue()
        self.dogs = MyQueue()
        self.all_animals = MyQueue()

    def enqueue_dogs(self, name="Dog"):
        new_dog = Animal(name, "dog")
        self.dogs.add_to_queue(new_dog)
        self.all_animals.add_to_queue(new_dog)

    def enqueue_cats(self, name="Cat"):
        new_cat = Animal(name, "cat")
        self.cats.add_to_queue(new_cat)
        self.all_animals.add_to_queue(new_cat)

    def dequeue_dogs(self):
        select_dog = self.dogs.pop_from_queue()
        if select_dog.availability is False:
            self.dequeue_dogs()
        else:
            select_dog.availability = False
        return select_dog

    def dequeue_cats(self):
        select_cat = self.cats.pop_from_queue()
        if select_cat.availability is False:
            self.dequeue_cats()
        else:
            select_cat.availability = False
        return select_cat

    def dequeue_all(self):
        select_animal = self.all_animals.pop_from_queue()
        if select_animal.availability is False:
            self.dequeue_all()
        else:
            select_animal.availability = False
        return select_animal

