# OOP-with-Python
#Academic curriculum in UTDallas

#Hamming Distance Function (Non-dynamic)
# def hammingdist(str1, str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#     count = 0
#     for i in range(0, len(str1)-1):
#         if str1[i] == str2[i]:
#             pass
#         else:
#             count = count+1
#     return count

#################################################
####Hamming Distance Function (Dynamic)##########
#################################################
def hammingdist(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    s1 = len(string1)
    s2 = len(string2)
    m = [[0 for x in range(s2+1)] for y in range(s1+1)] 

    for i in range(s1+1):
        m[i][0] = i
    for j in range(s2+1):
        m[0][j] = j

    for i in range(1,s1+1):
        for j in range(1,s2+1):
            m[i][j] = min(m[i-1][j-1] + (0 if string1[i-1]==string2[j-1] else 2), m[i-1][j] + 1, m[i][j-1] + 1)
    return(m[i][j])
    print(m[i][j])
    
    
###################################
######Edit Distance Function#######
###################################
def editdist(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    s1 = len(string1)
    s2 = len(string2)
    m = [[0 for x in range(s2+1)] for y in range(s1+1)] 

    for i in range(s1+1):
        m[i][0] = i
    for j in range(s2+1):
        m[0][j] = j

    for i in range(1,s1+1):
        for j in range(1,s2+1):
            m[i][j] = min(m[i-1][j-1] + (0 if string1[i-1]==string2[j-1] else 1), m[i-1][j] + 1, m[i][j-1] + 1)
    return(m[i][j])
    print(m[i][j])

# editdist('Dirrte', 'Dorte')
# editdist("Anny", "Hanne")


##################################################
#######Function for interection of lists##########
##################################################
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 



################################################
####################Main module#################
################################################
name = input("Enter a name: ")
legal_names = ['Thor', 'Bjork', 'Bailey', 'Anders', 'Bent', 'Bjarne', 'Bjorn', 'Claus', 'Emil', 'Finn', 'Jakob', 'Karen', 'Julie', 'Johanne', 'Anna', 'Anne', 'Bente', 'Eva', 'Helene', 'Ida', 'Inge', 'Susanne', 'Sofie', 'Rikkie', 'Pia', 'Torben', 'Soren', 'Rune', 'Rasmus', 'Per', 'Michael', 'Mads', 'Hanne', 'Dorte']

if name in legal_names:
    print('It is an appropriate Danish name')
else:
    edit_list = [None] * len(legal_names)
    hamming_list = [None] * len(legal_names)

#Creating list using edit distance function
for i in range(len(legal_names)):
    edit_list[i] = editdist(name, legal_names[i])
    edit_list = list(edit_list)
if min(edit_list) <= len(name):
    minimum_index = [i for i,j in enumerate(edit_list) if j == min(edit_list)]
    legal_names_edit = [legal_names[i] for i in minimum_index]

#Creating list using hamming distance function
for j in range(len(legal_names)):
    hamming_list[j] = hammingdist(name, legal_names[j])
if min(hamming_list) <= len(name):
    minimum_index = [i for i,j in enumerate(hamming_list) if j == min(hamming_list)]
    legal_names_hamming = [legal_names[i] for i in minimum_index]

#Creating final list with intersection of edit and hamming list
final_list = intersection(legal_names_edit, legal_names_hamming)

if final_list == []:
    print("No close matches found")
else:
    print("Suggested names are: ")
    print(final_list)
