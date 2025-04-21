# figuring out attendance percentage
def attendance_percentage(present, total):
    if total == 0:
        return 0 
    return (present / total) * 100
