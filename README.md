# RASA


Tải thư viện Rasa:

Lệnh tải phiên bản mới nhất:

pip install rasa

Lệnh tải phiên bản cụ thể:

pip install rasa==3.1

Hệ thống dùng Rasa phiên bản như sau:

Rasa Version      :         3.1.0

Minimum Compatible Version: 3.0.0

Rasa SDK Version  :         3.1.1

Python Version    :         3.8.12

****

Huấn luyện chatbot:

Ở thư mục RASA chạy lệnh:

rasa train


****

Sau khi huấn luyện, muốn chạy chatbot cần chạy 2 lệnh sau: (Lưu ý 2 lệnh này run ở 2 terminal khác nhau, cùng ở thư mục RASA chứ không cd vào thư mục khác)

- Chạy Rasa NLU:

rasa run --enable-api --cors "*"

- Chạy Rasa actions

rasa run actions


Lưu ý sau khi chạy 2 lệnh trên thì ta có API gọi đến chatbot là 

POST http://localhost:5005/webhooks/rest/webhook

Cấu trúc phần body của API :

{ "message": "Nhập câu nói bất kỳ ở đây"}


Nếu sử dụng Rasa/duckling, lần dùng đầu tiên thì chạy lệnh: 

docker run -d -p 8000:8000 rasa/duckling

Những lần sau đó thì chạy lệnh:

docker start <ID của container chạy Rasa/duckling đã tạo>


Ngoài ra nếu muốn xem chi tiết từng entity và intent Rasa nhận dạng được cho 1 câu thì chạy lệnh: (lệnh này cũng ở 1 terminal khác)

rasa shell nlu


****

Phần code của Rasa có 2 file chính cần quan tâm:

File nlu.yml ở thư mục data chứa dữ liệu huấn luyện

File actions.py ở thư mục action là nơi cài đặt actions tùy chỉnh


****

Chi tiết thêm về Rasa xem tại https://rasa.com/