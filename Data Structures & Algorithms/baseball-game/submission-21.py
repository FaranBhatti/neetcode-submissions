class Solution:
    def calPoints(self, operations: List[str]) -> int:
        runningSum = []

        for op in operations:
            match op:
                case '+':
                    runningSum.append(runningSum[-1] + runningSum[-2])
                case 'D':
                    runningSum.append(runningSum[-1] * 2)
                case 'C':
                    if runningSum:
                        runningSum.pop()
                case _:
                    runningSum.append(int(op))
        
        returnSum = sum(runningSum)
        
        return returnSum