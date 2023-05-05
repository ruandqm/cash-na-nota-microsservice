import re


def getDate(ocrData):
    for item in ocrData:
        if re.match(r"\d{2}/\d{2}/\d{4}", item):
            return item
    return "Nao foi possivel identificar a data da compra"
