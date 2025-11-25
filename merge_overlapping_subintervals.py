class Solution:
    def mergeOverlap(self, intervals):

        intervals.sort() # sorts by start time

        merged = [intervals[0]]  # start with the first interval

        for start,end in intervals[1:]:
          last_start,last_end = merged[-1]

          if start <= last_end:
            # merged[-1][1] --> end value of the last interval in the merged list
            # update the end of the last merged interval.
            merged[-1][1] = max(last_end,end) # merge/update by extending the end
          else:
            merged.append([start,end]) # no overlap → push new interval

        return merged
