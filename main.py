#from generate_code import CodeGenerator
# 这里我将使用的模型换成通义千问
from LLM import CodeGenerator
import os

from test_code import CodeTester
from prompt import prompts
from time import time


def main():
    TEST_SIMPLE_ALGORITHM_CODE = False
    TEST_FRAMEWORK_CODE = False
    TEST_COMPLEX_CODE = False
    TEST_PROJECT_CODE = True

    # 初始化生成器和测试器
    code_generator = CodeGenerator()
    code_tester = CodeTester()
    
    # 生成代码
    print("Generating code for each prompt...")
    
    global prompts

    if TEST_SIMPLE_ALGORITHM_CODE:
        # 测试生成的代码
        for prompt in prompts["生成简单算法代码"]:
            print("debug: ", prompt)
            print(f"\nTesting code for prompt: {prompt['prompt']}")
            code = code_generator.generate_code(prompt['prompt'])

            save_path = f"test_code/{prompt['save_path']}.py"
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(code)

                # 1. 编译测试
                print("  Testing compilation...")
                f.write("\n\n\n\n'''\n1. 编译测试\n")
                compile_result = code_tester.test_compile(code)
                f.write(f"    Compilation passed: {compile_result}\n")
                
                # 2. 性能测试
                print("  Testing performance...")
                performance_result = code_tester.test_performance(code)
                f.write(f"    Performance time: {performance_result:.4f} seconds\n")
                f.write("'''\n")

    if TEST_FRAMEWORK_CODE:
        # 为每个框架生成代码并进行测试
        for prompt in prompts['生成针对框架的代码']:

            # 生成代码
            print(f"Generating code for {prompt['prompt']}...")
            generated_codes = code_generator.generate_code(prompt['prompt'])

            for prompt, code in generated_codes.items():
                print(f"\nTesting code for prompt: {prompt}")

                # 1. 编译测试
                print("  Testing compilation...")
                compile_result = code_tester.test_compile(code)
                print(f"    Compilation passed: {compile_result}")

                # 2. 性能测试
                print("  Testing performance...")
                performance_result = code_tester.test_performance(code)
                print(f"    Performance time: {performance_result:.4f} seconds")

                # 4. 框架特定测试
                if framework == "flask":
                    flask_result = code_tester.test_flask(code)
                    print(f"    Flask app test passed: {flask_result}")
                elif framework == "django":
                    django_result = code_tester.test_django(code)
                    print(f"    Django app test passed: {django_result}")
                elif framework == "pytorch":
                    pytorch_result = code_tester.test_pytorch(code)
                    print(f"    PyTorch model test passed: {pytorch_result}")

    if TEST_COMPLEX_CODE:
        # 生成复杂需求代码
        print("Generating code for complex requirements...")
        generated_codes = code_generator.generate_code(prompts["生成复杂需求的代码"])

        # 测试生成的代码
        for prompt, code in generated_codes:
            print(f"\nTesting code for prompt: {prompt}")

            # 1. 编译测试
            print("  Testing compilation...")
            compile_result = code_tester.test_compile(code)
            print(f"    Compilation passed: {compile_result}")

            # 2. 性能测试
            print("  Testing performance...")
            performance_result = code_tester.test_performance(code)
            print(f"    Performance time: {performance_result:.4f} seconds")

            # 4. 复杂需求功能测试
            if "file downloader" in prompt:
                downloader_result = code_tester.test_file_downloader(code, ["file1.txt", "file2.txt"])
                print(f"    File downloader test passed: {downloader_result}")
            elif "login system" in prompt:
                login_result = code_tester.test_login_system(code)
                print(f"    Login system test passed: {login_result}")
            elif "machine learning" in prompt:
                ml_result = code_tester.test_ml_training(code)
                print(f"    ML training script test passed: {ml_result}")
            elif "web scraper" in prompt:
                crawler_result = code_tester.test_crawler(code)
                print(f"    Web crawler test passed: {crawler_result}")
            elif "unit test" in prompt:
                unittest_result = code_tester.test_unittest(code)
                print(f"    Unit test script test passed: {unittest_result}")

    if TEST_PROJECT_CODE:
        # 生成已有项目代码的测试用例
        print("Generating test cases for existing project code...")
        for prompt in prompts["生成已有项目代码的测试用例"]:
            generated_prompt = code_generator.generate_code(prompt['prompt'])
            print(generated_prompt)
            input()
            with open(f"{prompt['project_path']}/main.py", "r", encoding="utf-8") as f:

                project_code = f.read()

                generated_prompt = generated_prompt.replace("<code>", project_code)
                
                code = code_generator.generate_code(generated_prompt)

                save_path = f"{prompt['save_path']}/test.py"
                # with open(save_path, "w", encoding="utf-8") as f:
                #     f.write(code)
                # 检查保存路径是否存在，如果不存在则创建该目录
                if not os.path.exists(prompt['save_path']):
                    try:
                        os.makedirs(prompt['save_path'])
                    except Exception as e:
                        print(f"创建目录 {prompt['save_path']} 时出错: {e}")
                        return
                try:
                    with open(save_path, "w", encoding="utf-8") as f:
                        f.write(code)
                    print(f"文件已成功保存至 {save_path}")
                except Exception as e:
                    print(f"写入文件 {save_path} 时出错: {e}")

                print("开始准备测试")
                input()

                # 1. 编译测试
                print("  Testing compilation...")
                compile_result = code_tester.test_compile(code)
                print(f"    Compilation passed: {compile_result}")

                # 2. 性能测试
                print("  Testing performance...")
                performance_result = code_tester.test_performance(code)
                print(f"    Performance time: {performance_result:.4f} seconds")




if __name__ == "__main__":
    #main()
    with open(f"test_project/chatBot/test.py", "r", encoding="utf-8") as f:
        project_code = f.read()

#     test_code = '''
# def add(a, b):
#     print("jaja")
#     raise ValueError("This is a test exception")
#     return a + b
# add(1,2)
#         '''
    compile_result = CodeTester().test_compile(project_code)
    print(f"Compilation passed: {compile_result}")
