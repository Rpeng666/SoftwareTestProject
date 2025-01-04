import subprocess
import json
import random
import re
import ast
import matplotlib.pyplot as plt
import pandas as pd
from model import generateCode
from dataset.prompt import prompts
from util import get_pure_code


class FuzzTester:
    def __init__(self, model_command="ollama", model_name="codellama:latest", seed=42):
        random.seed(seed)
        self.model_command = model_command
        self.model_name = model_name

    def typo_mutation(self, prompt):
        index = random.randint(0, len(prompt) - 1)
        # print("debug ", prompt)
        return prompt[:index] + random.choice('abcdefghijklmnopqrstuvwxyz') + prompt[index + 1:]

    def noise_mutation(self, prompt):
        symbols = ['#', '@', '!', '?', '$', '%', '^', '&', '*', '(', ')', '💡', '-']
        position = random.randint(0, len(prompt))
        return prompt[:position] + random.choice(symbols) + prompt[position:]

    def boundary_mutation(self, prompt):
        # 增加多种嵌套结构
        return [
            self.generate_nested_loops(),  # 多层嵌套循环
            self.generate_recursive_function(),  # 递归函数
            self.generate_nested_conditions(),  # 嵌套条件语句
            self.generate_complex_structure()  # 复杂嵌套结构
        ]
    
    def generate_nested_loops(self, n=10):
        code = "for i in range(n):\n"
        for i in range(1, n):
            code += f"    for j in range(n):\n"
            for k in range(1, n):
                code += f"        for l in range(n):\n"
                code += "            print(i, j, k, l)\n"
        return code
    
    def generate_recursive_function(self, n=10):
        code = "def factorial(n):\n"
        code += "    if n == 0:\n"
        code += "        return 1\n"
        code += "    else:\n"
        code += "        return n * factorial(n-1)\n"
        return code

    def generate_nested_conditions(self, n=3):
        code = "if condition_1:\n"
        for i in range(n):
            code += f"    if condition_{i}:\n"
            code += "        perform_action()\n"
            code += f"    else:\n    # Nested Else\n"
        return code

    def generate_complex_structure(self, n=3):
        code = "def complex_function(n):\n"
        code += "    if n > 0:\n"
        code += "        for i in range(n):\n"
        code += "            if i % 2 == 0:\n"
        code += "                print(f'Even: {i}')\n"
        code += "            else:\n"
        code += "                complex_function(i - 1)\n"
        return code

    
    def fuzz_input(self, prompt, strategies=None):
        if strategies is None:
            strategies = ['typo', 'noise', 'boundary']

        fuzzed_prompts = []
        for strategy in strategies:
            if strategy == 'typo':
                fuzzed_prompts.append(self.typo_mutation(prompt))
            elif strategy == 'noise':
                fuzzed_prompts.append(self.noise_mutation(prompt))
            elif strategy == 'boundary':
                fuzzed_prompts.append(self.boundary_mutation(prompt))

        return fuzzed_prompts

    def run_tests(self, prompt):
        results = {}
        mutated_inputs = self.fuzz_input(prompt)

        response_pair_list = []

        for mutation, mutated_prompt in zip(["Typo", "Noise", "Boundary"], mutated_inputs):
            output = self._run_model(mutated_prompt)
            # print("debug output ", output)
            response_pair_list.append([mutated_prompt, output])

        result_type = self.evaluate_results(response_pair_list)
        results[mutation] = {
            "input": mutated_prompt,
            "output": output,
            "result": result_type
        }
        return results

    def _run_model(self, prompt):
        try:
            return generateCode(prompt)
        except Exception as e:
            return f"Error: {str(e)}"

    def evaluate_results(self, results):
        # print("debug result ", results)
        evaluation = []
        for fuzzed_prompt, code in results:
            code = get_pure_code(code)
            correctness = self._evaluate_correctness(code)
            evaluation.append({'prompt': fuzzed_prompt, 'result': correctness})

        # print("debug result ", results )
        # 假设 results 是包含所有测试结果的字典
        # print("debug correctness_rate ", evaluation)

        correctness_rate = self.calculate_correctness_rate(evaluation)
        syntax_error_rate = self.calculate_syntax_error_rate(evaluation)
        empty_output_rate = self.calculate_empty_output_rate(evaluation)
        error_mode_frequency = self.calculate_error_mode_frequency(evaluation)

        print(f"Correctness Rate: {correctness_rate}%")
        print(f"Syntax Error Rate: {syntax_error_rate}%")
        print(f"Empty Output Rate: {empty_output_rate}%")
        print(f"Error Mode Frequency: {error_mode_frequency}")

        return evaluation

    def _evaluate_correctness(self, code):
        if not code.strip():
            return 'Empty Output'
        # print("debug code ", code)
        try:
            ast.parse(code)
        except SyntaxError:
            return "Syntax Error"
        
        if code.count('(') != code.count(')'):
            return 'Unbalanced Parentheses'
        
        return 'Valid Code'
    
    def calculate_correctness_rate(self, results):
        '''生成代码正确率 (Correctness Rate)'''
        correct_count = sum(1 for result in results if result['result'] == 'Valid Code')
        total_tests = len(results)
        return (correct_count / total_tests) * 100
    
    def calculate_syntax_error_rate(self, results):
        '''语法错误率 (Syntax Error Rate)'''
        # print("debug result 222 ", results)
        syntax_error_count = sum(1 for result in results if result['result'] == 'Syntax Error')
        total_tests = len(results)
        return (syntax_error_count / total_tests) * 100
    
    def calculate_empty_output_rate(self, results):
        '''输出为空的比例 (Empty Output Rate)'''
        empty_output_count = sum(1 for result in results if result['result'] == 'Empty Output')
        total_tests = len(results)
        return (empty_output_count / total_tests) * 100
    
    def calculate_error_mode_frequency(self, results):
        '''错误模式统计 (Error Mode Frequency)'''
        error_modes = ['Syntax Error', 'Unbalanced Parentheses', 'Empty Output', 'Valid Code']
        error_counts = {error_mode: 0 for error_mode in error_modes}
        
        for result in results:
            error_counts[result['result']] += 1
        
        total_tests = len(results)
        return {mode: (count / total_tests) * 100 for mode, count in error_counts.items()}


    # 生成统计报告的功能
    def generate_statistics(self, results):
        # 统计每个错误类型的频率
        error_count = {"Valid Code": 0, "Syntax Error": 0, "Empty Output": 0, "Unbalanced Parentheses": 0}
        
        print("debug fhfsdoiafnoasfsadf ", results.values())

        for result in results.values():
            print("debug result ", result['result'])
            error_count[result['result']] += 1
        
        # 计算每种错误类型的发生频率
        total_tests = len(results)
        error_frequencies = {key: (count / total_tests) * 100 for key, count in error_count.items()}
        
        return error_count, error_frequencies

    # 生成图表来展示错误模式的频率
    def plot_error_frequencies(self, error_frequencies):
        # 将频率绘制为柱状图
        labels = list(error_frequencies.keys())
        values = list(error_frequencies.values())
        
        plt.bar(labels, values, color=['green', 'red', 'yellow', 'blue'])
        plt.xlabel("Error Type")
        plt.ylabel("Frequency (%)")
        plt.title("Error Mode Frequency")
        plt.show()

    # 生成数据表格并保存
    def save_results_to_table(self, results, filename="test_results.csv"):
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        print(f"Results saved to {filename}")

    

