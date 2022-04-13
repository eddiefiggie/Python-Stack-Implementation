# main

from ArrayStack import ArrayStack

if __name__ == '__main__':

    my_stack = ArrayStack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)

    print(my_stack.top())

    my_stack.pop()
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.top())






