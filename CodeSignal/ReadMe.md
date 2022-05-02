# Python Cheatsheet
    1. convert char to int and int to char
        chr(97) -> 'a'
        ord('a') -> 97
    2. reverse string/list st[::-1], st[i:j] : substring, sub list from i -> j-1, st[-1]: last item of string or list
    3. sum boolean (True = 1, False = 0) e.x: sum([True,False,True,True])  = 3
    4. init set,list,typle from string
        str1 = "cabca"
        print(set(str1))  >>> {'c', 'b', 'a'}
        print(list(str1))  >>> ['c', 'a', 'b', 'c', 'a']
        print(tuple(str1))  >>> ('c', 'a', 'b', 'c', 'a')
    5. convert number to array. ex 123 -> [1,2,3]
        [int(x) for x in str(123)]
    6. string.split('char or string') return list, regex split re.split('[^a-zA-Z]',text) return list of words
    7. char.isdigit(), isalpha(), islower(), isupper(), ...
    8. sorted(list)
    9. max with key: len, int. E.X find max digit in number:
        n = 123445
        print(max([i for i in str(n)],key=int)) <=> max([int(i) for i in str(n)])
    10. Convert binary string to int: print(int('01001000',2)) 2 is binary base, 16 is hex base, default decimal is 10
    11. inputString[1:-1:] : substring from index 1 to len -1 with step = 1
    12. zip , copy string, pop item from list. Ex check 2 strings diff one char
    sum([a[0] != a[1] for a in zip(str1, str2)]) == 1
    itemsSet = [1,2,3]
    tempSet = itemsSet.copy() -> create new list instance with same data to itemsSet
    tempSet.pop(i) -> remove item at i in list
    13. init 2D array  with value 0
    arr2D = [[0 for i in range(n)] for j in range(n)] or [[0] * n for i in range(n)]
    