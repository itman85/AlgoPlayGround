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
5. convert number to array. e.x 123 -> [1,2,3]
    [int(x) for x in str(123)]
6. string.split('char or string') return list, regex split re.split('[^a-zA-Z]',text) return list of words
7. char.isdigit(), isalpha(), islower(), isupper(), ...
8. sorted(list) sort ASC, sorted(list,reverse = True) sort DES
9. max with key: len, int. E.X find max digit in number:
    n = 123445
    print(max([i for i in str(n)],key=int)) <=> max([int(i) for i in str(n)])
10. Convert binary string to int: print(int('01001000',2)) 2 is binary base, 16 is hex base, default decimal is 10
11. inputString[1:-1:] : substring from index 1 to len -1 with step = 1
12. zip, copy string, pop item from list. E.x check 2 strings diff one char only
    sum([a[0] != a[1] for a in zip(str1, str2)]) == 1
    itemsSet = [1,2,3]
    tempSet = itemsSet.copy() -> create new list instance with same data to itemsSet
    tempSet.pop(i) -> remove item at i in list
13. init 2D array  with value 0
    arr2D = [[0 for i in range(n)] for j in range(n)] or [[0] * n for i in range(n)]
14. The all() function returns True if all items in an iterable are true, otherwise it returns False
    all(iterable) iterable is list,tuple,set,dict e.x: all([True, True, False]) -> False, all({0,1,1}) -> False
    check n is number format xx...xx (22,222,44444,...) all(i == str(n)[0] for i in str(n))
    all({0 : "Apple", 1 : "Orange"}) -> False because first key is false (0 is false in boolean, != 0 is true in boolean)
    For dictionaries the all() function checks the keys, not the values
15. min,max,sum,sorted for items in list,tuple,set, keys for dict
16. Set operators: set1&set2, set1|set2, set1-set2, set1^set2 (Note: set1|set2 = (set1&set2) | (set1^set2))
17. init Dict: dict1 = {0:"Zero",1:"One"}; dict({0: "Zero", 1: "One"}); dict([[0, "Zero"], [1, "One"]]); dict([(0, "Zero"), (1, "One")]); (list/tuple must have 2 items only (item 1 is key, item 2 is value))
    dict(zip([0, 1], ["Zero", "One"]))
18. The any() function return True if one if items in an iterable is True, otherwise it will return False
    any([True,False,False]) -> True
    any([False,False,False]) -> False
19. n.bit_length() return number of bits. e.x 50.bit_length() = 6
20. convert string number in base x to decimal number int(s,x)
21. lst = [1,2,3,4,5,6]; a, *lst, b = lst => a = 1, b= 6, lst = [2,3,4,5]