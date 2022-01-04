
m = 'visible everywhere'

def a():
    ma = 'visible in b() and a()'

    def b():
        print(m)
        print(ma)
        mb =' visible in c() and in b(), bot not visible in a()'

        def c():
            print(m)
            print(ma)
            print(mb)
            mc = 'visible only in c()'

        # print(mc)   -error
        c()
    b()
a()