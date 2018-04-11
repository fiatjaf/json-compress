var STARTLIST = '$'
var ENDLIST = '"'
var STARTOBJECT = '%'
var KVSEPARATOR = '}'
var ENDOBJECT = '*'
var SEPARATOR = '@'
var NUMBERPREFIX = '|'
var TRUE = '-'
var FALSE = '_'
var NULL = '#'


function decompress(input) {
  var curr = input.split('')

  for (var i = 0; i < input.length; i++) {
    if (input[i] === STARTOBJECT) {
      curr[i] = '{'
    } else if (input[i] === ENDOBJECT) {
      
    }
  }
