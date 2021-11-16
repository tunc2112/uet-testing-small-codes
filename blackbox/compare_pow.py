def compare_pow(x, y):
    """
    Compare x**y and y**x (x, y may be non-positive)
    """
    if x == 0 >= y or x <= 0 == y:
        return None

    if x == 0 or y == 0:
        return '<' if x < y else '>'

    if x < 0 < y:
        return '>' if y % 2 == 0 else '<'

    if x > 0 > y:
        return '<' if x % 2 == 0 else '>'

    if x < 0 > y:
        if x % 2 != y % 2:
            return '>' if y % 2 == 0 else '<'

        return compare_pow_positive(-y, -x) if x % 2 == 0 else compare_pow_positive(-x, -y)

    if x > 0 < y:
        return compare_pow_positive(x, y)


def compare_pow_positive(x, y):
    """
    Compare x**y and y**x (x, y are positive)
                     y       x
    x**y < y**x => ----- < -----
                   ln(y)   ln(x)
    """
    if x == y or (x, y) in [(2, 4), (4, 2)]:
        return '='

    if x == 1:
        return '<'
    
    if y == 1:
        return '>'
    
    if y == 3:
        return '<'
    
    if x == 3:
        return '>'

    return '<' if y < x else '>'
 
 
if __name__ == '__main__':
    print(compare_pow(*map(int, input().split())))
