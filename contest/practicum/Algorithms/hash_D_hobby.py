def get_unique_hobby_list(hobbies):
    buffer = set()
    result = []
    for item in hobbies:
        if item in buffer:
            continue
        buffer.add(item)
        result.append(item)
    return result


def main():
    #hobbies = ['sing', 'golf', 'tennis', 'golf', 'warhammer', 'sing']
    #print(get_unique_hobby_list(hobbies))
    n = int(input())
    hobbies = [None] * n
    for index in range(n):
        hobbies[index] = input()
    
    for hobby in get_unique_hobby_list(hobbies):
        print(hobby)


if __name__ == '__main__':
    main()
