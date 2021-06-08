class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far' , self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

"""lists and definite loops - best pals"""

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')

"""looking inside lists"""
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])
Glenn

"""How long is a list"""
"""len() function takes a list as a parameter and returns the number of elementsi nhte list"""
x = list()
type(x)
<tyle 'list'>
dir(x)
[...'count'] """for making sure item is less than 4 digits"""
"""is something in a list"""
some = [1, 9, 21, 10, 16]
>>>9 in some
True
>>>15 in some
False
>>>20 not in some
True

"Best Friends: Strings and Lists"
>>>abc = 'With three words'
>>stuff = abc.split()
>>>print(stuff)
['With', 'three', 'words']
>>>print(len(stuff))
3
>>>print(stuff[0])
With

>>>print(stuff)
['With', 'three', 'words']
>>>for w in stuff :
    print(w)
...
With
Three
Words
>>>
"""Split breaks a string into parts and produces a list of strings. We think of these as words.
We can access a particular word or loop through all the words."""

line = 'A lot           of spaces'\
etc = line.split()
print(etc)
['A', 'lot', 'of', 'spaces']

line = 'first;second;third'
thing = line.split()
print(thing)
['first;second;third']
thing = line.split(';')
print(thing)
['first', 'second', 'third']

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
words = line.split()
print(words)
['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '9:14:16', '2008']

words = line.split()
email = words[1]
pieces = email.split('@')   ['stephen.marquard', '@uct.ac.za']
print(pieces[1])            'uct.ac.za' \

"Regular Expressions: Matching and Extracting Data"                   '' \
re.search()
re.findall()
"Fine-Tuning String Extraction"














