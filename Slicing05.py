def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s=str(s)
    n=int(n)
    if len(s)>=n:
        answer=s[-n:]
    return answer
print(main('abcdefghijk',5))
