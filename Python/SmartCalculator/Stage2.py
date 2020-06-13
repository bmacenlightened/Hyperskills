def add(a, b):
    return a + b
    
def split_input(input):
    return [int(x) for x in input.split()]

def main():
    while True:
        action = input()
        if action == "/exit":
            print("Bye!")
            break
        if action == "":
            continue
        if action.find(" ") != -1:
            nums = split_input(action)
            if len(nums) == 2:  
                print(add(nums[0], nums[1]))
        else:
            print(action)


main()