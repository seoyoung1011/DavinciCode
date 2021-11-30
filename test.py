from GameEngine import *

for i in range(3):
    print(". ", end='')
    time.sleep(1)
print()
print("complete loading!")
time.sleep(1)
print()

p2 = person()
c2 = computer()
p2.code, c2.code = shuffle_card()
p2.start_sort()
c2.start_sort()
p2.print(); c2.print()
while(True):
    p2.guess(c2)
    c2.print()

"""
p1 = person()
c1 = computer()
p1.code, c1.code = shuffle_card()
p1.opencode = ["o", "o", "o", "o"]
c1.opencode = ["o", "o", "o", "o"]
print(f'{p1}\n{c1}')
p1.start_sort(); c1.start_sort()
p1.print(); c1.print()

p1.add_sort(); '''p1.opencode = ["o", "o", "o", "o", "o"]'''; print(p1)
p1.add_sort(); '''p1.opencode = ["o", "o", "o", "o", "o", "o"]'''; print(p1)
p1.opencode = ["o", "o", "o", "o", "o", "o"]
print(p1)
c1.add_sort(); '''c1.opencode = ["o", "o", "o", "o", "o"]'''; print(c1)
c1.add_sort(); '''c1.opencode = ["o", "o", "o", "o", "o", "o"]'''; print(c1)
c1.opencode = ["o", "o", "o", "o", "o", "o"]
print(c1)
"""


# b1 = person()
# b1.code = ["B0", "WJ", "W10", "B10"]
# b1.opencode = ["o", "o", "o", "o"]
# b1.start_sort()
# b1.print()
