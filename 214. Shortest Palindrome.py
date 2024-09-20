s = "aabbv"
length = len(s)

min_pal = 2*s

def isWordPalindrome(word):
    length = len(word)
    for i in range(0,length//2):
        l = word[i]
        r = word[length-1-i]
        if l != r:
            return False
    return True


for i in range(0,length):
    pointer = s[length-i-1]
    new = pointer + s 
    if isWordPalindrome(new) == True:
        print(new)
        break


# # same starting point
# for start in range(0,length):
#     # print(f'start = {start}')
#     i = 0

#     while ((start - i)>=0) & ((start + i) < length):
#         l = s[start - i]
#         r = s[start + i]
#         if i==0:
#             current_word = l
#         else:
#             current_word = l + current_word + r
#         # print(current_word)

#         # left end reached
#         if start - i == 0:
#             # print('left reached')
#             if isWordPalindrome(current_word)==True:
#                 pal = s[start+i+1:][::-1] + s 
#                 # # print(pal)
#                 if len(pal) < len(min_pal):
#                     min_pal = pal
#                     # print(f'new min: {min_pal}')
#             break
#         # right end reached
#         # elif start + i == length-1:
#         #     # print('right reached')
#         #     if isWordPalindrome(current_word)==True:
#         #         pal = s + s[:start-i][::-1]
#         #         # print(pal)
#         #         if len(pal) < len(min_pal):
#         #             min_pal = pal
#         #             # print(f'new min: {min_pal}')
#         #     break
#         # mismatch inside
#         elif r != l:
#             break
#         else:
#             i+=1


# # neighbouring starting point
# for start in range(0,length):
#     # print(f'start = {start},{start+1}')
#     i = 0

#     while ((start - i)>=0) & ((start+1 + i) < length):
#         l = s[start - i]
#         r = s[start+1 + i]
#         if i==0:
#             current_word = l+r
#         else:
#             current_word = l + current_word + r
#         # print(current_word)

#         # left end reached
#         if start - i == 0:
#             # print('left reached')
#             if isWordPalindrome(current_word)==True:
#                 pal = s[start+1+i+1:][::-1] + s 
#                 # # print(pal)
#                 if len(pal) < len(min_pal):
#                     min_pal = pal
#                     # print(f'new min: {min_pal}')
#             break
#         # right end reached
#         # elif start+1 + i == length-1:
#         #     # print('right reached')
#         #     if isWordPalindrome(current_word)==True:
#         #         pal = s + s[:start-i][::-1]
#         #         # print(pal)
#         #         if len(pal) < len(min_pal):
#         #             min_pal = pal
#         #             # print(f'new min: {min_pal}')
#         #     break
#         # mismatch inside
#         elif r != l:
#             break
#         else:
#             i+=1

# print(f'output:{min_pal}')