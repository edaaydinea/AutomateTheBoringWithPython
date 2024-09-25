def spam():
    eggs = 'spam local' # This is the local
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local' # This is the local
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
eggs = 'global'  # This is the global
bacon()
print(eggs) # prints 'global'

# Result
# bacon local
# spam local
# bacon local
# global