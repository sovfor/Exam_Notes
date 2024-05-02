from datetime import date as dt
count = 0

isEnd = False

def add(count):
    try:
        arr1 = []
        file = open("Notes.csv","r")
        
        
        for i in file:
            arr1.append(i.split(";"))
        count = int(arr1[-1][0]) + 1
        file.close()
        
    except Exception:
        pass
    
    arrArr = []
    string = ""
    arrArr.append(count)
    
    print("Введите заголовок")
    arrArr.append(input()) 
    
    arrArr.append(dt.today())
    
    print("Введите текст")
    arrArr.append(input())
    
    
    
    
    
    for i in range(3):
            string += str(arrArr[i])
            string += ";"
    string += str(arrArr[3])
    
    
    file = open("Notes.csv","a")
    file.write(string)
    file.write("\n")
    file.close()
    
    count += 1
            
def read():
    
    try:
        arr = []
        file = open("Notes.csv","r")
        
        
        for i in file:
            arr.append(i.split(";"))
        file.close()
    except Exception:
        print("Файла не существует")
        
    
    return arr
        

        
def toMap(arr = read()):

    map_ = {}
    
    for i in arr:
        array = []
        
        
        for j in range(1,4):
            array.append(i[j]) 
        if arr != []:
            map_[str(i[0])] = array
            

    return map_
    
    
def printNote(id): 
    map_ = toMap()
    try:  
        arr = map_.get(str(id))    
    
        print(arr[1])
        print(arr[0] + ":")
        print(arr[2])
        print()
    except Exception:
        print("Введён неправильно номер заметки")
    
def printNotes():
    map_ = toMap()
    
    for i in map_:
        printNote(i)   
    
def rewrite(id,name = None,note = None):
    try:
        map_ = toMap()
       
        if name != None:
            map_[str(id)][0] = name
        if note != None:
            map_[str(id)][2] = note
        
        if name != None or note != None:
            map_[str(id)][1] = dt.today()


        file = open("Notes.csv","w")

    
        for i in map_:
            string = ""
        
            for j in range(2):
                string+= str(map_[str(i)][j])
                string += ";"
            string += str(map_[str(i)][-1])
            file.write(str(i) + ";" + string )
    except Exception:
        print("В файле нет заметки с таким индексом")
    
def printByData(date,isFind = False):
    map_ = toMap()
    
    
        
    for i in map_:
        arr = map_[i]
        
        if arr[1] == date:
            printNote(i)
            
            isFind = True
        
    if not isFind:
        print("Заметки с данной датой не найдены")
                
def deledteNote(id, size = 0,count = 0):
    map_ = toMap()
    
    for j in map_:
        size += 1
    
    
    file = open("Notes.csv","w")
    
    
    for i in map_:
        
        if i != str(id):    
            
            string = ""

            for j in range(2):
                string+= map_[str(i)][j]
                string += ";"
            string += map_[str(i)][-1]
            file.write(str(count) + ";" + string)
            
            if count <= size:
                count += 1
    
    file.close()



print("Введите:")
print("1, что бы добавить заметку")
print("2, что бы удалить заметку")
print("3, что бы изменить заметку")
print("4, что бы вывести заметку")
print("5, что бы вывести весь список заметок")
print("6, что бы вывести заметки по определённой дате")

    
num = input("\n")
    
    
    
if num == "1":
    add(count)
    print()

elif num == "2":
    deledteNote(input("Какую заметку вы хотите удалить? \n"))
    print()
    
elif num == "3":
            
    if input("Если вы хотите изменить имя заметки, введите один, иначе любой символ \n") == "1":
        name = input("Введите имя заметки: \n")
        print()
    else:
        name = None
    if input("Если вы хотите изменить текст заметки, введите один, иначе любой символ \n") == "1":
        note = input("Введите текст заметки: \n")
        print()
    else:
            note = None
                
    rewrite(input("Введите номер заметки \n"),name,note)
        
elif num == "4":
            
    id = input("Введите номер заметки \n")
    print()
            
    printNote(id)
            

elif num == "5":
    print()
    printNotes()
            

elif num == "6":
            
    printByData(input("Введите дату создания/последнего изменения заметки в формате ГГГГ-ММ-ДД \n"))
    print()
            


