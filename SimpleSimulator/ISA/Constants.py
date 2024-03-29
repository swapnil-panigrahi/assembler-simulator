class Register:
    def __init__(self,address):
        self.address=address
        self.value=0b0000_0000_0000_0000
        
    def __repr__(self):
        return f'{bin(self.address)[2:].zfill(3)}'
    
    def __str__(self):
        return f'{bin(self.value)[2:].zfill(16)}'
    
class Memory:
    def __init__(self,var,value):
        self.var=var
        self.value=value        
        
        if Mem_block:
            self.address=Mem_block[-1]+0b1
        else:
            self.address=0b000_0000

    def __repr__(self):
        return f'{bin(self.value)[2:].zfill(7)}'
    
    def __str__(self):
        return f'{bin(self.address)[2:].zfill(7)}'

class Opcode:
    def __init__(self,opcode):
        self.opcode=opcode
    
    def __str__(self):
        return f'{bin(self.opcode)[2:].zfill(5)}'

class Flag(Register):
    def __init__(self,address):
        super().__init__(address)
        
    def overflow(self):
        self.value |= 0b0000_0000_0000_1000
    
    def less_than(self):
        self.value |= 0b0000_0000_0000_0100
    
    def greater_than(self):
        self.value |= 0b0000_0000_0000_0010
    
    def equal(self):
        self.value |= 0b0000_0000_0000_0001
        
R0=Register(0b000)
R1=Register(0b001)
R2=Register(0b010)
R3=Register(0b011)
R4=Register(0b100)
R5=Register(0b101)
R6=Register(0b110)

FLAGS=Flag(0b111)

Reg=[R0,R1,R2,R3,R4,R5,R6,FLAGS]

Mem_block=[]
Mem={}

Instructions=['var','add','sub','mov','ld','str','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']

def decode_register(encode):
    if encode=='000':
        return R0
    elif encode=='001':
        return R1
    elif encode=='010':
        return R2
    elif encode=='011':
        return R3
    elif encode=='100':
        return R4
    elif encode=='101':
        return R5
    elif encode=='110':
        return R6
    elif encode=='111':
        return FLAGS
    
def decode_memory(encode):
    if encode in Mem:
        return Mem[encode]
    else:
        Mem[encode]=0
        Mem_block.append(encode)