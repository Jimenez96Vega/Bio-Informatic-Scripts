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

