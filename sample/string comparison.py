
      # string comparison

s='sathiyanthan mu'
a= '10'

print(s.isalpha())  # true
print(s.isalnum())  # true
print(a.isalnum())  # true
print('2000' .isalnum())
print('sathya'.isdigit())
print('sathya'.isupper())
print('sathya'.islower())
       #search sub strings
print(s.endswith('than'))
print(s.startswith('yan'))
print(s.startswith('sat'))
print(s.find('yan'))
print(s.count('yan'))
print(s.count('a'))
print(s.endswith('u'))

        # converting the strings
s='PriyA'
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.replace('PriyA','sathya',))
print(s+' sathya')

s=input('enter the string')

print(s.upper())
print(s.swapcase())







