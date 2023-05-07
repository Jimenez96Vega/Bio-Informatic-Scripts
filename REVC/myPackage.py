# Global Variable
NUCLEOTIDS = ['A','C','G','T']

# This function converts a String into a List
def convert_to_List(list_x):
    aux = []
    aux[:0] = list_x.upper()
    return aux

# This function counts the frequency of nucleotids
def nucleotids_Frequency(list_x,masterList):
    for x in masterList:
        count = 0
        for nucleotid in list_x:
            if nucleotid == x:
                count = count + 1
                pass
            else:
                pass
        print(x,":", count)    
        pass
    return

# This function verifies if the List has correct DNA values
def format_is_Ok(list_x,masterList):
    for nucleotid in list_x:
        if nucleotid in masterList:
            pass
        else:
            return False
    return True

# This function replaces all "T" values to "U" values
def transcriber(list_x):
    for x in range(len(list_x)):
        if (list_x[x] == "T"):
            list_x[x] = "U"
            pass
    return list_x

def reversed_Complement(list_x):
    
    list_x.reverse()    
    
    for x in range(len(list_x)):
        if (list_x[x] == "A"):
            list_x[x] = "T"
            pass
        elif (list_x[x] == "T"):
            list_x[x] = "A"
            pass
        elif (list_x[x] == "C"):
            list_x[x] = "G"
            pass
        elif (list_x[x] == "G"):
            list_x[x] = "C"
            pass
    return list_x