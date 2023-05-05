import re


def replace_comma(values):  # turns commas into dots for later conversion to float
    for i in range(len(values)):
        values[i] = values[i].replace(",", ".")
    return values


def find_monetary_values(arr):
    pattern = r"\d+[,.](?:\d{2})$"
    monetary_values = []
    for item in arr:
        match = re.search(pattern, item)
        if match:
            monetary_values.append(match.group())
    return monetary_values


def find_largest_repeated(arr):
    counts = {}
    largest_repeated = None
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] == 2:
            if largest_repeated is None or num > largest_repeated:
                largest_repeated = num
        elif counts[num] > 2 and num > largest_repeated:
            largest_repeated = num
    return largest_repeated


def find_total(arrayAdapted):
    arrayAdapted = list(map(float, arrayAdapted))
    change = True
    x = max(arrayAdapted)
    for i in range(len(arrayAdapted)):
        if arrayAdapted[i] != x and arrayAdapted[i] != 0:
            diff = x - arrayAdapted[i]
            if diff in arrayAdapted:
                return arrayAdapted[i]
            else:
                change = False
    if change == False:
        maxValue = find_largest_repeated(arrayAdapted)
        return maxValue
    else:
        return "Nao foi possivel identificar o valor da nota"


def getTotalValue(ocrData):
    values = find_monetary_values(ocrData)
    arrayAdapted = replace_comma(values)
    total = find_total(arrayAdapted)
    return total
