# Author: Jimenez Vega, Isaac Daniel

# Importing packages
from myPackage import *

# Input String
dnaString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Converting String to List with the correct format
dnaString = convert_to_List(dnaString)

# Verifing if list format is ok
print(format_is_Ok(dnaString,NUCLEOTIDS))

# Counting the frequency of nucleotids appearing
nucleotids_Frequency(dnaString,NUCLEOTIDS)