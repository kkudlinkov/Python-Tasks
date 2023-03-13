def main(x: list):
    data = (
        {1986, 'LASSO', 1997, 1977},
        {1986, 'LASSO', 1997, 1994},
        {1986, 'LASSO', 1997, 2005},

        {1986, 'LASSO', 2019},

        {1986, 'CSV'},
        {1986, 'TEA'},

        {1999, 1977},
        {1999, 1994},

        {1999, 2005, 'ASP', 1997},
        {1999, 2005, 'ASP', 2019},

        {1999, 2005, 'EAGLE'},

        {1991}
    )
    x = set(x)
    for key, item in enumerate(data):
        if item.issubset(x):
            return key
    return -1


# print(main([1997, 'LASSO', 'EAGLE', 1991, 1977]))
# print(main([1997, 'LASSO', 'ASP', 1986, 1977]))
# print(main([1997, 'CSV', 'EAGLE', 1986, 2005]))
# print(main([2019, 'LASSO', 'ASP', 1999, 2005]))
# print(main([1997, 'TEA', 'EAGLE', 1986, 1977]))
print(main([1997, 'CSV', 'ASP', 1999, 1994]))
