STARTLIST = '$'
ENDLIST = '"'
STARTOBJECT = '%'
KVSEPARATOR = '}'
ENDOBJECT = '*'
SEPARATOR = '@'
NUMBERPREFIX = '|'
TRUE = '-'
FALSE = '_'
NULL = '#'

SPECIAL = {STARTLIST, ENDLIST, STARTOBJECT, ENDOBJECT, KVSEPARATOR,
           SEPARATOR, NUMBERPREFIX, TRUE, FALSE, NULL}
REPLACE = {True: TRUE, False: FALSE, None: NULL}


def compress(data):
    t = type(data)
    if t is bool or t is None:
        return REPLACE[data]
    elif t is str:
        return data
    elif t is float or t is int:
        return NUMBERPREFIX + str(data)
    elif t is dict:
        return STARTOBJECT + compress_object(data) + ENDOBJECT
    elif t is list:
        return STARTLIST + compress_list(data) + ENDLIST
    else:
        return ''


def compress_object(d):
    result = []
    for k, v in d.items():
        result.append(k + KVSEPARATOR + compress(v))
    return SEPARATOR.join(result)


def compress_list(l):
    result = []
    for v in l:
        result.append(compress(v))
    return SEPARATOR.join(result)

'''
{
  "key": "value",
  "another key": [
    "a list",
    "of",
    {
      "values": "and",
      "objects": ["1", 2, 3]
    },
    377
  ],
  "still": true
}

{"key":"value","another key":["a list","of",{"values":"and","objects":["1",2,3]},377],"still":true}

%key}value@another key}$a list@of@%values}and@objects}$1@(2@(3"*(377"still@-*
'''
