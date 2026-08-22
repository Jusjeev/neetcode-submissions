class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # dont worry about poping empty stack! for 'C' there will always be a previous score!
        record = []
        for i in range(len(operations)):
            # order kinda matters so in else only ints possible
            if operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                record.append(record[-1] * 2)
            elif operations[i] == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(operations[i]))
        return sum(record)
            

        
        