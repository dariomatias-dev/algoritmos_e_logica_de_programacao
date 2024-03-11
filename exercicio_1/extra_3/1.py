def calculate(x, y, z):
    print(
    '''
{} * {} < {} / {} or {} / {} < {} * {} and {} * {} < {}
    '''.format(
            x, y, z, x, x, y, z, x, z, y, x,
        )
    )

    divisionResult1 = z / x
    divisionResult2 = x / y

    print(
        '''
{} < {} or {} < {} and {} < {}
        '''.format(
            x * y,
            int(divisionResult1) if int(divisionResult1) == divisionResult1 else divisionResult1,
            int(divisionResult2) if int(divisionResult2) == divisionResult2 else divisionResult2,
            z * x,
            z * y,
            x,
        )
    )

    result1 = x * y < z / x
    result2 = x / y < z * x
    result3 = z * y < x

    print(
        '''
{} or {} and {}
        '''.format(
            result1, result2, result3,
        )
    )

    print(
        '''
{} or {}
        '''.format(
            result1, result2 and result3,
        )
    )

    print(
        '''
{}
        '''.format(
            result1 or result2 and result3,
        )
    )

    print("------------------------------------------------------------")

calculate(5, 10, 15)
calculate(40, 10, 3)
calculate(20, 2, 13)
