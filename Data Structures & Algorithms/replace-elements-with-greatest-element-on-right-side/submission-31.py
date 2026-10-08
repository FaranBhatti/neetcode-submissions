class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        given: array arr. reaplce every element in there with greatest element among the elements to its right. last element with -1
        return: arr
        """
        largest_num = -1
        track_val = -1

        for i in reversed(range(len(arr))):
            track_val = arr[i]
            arr[i] = largest_num

            
            if track_val > largest_num:
                largest_num = track_val

        return arr