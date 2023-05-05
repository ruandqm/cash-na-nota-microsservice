def getEstablishment(ocrData):
    first_item = ocrData[0]
    index_of_newline = first_item.find("\n")
    # If at least one occurrence of "\n" is found in the first item of the array
    if index_of_newline != -1:
        # Extract the substring after the "\n" and check if it is "super" or "merc"
        term_after_newline = (
            first_item[index_of_newline + 1 :].strip().lower().split()[0]
        )
        if term_after_newline == "super" or term_after_newline == "merc":
            # If the term after "\n" is "super" or "merc", find the index of the second occurrence of "\n"
            index_of_second_newline = first_item.find("\n", index_of_newline + 1)
            # If the second occurrence of "\n" is found
            if index_of_second_newline != -1:
                # Return everything between the first and second occurrence of "\n"
                return first_item[
                    index_of_newline + 1 : index_of_second_newline
                ].strip()
            else:
                # If the second occurrence of "\n" is not found, return everything after the first occurrence of "\n"
                return first_item[index_of_newline + 1 :].strip()
        else:
            # If the term after "\n" is not "super" nor "merc", return everything before the first occurrence of "\n"
            return first_item[:index_of_newline].strip()
    else:
        # If no occurrence of "\n" is found in the first item of the array, return None
        return "Nao foi possivel identificar o estabelecimento"
