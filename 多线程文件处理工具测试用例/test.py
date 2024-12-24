import os
import unittest
import os
import sys
# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取上一级目录
parent_dir = os.path.dirname(current_dir)

# 将上一级目录添加到 sys.path 中
sys.path.append(parent_dir)

from test_project.multiThreadDownload.main import FileProcessor

class TestFileProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建测试文件
        cls.test_directory = 'test_directory'
        os.makedirs(cls.test_directory, exist_ok=True)
        cls.files = [
            ('file1.txt', "line1\nline2\nline3"),
            ('file2.txt', "lineA\nlineB"),
            ('file3.txt', "")
        ]
        for filename, content in cls.files:
            file_path = os.path.join(cls.test_directory, filename)
            with open(file_path, 'w') as f:
                f.write(content)

    @classmethod
    def tearDownClass(cls):
        # 删除测试文件和目录
        for _, content in cls.files:
            file_path = os.path.join(cls.test_directory, _)
            os.remove(file_path)
        os.rmdir(cls.test_directory)

    def test_single_file_line_count(self):
        processor = FileProcessor(self.test_directory)
        line_count = processor.count_lines(os.path.join(self.test_directory, 'file1.txt'))
        self.assertEqual(line_count, 3)

    def test_multiple_files_line_count(self):
        processor = FileProcessor(self.test_directory)
        results = processor.process_files()
        expected_results = {
            os.path.join(self.test_directory, 'file1.txt'): 3,
            os.path.join(self.test_directory, 'file2.txt'): 2,
            os.path.join(self.test_directory, 'file3.txt'): 0
        }
        self.assertDictEqual(results, expected_results)

    def test_threaded_processing(self):
        processor = FileProcessor(self.test_directory)
        results = processor.process_files()
        expected_results = {
            os.path.join(self.test_directory, 'file1.txt'): 3,
            os.path.join(self.test_directory, 'file2.txt'): 2,
            os.path.join(self.test_directory, 'file3.txt'): 0
        }
        self.assertDictEqual(results, expected_results)

    def test_empty_directory(self):
        empty_dir = 'empty_directory'
        os.makedirs(empty_dir, exist_ok=True)
        processor = FileProcessor(empty_dir)
        results = processor.process_files()
        self.assertDictEqual(results, {})
        os.rmdir(empty_dir)

    def test_nonexistent_file(self):
        non_existent_file = 'non_existent.txt'
        processor = FileProcessor(self.test_directory)
        results = processor.process_files()
        self.assertNotIn(non_existent_file, results)

if __name__ == '__main__':
    unittest.main()
