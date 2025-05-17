import re

def analyze_docker_logs(file_path):
    error_pattern = re.compile(r'(?P<timestamp>\d{4}-\d{2}-\d{2}T[\d:.]+Z).*?(ERROR|Exception)', re.IGNORECASE)

    with open(file_path, 'r') as log_file:
        for line_number, line in enumerate(log_file, start=1):
            match = error_pattern.search(line)
            if match:
                timestamp = match.group("timestamp")
                print(f"[Line {line_number}] {timestamp} --> {line.strip()}")

if __name__ == "__main__":
    log_file_path = 'docker_logs.txt'
    analyze_docker_logs(log_file_path)

