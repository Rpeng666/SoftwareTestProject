# file_processor.py

import os
import threading

class FileProcessor:
    def __init__(self, directory):
        self.directory = directory

    def count_lines(self, file_path):
        with open(file_path, 'r') as file:
            return len(file.readlines())

    def process_files(self):
        results = {}
        threads = []
        for file_name in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file_name)
            if os.path.isfile(file_path):
                thread = threading.Thread(target=self._process_file, args=(file_path, results))
                threads.append(thread)
                thread.start()
        for thread in threads:
            thread.join()
        return results

    def _process_file(self, file_path, results):
        results[file_path] = self.count_lines(file_path)
