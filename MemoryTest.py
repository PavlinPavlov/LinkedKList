from FileUtils import make_list_from_file
from pympler import tracker

file_name = "binfile_5_000_000.bin"
k = 1000

tr = tracker.SummaryTracker()
l_list = make_list_from_file(file_name, k)
tr.print_diff()