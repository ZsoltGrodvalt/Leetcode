def lengthOfLongestSubstring(s):
    max_str = ''
    max_len = 0
    cur_str = max_str

    for c in s:
        if c not in cur_str:
            print(f'# add "{c}" to cur')
            cur_str = cur_str + c
            print(f'"{cur_str}"')
            
            # update max string if needed
            if len(cur_str) > max_len :
                print('# update max')
                max_len = len(cur_str)
                max_str = cur_str
                print(max_str)
        else:
            # update max string if needed
            if len(cur_str) > max_len :
                print('# update max')
                max_len = len(cur_str)
                max_str = cur_str
                print(max_str)
            
            # remove first letter from current string and add the new one
            c_index = cur_str.find(c)
            # print(f'"{c}" in "{cur_str}" is {c_index}')
            cur_str = cur_str[c_index+1:] + c
            # print(f'new cur: "{cur_str}"')

    return max_len

# Test case:
test1 = 'abcabcabc'
test2 = 'bbbbbb'
test3 = 'pwwkew'
test4 = ''      # 0
test5 = ' '     # 1
# print(len(test5))
print(lengthOfLongestSubstring(test5))