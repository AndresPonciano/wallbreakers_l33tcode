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
        
def mergeSort(arr) -> list:
        # print("---")
        if len(arr) <= 1:
                return arr

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        # print(left)
        # print(right)

        part1 = mergeSort(left)
        part2 = mergeSort(right)

        print(part1, part2)
        return merge(part1, part2)

def handler(outList):
        return []

def doStuffWith(keyword):
        # result = []
        input2 = [38, 27, 43, 3, 9, 82, 10]
        thread = threading.Thread(target=mergeSort, args=(input2, ))
        thread.start()
        return(thread, input2)


if __name__ == "__main__":
        input2 = [83, 86, 77, 15, 93, 35, 86, 92, 49, 21, 
        62, 27, 90, 59, 63, 26, 40, 26, 72, 36]

        # input2 = [38, 27, 43, 3, 9, 82, 10]
        # input2 = [38, 27, 43, 3, 9, 82]
        threads = [doStuffWith(k) for k in range(4)]

        # for t in threads:
        #         t[0].start()

        for t in threads:
                t[0].join()
                ret = t[1]

        print(threads)

        # print(input2)

        # result = mergeSort(input2)

        # print(result)
    
