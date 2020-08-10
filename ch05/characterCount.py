message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
"""setdefault()は
cout["a"]=2とかと一緒"""
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
