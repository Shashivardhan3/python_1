'''def outer():
    print('one')
    def inner():
        print('two')
        print('three')
    print('four')
outer()
inner()
print('\n') '''
#----------------------------------------------------------------------
'''def outer():
    print('one')
    def inner():
        print('two')
        print('three')
    inner()
    print('four')
outer()

print('\n')'''
#-----------------------------------------------------------------------
def outer():
    print('one')
    def inner():
        print('two')
        print('three')
    print('four')
    inner()
    
outer()

print('\n')
