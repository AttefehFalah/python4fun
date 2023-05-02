# Senior Solution
print("{:,}".format(100000000))
#
# More details about 'format' method:
# e.g. "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# special e.g.: ":,	==> Use a comma as a thousand separator"


# Junior Solution
def format_number(amount):
    amount_string = str(amount)[::-1]
    iterator = 1
    while 3 * iterator < len(amount_string):
        amount_string = amount_string[:3 * iterator + iterator - 1] + ',' + amount_string[3 * iterator + iterator - 1:]
        iterator += 1
    print(amount_string[::-1])


format_number(1000000)
