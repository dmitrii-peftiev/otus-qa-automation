import datetime
import subprocess
from collections import defaultdict


def get_ps_output():
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True, check=False)
    return result.stdout


def parse_ps_data(ps_output):
    lines = ps_output.strip().split("\n")
    process_lines = lines[1:]

    total_processes = len(process_lines)
    user_counts = defaultdict(int)

    total_mem = 0.0
    total_cpu = 0.0

    max_mem_val = -1.0
    max_mem_proc = ""

    max_cpu_val = -1.0
    max_cpu_proc = ""

    for line in process_lines:
        if not line:
            continue
        parts = line.split(None, 10)
        if len(parts) < 11:
            continue

        user = parts[0]
        cpu = float(parts[2])
        mem = float(parts[3])
        command = parts[10].strip()

        user_counts[user] += 1
        total_cpu += cpu
        total_mem += mem

        if mem > max_mem_val:
            max_mem_val = mem
            max_mem_proc = command[:20]

        if cpu > max_cpu_val:
            max_cpu_val = cpu
            max_cpu_proc = command[:20]

    users_list = ", ".join(f"'{u}'" for u in sorted(user_counts.keys()))

    user_processes_report = ""
    for user, count in sorted(user_counts.items(), key=lambda x: x[1], reverse=True):
        user_processes_report += f"{user}: {count}\n"

    report = (
        f"System status report:\n"
        f"System users: {users_list}\n"
        f"Processes running: {total_processes}\n\n"
        f"User processes:\n"
        f"{user_processes_report.strip()}\n\n"
        f"Total memory used: {total_mem:.1f}%\n"
        f"Total CPU used: {total_cpu:.1f}%\n"
        f"Most memory used by: {max_mem_proc}\n"
        f"Most CPU used by: {max_cpu_proc}\n"
    )

    return report


def main():
    raw_data = get_ps_output()
    report = parse_ps_data(raw_data)

    print(report)

    now = datetime.datetime.now(datetime.UTC)
    filename = now.strftime("%d-%m-%Y_%H-%M-scan.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()
