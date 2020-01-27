import re

def compare(version1, version2):
    if not is_canonical(version1) and not is_canonical(version2):
        return "Invalid version format for both versions"
    elif not is_canonical(version1):
        return "Invalid version format for version 1"
    elif not is_canonical(version2):
        return "Invalid version format for version 2"


    array1 = version1.split(".")
    array2 = version2.split(".")

    length = len(array1) if len(array1) <= len(array2) else len(array2)

    for i in range(length):
        if array1[i].isnumeric() and array2[i].isnumeric():
            if (int(array1[i]) > int(array2[i])):
                return version1 + " is greater than " + version2
            elif (int(array1[i]) < int(array2[i])):
                return version1 + " is lesser than " + version2

        elif any(u in "abrc" for u in array1[i]) or any(w in "abrc" for w in array2[i]):
            temp1 = re.search(r"^[0-9]+", array1[i])
            temp2 = re.search(r"^[0-9]+", array2[i])
            temp1 = int(temp1.group(0))
            temp2 = int(temp2.group(0))
            if temp1 > temp2:
                return version1 + " is greater than " + version2
            elif temp1 < temp2:
                return version1 + " is lesser than " + version2

            temp1 = re.search(r"[abrc]+", array1[i])
            temp2 = re.search(r"[abrc]+", array2[i])
            if temp1 != None and temp2 == None:
                return version1 + " is lesser than " + version2
            elif temp1 == None and temp2 != None:
                return version1 + " is greater than " + version2
            elif temp1.group(0) > temp2.group(0):
                return version1 + " is greater than " + version2
            elif temp1.group(0) < temp2.group(0):
                return version1 + " is lesser than " + version2

            temp1 = re.search(r"[0-9]+$", array1[i])
            temp2 = re.search(r"[0-9]+$", array2[i])
            temp1 = int(temp1.group(0))
            temp2 = int(temp2.group(0))
            if temp1 > temp2:
                return version1 + " is greater than " + version2
            elif temp1 < temp2:
                return version1 + " is lesser than " + version2

        elif "post" in array1[i] or "post" in array2[i]:
            if "post" in array1[i] and "post" in array2[i]:
                temp1 = int(array1[i][4:])
                temp2 = int(array2[i][4:])
                if temp1 > temp2:
                    return version1 + " is greater than " + version2
                elif temp1 < temp2:
                    return version1 + " is lesser than " + version2

            elif ("post" in array1[i] and "dev" in array2[i]) or array1[i].isnumeric():
                return version1 + " is greater than " + version2
            elif ("dev" in array1[i] and "post" in array2[i]) or array2[i].isnumeric():
                return version1 + " is lesser than " + version2

        elif "dev" in array1[i] or "dev" in array2[i]:
            if "dev" in array1[i] and "dev" in array2[i]:
                temp1 = int(array1[i][3:])
                temp2 = int(array2[i][3:])
                if temp1 > temp2:
                    return version1 + " is greater than " + version2
                elif temp1 < temp2:
                    return version1 + " is lesser than " + version2
            
            elif "dev" not in array2[i]:
                return version1 + " is lesser than " + version2
            elif "dev" not in array1[i]:
                return version1 + " is greater than " + version2

    if len(array1) > len(array2):
        return version1 + " is greater than " + version2
    elif len(array1) < len(array2):
        return version1 + " is lesser than " + version2
    else:
        return version1 + " is equal to " + version2


# This is a sligtly modified version of the function found in Appendix B of https://www.python.org/dev/peps/pep-0440/
# It checks if the input string is a valid version format
def is_canonical(version):
    return re.search(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*)){1,2}((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

version1 = "1.1a1.dev1"
version2 = "1.1a2"
print(compare(version1, version2))

# print(is_canonical("1.0.1a1"))
# print(is_canonical("1.0"))
# print(is_canonical("1.0a2.dev456"))
