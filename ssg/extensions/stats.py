from ssg import hooks
import time

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time
    start_time = time.time()

@hooks.register("written")
def written():
    global total_written
    total_written = total_written + 1
    # total_written += 1 does not cut it

@hooks.register("stats")
def stats():
    global start_time
    final_time = time.time() - start_time
    # use Truthy-ness of total_written, not a comparison with 0
    average = final_time / total_written if total_written else 0
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"
    print(report.format(total_written, final_time, average))
