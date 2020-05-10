import time

from FileUtils import make_list_from_file

if __name__ == '__main__':
    # Controls
    search_index = 2_876
    print_count = 200
    file_name = "binfile_5_000.bin"

    print("\nCreating normal list ...")
    start_time = time.time()
    l_list = make_list_from_file(file_name)
    end_time = time.time() - start_time
    print("Normal list ({0}) created for {1:3.6} seconds".format(l_list.size, end_time))

    print("\nCreating K-100 list ...")
    start_time = time.time()
    k_list_100 = make_list_from_file(file_name, 100)
    end_time = time.time() - start_time
    print("K-100 list ({0}) created for {1:3.6} seconds".format(k_list_100.size, end_time))

    print("\nCreating K-1000 list ...")
    start_time = time.time()
    k_list_1000 = make_list_from_file(file_name, 1000)
    end_time = time.time() - start_time
    print("K-1000 list ({0}) created for {1:3.6} seconds".format(k_list_1000.size, end_time))

    print("\nSearching {0} list for index {1}".format("Normal", search_index))
    start_time = time.time()
    found_data = l_list.search(search_index)
    end_time = time.time() - start_time
    print("Found element - {0} from {1} list in {2:3.6} seconds".format(found_data, "Normal", end_time))

    print("\nSearching {0} list for index {1}".format("K-100", search_index))
    start_time = time.time()
    found_data = k_list_100.search(search_index)
    end_time = time.time() - start_time
    print("Found element - {0} from {1} list in {2:3.6} seconds".format(found_data, "K-100", end_time))

    print("\nSearching {0} list for index {1}".format("K-1000", search_index))
    start_time = time.time()
    found_data = k_list_1000.search(search_index)
    end_time = time.time() - start_time
    print("Found element - {0} from {1} list in {2:3.6} seconds".format(found_data, "K-1000", end_time))

    input("\n\nPress ENTER to display {0} elements of the {1} list ...".format(print_count, "K-100"))
    print("\n\nPrinting {0} elements from {1} list".format(print_count, "K-100"))
    k_list_100.print(print_count)
