


def brainfuck_interpreter(code):
    memory = [0] * 30000
    pointer = 0
    output = ""

    loop_stack = []
    loop_dict = {}

    code_ptr = 0

    while code_ptr < len(code):
        command = code[code_ptr]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output += chr(memory[pointer])
        elif command == ',':

            pass
        elif command == '[':
            if memory[pointer] == 0:
    
                code_ptr = loop_dict[code_ptr]
            else:
 
                loop_stack.append(code_ptr)
        elif command == ']':
            if memory[pointer] != 0:

                code_ptr = loop_stack[-1] - 1
            else:

                loop_stack.pop()

        code_ptr += 1

    return output

if __name__ == "__main__":

    brainfuck_code = "-[--->+<]>-.[---->+++++<]>-.+.++++++++++.+[---->+<]>+++.-[--->++<]>-.++++++++++.+[---->+<]>+++.+[----->+<]>+.+.+++++.[---->+<]>+++.[->+++<]>+.-[->+++<]>.[->+++<]>++.[--->+<]>----.+++[->+++<]>++.++++++++.+++++.--------.-[--->+<]>--.+[->+++<]>+.++++++++.-[++>---<]>+.+[->+++<]>.++++++.+++++++.--------.---.+++++++++++++."
    output = brainfuck_interpreter(brainfuck_code)
    print(output)
