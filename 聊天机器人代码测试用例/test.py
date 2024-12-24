import unittest
import os
import sys
# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取上一级目录
parent_dir = os.path.dirname(current_dir)

# 将上一级目录添加到 sys.path 中
sys.path.append(parent_dir)

from test_project.chatBot.main import Chatbot

class TestChatbot(unittest.TestCase):
    
    def setUp(self):
        # 创建一个Chatbot实例供每个测试方法使用
        self.bot = Chatbot()

    def test_known_responses(self):
        # 测试已知输入返回正确的响应
        self.assertEqual(self.bot.respond("hello"), "Hi there!")
        self.assertEqual(self.bot.respond("how are you"), "I'm just a bot, but I'm doing fine!")
        self.assertEqual(self.bot.respond("bye"), "Goodbye!")

    def test_unknown_response(self):
        # 测试未知输入返回默认响应
        self.assertEqual(self.bot.respond("unknown"), "I don't understand that.")

    def test_case_insensitivity(self):
        # 测试机器人不区分大小写
        self.assertEqual(self.bot.respond("Hello"), "Hi there!")
        self.assertEqual(self.bot.respond("HELLO"), "Hi there!")

if __name__ == '__main__':
    unittest.main()
