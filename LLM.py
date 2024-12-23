import ollama
import re
import time
import random as rd
from http import HTTPStatus
import dashscope


dashscope.api_key = "sk-e2082287725c4efeb797bda10765379e"


class CodeGenerator:
    def __init__(self, model="toyi", temperature=0):
        self.model = model
        self.temperature = temperature
        self.client = dashscope.Generation

    def generate_code(self, prompt: str) -> str:
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                   {'role': 'user', 'content': prompt}]
        # 重试次数和初始延迟
        max_retries = 4
        base_delay = 2
        for attempt in range(1, max_retries + 1):
            try:
                response = self.client.call(
                    dashscope.Generation.Models.qwen_turbo,
                    messages=messages,
                    result_format='message'
                )
                if response.status_code == HTTPStatus.OK:
                    content = response["output"]["choices"][0]["message"]["content"]
                    # return content
                    # 提取代码块
                    pattern = re.compile(r"```python\s*([\s\S]*)\s*```")
                    code = re.findall(pattern, content)
                    if len(code) > 0:
                        return code[0]
                    else:
                        return content
                else:
                    print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                        response.request_id, response.status_code,
                        response.code, response.message
                    ))
            except Exception as e:
                print("Error:", e)
                if attempt < max_retries:
                    sleeptime = base_delay ** attempt
                    time.sleep(sleeptime)
                    print(f"Retry {attempt + 1}, delay {sleeptime}")
        return "error"

    def generate_codes(self, prompts: list) -> dict:
        code_dict = {}
        for prompt in prompts:
            code_dict[prompt] = self.generate_code(prompt)
        return code_dict
    
# if __name__ == "__main__":
#     code_generator = CodeGenerator()
#     # 生成单个代码
#     single_result = code_generator.generate_code("请为我生成一个计算两个数相加的 Python 函数。")
#     print(single_result)
#     # 生成多个代码
#     prompts = ["请为我生成一个计算两个数相加的 Python 函数。", "请为我生成一个计算两个数相减的 Python 函数。"]
#     multiple_results = code_generator.generate_codes(prompts)
#     print(multiple_results)