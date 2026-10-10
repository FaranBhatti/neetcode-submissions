class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        need: return the sum of all the scores on the record after all ops are applied.
        doing: recording scores in an array.
        case 1: recording a new score that is the sum of previous two scores
        case 2: recording a new score that is the dobule of the previous score
        case 3: invalidate the previous score, removing it from the record
        case 4: an integer 'x'. record a new score of 'x'

        assumptions: 
        - x will always be a valid integer value
        - the array ops will always be in an order that is valid
        """
        scores = []

        for op in operations:
            match op:
                case '+':
                    scores.append(scores[-1] + scores[-2])
                case 'D':
                    scores.append(scores[-1] * 2)
                case 'C':
                    scores.pop()
                case _:
                    scores.append(int(op))

        return sum(scores)
