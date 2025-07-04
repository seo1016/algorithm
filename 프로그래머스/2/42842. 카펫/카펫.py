def solution(brown, yellow):
    for height in range(1, yellow + 1):
        if yellow % height == 0:
            width = yellow // height
            total_width = width + 2
            total_height = height + 2
            total_area = total_width * total_height
            if total_area == brown + yellow:
                return [total_width, total_height]