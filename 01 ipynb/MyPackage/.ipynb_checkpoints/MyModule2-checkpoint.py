#
# ---- zweites Modul
#
def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        count += 1
        index = string.find(sub_string)
        if index == -1: 
            break
        else:
            string = string[index+1:]
                  
    return (count)


string = str(input("String:").strip())
sub_string = str(input("Sub-String:").strip())
    
count = count_substring(string, sub_string)
print (count)