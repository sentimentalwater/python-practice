from log_utils import get_number, get_log, print_logs, get_total, get_average
from file_utils import write_logs, read_logs

log = get_log()
write_logs(log)

print("logs saved")

logs = read_logs()
print_logs(logs)

if len(logs) > 0:
    total = get_total(logs)
    average = get_average(logs)

    print("total:", total)
    print("average:", average)
else:
    print("no log!")
