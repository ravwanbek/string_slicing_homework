def main(s):
    """
    The s string variable is given. return the characters in the odd position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s=str(s)
    answer=s[0::2]
    
    return answer
print(main('salomatlik'))