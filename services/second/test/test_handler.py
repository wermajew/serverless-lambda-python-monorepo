from unittest import TestCase

from src import handler


class HandlerTest(TestCase):

    def test_handler(self):
        event = {}
        result = handler.handler(event, None)
