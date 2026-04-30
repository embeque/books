def is_in(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    return False

def test():
    strings = ["an", "elephant", "ant", "march", "one", "antonee"]
    for str1 in strings:
        for str2 in strings:
            if str1 == str2:
                continue
            print(f'{str1} or {str2} are some text in common: {is_in(str1, str2)}')

if __name__ == "__main__":
    test()
