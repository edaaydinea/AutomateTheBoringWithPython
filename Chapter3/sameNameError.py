def spam():
    print(eggs) # ERROR!
    # UnboundLocalError: local variable 'eggs' where it is not associated with any value
    eggs = 'spam local'

eggs = 'global'
spam()