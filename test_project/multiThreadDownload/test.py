# test_file_processor.py

import unittest
import os
from file_processor import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_files'
        os.makedirs(self.test_dir, exist_ok=True)
        self.files = {
            "file1.txt": "Line 1\nLine 2\n",
            "file2.txt": "Line 1\nLine 2\nLine 3\n",
        }
        for file_name, content in self.files.items():
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write(content)

    def tearDown(self):
        for file_name in self.files.keys():
            os.remove(os.path.join(self.test_dir, file_name))
        os.rmdir(self.test_dir)

    def test_count_lines(self):
        processor = FileProcessor(self.test_dir)
        for file_name, content in self.files.items():
            file_path = os.path.join(self.test_dir, file_name)
            self.assertEqual(processor.count_lines(file_path), content.count('\n'))

    def test_process_files(self):
        processor = FileProcessor(self.test_dir)
        results = processor.process_files()
        for file_name, content in self.files.items():
            file_path = os.path.join(self.test_dir, file_name)
            self.assertEqual(results[file_path], content.count('\n'))
