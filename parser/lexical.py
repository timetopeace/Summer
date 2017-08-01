
def lex(charArr):
    result = []
    reserved = ['absolute', 'and', 'array', 'as', 'asm', 'begin', 'case', 'class',
                'const', 'constructor', 'destructor', 'dispinterface', 'dispose',
                'div', 'do', 'downto', 'end', 'except', 'exit', 'exports', 'file',
                'finalization', 'finally', 'for', 'function', 'goto', 'implementation',
                'in', 'inherited', 'initialization', 'inline', 'interface', 'is', 'label',
                'library', 'mod', 'new	', 'nil', 'not', 'object', 'of', 'on', 'operator',
                'or', 'out', 'packed', 'procedure', 'program', 'property', 'raise', 'record',
                'reintroduce', 'repeat', 'resourcestring', 'self', 'set', 'shl', 'shr', 'string',
                'threadvar', 'to', 'try', 'type', 'unit', 'until', 'uses', 'var', 'while', 'with', 'xor']
    word = ''
    num = 0
    f_d_spase = False
    for item in charArr:
        if item.s_type == 'LETTER':
            if num != 0:
                result.append('number')
                num = 0
            word += item.sym
            f_d_spase = True
            continue

        if item.s_type == 'NUM':
            if word != '':
                word += item.sym
            else:
                if num == 0:
                    num = int(item.sym)
                else:
                    num = int(str(num) + item.sym)
            continue
        if item.s_type == 'D_SPACE':
            if num != 0:
                result.append('number')
                num = 0
            word += '_'
            continue

        if item.s_type in ['SPACE','LEFT SB', 'RIGHT SB', 'SEMICOLON','EQ','COLON','SYM', 'COMMA']:
            if num != 0:
                result.append('number')
                num = 0

            if word != '':
                if not f_d_spase:
                    result.append('error')
                    break
                else:
                    if word.lower() in ['while', 'do']:
                        result.append(word.lower())
                    elif word.lower() in ['true', 'false']:
                        result.append('bool')
                    elif word.lower() in reserved:
                        result.append('keyword')
                    else:
                        result.append('id')
                        f_d_spase = False

            if item.s_type == 'LEFT SB':
                result.append('left_sb')
            if item.s_type == 'RIGHT SB':
                result.append('right_sb')
            if item.s_type == 'SEMICOLON':
                result.append('semicolon')
            if item.s_type == 'COLON':
                result.append('colon')
            if item.s_type == 'EQ':
                result.append('eq')
            if item.s_type == 'SYM':
                result.append('sym')
            if item.s_type == 'COMMA':
                result.append('comma')

            word = ''
            f_d_spase = False
            continue
        result.append('error')
        print('Invalid symbol')
        break
    return result
