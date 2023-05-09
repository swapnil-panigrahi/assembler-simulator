from ISA import Constants as Const
from ISA import A
from ISA import B
from ISA import C
from ISA import D
from ISA import E
from ISA import F        

for i in Const.Reg:
    print(i.__repr__())

print(A.add("add R0 $100"))
print(A.sub("sub R1 R2 R3"))
print(B.movi("mov R1 $12"))
print(C.movr("mov R5 FLAGS"))
print(D.var("var xyz"))
print(D.load("ld R1 myvar"))
print(D.store("st R2 xyz"))