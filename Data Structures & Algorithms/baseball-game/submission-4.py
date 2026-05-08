class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            record_len = len(record)
            
            if operation == '+':
                record.append(record[record_len - 1] + record[record_len - 2])
            elif operation == 'D':
                record.append(2 * record[record_len - 1])
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))

        return sum(record)