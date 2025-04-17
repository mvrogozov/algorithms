def alpha_phone(digits, iter, n, words):
    ALPHABET = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    nums = len(digits)
    
    if n == nums:
        print(words, end = ' ')
        return
    alphas = ALPHABET.get(int(digits[n]))
    alpha_phone(digits, iter, n + 1, words + alphas[iter])
    alpha_phone(digits, iter, n + 1, words + alphas[iter + 1])
    alpha_phone(digits, iter, n + 1, words + alphas[iter + 2])
    if digits[n] == '7' or digits[n] == '9':
        alpha_phone(digits, iter, n + 1, words + alphas[iter + 3])

    #return alphas[iter]
    '''if iter == len(alphas):
        alpha_phone(digits, 0, n + 1, words + alphas[iter])
        return
    alpha_phone(digits, iter + 1, n + 1, words + alphas[iter])'''
    

alpha_phone(input(), 0, 0, '')
