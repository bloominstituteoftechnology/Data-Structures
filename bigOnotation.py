def find_name(name, phone_book):
    a = 2
    b = 10**a
    c = 3 + 4
    for person in phone_book:
        if name == person:
            print('hello')
​
    for person in phone_book:
        if name == person:
            return True
​
name = "Kim"
phone_book = ["Oliver", "BobbyG", "Tim", "Dan", "Oliver", "Kim"]
​
# O(n + n) --> O(n)
​
def find_name(austin_phone_book, philly_phone_book):
    for austinite in austin_phone_book:
        print(austinite)
​
    c = 3 + 4
​
    for austinite in austin_phone_book:
        for philadelphian in philly_phone_book:
            if austinite == philadelphian:
                return True
​
​
​
austin_phone_book = ["Oliver", "BobbyG", "Tim", "Dan", "Oliver", "Kim"]
philly_phone_book = ["Patrick", "Brandy", "Soosh", "Jen", "Carl", "Ace"]
"""
O(n^2)
O(16)
​
O(6 + 1 + 36)
O(n + 1 + n^2)
# when list gets to 10000
O(100000000)
O(n^2)
"""
