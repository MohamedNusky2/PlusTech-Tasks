# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHW0qaPM8aA9HnWMeeiYR5SYJbco0vJb
"""

nums  = list(map(int, input("enter numbers: ").split())) 


print(nums)
print(len(nums))
print(min(nums))
print(max(nums))
Ttal = sum(nums)

averg = Ttal//(len(nums))

print("total = ", Ttal)
print("Average = ", averg)