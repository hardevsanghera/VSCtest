import sys
import requests
#print(sys.version)
print(sys.executable)
print('Hardev')


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Corey'))
r = requests.get('https://coreyms.com')
print(r.status_code)

name = input("Your Name? ")
print("Hello,", name)
print("Hello again, ", name)