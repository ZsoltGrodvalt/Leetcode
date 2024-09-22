def findKthNumber(n, k):
    def printBranch(preNum,knum_passed):
        knum = knum_passed
        if knum == k:
            # print('return @ knum == k')
            # print(f'return: {preNum}, {knum}')
            return preNum,knum

        for lastNum in range(0,10):
            new_num = preNum + lastNum
            # print(f'? num: {new_num} ?')
            if new_num <= n:
                num = new_num
                # print(f'-> knum: {knum}')
                # print(f'-> num: {num}')
                # knum += 1
                # print(f'knum -> {knum}')

                if knum == k:
                    # print(f'k-th value: {num}')
                    # print('return @ k-th value found2')
                    # print(f'return: {num}, {knum}')
                    return num, knum

                knum += 1

                if num*10 <= n:
                    # calling next level
                    ans, knum = printBranch(num*10,knum)
                    if ans != 0:
                        # print('return @ 3')
                        # print(f'return: {ans}, {knum}')
                        return ans, knum
        # knum += 1
        # xxx9
        # print(f'return: 0, {knum}')
        return 0,knum

    ans, knum = printBranch(1,1)
    return ans

        


print(f'Kth number: {findKthNumber(804289,426)}')