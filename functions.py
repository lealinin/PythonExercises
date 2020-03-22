def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}')
    print('Welcome aboard!')


print('Start')
# positional arguments
greet_user('John', 'Smith')
# keyword arguments
greet_user(last_name='Morrissey', first_name='Steven')
# if you mix positional and keyword arguments
greet_user('Jerry', last_name='Salinger')
print('Finish')

