import ollama
import re

class CodeGenerator:
    def __init__(self, model="llama3.2"):
        self.client = ollama.Client()
        self.model = model

    def generate_code(self, prompt: str) -> str:
        """与Llama3.2进行交互并返回生成的代码"""
        response = self.client.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        print("debug response: ", response)
        # 提取代码块
        pattern = re.compile(r"```python\s*([\s\S]*)\s*```")
        code = re.findall(pattern, response.get("message", {}).get("content", ""))
        
        if len(code) > 0:
            return code[0]
        else:
            return response.get("message", {}).get("content", "")

    def generate_codes(self, prompts: list) -> dict:
        """为多个prompt生成代码并返回"""
        code_dict = {}
        for prompt in prompts:
            code_dict[prompt] = self.generate_code(prompt)
        return code_dict


if __name__ == "__main__":
    code_generator = CodeGenerator()
    print(code_generator.generate_code("Generate a Python function that adds two numbers."))

