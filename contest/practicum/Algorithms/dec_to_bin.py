dec = int(input())

def dec_to_bin(dec):
    bin = ''
    whole = dec // 2
    remain = dec % 2
    if remain == 1:
        bin = '1' + bin
    else:
        bin = '0' + bin
    if whole > 1:
        bin = dec_to_bin(whole) + bin
    else:
        bin = '1' + bin
    return bin


if __name__ == '__main__':
    print(dec_to_bin(dec))