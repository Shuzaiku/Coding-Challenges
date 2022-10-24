# 15 / 15 submission
instructions = input()
start_idx = 0

actions = {
    '+': " tighten ",
    '-': " loosen "
}

for i in range(1, len(instructions)):
    if (instructions[i-1].isdigit() and not instructions[i].isdigit()) or i == len(instructions)-1:
        if i == len(instructions)-1:
            i += 1
        subbed = instructions[start_idx:i]
        symbol = subbed.find('+') != -1 and '+' or '-'
        print(subbed.replace(symbol, actions[symbol]))
        start_idx = i
