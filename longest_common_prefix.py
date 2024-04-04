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
