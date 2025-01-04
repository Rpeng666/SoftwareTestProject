import re

def get_pure_code(code):
    '''从Markdown中提取出代码'''
    # 匹配以```开头和结尾的代码块（包括语言标签）
    code_blocks = re.findall(r'```.*?\n(.*?)```', code, re.DOTALL)
    
    # 如果有代码块，返回所有代码块的内容
    pure_code = '\n'.join(code_blocks)
    
    return pure_code
