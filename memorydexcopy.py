def extractbin(begin,size):
    buff=""
    for c in range(0,size):
        buff+=chr(Byte(begin+c))
        
    f=open("test.dex","wb")
    f.write(buff)
    f.close()
    
extractbin(16진수시작메모리주소,16진수추출할데이터크기)