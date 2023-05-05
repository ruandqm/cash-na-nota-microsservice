from shared import getCode, getDate, getEstablishment, getExtract, getTotalValue


def extractData(ocrResult):
    code = getCode.getCode(ocrResult)
    date = getDate.getDate(ocrResult)
    establishment = getEstablishment.getEstablishment(ocrResult)
    extact = getExtract.getExtract(ocrResult)
    totalValue = getTotalValue.getTotalValue(ocrResult)

    response = {
        "code": code,
        "date": date,
        "establishment": establishment,
        "extract": extact,
        "totalValue": totalValue,
    }

    return response
