n = int(input())
cards = list(map(int, input().split()))
cards.sort()
cardslen = len(cards)
sereja_score = 0
dima_score = 0
for card in cards:
    sereja_score = sereja_score + cards.pop()
    dima_score = dima_score + cards.pop()
print(sereja_score , dima_score )
print(cards)
