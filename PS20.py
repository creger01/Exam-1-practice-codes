#the authors names are: Cadyn
def function(grade):
    if 93 <= grade <= 100:
        print("A")
    elif 90 <= grade <= 92:
        print("A-")
    elif 87  <= grade <= 89:
        print("B+")
    elif 83 <= grade <= 86:
        print("B")
    elif 80 <= grade <= 82:
        print("B-")
    elif 77 <= grade <= 79:
        print("C+")
    elif 73 <= grade <= 76:
        print("C")
    elif 70 <= grade <= 72:
        print("C-")
    elif 65 <= grade <= 69:
        print("D")
    elif 55 <= grade <= 64:
        print("D-")
    else:
        print("F")


function(30)
