def getCode(ocrData):
    for i in range(len(ocrData)):
        # Check if the current item is a sequence of 44 digits
        if len(ocrData[i]) == 44 and ocrData[i].isdigit():
            return ocrData[i]
        # Check if the current item is a sequence of 4 digits
        if len(ocrData[i]) == 4 and ocrData[i].isdigit():
            numbers = [ocrData[i]]
            j = i + 1
            # Loop through the remaining items until they are no longer a sequence of 4 digits or the end of the ocrData is reached
            while j < len(ocrData) and len(ocrData[j]) == 4 and ocrData[j].isdigit():
                numbers.append(ocrData[j])
                j += 1
            if len(numbers) == 11:
                return "".join(numbers)
    return "Nao foi possivel identificar o codigo da nota"
