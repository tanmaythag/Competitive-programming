""" 
Generate All Binary Strings
if n=2 ['00', '01', '10', '11']
if n=3 ['000', '001', '010', '011', '100', '101', '110', '111']
if n=4 ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', 
           '1010', '1011', '1100', '1101', '1110', '1111'] """





def append_bits(x, L):
    return [x + element for element in    L]

def generate_bit(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (append_bits("0", generate_bit(n - 1)) + 
                append_bits("1", generate_bit(n - 1)))
                
print(generate_bit(4))