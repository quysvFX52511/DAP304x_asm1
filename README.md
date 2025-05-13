# Dự Án Chấm Điểm Bài Thi Học Sinh

## Github link
https://github.com/quysvFX52511/DAP304x_asm1

## Mô Tả Dự Án
Dự án này thực hiện việc chấm điểm cho bài thi của học sinh dựa trên một bộ câu trả lời đúng đã được xác định trước. Chương trình sẽ đọc dữ liệu từ các tệp `.txt` chứa thông tin học sinh và kết quả của họ, tính điểm cho từng học sinh, và xuất ra các thống kê như điểm trung bình, điểm cao nhất, điểm thấp nhất, cũng như phân tích câu hỏi nào bị bỏ qua hoặc sai nhiều nhất.

## Yêu Cầu
- Python 3.x
- Các thư viện: pandas, numpy
  - Cài đặt các thư viện bằng cách sử dụng `pip`:
    ```bash
    pip install pandas numpy
    ```

## Cài Đặt
1. **Cài Đặt Python**: Đảm bảo rằng bạn đã cài đặt Python phiên bản 3.x.
2. **Cài Đặt Các Thư Viện Cần Thiết**:
   - Mở terminal và chạy lệnh sau để cài đặt các thư viện cần thiết:
     ```bash
     pip install pandas numpy
     ```
3. **Tải Dự Án**: 
   - Tải hoặc clone mã nguồn dự án về máy tính của bạn từ GitHub.
   
   ```bash
   git clone https://github.com/username/project-name.git
   ```

## Cấu Trúc Dự Án
```
project-directory/
│
├── lastname_firstname_grade_the_exams.py   # Tệp Python chính để xử lý và chấm điểm
├── README.md                               # Tệp hướng dẫn này
└── requirements.txt                        # Các thư viện yêu cầu cho dự án
```

## Cách Sử Dụng

### 1. Đọc Dữ Liệu Từ Tệp
Chương trình yêu cầu một tệp `.txt` chứa thông tin bài làm của học sinh. Dữ liệu trong tệp phải có định dạng sau:
- Mỗi dòng tương ứng với một học sinh.
- Đầu tiên là mã số học sinh (bắt đầu bằng chữ "N" và tiếp theo là 8 chữ số).
- Các câu trả lời của học sinh sau dấu phẩy (có 25 câu hỏi trong mỗi bài thi).

### 2. Chạy Chương Trình
Chạy chương trình bằng cách sử dụng lệnh sau trong terminal:
```bash
python lastname_firstname_grade_the_exams.py
```

Khi chạy, chương trình sẽ yêu cầu bạn nhập tên tệp chứa dữ liệu lớp học (ví dụ: `class1` cho tệp `class1.txt`). Sau khi nhập tên tệp, chương trình sẽ tiến hành:
- Đọc tệp và kiểm tra tính hợp lệ của dữ liệu.
- Tính điểm cho từng học sinh.
- Phân tích và báo cáo các thống kê về điểm thi, bao gồm điểm cao nhất, thấp nhất, điểm trung bình, và câu hỏi bị bỏ qua hoặc sai nhiều nhất.
- Xuất kết quả vào một tệp mới với tên `class1_grades.txt`.

### 3. Báo Cáo Kết Quả
Sau khi chương trình hoàn tất, báo cáo sẽ được hiển thị trên màn hình và lưu vào tệp kết quả. Các thông tin trong báo cáo bao gồm:
- Số dòng dữ liệu hợp lệ và không hợp lệ.
- Tổng số học sinh đạt điểm cao.
- Các thống kê điểm thi (trung bình, cao nhất, thấp nhất, khoảng cách giữa các điểm).
- Các câu hỏi bị bỏ qua nhiều nhất và câu hỏi bị sai nhiều nhất.

## Các Hàm Chính
- **read_file(full_filename: str)**: Đọc dữ liệu từ tệp.
- **validate_student_id(student_id: str)**: Kiểm tra tính hợp lệ của mã học sinh.
- **validate_line(line: str)**: Kiểm tra tính hợp lệ của dòng dữ liệu.
- **calculate_score(answers: list[str], answer_key: list[str])**: Tính điểm cho học sinh.
- **analyze_questions(valid_data: list[list[str]], answer_key: list[str])**: Phân tích câu hỏi bị bỏ qua và sai nhiều nhất.
- **format_question_stats(stats: dict[int, int], total_students: int)**: Định dạng thống kê câu hỏi.

## Ghi Chú
- Nếu có bất kỳ lỗi nào khi mở tệp hoặc dữ liệu không hợp lệ, chương trình sẽ thông báo lỗi và yêu cầu bạn thử lại.
- Tệp kết quả sẽ được lưu dưới định dạng `class1_grades.txt` (với tên lớp học là tên tệp đầu vào).

## Cảm ơn!
Cảm ơn bạn đã sử dụng dự án này! Nếu bạn có bất kỳ câu hỏi nào hoặc gặp vấn đề, vui lòng mở issue trên GitHub để chúng tôi có thể hỗ trợ.
