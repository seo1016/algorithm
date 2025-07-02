def solution(sizes):
    width = 0
    height = 0
    for w,h in sizes:
        if max(w,h)>width:
            width = max(w,h)
        if min(w,h)>height:
            height = min(w,h)
    return width*height