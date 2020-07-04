import homeauto.preprocessing as pp

lowerCasedString = pp.to_lower(['HELLO', 'My', 'name', 'IS', 'Arjun'])
print(lowerCasedString)

print(pp.remove_stop_words('this is my name arjun please', ['this']))