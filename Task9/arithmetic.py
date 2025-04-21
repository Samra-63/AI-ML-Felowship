# basic math stuff like percentage and grade 
def calculate_percentage(obtained, total):
    if total == 0:
        return 0  
    return (obtained / total) * 100
def classify_grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 80:
        return 'B'
    elif percent >= 70:
        return 'C'
    else:
        return 'D'
