n = int(input("number = "))
assert n%2 == 0
print(f'{n} is an even number')

'''
number = 6
6 is an even number

number = 5
Traceback (most recent call last):
  File "assert.py", line 2, in <module>
    assert n%2 == 0
AssertionError
'''