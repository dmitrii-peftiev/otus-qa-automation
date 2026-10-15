import argparse
import collections
import json
import os
import re
import sys

LOG_PATTERN = re.compile(
    r"(?P<ip>\S+) - - "
    r"\[(?P<time>.*?)] "
    r'"(?P<request>[^"]*)" '
    r"(?P<status>\d{3}) "
    r"(?P<bytes>\S+) "
    r'"(?P<referer>[^"]*)" '
    r'"(?P<user_agent>[^"]*)" '
    r"(?P<duration>\d+)"
)

TARGET_METHODS = {"GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"}


def parse_log_file(file_path):
    total_requests = 0
    method_counts = collections.Counter()
    ip_counts = collections.Counter()
    longest_requests = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total_requests += 1

            match = LOG_PATTERN.match(line)
            if not match:
                continue

            data = match.groupdict()

            request_content = data["request"].split()
            method = request_content[0] if len(request_content) > 0 else "UNKNOWN"
            url = request_content[1] if len(request_content) > 1 else "-"

            if method in TARGET_METHODS:
                method_counts[method] += 1

            ip = data["ip"]
            ip_counts[ip] += 1

            duration = int(data["duration"])
            request_info = {
                "method": method,
                "url": url,
                "ip": ip,
                "duration": duration,
                "date_time": data["time"],
            }

            if len(longest_requests) < 3:
                longest_requests.append((duration, request_info))
                longest_requests.sort(key=lambda x: x[0], reverse=True)
            elif duration > longest_requests[-1][0]:
                longest_requests[-1] = (duration, request_info)
                longest_requests.sort(key=lambda x: x[0], reverse=True)

    top_ips = dict(ip_counts.most_common(3))
    top_longest = [item[1] for item in longest_requests]

    metrics = {
        "top_ips": top_ips,
        "top_longest": top_longest,
        "total_stat": dict(method_counts),
        "total_requests": total_requests,
    }

    return metrics


def save_and_print_results(metrics, log_file_path):
    print(f"ANALYSIS RESULTS: {os.path.basename(log_file_path)}")
    print(f"Total requests: {metrics['total_requests']}")

    print("Method counts:")
    for method in sorted(TARGET_METHODS):
        print(f"  {method}: {metrics['total_stat'].get(method, 0)}")

    print("Top 3 IP addresses:")
    for ip, count in metrics["top_ips"].items():
        print(f"  {ip} - {count} times")

    print("Top 3 longest requests:")
    for req in metrics["top_longest"]:
        print(
            f"  Method: {req['method']} | URL: {req['url']} | IP: {req['ip']} | Duration: {req['duration']} ms | Date/Time: {req['date_time']}"
        )

    json_file_name = f"result_{os.path.basename(log_file_path)}.json"
    with open(json_file_name, "w", encoding="utf-8") as jf:
        json.dump(metrics, jf, indent=4, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True)
    args = parser.parse_args()

    target_path = args.path

    if not os.path.exists(target_path):
        print(f"Path {target_path} does not exist.")
        sys.exit(1)

    files_to_parse = []

    if os.path.isfile(target_path):
        files_to_parse.append(target_path)
    elif os.path.isdir(target_path):
        for file_name in os.listdir(target_path):
            full_path = os.path.join(target_path, file_name)
            if os.path.isfile(full_path) and file_name.endswith(".log"):
                files_to_parse.append(full_path)

    for file_path in files_to_parse:
        result_metrics = parse_log_file(file_path)
        save_and_print_results(result_metrics, file_path)


if __name__ == "__main__":
    main()
