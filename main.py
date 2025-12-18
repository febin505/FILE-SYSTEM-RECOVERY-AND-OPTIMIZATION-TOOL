from analyzer import analyze
from recovery import recover
from optimizer import optimize

PATH = "test_directory"
TRASH = "test_directory/.trash"
RECOVERED = "recovered_files"

files, size = analyze(PATH)
recovered = recover(TRASH, RECOVERED)
removed = optimize(PATH








)

with open("report.txt", "w") as r:
    r.write("File System Recovery and Optimization Report\n")
    r.write(f"Total Files Scanned: {files}\n")
    r.write(f"Total Size: {size} bytes\n")
    r.write(f"Files Recovered: {recovered}\n")
    r.write(f"Temporary Files Removed: {removed}\n")

print("Process Completed. Check report.txt")
