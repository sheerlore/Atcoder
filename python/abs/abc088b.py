from sys import stdin

N = int(stdin.readline().rstrip())
cards = [int(x) for x in stdin.readline().rstrip().split()]
alice = 0
bob = 0

sorted_cards = sorted(cards, reverse=True)
for i in range(len(sorted_cards)):
    if i % 2 == 0:
        alice += sorted_cards[i]
    else:
        bob += sorted_cards[i]

print(alice - bob)