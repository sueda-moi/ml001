import subprocess
import os
import datetime

LOG_DIR = r"D:\Logs"
LOG_FILE_BASE = "cmd_history"
MAX_LOG_SIZE = 10 * 1024 * 1024  # 设置日志文件最大大小 10MB

log_index = 1

def get_log_file_path(index=1):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    return os.path.join(LOG_DIR, f"{LOG_FILE_BASE}_{index}.log")

log_file_path = get_log_file_path()

def log_message(message):
    global log_file_path, log_index

    with open(log_file_path, 'a') as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] {message}\n")

    if os.path.getsize(log_file_path) >= MAX_LOG_SIZE:
        log_index += 1
        log_file_path = get_log_file_path(log_index)
        print(f"切换到新日志文件：{log_file_path}")

def run_cmd():
    process = subprocess.Popen("cmd.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        while True:
            # 捕获CMD输入
            user_input = input(">> ")
            if user_input.lower() in ["exit", "quit"]:
                process.terminate()
                break

            log_message(user_input)
            process.stdin.write(user_input + "\n")
            process.stdin.flush()

    except KeyboardInterrupt:
        process.terminate()

if __name__ == "__main__":
    run_cmd()
