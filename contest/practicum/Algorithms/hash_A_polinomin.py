def get_poli_hash(alpha, modul, string):
    if len(string) == 0:
        return 0
    result = ord(string[0])
    for value in string[1:]:
        result = (result * alpha + ord(value)) % modul
    return result % modul


def main():
    alpha = int(input())
    modul = int(input())
    string = input()
    result = get_poli_hash(alpha, modul, string)
    print(result)


def main1():
    modul = 10
    string = 'abc'
    for i in range(10):
        alpha = 1000
        modul = 100000
        string *= 3
        result = get_poli_hash(alpha, modul, string)
        print(result)
    



if __name__ == '__main__':
    main1()
