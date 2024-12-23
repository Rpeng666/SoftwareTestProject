# test_chatbot.py

import unittest
from main import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = Chatbot()

    def test_known_responses(self):
        self.assertEqual(self.bot.respond("hello"), "Hi there!")
        self.assertEqual(self.bot.respond("how are you"), "I'm just a bot, but I'm doing fine!")
        self.assertEqual(self.bot.respond("bye"), "Goodbye!")

    def test_unknown_responses(self):
        self.assertEqual(self.bot.respond("unknown"), "I don't understand that.")

TestChatbot.setUp()
TestChatbot.test_known_responses()
TestChatbot.test_unknown_responses