def check_palindrome(number):
    
    if number < 0:
        return "Number cannot be negative"
    
    res, x_remaining = 0, abs(number)
    while x_remaining:
        res = res * 10 + x_remaining%10
        x_remaining = x_remaining // 10

    return res==number


if __name__ =="__main__":
    number = 1441
    bool_ = check_palindrome(number)
    print(bool_)

    