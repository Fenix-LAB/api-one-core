import subprocess
from datetime import datetime
from collections import defaultdict

def get_commit_data():
    # Obtiene los commits con fecha y mensaje
    result = subprocess.run(
        ["git", "log", "--pretty=format:%ct|%s"],  # %ct = timestamp, %s = mensaje del commit
        capture_output=True, text=True, check=True
    )

    commit_data = []
    for line in result.stdout.split("\n"):
        if "|" in line:
            ts, message = line.split("|", 1)
            commit_data.append((int(ts), message.strip()))

    return commit_data

def calculate_work_time(commit_data):
    daily_work = defaultdict(list)
    daily_messages = defaultdict(set)  # Usamos un set para evitar mensajes repetidos

    for ts, message in commit_data:
        date = datetime.fromtimestamp(ts).date()
        daily_work[date].append(ts)
        daily_messages[date].add(message)

    work_summary = {}
    total_time = 0

    print("\n===== Resumen de actividad =====\n")
    for date, timestamps in daily_work.items():
        timestamps.sort()
        start_time = datetime.fromtimestamp(timestamps[0])
        end_time = datetime.fromtimestamp(timestamps[-1])
        work_duration = (end_time - start_time).total_seconds() / 3600  # Horas

        work_summary[date] = work_duration
        total_time += work_duration

        print(f"📅 {date}: {work_duration:.2f} horas (de {start_time.time()} a {end_time.time()})")
        print("   🔹 Commits del día:")
        for message in daily_messages[date]:
            print(f"      - {message}")
        print("")

    print(f"⏳ Tiempo total trabajado: {total_time:.2f} horas")

if __name__ == "__main__":
    commit_data = get_commit_data()
    calculate_work_time(commit_data)
