# JSON = JavaScript Objecct Notation

import json # imported json from the python library

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Tim",
                "age": 21,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Joe",
                "age": 33,
                "full-time": false
            }
        ]
    }
'''

data  = json.loads(json_string)
print(data) # prints all data but in Python dictionary
print(data['students']) # Prints using 'students' key
print(data['students'][0]) # Prints using 'students' key from first index (0 = 1, 1 = 2)
