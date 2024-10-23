calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    x = 0
    y = False
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            x += 1
    if x >= 1:
        y = True
    return y

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cycl']))
print(calls)