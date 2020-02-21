'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    # Cant contain 'th' if the length of the word is less than 2, base case
    if len(word) < 2:
        return 0
    else:
        # if the first 2 letters are 'th' increment count by 1
        if word[:2] == 'th':
            count += 1
    # Recursion to call count_th but this time if word was 'abcthefthghith' we pass in 'bcthefthghith' everything but the first letter to the recursive function, then the next recursion call would be 'cthefthghith'
    count += count_th(word[1:])
    return count
