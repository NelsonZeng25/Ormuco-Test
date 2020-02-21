import re

# This is a modified version of the function (is_canonical()) found in Appendix B of https://www.python.org/dev/peps/pep-0440/
# It checks if the input string is a valid version string format
def is_valid(version):
    if version == None:
        return False
    return re.search(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))(((a|b|rc)(0|[1-9][0-9]*))|(\.(0|[1-9][0-9]*)))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None

def compare(version1, version2):
    # We start by checking if both inputs are valid version strings using the is_valid() function
    if not is_valid(version1) and not is_valid(version2):
        return "Invalid version format for both versions"
    elif not is_valid(version1):
        return "Invalid version format for version 1"
    elif not is_valid(version2):
        return "Invalid version format for version 2"

    GREATER = version1 + " is greater than " + version2
    LESSER = version1 + " is lesser than " + version2
    EQUAL = version1 + " is equal to " + version2

    # Check if they're exactly the same
    if version1 == version2:
        return EQUAL

    # We split the strings with "." as the delimiters and evaluate each split element individually
    array1 = version1.split(".")
    array2 = version2.split(".")

    # We use the length of the array with the least elements
    length = len(array1) if len(array1) <= len(array2) else len(array2)

    # We iterate through both arrays check for specific cases
    for i in range(length):
        # Case 1: Both elements are numeric
        # Simply compare numbers and check which one is greater
        if array1[i].isnumeric() and array2[i].isnumeric():
            if (int(array1[i]) > int(array2[i])):
                return GREATER
            elif (int(array1[i]) < int(array2[i])):
                return LESSER

        # Case 2: One of them contains a pre-release string (i.e. a|b|rc)
            '''
            Since we know the format is (r"^[0-9]*(a|b|rc)[0-9]*$""), we can seperate this in 3 cases:
                1. We first compare the first number of each array
                2. Then, if they're the same, we check the "a|b|rc" of each array and
                    if one them contains a letter and the other doesn't, we know the other
                    is the greater version since having letters means it's a pre-release and
                    having no letters means it's a final releases
                    If they both have letters, simply compare them
                3. If they're still the same at this point, we check the numbers at the
                    end of the string and simply compare them
            '''
        elif any(u in "abrc" for u in array1[i]) or any(w in "abrc" for w in array2[i]):
            temp1 = re.search(r"^[0-9]+", array1[i])
            temp2 = re.search(r"^[0-9]+", array2[i])
            temp1 = int(temp1.group(0))
            temp2 = int(temp2.group(0))
            if temp1 > temp2:
                return GREATER
            elif temp1 < temp2:
                return LESSER

            temp1 = re.search(r"[abrc]+", array1[i])
            temp2 = re.search(r"[abrc]+", array2[i])
            if temp1 != None and temp2 == None:
                return LESSER
            elif temp1 == None and temp2 != None:
                return GREATER
            elif temp1.group(0) > temp2.group(0):
                return GREATER
            elif temp1.group(0) < temp2.group(0):
                return LESSER

            temp1 = re.search(r"[0-9]+$", array1[i])
            temp2 = re.search(r"[0-9]+$", array2[i])
            temp1 = int(temp1.group(0))
            temp2 = int(temp2.group(0))
            if temp1 > temp2:
                return GREATER
            elif temp1 < temp2:
                return LESSER

        # Case 3: One of them contains a "post"
            '''
            Since we know the format is (r"^post[0-9]*$") and "post" > "dev",
                1. If they both contain "post", we simply compare the numbers at the end
                2. If one contains "post" and the other has "dev", we follow "post" > "dev"
                3. If one contains "post" and the other is just numeric, we follow numeric > "post"
            '''
        elif "post" in array1[i] or "post" in array2[i]:
            if "post" in array1[i] and "post" in array2[i]:
                temp1 = int(array1[i][4:])
                temp2 = int(array2[i][4:])
                if temp1 > temp2:
                    return GREATER
                elif temp1 < temp2:
                    return LESSER

            elif ("post" in array1[i] and "dev" in array2[i]) or array1[i].isnumeric():
                return GREATER
            elif ("dev" in array1[i] and "post" in array2[i]) or array2[i].isnumeric():
                return LESSER

        # Case 4: One of them contains a "dev"
            '''
            Since we know the format is (r"^dev[0-9]*$") and "dev" < everything else,
                1. If they both contain "dev", we simply compare the numbers at the end
                2. If one contains "dev" and the other doesn't, we know the other is greater 
            '''
        elif "dev" in array1[i] or "dev" in array2[i]:
            if "dev" in array1[i] and "dev" in array2[i]:
                temp1 = int(array1[i][3:])
                temp2 = int(array2[i][3:])
                if temp1 > temp2:
                    return GREATER
                elif temp1 < temp2:
                    return LESSER

            elif "dev" not in array2[i]:
                return LESSER
            elif "dev" not in array1[i]:
                return GREATER

    # After going through the for loop, we check if one of the arrays is bigger than the other
    # The larger one is greater than the other and if they have the same length, it means they're equal
    if len(array1) > len(array2):
        return GREATER
    elif len(array1) < len(array2):
        return LESSER
    else:
        return EQUAL