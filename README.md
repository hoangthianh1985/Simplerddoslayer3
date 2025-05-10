📄 README.md
# TCP Connection Tester

Một công cụ đơn giản viết bằng Python để mô phỏng việc gửi nhiều kết nối TCP đến một máy chủ — thường dùng để kiểm thử khả năng chịu tải hoặc phân tích bảo mật mạng (ví dụ như máy chủ game Minecraft).

> ⚠️ **Chỉ sử dụng công cụ này trong môi trường nội bộ, do bạn sở hữu và được phép kiểm thử.** Mọi hành vi sử dụng sai mục đích đều vi phạm pháp luật.

---

## 🚀 Tính năng

- Gửi nhiều kết nối TCP đến địa chỉ IP và cổng tùy chọn.
- Cho phép cấu hình số luồng (thread) đồng thời.
- Gửi 100 gói tin mỗi đợt và nghỉ 2 giây giữa các đợt.
- In thời gian thực hiện mỗi đợt để tiện theo dõi hiệu suất.
- Được thiết kế dễ sử dụng, đơn giản và hiệu quả.

---

## 🛠️ Cách sử dụng

### 1. Cài đặt Python

Bạn cần Python 3.6 trở lên. Kiểm tra bằng lệnh:

```bash
python --version
```
2. Chạy chương trình
```python main.py```


# ⚠️ Cảnh báo pháp lý

## Công cụ này không phải công cụ DDoS. Nó được phát triển với mục đích kiểm thử nội bộ và giáo dục. Việc sử dụng công cụ này để tấn công, quấy rối hay gây gián đoạn dịch vụ của người khác là vi phạm pháp luật và có thể bị truy cứu trách nhiệm hình sự.
