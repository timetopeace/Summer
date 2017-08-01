def syntax(lexArray):
    formula = { 'start': {'while': 'while'},
                'while': {'id': 'condition', 'bool': 'condition'},
                'condition': {'do': 'do'},
                'do': {'id': 'id'},
                'id': {'left_sb': 'left_sb', 'colon': 'colon', 'semicolon': 'semicolon'},
                'colon': {'eq': 'do'},
                'left_sb': {'sym': 'sym', 'number': 'number'},
                'sym': {'number': 'number'},
                'number': {'comma': 'left_sb', 'right_sb': 'right_sb', 'sym': 'sym'},
                'right_sb': {'semicolon': 'semicolon'},
                'semicolon': {'error': 'error'},
                'error': {'error': 'error'}}

    currentState = 'start'
    result = 'REJECT'

    for currentWord in lexArray:
        try:
            currentState = formula[currentState][currentWord]
            if currentState == 'semicolon':
                result = 'ACCEPT'
        except:
            result = 'REJECT'
            break

    print(currentState)
    return result
