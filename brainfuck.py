

def execute(s: str):
    code_pos = 0
    mem_pos = 0
    mem = [0] * 30_000
    while (code_pos < len(s)):
        if s[code_pos] == '>':
            mem_pos += 1
        elif s[code_pos] == '<':
            mem_pos -= 1
        elif s[code_pos] == '+':
            mem[mem_pos] += 1
        elif s[code_pos] == '-':
            mem[mem_pos] -= 1
        elif s[code_pos] == '.':
            print(chr(mem[mem_pos]), sep='', end='')
        elif s[code_pos] == ',':
            mem[mem_pos] = ord(input()[0])
        elif s[code_pos] == '[':
            if mem[mem_pos] == 0:
                code_pos = s.find(']', code_pos) + 1
        elif s[code_pos] == ']':
            if mem[mem_pos] != 0:
                code_pos -= s[:code_pos][::-1].find('[', 0) + 1
        code_pos += 1

if __name__ == '__main__':
    execute("""
    +++++++++++++++++++++++++++++++++++++++++++++
    +++++++++++++++++++++++++++.+++++++++++++++++
    ++++++++++++.+++++++..+++.-------------------
    ---------------------------------------------
    ---------------.+++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++.++++++++++++++++++
    ++++++.+++.------.--------.------------------
    ---------------------------------------------
    ----.-----------------------."""
         )
    execute("""
    ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++
    .>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.
    ------.--------.>+.>.""")