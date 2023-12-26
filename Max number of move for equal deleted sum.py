def solution(A):

    def recurse(res, left, right):
        if right - left < 2:
            return 0

        twice_start = A[left] + A[left + 1]
        twice_end = A[right] + A[right - 1]
        start_end = A[left] + A[right]

        p1 = p2 = p3 = 0
        if twice_start == res:
            p1 += 1 + recurse(res, left + 2, right)
        if twice_end == res:
            p2 += 1 + recurse(res, left, right - 2)
        if start_end == res:
            p3 += 1 + recurse(res, left + 1, right - 1)

        # if p1, p2, p3 stayed 0, there's no more available moves because no more deletions will produce the same sum
        if p1 == p2 == p3 == 0:
            return 0

        return max(p1, p2, p3)

    return max(recurse(A[0] + A[1], 2, len(A) - 1), recurse(A[-1] + A[-2], 0, len(A) - 3), recurse(A[0] + A[-1], 1,
                                                                                                  len(A) - 2))




