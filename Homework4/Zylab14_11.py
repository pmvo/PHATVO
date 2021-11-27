#Name: Phat Vo
#PSID: 2024127
#Zylab 14.11

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        min = i
        for j in range(i+1,len(numbers)):
            if int(numbers[min]) < int(numbers[j]):
                min = j

        temp = numbers[i]
        numbers[i] = numbers[min]
        numbers[min] = temp
        for item in numbers:
            print(item,end=' ')
        print()
if __name__=='__main__':
    user_input=input()
    numbers=user_input.split()
    selection_sort_descend_trace(numbers)

