def getExtract(ocrData):
    for i in range(len(ocrData)):
        if ocrData[i] == "Extrato":
            if i + 2 < len(ocrData):
                return " ".join(ocrData[i : i + 3])
    return "Nao foi possivel identificar o extrato da nota"
