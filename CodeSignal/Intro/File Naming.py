'''
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
solution(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string names

Guaranteed constraints:
5 ≤ names.length ≤ 1000,
1 ≤ names[i].length ≤ 15.

[output] array.string
'''
def solution(names):
    names1 = []
    for name in names:
        if name not in names1:
            names1.append(name)
        else:
            k = 1
            name1 = name + f"({k})"
            while name1 in names1:
                k += 1
                name1 = name + f"({k})"
            names1.append(name1)
    return names1

print(solution(["doc", "doc", "image", "doc(1)", "doc"]))