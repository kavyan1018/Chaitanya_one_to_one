# list 

arr = [10, 20, 30, 40, 50]
key = int(input("Enter the element to search: "))
found = False


for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element found at index {i}")
        found = True
        break
    
    
if not found:
    print("Element not found in the list")