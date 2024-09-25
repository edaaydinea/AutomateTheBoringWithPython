def a():
    print('a() starts')
    b() # Call b() from a()
    d() # Call d() from a()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() returns')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() returns')
    
a() # Call a() from the global scope
# Result
# a() starts
# b() starts
# c() starts
# c() returns
# b() returns
# d() starts
# d() returns
# a() returns