if __name__ == "__main__":
    tester = FuzzTester()
    
    for prompt in prompts:
        print(f"Prompt: {prompt['description']}")

        for idx, data in enumerate(prompt['data']):
            print(f"epoch: {idx + 1} | Data: {data}")
            test_results = tester.run_tests(data)
            
            # print("debug test_result ", test_results)

            # 打印测试结果
            log_path = "./log/"
            from time import time
            import os

            for mutation, result in test_results.items():
                timestamp = int(time())

                file_path = f"{log_path}/{mutation}/{timestamp}.txt"
                if not os.path.exists(f"{log_path}/{mutation}"):
                    os.makedirs(f"{log_path}/{mutation}")

                with open(f"{log_path}/{mutation}/{timestamp}.txt", "w") as f:
                    f.write(f"Mutation Type: {mutation}\n")
                    f.write(f"Input: {result['input']} ...\n")
                    f.write(f"Output: {result['output']} ...\n")
                    f.write(f"Result: {result['result']}\n\n")

            # # 生成统计数据
            # error_count, error_frequencies = tester.generate_statistics(test_results)
            
            # # 打印详细错误统计
            # print("Error Mode Count:", error_count)
            # print("Error Mode Frequency (%):", error_frequencies)
            
            # # 绘制图表
            # tester.plot_error_frequencies(error_frequencies)
            
            # # 保存测试结果
            # tester.save_results_to_table(test_results)
