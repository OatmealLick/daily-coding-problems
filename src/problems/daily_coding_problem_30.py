def trap_water(heights):
    """
    Count all the water trapped in blocks of heights (given as list).
    For [3, 0, 1, 3, 0, 5] (len = 6) it should return:

     3---0---1---3---0---5
         3 + 2 + 0 + 3  =  8

    :param heights:
    :return:
    """
    left = 0
    right = len(heights) - 1
    max_left = -1
    max_right = -1
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > max_left:
                max_left = heights[left]
            else:
                water += max_left - heights[left]
            left += 1
        else:
            if heights[right] > max_right:
                max_right = heights[right]
            else:
                water += max_right - heights[right]
            right -= 1
    return water
