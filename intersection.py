# Program for finding intersection of lines with determining conditions...
# Purpose is not to use external libraries
def write_file(IX, IY, array2, id, name):
    # User determine ID of new point.
    new_id = input("Enter ID for intersected point:")
    # Adding new point
    try:
        sr = id.index(new_id)
        print("Do you want to change values of", new_id, "\ny or n")
        sw = input("Y or N:")
        if sw == "y" or sw == "Y":
            # To be avoid of case-sensitivity...
            array2[sr] = [new_id, IX, IY, None]
            f = open(name, "w")
            f.seek(0)
            # Appropriate tab format is set.
            for i in range(len(array2)):
                f.write((array2[i][0]) + "\t" + str(array2[i][1]) + "\t" +
                        str(array2[i][2]) + "\t" + str(array2[i][2]) + "\n")
            f.close()

    except ValueError:
        array2.append([new_id, IX, IY, None])
        f = open(name, "w")
        f.seek(0)
        for i in range(len(array2)):
            f.write((array2[i][0]) + "\t" + str(array2[i][1]) + "\t" +
                    str(array2[i][2]) + "\t" + str(array2[i][2]) + "\n")

        f.close()


def intr(x1, y1, x2, y2, x3, y3, x4, y4, id, name, array2):
    # Converting string into integer values...
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    x4 = float(x4)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    y4 = float(y4)
    # Conditions of lines...
    if x1 == x2 and y1 == y2 or x3 == x4 and y3 == y4:
        print("Points are not satisfy a line.")
        return intr(x1, y1, x2, y2, x3, y3, x4, y4, id, name, array2)
    else:
        print("")
    if x4 - x3 == 0 and x2 - x1 == 0:
        m1 = float("inf")
        m2 = float("inf")
    elif x4 - x3 != 0 and x2 - x1 == 0:
        m1 = float("inf")
        m2 = (y4 - y3) / (x4 - x3)
    elif x4 - x3 == 0 and x2 - x1 != 0:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = float("inf")
    else:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
    try:
        # Mathematical function of finding intersection.
        T = (((y4 - y3) * (x3 - x1)) -
             ((y3 - y1) * (x4 - x3))) / (((y4 - y3) * (x2 - x1)) -
                                         ((y2 - y1) * (x4 - x3)))
        IX = x1 + (x2 - x1) * T
        IY = y1 + (y2 - y1) * T
        print("Intersection of X is:", format(IX, ".3f"),
              "Intersection of Y is:", format(IY, ".3f"))

        if m1 * m2 == -1:
            print("Lines are perpendicular.")
        else:
            print("")
        wrt = input("1 for write to the file or enter 2 for do not write.")
        if wrt == "1":
            return write_file(IX, IY, array2, id, name)
        else:
            print("")
    # Conditions of zero division error...
    except ZeroDivisionError:
        y11 = m1 * (2 - x1) + y1
        y22 = m2 * (2 - x3) + y3
        # Conditions according to tangent.
        if y11 == y22:
            print("Lines are overlapped.")
        else:
            print("Lines are parallel.")


def file1():
    name = input("Enter the filename:")
    try:
        Fileop = open(name, "r")
        # Catching the error of wrong named file.

    except FileNotFoundError:
        print("File is not found.")
        return file1()

    array = Fileop.readlines()
    array2 = [x.split() for x in array]
    Fileop.close()
    i = 0
    id = []
    while len(array2) > i:
        id.append(array2[i][0])
        i += 1
    try:
        # Adding identifications to the list in string format
        # (Converted to float for calculations again at line 30-37)
        id1 = input("Enter the 1. ID:")
        id2 = input("Enter the 2. ID:")
        id3 = input("Enter the 3. ID:")
        id4 = input("Enter the 4. ID:")
        id11 = id.index(id1)
        id22 = id.index(id2)
        id33 = id.index(id3)
        id44 = id.index(id4)
    except ValueError:
        return file1()
    # Assigning values of x and y to the point list.
    x1 = array2[id11][1]
    y1 = array2[id11][2]

    x2 = array2[id22][1]
    y2 = array2[id22][2]

    x3 = array2[id33][1]
    y3 = array2[id33][2]

    x4 = array2[id44][1]
    y4 = array2[id44][2]
    intr(x1, y1, x2, y2, x3, y3, x4, y4, id, name, array2)


file1()
