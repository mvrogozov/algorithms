def generate_brackets(n, br_op, br_cl, metric):
    if n == 2:
        print(br_op + br_cl)
    else:
        #generate_brackets(n - 1, br_op + '(', br_cl)
        #generate_brackets(n - 1, br_op, br_cl + ')')
        if n - 2 > metric >= 0:
            generate_brackets(n - 1, br_op + '(', br_cl, metric + 1)
            generate_brackets(n - 1, br_op + ')', br_cl, metric - 1)
        #elif n // 2 > metric >= 0:
        #    generate_brackets(n - 1, br_op + '(', br_cl, metric + 1)
        #    generate_brackets(n - 1, br_op + ')', br_cl, metric - 1)
        elif metric < 0:
            generate_brackets(n - 1, br_op + '(', br_cl, metric + 1)
        else:
            generate_brackets(n - 1, br_op + ')', br_cl, metric - 1)



generate_brackets(int(input()) * 2, '(', ')', 0)
