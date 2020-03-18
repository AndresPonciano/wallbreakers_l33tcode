import threading

def merge(list1, list2):
        # print("merging")
        # print(list1, list2)

        toReturn = []
        i = 0
        j = 0
        while list1 and list2:
                # print(list1, list2, "what")
                if list1[0] <= list2[0]:
                        toReturn.append(list1.pop(0))
                        i += 1
                elif list1[0] > list2[0]:
                        toReturn.append(list2.pop(0))
                        j += 1
        
        # print(list1, list2)

        if list1:
                while list1:
                        toReturn.append(list1.pop(0))


        if list2:
                while list2:
                        toReturn.append(list2.pop(0))

        # print(toReturn)

        return toReturn
        
def mergeSort(arr):
        if len(arr) <= 1:
                return arr

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        part1 = mergeSort(left)
        part2 = mergeSort(right)

        i = 0
        j = 0
        k = 0

        while part1 and part2:
                if part1[0] <= part2[0]:
                        arr[k] = part1.pop(0)
                        i += 1
                elif part1[0] > part2[0]:
                        arr[k] = part2.pop(0)
                        j += 1
                k += 1

        if part1:
                while part1:
                        arr[k] = part1.pop(0)
                        k += 1
        if part2:
                while part2:
                        arr[k] = part2.pop(0)
                        k += 1

        return arr
        # return merge(part1, part2)

if __name__ == "__main__":
        input2 = [83, 86, 77, 15, 93, 35, 86, 92, 49, 21, 
        62, 27, 90, 59, 63, 26, 40, 26, 72, 36]

        div = len(input2)//4
        arr1 = input2[0:div]
        arr2 = input2[div:div*2]
        arr3 = input2[div*2:div*3]
        arr4 = input2[div*3:div*4]
        arrRest = input2[div*4:]

        thread1 = threading.Thread(target=mergeSort, args=(arr1, ))
        thread2 = threading.Thread(target=mergeSort, args=(arr2, ))
        thread3 = threading.Thread(target=mergeSort, args=(arr3, ))
        thread4 = threading.Thread(target=mergeSort, args=(arr4, ))
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()

        arr1_1 = merge(arr1, arr2)
        arr2_1 = merge(arr3, arr4)
        arr3_1 = merge(arr1_1, arr2_1)
        mergeSort(arrRest)
        final = merge(arr3_1, arrRest)

        print(input2)
        print(final)
        # print("input is: ", input2)
        # mergeSort(input2)
        # print("input is: ", input2)
    
