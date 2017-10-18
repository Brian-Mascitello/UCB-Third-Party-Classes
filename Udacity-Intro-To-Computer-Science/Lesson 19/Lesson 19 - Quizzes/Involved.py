# Dictionaries of Dictionaries (of Dictionaries)

# The next several questions concern the data structure below for keeping
# track of Udacity's courses (where all of the values are strings):

#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

# For example,

courses = {
    'feb2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian',
                          'assistant': 'Andy'}},
    'apr2012': {'cs101': {'name': 'Building a Search Engine',
                          'teacher': 'Dave',
                          'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                          'teacher': 'Peter N.',
                          'assistant': 'Andy',
                          'prereq': 'cs101'},
                'cs253':
                    {'name': 'Web Application Engineering - Building a Blog',
                     'teacher': 'Steve',
                     'prereq': 'cs101'},
                'cs262':
                    {'name': 'Programming Languages - Building a Web Browser',
                     'teacher': 'Wes',
                     'assistant': 'Peter C.',
                     'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                          'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                          'teacher': 'Dave'}},
    'jan2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                          'teacher': 'Dorina'},
                'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                          'teacher': 'Jasper'},
                }
}

try_again = {'june2043': {'cs111': {'name': 'Historical Computers - Before Voice Activation', 'teacher': 'Scotty'},
                          'cs312': {'assistant': 'Amy', 'name': 'Build your own Time Machine', 'teacher': 'Melody'}},
             'apr2012': {'cs262': {'assistant': 'Peter C.', 'prereq': 'cs101',
                                   'name': 'Programming Languages - Building a Web Browser', 'teacher': 'Wes'},
                         'cs101': {'assistant': 'Sarah', 'name': 'Building a Search Engine', 'teacher': 'Dave'},
                         'cs253': {'prereq': 'cs101', 'name': 'Web Application Engineering - Building a Blog',
                                   'teacher': 'Steve'},
                         'cs373': {'name': 'Programming a Robotic Car', 'teacher': 'Sebastian'},
                         'cs212': {'assistant': 'Andy', 'prereq': 'cs101', 'name': 'The Design of Computer Programs',
                                   'teacher': 'Peter N.'},
                         'cs387': {'name': 'Applied Cryptography', 'teacher': 'Dave'}}, 'jan2044': {
        'cs003': {'assistant': 'Amy', 'name': 'Programming a Robotic Robotics Teacher', 'teacher': 'Jasper'},
        'cs001': {'name': 'Building a Quantum Holodeck', 'teacher': 'Dorina'},
        'cs312': {'assistant': 'Amy', 'name': 'Build your own Time Machine', 'teacher': 'Melody'}},
             'feb2012': {'cs101': {'assistant': 'Peter C.', 'name': 'Building a Search Engine', 'teacher': 'Dave'},
                         'cs373': {'assistant': 'Andy', 'name': 'Programming a Robotic Car', 'teacher': 'Sebastian'}}}


# For the following questions, you will find the
#         for <key> in <dictionary>:
#                    <block>
# construct useful. This loops through the key values in the Dictionary. For
# example, this procedure returns a list of all the courses offered in the given
# hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res


# [Double Gold Star] Define a procedure, involved(courses, person), that takes
# as input a courses structure and a person and returns a Dictionary that
# describes all the courses the person is involved in.  A person is involved
# in a course if they are a value for any property for the course.  The output
# Dictionary should have hexamesters as its keys, and each value should be a
# list of courses that are offered that hexamester (the courses in the list
# can be in any order).

def involved(courses, person):
    descriptions = dict()
    for hexamester in courses.keys():
        class_list = list()
        for classes in courses[hexamester].keys():
            if person in courses[hexamester][classes].values():
                class_list.append(classes)
        if class_list:
            descriptions[hexamester] = class_list
    return descriptions


# For example:

# print involved(courses, 'Dave')
# >>> {'apr2012': ['cs101', 'cs387'], 'feb2012': ['cs101']}

# print involved(courses, 'Peter C.')
# >>> {'apr2012': ['cs262'], 'feb2012': ['cs101']}

# print involved(courses, 'Dorina')
# >>> {'jan2044': ['cs001']}

# print involved(courses,'Peter')
# >>> {}

# print involved(courses,'Robotic')
# >>> {}

# print involved(courses, '')
# >>> {}

print(involved(courses, 'Dave'))

print(involved(courses, 'Peter C.'))

print(involved(courses, 'Dorina'))

print(involved(courses, 'Peter'))

print(involved(courses, 'Robotic'))

print(involved(courses, ''))

print(involved(try_again, 'Amy'))
# {'june2043': ['cs312'], 'jan2044': ['cs312', 'cs003']}

print(involved(try_again, 'Andy'))
# Incorrect. There was a TypeError running your procedure for the input 'Andy' in the dictionary...
