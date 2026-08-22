class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # dont worry about poping empty stack! for 'C' there will always be a previous score!
        record = []
        res = 0
        for i in range(len(operations)):
            # order kinda matters so in else only ints possible
            if operations[i] == 'C':
                res -= record.pop()
            elif operations[i] == 'D':
                res += record[-1] * 2
                record.append(record[-1] * 2)
            elif operations[i] == '+':
                res += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            else:
                res += int(operations[i])
                record.append(int(operations[i]))
        return res
            

        
        