#Contains methods that are to be used in the piratize file, and the various classes

from fractions import Fraction


"""General method that takes a string, s1, and returns the string after being
   translated to pirish. Couldn't find a great equivalent to Ruby's 
   talk_like_a_pirate gem, so I just covered some of the basics here"""
def translate_to_pirish(s1):
    s1 = s1.replace('gold', '')
    s1 = s1.replace('treasure', '')
    s1 = s1.replace('coin', '')
    s1 = s1.replace('coins', '')
    s1 = s1.replace('Hello', 'Ahoy')
    s1 = s1.replace('hello', 'ahoy')
    s1 = s1.replace('Hi', 'Yo-ho-ho')
    s1 = s1.replace('hi', 'yo-ho-ho')
    s1 = s1.replace('My', 'Me')
    s1 = s1.replace('my', 'me')
    s1 = s1.replace('Friend', 'Bucko')
    s1 = s1.replace('friend', 'bucko')
    s1 = s1.replace('Sir', 'Matey')
    s1 = s1.replace('sir', 'matey')
    s1 = s1.replace('Miss', 'Proud beauty')
    s1 = s1.replace('miss', 'proud beauty')
    s1 = s1.replace('Stranger', 'Scurvy Dog')
    s1 = s1.replace('stranger', 'scurvy dog')
    s1 = s1.replace('Officer', 'Foul blaggart')
    s1 = s1.replace('officer', 'foul blaggart')
    s1 = s1.replace('Where', 'Whar')
    s1 = s1.replace('where', 'whar')
    s1 = s1.replace('Is', 'Be')
    s1 = s1.replace('is', 'be')
    s1 = s1.replace('The', "Th'")
    s1 = s1.replace('the', "th'")
    s1 = s1.replace('You', 'Ye')
    s1 = s1.replace('you', 'ye')
    s1 = s1.replace('Old', 'Barnacle covered')
    s1 = s1.replace('old', 'barnacle covered')
    s1 = s1.replace('Happy', 'Grog-filled')
    s1 = s1.replace('happy', 'grog-filled')
    s1 = s1.replace('Nearby', 'Broadside')
    s1 = s1.replace('nearby', 'broadside')
    s1 = s1.replace('Restroom', 'Head')
    s1 = s1.replace('restroom', 'head')
    s1 = s1.replace('Restaurant', 'Galley')
    s1 = s1.replace('restaurant', 'galley')
    s1 = s1.replace('Hotel', 'Fleabag inn')
    s1 = s1.replace('hotel', 'fleabagg inn')
    return s1
    
"""A method that takes a float and returns the nearest rational
   where 8 is the denominator. Fraction reduces the passed-in numbers
   though, so I left numerator and denominator commented out in case
   those would be better to use"""
def float_to_rational(f1):
    #numerator = int(round(f1 * 8))
    #denominator = 8
    return Fraction(int((round(f1*8))), 8)
    
"""A method that iterates through a list(array) and checks the type
   of each index. If it's a string, piratize the string. If it's a float,
   convert it to the Rational near 8"""
def process_array(list_1):
    temp_list = []
    for i in range(len(list_1)):
        if isinstance(list_1[i], basestring):
            #list_1[i] = translate_to_pirish(list_1[i])
            temp = translate_to_pirish(list_1[i])
            temp_list.append(temp)
        elif isinstance(list_1[i], float):
            #list_1[i] = float_to_rational(list_1[i])
            temp = float_to_rational(list_1[i])
            temp_list.append(temp)
    #return list_1
    return temp_list
    
test_list_1 = ["Hello my coin", "Where is the treasure"]
t1 =  process_array(test_list_1)
print t1

"""Should be a method that iterates through a dictionary(hash table) and does
   the same as process_array. In this case, I'm not sure what key we would be
   looking for, so not sure how to iterate through it without just repeating
   process_array """     
def process_hash(dict_1):
    return ''