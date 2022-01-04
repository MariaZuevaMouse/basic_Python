def my_f(my_var):
    my_var = 999
    print('In function', my_var)


a = 1;
my_f(a)
print('After func implementation a =', a)

# ______________________________
global_var = 1


def my_f2():
    global global_var  # bad approach
    local_var = 100
    print('local_var ', local_var)
    print('global_var ', global_var)
    global_var = 999

my_f2()
print(global_var, 'after my_f2() impl')
