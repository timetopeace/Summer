def get():
    with open('input.txt') as f:
        return f.read()
def set(result):
    with open('output.txt', 'w') as f:
        f.write(result)