n = int(input())

arr = []
for i in range(n):
    a = input()
    arr.append(a)


for i in range(n-1):
    for j in range(i+1, n):
        # 짧은 것이 먼저
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

        elif len(arr[i]) == len(arr[j]):
            suma=0
            sumb=0
            for x,y in zip(arr[i],arr[j]):
                if x.isdigit():
                    suma+=int(x)
                if y.isdigit():
                    sumb+=int(y)
            if suma > sumb:
                arr[i],arr[j] = arr[j], arr[i]

            elif suma == sumb:
                for x,y in zip(arr[i], arr[j]):
                    if x > y:
                        arr[i],arr[j] = arr[j], arr[i]
                        break
                    elif x < y:
                        break


for i in arr:
    print(i)