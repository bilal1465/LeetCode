def isValid(s):
    bracket_sets = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    open_brackets = []
    
    for bracket in s:
        if bracket in "([{":
            open_brackets.insert(0, bracket)
        else:
            if len(open_brackets) != 0 and open_brackets[0] == bracket_sets[bracket]:
                if len(open_brackets) != 0 and open_brackets[0] == bracket_sets[bracket]:
                    open_brackets.remove(open_brackets[0])
            else:
                return False
    return not len(open_brackets)

print(isValid("]"))


# bracket_sets = dictionary with bracket pairings
# open_brackets = start with empty array
# for bracket in s:
#   if bracket equal to "(" or "[" "{"
#       add bracket to open_brackets
#   else:
#       if open_brackets index counter equal to bracket_sets[bracket]:
#            remove open_brackets first element
#       else:
#           exit loop
# return not len(open_brackets)