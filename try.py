# t=int(input())
# for _ in range(t):
#     N,M=map(int,input().split())
#     A=list(map(int,(input().split())))
#     B=list(map(int,(input().split())))
#     t=[]
#     for i in B:
#         r_time=N
#         f_time=N
#         if A[i-1]!=0:
#             t.append(0)
#         elif A[i-1]==0:
#             for j in range(i-2,-1,-1):
#                 if A[j]==1:
#                     f_time=i-j-1
#             for j in range(i,N,1):
#                 if A[j]==2:
#                     r_time=j-i+1
#             if r_time==N and f_time==N:
#                 t.append(-1)
#             else:
#                 t.append(min(r_time,f_time))
#     print(*t)


# t=int(input())
# for _ in range(t):
#     D,d,P,Q=map(int,input().split())
#     n=(D//d)
#     p=(n//2*((2*P)+(n-1)*Q))*d
#     s=(D-(n*d))*(P+(n*Q))
#     print(p+s)


# t=int(input())
# for _ in range(t):
#     N,M=map(int,input().split())
#     A=list(map(int,(input().split())))
#     B=list(map(int,(input().split())))
#     t=[]
#     l_index=r_index=-1
#     for i in range(N):
#         if i==0:
#             t.append(0)
#         elif A[i]!=0:
#             t.append(0)
#         else:
#             t.append(len(A))
#     for i in range(N):
#         if A[i]==1:
#             l_index=i
#         if l_index!=-1:
#             if A[i]==0:
#                 t[i]=min(t[i],i-l_index)
#     for i in range(N-1,-1,-1):
#         if A[i]==2:
#             r_index=i
#         if r_index!=-1:
#             if A[i]==0:
#                 t[i]=min(t[i],r_index-i)
#     for i in B:
#         if t[i-1]!=5:
#             print(t[i-1])
#         else:
#             print(-1, end=" ")


# a=[5,7,9,13,15,17,18,25]
# print(a)
# d=[]
# for x in range(8):
#     if x==0:
#         d.append(a[x])
#     else:
#         d.append(a[x]-a[x-1])
# print(d)
# d[0]=d[0]+3
# # d[7]=d[7]-3
# for i in range(8):
#     if i==0:
#         a[i]=d[i]
#         print(a[i])
#     else:
#         a[i]=d[i]+d[i-1]
#         d[i]=d[i]+d[i-1]
#         print(a[i])
# print(*a)
# print(*d)

# # Factorial of a number using recursion
# def word_split(phrase,lst_of_word,output=[]):
#     # if output==None:
#     # output=[]
#     for word in lst_of_word:
#         if phrase[:len(word)]==word:
#             output.append(word)
#             return word_split(phrase[len(word):],lst_of_word,output)
#     return output
# print(word_split("themanranafteryou bsblj",['the','ran','man','you',' ','after']))
# 
# def reverse(s):
#     if len(s)==1:
#         return s
#     else:
#         return s[(len(s)-1)]+reverse(s[:len(s)-1])
# print(reverse('shiv'))
# 
# 
# from itertools import permutations
# def permute(s):
#     out=[]
#     if len(s)==1:
#         return s
#     else:
#         for i,letter in enumerate(s):
#             for per in permute(s[:i]+s[i+1:]):
#                 out+=[letter+per]
#     return out
# print(permute("abc"))
# 


# #  Base Number system conversion
#
# n=input()
# value={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
# num=0
# l=len(n)
# for i in range(l):
#     if n[i] in value:
#         num+=value[n[i]]*pow(17,l-1-i)
#     else:
#         num+=int(n[i])*pow(17,l-1-i)
# print(num)


def findMaxConsecutiveOnes(nums) -> int:
    lst = []
    temp_list = []
    for i in range(len(nums)):
        if nums[i] == 1:
            temp_list.append(nums[i])
        elif nums[i] == 0:
            lst.append(len(temp_list))
            temp_list.clear()
    lst.append(len(temp_list))
    return max(lst)
print(findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,0,1]))


nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
lst = []
for i in range(m):
    lst.append(nums1[i])
for i in range(n):
    lst.append(nums2[i])
    nums1=lst.sort()
    # nums1=lst
print(nums1)
print(lst)

