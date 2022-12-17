import csv

def getLetterGrade(average_score: float) -> str:
    '''
    A function to get the equivalent letter grade of a given average score
    Parameters:
        average_score (float): The average score
    Returns:
        letter_grade (str): The equivalent letetr grade
    '''
    letter_grade = ""
    
    if average_score >= 90:
        letter_grade = "A"
    elif average_score >= 80 and average_score < 90:
        letter_grade = "B"
    elif average_score >= 70 and average_score < 80:
        letter_grade = "C"
    elif average_score >= 60 and average_score < 70:
        letter_grade = "D"
    elif average_score < 60:
        letter_grade = "F"
    
    return letter_grade

def main():
    input_file = "StudentInfo.tsv"
    output_file = "report.txt"
    total_midterm1, total_midterm2, total_final, student_count = 0.0, 0.0, 0.0, 0

    # Open output file for writing
    report_file = open(output_file, "w")
    # Open the file for reading
    csv_file = open(input_file)

    reader = csv.reader(csv_file, delimiter="\t")

    for row in reader:
        last_name = row[0]
        first_name = row[1]
        midterm1 = int(row[2])
        midterm2 = int(row[3])
        final = int(row[4])

        # Add to accumulators
        total_midterm1 += midterm1
        total_midterm2 += midterm2
        total_final += final
        student_count += 1

        average = float(midterm1 + midterm2 + final) / 3
        letter_grade = getLetterGrade(average)

        report_file.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")

    # Create report
    report_file.write("\n")
    average_midterm1 = total_midterm1 / student_count
    average_midterm2 = total_midterm2 / student_count
    average_final = total_final / student_count

    report_file.write(f"Averages: midterm1 {average_midterm1:.2f}, midterm2 {average_midterm2:.2f}, final {average_final:.2f}")

    csv_file.close()
    report_file.close()

if __name__ == "__main__":
    main()
