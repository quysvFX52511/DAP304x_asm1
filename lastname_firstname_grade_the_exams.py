
# run with
# python lastname_firstname_grade_the_exams.py
# lastname_firstname_grade_the_exams.py

# Import
import pandas as pd
import numpy as np
import re
from typing import List, Tuple, Dict

ANSWER_KEY = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" # Câu trả lời đúng
CORRECT_POINTS = 4 # Điểm câu đúng
SKIP_POINTS = 0 # Điểm câu bỏ qua
WRONG_POINTS = -1 # Điểm câu sai
HIGH_SCORE_THRESHOLD = 80 # Ngưỡng điểm cao

# Task 1

def read_file(full_filename: str) -> List[str] | None:
    try:
        with open(full_filename, 'r') as file:
            print(f"Successfully opened {full_filename}")
            return file.readlines()
    except FileNotFoundError:
        print("File cannot be found.")
        return None


# Task 2
""" 
    Kiểm tra ID học sinh có hợp lệ hay không?
    Bắt đầu bằng chữ N
    Kế tiếp bằng 8 kí tự số
    Kết quả trả về True nếu hợp lệ, False nếu không hợp lệ
"""
def validate_student_id(student_id: str) -> bool:
    return bool(re.match(r'^N\d{8}$', student_id))

"""
    Kiểm tra tính hợp lệ của dòng
    len là 26 giá trị, ngăn cách bởi dấu phẩy
"""
def validate_line(line: str) -> tuple [bool, str]:
    parts = line.split(',')
    # Kiểm tra tính hợp lệ về độ dài
    if len(parts) != 26:
        return False, "Invalid line of data: does not contain exactly 26 values:"
    # Kiểm tra tính hợp lệ về mã học sinh
    if not validate_student_id(parts[0]):
        return False, "N# is invalid"
    return True, ""

# Task 3
""" 
    Tính điểm cho học sinh
    +4 điểm cho mỗi câu trả lời đúng 
    0 điểm cho mỗi câu trả lời bị bỏ qua 
    -1 điểm cho mỗi câu trả lời sai
"""
def calculate_score(answers: list[str], answer_key: list[str]) -> int:
    score = 0
    for student_ans, correct_ans in zip(answers, answer_key):
        if not student_ans:
            score += SKIP_POINTS
        elif student_ans == correct_ans:
            score += CORRECT_POINTS
        else:
            score += WRONG_POINTS
    return score

"""
    Phân tích câu hỏi bị bỏ qua nhiều nhất và sai nhiều nhất
"""
def analyze_questions(valid_data: list[list[str]], answer_key: list[str]) -> tuple[dict[int, int], dict[int, int]]:
    skipped = {i: 0 for i in range(1, 26)}
    incorrect = {i: 0 for i in range(1, 26)}
    total_students = len(valid_data)
    
    for student_data in valid_data:
        answers = student_data[1:]
        for i, (student_ans, correct_ans) in enumerate(zip(answers, answer_key), 1):
            if not student_ans:
                skipped[i] += 1
            elif student_ans != correct_ans:
                incorrect[i] += 1
    return skipped, incorrect

"""
    Tìm ra câu hỏi bị sai hoặc bỏ qua nhiều nhất in ra kết quả gồm: câu hỏi - số lần - tỷ lệ
"""
def format_question_stats(stats: dict[int, int], total_students: int) -> str:
    max_count = max(stats.values())
    result = []
    for question, count in stats.items():
        if count == max_count:
            ratio = count / total_students
            result.append(f"{question} - {count} - {ratio:.2f}")
    return " ,".join(result)

# Task 4
def main():
    while True:
        # Lấy tên file
        filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
        full_filename = filename + ".txt"

        # Đọc và kiểm tra file
        lines = read_file(full_filename)
        if lines is None:
            print("File cannot be found.")
            continue

        print(f"Successfully opened {full_filename}")
        print("**** ANALYZING ****")

        # Xử lí dữ liệu
        valid_data = []
        invalid_count = 0
        answer_key_list = ANSWER_KEY.split(',')

        # Kiểm tra từng dòng dữ liệu
        for line in lines:
            line = line.strip()
            if not line:
                continue

            is_valid, error_msg = validate_line(line)
            if is_valid:
                valid_data.append(line.split(','))
            else:
                print(f"Invalid line of data: {error_msg}")
                print(line)
                invalid_count += 1

        # Tính điểm cho dữ liệu hợp lệ
        scores = []
        for student_data in valid_data:
            score = calculate_score(student_data[1:], answer_key_list)
            scores.append((student_data[0], score))

        # Sắp xếp theo ID học sinh
        scores.sort(key=lambda x: x[0])

        # Lấy danh sách điểm để tính thống kê
        score_values = [score for _, score in scores]

        # Tính toán thống kê
        high_scores = sum(1 for score in score_values if score > HIGH_SCORE_THRESHOLD)
        mean_score = np.mean(score_values)
        highest_score = max(score_values)
        lowest_score = min(score_values)
        score_range = highest_score - lowest_score
        median_score = np.median(score_values)

        # Phân tích câu hỏi
        skipped, incorrect = analyze_questions(valid_data, answer_key_list)
        skipped_stats = format_question_stats(skipped, len(valid_data))
        incorrect_stats = format_question_stats(incorrect, len(valid_data))

        # In báo cáo
        print("**** REPORT ****")
        print(f"Total valid lines of data: {len(valid_data)}")
        print(f"Total invalid lines of data: {invalid_count}")
        print(f"Total student of high scores: {high_scores}")
        print(f"Mean (average) score: {mean_score:.2f}")
        print(f"Highest score: {highest_score}")
        print(f"Lowest score: {lowest_score}")
        print(f"Range of scores: {score_range}")
        print(f"Median score: {median_score}")
        print(f"Question that most people skip: {skipped_stats}")
        print(f"Question that most people answer incorrectly: {incorrect_stats}")

        # Ghi kết quả vào file theo thứ tự ID học sinh
        output_filename = f"{filename}_grades.txt"
        with open(output_filename, 'w') as f:
            for student_id, score in scores:
                f.write(f"{student_id},{score}\n")

        break

if __name__ == "__main__":
    main()


