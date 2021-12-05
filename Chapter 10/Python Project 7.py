import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)

try:
    nameFile = input("Masukkan nama file : ")    
    file = open(path + "/" + nameFile,'r')
    caesar = int(input("Masukkan n sandi untuk decode caesar : "))
    listTeks = list(file.readline())

    result = ""
    for charTeks in listTeks:
        if(charTeks.isalpha()):
            hurufAscii  = ord(charTeks)
            indexAplha  = hurufAscii - ord("A")
            newIndex    = (indexAplha - caesar) % 26
            newCaesar   = newIndex + ord("A")
            newChar     = chr(newCaesar)
            result += newChar 
        else:
            result += charTeks
        
        
    resultFile = open(path + '/ResultDecodeCaesar.txt','w')
    resultFile.write(result)
    resultFile.close

except FileNotFoundError:
    print('file tidak ada')