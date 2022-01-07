def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a=str(s)
    answer=a[1:-1]
    return answer
print(main('abcdefghijk'))