arr = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter the element to search: "))

low = 0
high = len(arr) - 1

found = False


# loop -> mid f -> comp with mid -> left or right 

while low <= high:
    
    # mid 
    mid = (low + high) // 2
    
    if arr[mid] == key:
        print(f"Element found at index {mid}")
        found = True
        break
    
    elif key < arr[mid]:
        high = mid - 1
    else: 
        low = mid + 1
        
        
if not found:
    print("Element not found in the list")