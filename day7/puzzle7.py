card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
type_values = {'high card': 1, 'one pair': 2, 'two pairs': 3, 'three of a kind': 4, 'full house': 5, 'four of a kind': 6, 'five of a kind': 7}

def get_type(hand):
    number_of_same_cards = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
    for card in hand:
        number_of_same_cards[card] += 1
    if 5 in number_of_same_cards.values():
        return type_values["five of a kind"]
    elif 4 in number_of_same_cards.values():
        return type_values["four of a kind"]
    elif 3 in number_of_same_cards.values() and 2 in number_of_same_cards.values():
        return type_values["full house"]
    elif 3 in number_of_same_cards.values():
        return type_values["three of a kind"]
    elif list(number_of_same_cards.values()).count(2) == 2:
        return type_values["two pairs"]
    elif 2 in number_of_same_cards.values():
        return type_values["one pair"]
    else:
        return type_values["high card"]
    

def ordering_rule(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if card_values[card1] > card_values[card2]:
            return 1
        elif card_values[card1] < card_values[card2]:
            return 2
    return 0 


def compare_two_hands(hand1, hand2):
    if get_type(hand1) > get_type(hand2):
        return 1
    elif get_type(hand1) < get_type(hand2):
        return 2
    else:
        return ordering_rule(hand1, hand2)
    
def merge_sort(list):
    if len(list) == 1:
        return list
    else:
        return merge(merge_sort(list[:len(list)//2]), merge_sort(list[len(list)//2:]))

def merge(list1, list2):
    merged_list = []
    while len(list1) > 0 and len(list2) > 0:
        if compare_two_hands(list1[0], list2[0]) == 1:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    if len(list1) > 0:
        merged_list.extend(list1)
    else:
        merged_list.extend(list2)
    return merged_list
        

with open("input.txt") as f:
    hands = []
    bids = []
    for line in f.readlines():
        hand, bid = line.replace("\n", "").split(" ")
        hands.append(hand)
        bids.append(bid)
    bids = {hands[int(i)]:int(bid) for i, bid in enumerate(bids)}
    hands_sorted = merge_sort(hands)
    points = [(len(hands)-i)*bids[hand] for i, hand in enumerate(hands_sorted)]
    total_point = sum(points)
    
    print(hands_sorted)
    print(total_point)