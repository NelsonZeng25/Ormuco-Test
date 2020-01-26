import re

def compare(version1, version2):
    if not (is_canonical(version1) and is_canonical(version2)):
        return "Invalid version format"

    array1 = version1.split(".")
    array2 = version2.split(".")

    length = len(array1) if len(array1) <= len(array2) else len(array2)

    for i in range(length):
        if array1[i].isnumeric() and array2[i].isnumeric():
            if (int(array1[i]) > int(array2[i])):
                return version1 + " is greater than " + version2
            elif (int(array1[i]) < int(array2[i])):
                return version1 + " is lesser than " + version2

        if i == 1:
            if any(u in "abrc" for u in array1[i]) or any(w in "abrc" for w in array2[i]):
                a = re.search(r"^[0-9]+", array1[i])
                b = re.search(r"^[0-9]+", array2[i])
                a = int(a.group(0))
                b = int(b.group(0))
                if a > b:
                    return version1 + " is greater than " + version2
                elif a < b:
                    return version1 + " is lesser than " + version2
                
                a = re.search(r"[abrc]+", array1[i])
                b = re.search(r"[abrc]+", array2[i])
                if a.group != None and b.group == None:
                    return version1 + " is greater than " + version2
                elif a.group == None and b.group != None:
                    return version1 + " is lesser than " + version2
                elif a.group(0) > b.group(0):
                    return version1 + " is greater than " + version2
                elif a.group(0) < b.group(0):
                    return version1 + " is lesser than " + version2
                
                a = re.search(r"[0-9]+$", array1[i])
                b = re.search(r"[0-9]+$", array2[i])
                a = int(a.group(0))
                b = int(b.group(0))
                if a > b:
                    return version1 + " is greater than " + version2
                elif a < b:
                    return version1 + " is lesser than " + version2

        if "dev" in array1[i] or "dev" in array2[i]:
            a = int(array1[i][3:])
            b = int(array2[i][3:])
            if a > b:
                return version1 + " is greater than " + version2
            elif a < b:
                return version1 + " is lesser than " + version2
        
        if "post" in array1[i] or "post" in array2[i]:
            a = int(array1[i][4:])
            b = int(array2[i][4:])
            if a > b:
                return version1 + " is greater than " + version2
            elif a < b:
                return version1 + " is lesser than " + version2

    if len(array1) > len(array2):
        return version1 + " is greater than " + version2
    elif len(array1) < len(array2):
        return version1 + " is lesser than " + version2
    else:
        return version1 + " is equal to " + version2
        

# This function was found in Appendix B of https://www.python.org/dev/peps/pep-0440/
# It checks if the input string is a valid version format
def is_canonical(version):
    return re.search(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

print(is_canonical("11.1.2"))
print(is_canonical("1.0"))
print(is_canonical("1.0a2.dev456"))