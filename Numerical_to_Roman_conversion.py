
# Online Python - IDE, Editor, Compiler, Interpreter
def convert_to_roman(n):
    roman=""
    a=n//100
    b=n%100
    if a<4:
        roman=roman+'C'*a
    elif a==5:
        roman=roman+'D'
    elif a==4:
        roman=roman+'CD'
    elif a==6:
        roman=roman+'DC'
    elif a>6 and a<9:
        roman=roman+'D'+'C'*(a-5)
    elif a==9:
        roman=roman+'CM'
    c=b//10
    d=b%10
    if c<4:
        roman=roman+'X'*c
    elif c==5:
        roman=roman+'L'
    elif c==4:
        roman=roman+'XL'
    elif c==6:
        roman=roman+'LX'
    elif c>6 and c<9:
        roman=roman+'L'+'X'*(c-5)
    elif c==9:
        roman=roman+'XC'
    if d<4:
        roman=roman+'I'*d
    elif d==5:
        roman=roman+'V'
    elif d==4:
        roman=roman+'IV'
    elif d==6:
        roman=roman+'VI'
    elif d>6 and d<9:
        roman=roman+'V'+'I'*(d-5)
    elif d==9:
        roman=roman+'IX'
    print(roman)


no = int(input('Enter a number: '))
if no==10:
    print("The Roman number is : X")
elif no==50:
    print("The Roman number is : L")
elif no==100:
    print("The Roman number is : C")
elif no==500:
    print("The Roman number is : D")
elif no==1000:
    print("The Roman number is : M")
else:
    convert_to_roman(no)

