import re
PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
def valid_card_number(sequence):
    match = re.match(PATTERN,sequence)
    if match == None:
        return False
    for group in match.groups:
        if group[0] * 4 == group:
            return False
    return True
