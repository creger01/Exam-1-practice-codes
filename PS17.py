# the authors names are: Cadyn
def show_in_backwards(a,b):
    if a == b:
        print("Numbers are equal: there is no number BETWEEN them!")
    elif a < b:
        diff = b-a
        end_point = b
        for item in range(diff):
            end_point = end_point - 1
            print(end_point)

    else: #a>b
        diff = a-b
        end_point = a
        for item in range(diff):
            end_point = end_point - 1
            if end_point != a:
                print(end_point)

show_in_backwards(2,25)
