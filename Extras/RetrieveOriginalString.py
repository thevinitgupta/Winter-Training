def  solve(n, str) :
        count = 1
        i = 0
        j = 0
        while (i < n and j < n) :
            if (str[i] == '2' or str[i] == '3') :
                c = 0
                while (j < n and str[i] == str[j]) :
                    j += 1
                    c += 1
                count = (count * c) % 1000000007
                i = j
                j = i
            else :
                i += 1
                j += 1
        return count