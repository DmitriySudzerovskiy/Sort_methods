def insert_sort(a):
   """Сортировка вставками"""
   for top in range(1, len(a)):
       k = top
       while k > 0 and a[k-1] > a[k]:
           a[k], a[k-1] = a[k - 1], a[k]
           k -= 1

def choise_sort(a):
    """Сортировка выбором"""
    for pos in range(0, len(a) - 1):
        for k in range(pos + 1, len(a)):
            if a[k] < a[pos]:
                a[pos], a[k] = a[k], a[pos]
def bubble_sort(a):
    """Сортировка пузырьком"""
    for bypass in range(1,len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]



def test_sort(sort_algoritm):
    print("Тестируем: ", sort_algoritm.__doc__)
    print("testcase #1: ", end='')
    a = [1,5,3,7,48,49,3,4,5,99,0,2]
    a_sort = [0, 1, 2, 3, 3, 4, 5, 5, 7, 48, 49, 99]
    sort_algoritm(a)
    print("Ok" if a == a_sort else "Faill")

    print("testcase #1: ", end='')
    a = [4,2,5,1,3]
    a_sort = [1,2,3,4,5]
    sort_algoritm(a)
    print("Ok" if a == a_sort else "Faill")

    print("testcase #1: ", end='')
    a = [1,5,3,7,48,49,3,4,5,99,0,2]
    a_sort = [0, 1, 2, 3, 3, 4, 5, 5, 7, 48, 49, 99]
    sort_algoritm(a)
    print("Ok" if a == a_sort else "Faill")


if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)



