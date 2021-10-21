empty= 99999
puzzle=[[6,2,5],[1,empty,8],[4,7,3]]
def print_lines (n):
    print("|",n,end=" ")
def print_bars():
    print("\n -----------")
print_bars()
for row in puzzle:
    for x in row:
        if(x==empty):
            print("|   ",end="")
        else:
            print_lines(x)
    print("|",end=" ")
    print_bars()

