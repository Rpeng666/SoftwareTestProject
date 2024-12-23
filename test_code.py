import subprocess
import time
import pylint.lint
from io import StringIO
from pylint.reporters import JSONReporter
import sys

class CodeTester:
    def __init__(self):
        pass
    
    def test_compile(self, code: str) -> bool:
        """测试代码是否能够成功编译（是否有语法错误）"""
        try:
            # 将代码保存到临时文件中
            with open("temp_test_code.py", "w", encoding="utf-8") as f:
                f.write(code)
            
            # 使用Python解释器进行测试
            result = subprocess.run(["python", "temp_test_code.py"], capture_output=True)
            #result = subprocess.run([sys.executable, "temp_test_code.py"], capture_output=True)
            # 如果没有错误输出，则说明编译通过
            return result.returncode == 0
        except Exception as e:
            print(f"Compilation error: {e}")
            return False
    
    def test_code_style(self, code: str) -> str:
        """使用Pylint进行代码风格检查"""
        try:
            pylint_output = StringIO()
            pylint.lint.Run(["--disable=all", "--enable=C", "--output-format=text", "temp_test_code.py"], do_exit=False, reporter=JSONReporter(output=pylint_output))
            return pylint_output.getvalue()
        except Exception as e:
            print(f"Style check failed: {e}")
            return str(e)

    def test_performance(self, code: str) -> float:
        """测试代码的性能（运行时间）"""
        try:
            # 保存代码到临时文件
            with open("temp_test_code.py", "w") as f:
                f.write(code)
            
            start_time = time.time()
            subprocess.run(["python3", "temp_test_code.py"], capture_output=True)
            end_time = time.time()

            # 返回运行时间
            return end_time - start_time
        except Exception as e:
            print(f"Performance test failed: {e}")
            return float('inf')  # 出错时返回无穷大

    def test_flask(self, code: str) -> bool:
        """测试Flask应用是否能正常启动"""
        try:
            with open("temp_flask_app.py", "w") as f:
                f.write(code)

            # 启动Flask应用
            flask_process = subprocess.Popen(["python3", "temp_flask_app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(2)  # 等待Flask应用启动

            # 发送GET请求测试
            response = requests.get("http://127.0.0.1:5000/")
            flask_process.kill()  # 关闭Flask进程

            return response.status_code == 200
        except Exception as e:
            print(f"Flask test failed: {e}")
            return False

    def test_django(self, code: str) -> bool:
        """测试Django应用是否能正常启动"""
        try:
            with open("temp_django_app.py", "w") as f:
                f.write(code)

            # 启动Django应用
            django_process = subprocess.Popen(["python3", "temp_django_app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(2)  # 等待Django应用启动

            # 发送GET请求测试
            response = requests.get("http://127.0.0.1:8000/")
            django_process.kill()  # 关闭Django进程

            return response.status_code == 200
        except Exception as e:
            print(f"Django test failed: {e}")
            return False

    def test_pytorch(self, code: str) -> bool:
        """测试PyTorch模型是否能正常运行"""
        try:
            with open("temp_pytorch_model.py", "w") as f:
                f.write(code)

            # 执行PyTorch模型
            # result = subprocess.run(["python3", "temp_pytorch_model.py"], capture_output=True)
            subprocess.run([sys.executable, "temp_test_code.py"], capture_output=True)

            return result.returncode == 0
        except Exception as e:
            print(f"PyTorch test failed: {e}")
            return False


    def test_file_downloader(self, code: str, files: list) -> bool:
        """测试文件下载器是否能够并发下载文件"""
        try:
            with open("temp_downloader.py", "w") as f:
                f.write(code)

            # 运行下载器
            result = subprocess.run(["python3", "temp_downloader.py"] + files, capture_output=True)

            # 检查是否下载了指定文件
            return result.returncode == 0
        except Exception as e:
            print(f"File downloader test failed: {e}")
            return False

    def test_login_system(self, code: str) -> bool:
        """测试登录系统功能"""
        try:
            with open("temp_login_system.py", "w") as f:
                f.write(code)

            # 运行登录系统并测试
            result = subprocess.run(["python3", "temp_login_system.py"], capture_output=True)
            return result.returncode == 0
        except Exception as e:
            print(f"Login system test failed: {e}")
            return False

    def test_ml_training(self, code: str) -> bool:
        """测试机器学习训练脚本"""
        try:
            with open("temp_ml_training.py", "w") as f:
                f.write(code)

            # 运行训练脚本
            result = subprocess.run(["python3", "temp_ml_training.py"], capture_output=True)
            return result.returncode == 0
        except Exception as e:
            print(f"ML training test failed: {e}")
            return False

    def test_crawler(self, code: str) -> bool:
        """测试爬虫应用"""
        try:
            with open("temp_crawler.py", "w") as f:
                f.write(code)

            # 运行爬虫
            result = subprocess.run(["python3", "temp_crawler.py"], capture_output=True)
            return result.returncode == 0
        except Exception as e:
            print(f"Crawler test failed: {e}")
            return False

    def test_unittest(self, code: str) -> bool:
        """测试自动化测试脚本"""
        try:
            with open("temp_unittest.py", "w") as f:
                f.write(code)

            # 运行单元测试
            result = subprocess.run(["python3", "temp_unittest.py"], capture_output=True)
            return result.returncode == 0
        except Exception as e:
            print(f"UnitTest test failed: {e}")
            return False