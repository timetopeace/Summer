import editData
from transliterator import trans as Transliterator
from lexical import lex
from  syntax import syntax

inputStr = editData.get()
transliteration = Transliterator(inputStr)
for i in transliteration:
    print(i.sym, ': ', i.s_type)
lexArray = lex(transliteration)
print(lexArray)
result = syntax(lexArray)
editData.set(result)