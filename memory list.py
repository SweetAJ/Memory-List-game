import random

NUM_PAIRS = 3

def main():
    truth_list = create_truth_list(NUM_PAIRS)
    random.shuffle(truth_list) # shuffles list

    displayed_list = ['*'] * len(truth_list)

    while '*' in displayed_list:
        print(displayed_list)
        index1 = get_valid_index(displayed_list)
        index2 = get_valid_index(displayed_list)
        check_match(truth_list, displayed_list, index1, index2)

    print('Congratulations! You won!')

#Create truth list        
def create_truth_list(NUM_PAIRS):    
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
    return truth_list

#Get a valid index from user
def get_valid_index(displayed_list):
    while True:
        index = input('Enter an index: ')
        if not index.isdigit():
            print('Not a number. Try again.')
        else:
            index = int(index)
            if index < 0 or index >= len(displayed_list):
                print("Invalid index. Try again.")
            elif displayed_list[index] != '*':
                print("This number has already been matched. Try again.")
            else:
                return index

#Check if selected indices match
def check_match(truth_list, displayed_list, index1, index2):
    if truth_list[index1] == truth_list[index2]:
        print(f"Match! Both indices contain {truth_list[index1]}.")
        displayed_list[index1] = truth_list[index1]
        displayed_list[index2] = truth_list[index2]
    else:
        print(f"Value at index {index1} is {truth_list[index1]}")
        print(f"Value at index {index2} is {truth_list[index2]}")
        print("No match. Try again.")
    input("Press Enter to continue...")

if __name__ == '__main__':
    main()