class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # dont worry about poping empty stack! for 'C' there will always be a previous score!
        record = []
        res = 0
        for op in operations:
            # order kinda matters so in else only ints possible
            if op == 'C':
                res -= record.pop()
            elif op == 'D':
                res += record[-1] * 2
                record.append(record[-1] * 2)
            elif op == '+':
                res += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            else:
                res += int(op)
                record.append(int(op))
        return res
            

        
        