# how good is a student overall based on GPA?
def evaluate_performance(gpa_list):
    if not gpa_list:
        return "No data to evaluate"
    avg = sum(gpa_list) / len(gpa_list)
    if avg >= 3.5:
        return "Excellent"
    elif avg >= 3.0:
        return "Good"
    else:
        return "Needs Improvement"
