from SymModel import SymModel as sym


def trans(inputString):
    result = []
    for char in inputString:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            result.append(sym(char, 'LETTER'))
        elif '0' <= char <= '9':
            result.append(sym(char, 'NUM'))
        elif char == ' ':
            result.append(sym(char, 'SPACE'))
        elif char == ',':
            result.append(sym(char, 'COMMA'))
        elif char == '=':
            result.append(sym(char, 'EQ'))
        elif char == ':':
            result.append(sym(char, 'COLON'))
        elif char == ';':
            result.append(sym(char, 'SEMICOLON'))
        elif char == '[':
            result.append(sym(char, 'LEFT SB'))
        elif char == ']':
            result.append(sym(char, 'RIGHT SB'))
        elif char == '+' or char == '-':
            result.append(sym(char, 'SYM'))
        elif char == '_':
            result.append(sym(char, 'D_SPACE'))
        else:
            result.append(sym(char, 'ERROR'))
    return result
