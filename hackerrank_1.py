
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     list = []
#     abc = []

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(k+1):
#             if x+y+z !=n:
#                 abc=[i,j,k]
#                 list.append([i,j,k])
            
# print(list)




if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = []
    abc = []
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z]
                    output.append(abc)
print(output);    