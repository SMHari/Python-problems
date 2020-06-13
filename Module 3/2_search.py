import math

lst_xyz = [88, 77, 54, 41, 34, 56, 12, 90, 33, 87, 67, 51]


def binsearch(xyz,element):
    bottom = 0
    top = len(xyz)
    print(top)
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if xyz[mid] == element:
            index = mid
        elif xyz[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1

    return index


if __name__ == '__main__':

    print("Elements in xyz sorted list is :", sorted(lst_xyz))
    while True:
        fin = int(input("Enter the element to find in the list: (0 to exit)"))
        if fin != 0:
            res= binsearch(sorted(lst_xyz),fin)
            if res != -1:
                print("Element is present at index %d and pos %d"%(res,res+1))
            else:
                print("Element is not present in array")
        else:
            break
