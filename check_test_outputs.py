# take in two files

val = input("What number test: ")
file1 = open("tc" + str(val) + "_output.txt", "r")
file2 = open("tc" + str(val) + "_expected_output.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

for i in range(len(lines1)):
    if (lines1[i].strip() != lines2[i].strip()):
        print("Line " + str(i + 1) + " is different")
        print("Expected: " + lines2[i])
        print("Actual: " + lines1[i])