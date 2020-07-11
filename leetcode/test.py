
class Solution188:
    def generate(self, num_rows):
        t = []
        for n in range (num_rows):
            row = [None for _ in range(n+1)]
            row[0], row[-1] = 1, 1

            # 从1到(-1)数组位置之间
            for j in range(1,len(row)-1):
                row[j] = t[n-1][j-1] + t[n-1][j]

            t.append(row)

        return t


def main():
    result = Solution188().generate(5)
    print(result)

if __name__ == '__main__':
    main()
