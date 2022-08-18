import Search

Length = 100
begin = 0
end = 1000

try:
    usr = int(input("Enter some number (0-1000):"))
except ValueError:
    print("You've typed symbol!")
    exit(-1)

Array = Search.GenerateArray(Length, begin, end)
Search.AdvSearch(Array, usr)
