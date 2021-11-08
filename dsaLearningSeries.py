# # Anagram starts here...........
# def anagram1(s1, s2):
#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()
#     print(sorted(s1) == sorted(s2))
#
#
# anagram1(' ', '')
#
#
# def anagram2(a, b):
#     d = list(a.lower())
#     d.append(' ')
#     e = list(b.lower())
#     on = True
#     count = 0
#     while on:
#         if len(a) != len(b):
#             on = False
#             print("False")
#         for i in e:
#             if i not in d:
#                 on = False
#                 print("False")
#             else:
#                 count += 1
#         if count == len(b):
#             on = False
#             print("True")
#
#
# anagram2("God", "dogg")
#
#
# def anagram3(s1, s2):
#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()
#
#     if len(s1) != len(s2):
#         print("False")
#
#     count = {}
#     # try using default dictionary using coolections
#     # import collections
#     # count=collections.defaultdict()
#     for i in s1:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1
#     print(count)
#     for letter in s2:
#         if letter in count:
#             count[letter] -= 1
#         else:
#             count[letter] = 1
#     print(count)
#     for k in count:
#         if count[k] != 0:
#             print("False")
#     print("True")
#
#
# anagram3('God', 'dogg')
#
#
# # Pairsum Starts
#
# def pairsum1(lst, k):
#     count = 0
#     for i in lst:
#         if k - i in lst:
#             count += 1
#     print(count)
#     seen = set()
#
#
# pairsum1([1, 3, 2, 2], 4)
#
#
# def pairsum2(lst, k):
#     if len(lst) < 2:
#         return
#     seen = set()
#     output = set()
#     print(type(seen))
#     for num in lst:
#         target = k - num
#
#         if target not in seen:
#             seen.add(num)
#         else:
#             output.add((min(target, num), max(target, num)))
#     print(len(output))
#     print('\n'.join(list(map(str, output))))
#
#
# pairsum2([1, 3, 2, 2], 4)
#
# # Finding Missing Element Starts
# import random
#
# arr1 = [3, 4, 5, 6, 8, 10, 3, 7, 34, 56, 76, 78]
# print(arr1)
#
#
# def finder(arr1, arr2):
#     for i in arr1:
#         if i not in arr2:
#             print(i)
#
#
# finder([2, 3, 4, 6, 4, 5], [4, 2, 3, 6])
# arr2 = [3, 4, 5, 6, 7]
# for i in range(5):
#     print(zip(arr1, arr2))
#
#
# Largest Continuous Sum
# def largesum1(arr1):
#     sum = []
#     for i in range(len(arr1)):
#         if i == 0:
#             sum.append(arr1[i])
#         else:
#             sum.append(arr1[i] + sum[i - 1])
#     print(max(sum))
#     print(sum)
#
#
# largesum1([-2,1,-3,4,-1,2,1,-5,4])
#
# largesum1([2, 3, -4, 25, -56, 98, 7, 8, -98])
# #
# #
# def largesum2(arr):
#     if len(arr) == 0:
#         print(0)
#     else:
#         max_sum = current_sum = arr[0]
#         for i in arr[1:]:
#             current_sum = max(current_sum + i, i)
#             # print(current_sum)
#             max_sum = max(current_sum, max_sum)
#
#         print(max_sum)
#
# largesum2([-2,1,-3,4,-1,2,1,-5,4])
#
# # largesum2([2, 3, -4, 25, -56, 98, 7, 8, -98])
# #
# #
# # Sentence Reversal starts
# # def reverse1(s):
# #     s = s.strip(' ').replace(".", "")
# #     s = list(map(str, s.split(" ")))
# #     s[0] += '.'
# #     for word in range(len(s) - 1, -1, -1):
# #         if len(s[word]) > 1:
# #             print(s[word], end=" ")
# #     print("\n")
# #
# #
# # reverse1("   This is a    nice    morning.   ")
# #
# #
# # def reverse2(s):
# #     print(" ".join(reversed(s.split())))
# #     #     or
# #     print(" ".join(s.split()[::-1]))
# #
# #
# # reverse2("   This is a    nice    morning.   ")
# #
# #
# # # String Compression starts here
# #
# # def compress(s):
# #     import collections
# #     d = {}
# #     for i in s:
# #         if i in d:
# #             d[i] += 1
# #         else:
# #             d[i] = 1
# #     for key in d:
# #         print("".join(f"{key}{d[key]}"), end="")
# #     # print(d)
# #
# #
# # compress('aaaAAAbbbAAAvvvvVVVnmgdj')
# #
# #
# # # def factorial(n):
# # #     if n == 0:
# # #         print(1)
# # #     else:
# # #         print(n * factorial(n - 1))
# # #
# # # factorial(5)
# #
# # # Fibonacci Series
# # def fibonacci1(n):
# #     n1=0
# #     n2=1
# #     print(f"{n1} {n2}",end=' ')
# #     for i in range(2,n):
# #         c=n1+n2
# #         n1=n2
# #         n2=c
# #         print(c,end=' ')
# # fibonacci1(24)
# # def febonacci2(n):
# #     output=[]
# #     if n==0 or n==1:
# #         return n
# #     else:
# #         output.append(febonacci2(n-1)+febonacci2(n-2))
# #         return output
# # print(febonacci2(10),end='\n')
#
#
# # Sorting an array using recursion
#
#
# # def insert(arr, value):
# #     if len(arr) == 0 or arr[len(arr) - 1] <= value:
# #         arr.append(value)
# #         return arr
# #     else:
# #         temp = arr[len(arr) - 1]
# #         arr.pop()
# #         insert(arr, value)
# #         arr.append(temp)
# #         return arr
# #
# #
# # def sort(arr):
# #     if len(arr) <= 1:
# #         return arr
# #     else:
# #         value = arr[len(arr) - 1]
# #         arr.pop()
# #         sort(arr)
# #         insert(arr, value)
# #         return arr
# #
# #
# # print(sort([2, 3, 0, 5, 6, 4, 10, 78, 56, 43, 22, 57, 98, 76, 66]))
# #
# #
# # # Delete the middle element of Stack
# # def solve(arr, k):
# #     if k == 1:
# #         arr.pop()
# #         return
# #     else:
# #         temp = arr[len(arr) - 1]
# #         arr.pop()
# #         solve(arr, k - 1)
# #         arr.append(temp)
# #     return
# #
# #
# # def deleteMiddle(arr):
# #     k = len(arr) // 2 + 1
# #     if len(arr) == 0:
# #         return arr
# #     else:
# #         solve(arr, k)
# #         return arr
# #
# #
# # print(deleteMiddle([5, 3, 2, 1, 7, 8]))
# #
# #
# # # Reverse a stack using recursion
# # def insertelement(arr, element):
# #     if len(arr) == 0:
# #         arr.append(element)
# #         return
# #     else:
# #         temp = arr[len(arr) - 1]
# #         arr.pop()
# #         insertelement(arr, element)
# #         arr.append(temp)
# #         return
# #
# #
# # def reverse(stack):
# #     if len(stack) <= 1:
# #         return stack
# #     else:
# #         temp = stack[len(stack) - 1]
# #         stack.pop()
# #         reverse(stack)
# #         insertelement(stack, temp)
# #         return stack
# #
# #
# # print(reverse([1, 2, 3, 4, 5]))
#
#
# # Tower of Hanoi
# # def solve(s,d,h,n,ans):
# #     if n==1:
# #         ans+=1
# #         print(f'moving plate {n} from {s} to {d}')
# #         return ans
# #     else:
# #         solve(s,h,d,n-1,ans)
# #         print(f"moving plate {n} from {s} to {h}")
# #         ans+=1
# #     solve(h,d,s,n-1,ans)
# #     print(ans)
# #     return
# #
# # n=int(input())
# # s=1
# # h=2
# # d=3
# # ans=0
# # print(solve(s,h,d,n,ans))
# # print(ans)
#
# # Subset Problems
# # def subset(input, output):
# #     if len(input) == 0:
# #         print(output)
# #         return
# #     else:
# #         output1 = output
# #         output2 = output
# #         output2+=input[0]
# #         input.pop(0)
# #         subset(input, output1)
# #         subset(input, output2)
# #         return
# # output=''
# # string='abc'
# # input=[x for x in string]
# # print(subset(input,output))
# # print(output)
#
#
# # Bubble Sort
# a=[4,5,3,8,6,2,7]
# # for i in range(len(a)-1):
# #     for j in range(len(a)-1):
# #         if a[j]>a[j+1]:
# #             temp=a[j]
# #             a[j]=a[j+1]
# #             a[j+1]=temp
# # print(a)
#
# # Selection Sort
# # for i in range(len(a)-1):
# #     minIndex=i
# #     for j in range(i,len(a)):
# #         if a[j]<a[minIndex]:
# #             minIndex=j
# #     temp=a[i]
# #     a[i]=a[minIndex]
# #     a[minIndex]=temp
# # print(a)
#
# # Insertion Sort
# # for i in range(1,len(a)):
# #     current_value=a[i]
# #     position=i
# #     while position>0 and current_value<a[position-1]:
# #         a[position]=a[position-1]
# #         position-=1
# #         a[position]=current_value
# #     print(a)
# #
# # # Merge Sort
# #
# # def reverseWords(s):
# #     s = list(map(str, s.split(" ")))
# #     for i in s:
# #         print("".join(reversed(i)), end=" ")
# # print(reverseWords("Hellow World"))
#
# s="dog cat lion dog cat cat"
# pattern="abcacc"
# s=s.split(' ')
# d={}
# p=set(pattern)
# for i in range(len(s)):
#     if pattern[i] not in d:
#         d[pattern[i]]=s[i]
#     elif d[pattern[i]]!=s[i]:
#         print("False")
#     print("True")
# from collections import Counter
# t=Counter(s)
# for k,v in t.items():
#     print(k,v)
# print(Counter(s))
# print(t.values())
# print(t.items())
# print(t.keys())
#
# a='101'
# print(a.count("1"))
# def binary(n):
#     a=[]
#     for i in range(n+1):
#         a.append(bin(i).count('1'))
#     print(a)
# binary(3)
# print(type(bin(5)))
# d={0:0,1:1,2:5,5:2,6:9,8:8,9:6}
# for i in d:
#     print(d[i])
#
# print(10**2)
# print(3*1**3)
# x=345
# print("%06d"%x)
# i=1
# while True:
#     if i%0o7==0:
#         break
#     print(i)
#     i+=1
# j=2
# while True:
#     if j%3==0:
#         break
#     print(j)
#     j+=2
# k="abcdef"
# # print(m[:-1])
# # print(k[::-1])
# i="a"
# while i in k[:-1]:
#     # k=k[:-1]
#     # print(k)
#     print(i, end="")
a={}
print(a)
print(a.fromkeys([1,2,3],"check"))
print(all(a))
class demo(dict):
    def __test__(self,key):
        return []
        a = demo()
        a['test'] = 7
    print(a)
l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])
l=[1,2,3,4,5]
print([x&1 for x in l])
s=(1,2)
a=("hello",6)
print(s*2)
print(s+a)
s="swetant"
s[0]="t"
print(s)
d={1:2,2:3}
print(len(d))