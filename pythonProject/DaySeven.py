file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()



lines = []
fickleString = ""
safeCount = 0
for i in content:
    if i != "\n":
        fickleString += i
    else:
        lines.append(fickleString)
        fickleString = ""

for i in lines:
    array = []
    multiplyArray = []
    lineSum = 0
    colonIndex = i.index(":")
    lineSum = int(i[:colonIndex])
    equationVars = i[colonIndex + 2:]
    print(equationVars)
    tempString = ""
    for j in equationVars:
        if j != " ":
            tempString += j
        else:
            array.append(int(tempString))
            tempString = ""
    print(array)
    for l in array:
        multiplyArray.append(False)


    tempSum = 0
    for k in range(len(array) - 1):
        if k = 0:
            multiplyArray.index(False) = True
        if multiplyArray[k]:
            tempSum += array[k] + array[k + 1]
        else:
            tempSum += array[k] * array[k + 1]

            
    if tempSum == lineSum:
        safeCount += 1





