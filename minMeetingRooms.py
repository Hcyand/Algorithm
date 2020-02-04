"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2

示例 2:

输入: [[7,10],[2,4]]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq  # heapq为最小堆排序算法


class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        # 比较最小堆中最小数与开始会议时间是否冲突
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[0])
        meeting_list = []
        start_list = [x[0] for x in intervals]
        end_list = [x[1] for x in intervals]
        heapq.heapify(meeting_list)
        heapq.heappush(meeting_list, end_list[0])
        for i in range(1, len(start_list)):
            earlist = heapq.heappop(meeting_list)
            if start_list[i] < earlist:
                heapq.heappush(meeting_list, earlist)
            heapq.heappush(meeting_list, start_list[i])
        return len(meeting_list)

    def minmeetingrooms2(self, intervals):
        if not intervals:
            return 0
        used_room = 0
        start_timings = sorted(i[0] for i in intervals)
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        end_p = 0
        start_p = 0
        while start_p < L:
            if start_timings[start_p] >= end_timings[end_p]:
                used_room -= 1
                end_p += 1
            used_room += 1
            start_p += 1
        return used_room


if __name__ == '__main__':
    d = Solution()
    print(d.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(d.minmeetingrooms2([[0, 30], [5, 10], [15, 20]]))
