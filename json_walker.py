import twitter1
import json


def main():
    '''
    Prints current "location"(values of wanted keys) in json file
    '''
    twt_main = twitter1.twitter1_main()
    fl = open("twitter1_data.json", encoding = 'utf-8')
    data = json.load(fl)
    fl.close()
    print(data)
    our_loc = data
    if type(our_loc) == list:
        numbers = [nums for nums in range(len(our_loc))]
        print("Enter which element of list you need(enter number from ", numbers, "): ")
        num_loc = int(input())
        our_loc = our_loc[num_loc]
        print(our_loc)

    while True:
        curr_loc = location(our_loc)
        if curr_loc == 'back':
            our_loc = data[1]
            print(our_loc)
        elif curr_loc == False:
            break
        elif curr_loc == 'unknown':
            print("There is no element with this name or this name is not a key")
        else:
            print(curr_loc)
            if type(curr_loc) == list:
                numbers = [nums for nums in range(len(curr_loc))]
                print("Enter which element of list you need(enter number from ", numbers, "): ")
                num_loc = int(input())
                our_loc = curr_loc[num_loc]
                print(our_loc)
            else:
                our_loc = curr_loc
        


def location(current_loc):
    '''
    Finds value of certain dict key if this key exists
    '''
    loc = input("Enter where you want to go now: ")
    if loc == 'back' or loc == "Back" or loc == "BACK":
        return 'back'
    elif len(loc) < 1:
        return False
    elif loc not in current_loc:
        return 'unknown'
    elif type(current_loc) == list:
        return current_loc[loc]
    elif type(current_loc) == dict and loc in current_loc:
        return current_loc[loc]
    else:
        return 'unknown'


main()