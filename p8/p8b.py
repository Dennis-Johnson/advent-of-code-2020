import re

def main():
    #with open("test.txt", "r") as f:
    with open(r"input.txt", "r") as f:
        lines = f.readlines()
    
    code = [()] * len(lines)
    
    for i in range(len(lines)):
        line = lines[i]
        
        matchObj = re.search(r"([a-z]+)\s([+-])([\d]+)", line)
        
        instruction = matchObj.group(1)
        sign = matchObj.group(2)
        num = int(matchObj.group(3))

        if sign == '-':
            num *= -1
        
        code[i] = (instruction, num)
    
    # Find all indices of nop or jmp in code:
    jmp_indices = [i for i, tup in enumerate(code) if tup[0] == "jmp"]
    nop_indices = [i for i, tup in enumerate(code) if tup[0] == "nop"]
    
    terminated = False

    for i in jmp_indices:
        old_instr, num = code[i]
        replaced = ("nop", num)

        new_code = list(code)
        new_code[i] = replaced
      
        t, acc = run(new_code)
        
        if t: 
            terminated = True
            print(acc, terminated)   
            break
    
    if not terminated:
        for i in nop_indices:
            old_instr, num = code[i]
            replaced = ("jmp", num)

            new_code = list(code)
            new_code[i] = replaced
          
            t, acc = run(new_code)
            
            if t: 
                terminated = True
                print(acc, terminated)   
                break
    

def run(code):
    acc = 0
    line_no = 0
    terminated = False
    
    executed = [False] * len(code)
    
    while True:
        if not 0 <= line_no < len(code):
            return False, 0

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
        elif instr == "end":
            terminated = True
            break

    return terminated, acc


if __name__ == "__main__":
    main()
