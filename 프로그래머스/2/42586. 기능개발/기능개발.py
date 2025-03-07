def solution(progresses, speeds):
    answer = []
    arr = []
    for i in range(len(progresses)):
        end = progresses[i]
        time = 0
        while True:
            if end >= 100:
                maxx = 0
                if len(arr) == 0:
                    arr.append(time)
                else:
                    for i in arr:
                        if i > time:
                            maxx = i
                        else:
                            continue
                    if maxx == 0:
                        arr.append(time)
                    else:
                        arr.append(maxx)
                break
            else:
                end += speeds[i]
                time += 1
                
    arr.sort() # 7, 7, 9
    print(arr)
    
    num = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            num += 1
        else:
            answer.append(num)
            num = 1
            
    answer.append(num)
            
    return answer