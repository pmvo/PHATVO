#Name: Phat Vo
#PSID: 2024127
#Zylab 14.13

num_calls=0
def partition(numbers, i, k):

    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]

    done = False
    l = i
    h = k
    while not done:
        while numbers[l] < pivot:
            l = l + 1
        while pivot < numbers[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
    return h


def quicksort(numbers, i, k):
    global num_calls
    num_calls += 1
    j = 0
    if i <k:
        j = partition(numbers, i, k)
        quicksort(numbers, i, j)
        quicksort(numbers, j + 1, k)

if __name__=='__main__':
    list = []
    while True:
        user_input = input()
        if user_input=='-1':
            break
        elif user_input not in list:
            list.append(user_input)
    quicksort(list,0,len(list)-1)
    print(num_calls)
    for id in list:
        print(id)




