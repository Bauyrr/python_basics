with open('/Users/bauyrzanbakytzan/Desktop/python_basics /lab6/fignya.txt',"a") as txt:
    a = list(input("Write list: ").split())
    for i in a:
        txt.write(i + " ")
    