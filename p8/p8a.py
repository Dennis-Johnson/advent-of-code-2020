import re

def main():
    # with open("test.txt", "r") as f:
    with open(r"input.txt", "r") as f:
        lines = f.readlines()
    
    code = [()] * len(lines)
    executed = [False] * len(lines)
    
    for i in range(len(lines)):
        line = lines[i]
        
        matchObj = re.search(r"([a-z]+)\s([+-])([\d]+)", line)
        
        instruction = matchObj.group(1)
        sign = matchObj.group(2)
        num = int(matchObj.group(3))

        if sign == '-':
            num *= -1
        
        code[i] = (instruction, num)
    
    acc = 0
    line_no = 0
    for c in code:
        print(c)

    while True:
        # Repeated instruction
        if executed[line_no]:
            break
        
        instr, num = code[line_no]
        print(instr, num)    
        
        executed[line_no] = True

        if instr == "nop":
            line_no += 1
        elif instr == "acc":
            line_no += 1
            acc += num
        elif instr == "jmp":
            line_no += num
    
    print(acc)


if __name__ == "__main__":
    main()
