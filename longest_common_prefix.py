def longestCommonPrefix(strs):

    first_item = strs[0]
    counter = 0
    should_continue = True
    prefix = ""

    while should_continue:
        
        if counter >= len(first_item):
            break
        for string in strs:
            if string[0:counter+1] == first_item[0:counter+1]:
                continue
            else:
                should_continue = False
                break
        if should_continue == False:
            break
        prefix = first_item[0:counter+1]
        counter += 1

    return prefix

print(longestCommonPrefix(["dog","racecar","car"]))

# first_item = first item in strs
# current_prefix = set to index 0 of first_item
# counter = set to 0 

# While True:
#     FOR each item in STRS
#         if item slice index 0 to counter is equal to first_item slice index 0 to counter:
#             continue
#         else:
#             break
#     current_prefix = first_item[0:counter]
#     counter += 1   
    


# return current_prefix