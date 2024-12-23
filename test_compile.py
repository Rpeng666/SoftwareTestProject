import subprocess
import sys


def test_compile(code: str) -> bool:
    """测试代码是否能够成功编译（是否有语法错误）"""
    try:
        # 将代码保存到临时文件中
        with open("temp_test_code.py", "w", encoding="utf-8") as f:
            f.write(code)
        # 使用 Python 解释器进行测试
        result = subprocess.run([sys.executable, "temp_test_code.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")
        if result.returncode == 0:
            return True
        else:
            print(f"Error output: {result.stderr}")
            return False
    except Exception as e:
        print(f"Compilation error: {e}")
        return False


# 测试代码
# test_code = '''
# def add(a, b):
#     print(f"Adding {a} and {b}")
#     # 故意引发一个异常
#     raise ValueError("This is a test exception")
#     return a + b
# add(33,4)
# '''
with open(f"test_project/RestfullAPI/test2.py", "r", encoding="utf-8") as f:
    project_code = f.read()
print(test_compile(project_code))