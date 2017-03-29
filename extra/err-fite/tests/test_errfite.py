import os
from errbot.backends.test import testbot

"""
class TestErrFite(object):
    extra_plugin_dir = '.'

    def test_command(self, testbot):
        testbot.push_message('!fite')
        assert 'fiting' in testbot.pop_message()

    def test_get_fite_list(self, testbot):
        testbot.push_message('!get fites')
        assert "No fites found!" in testbot.pop_message()


    def test_make_fite(self, testbot):
        testbot.push_message('!new fitelist foo')
        assert "Fite Created" in testbot.pop_message()

        testbot.push_message('!get fites')
        assert not "No fites found!" in testbot.pop_message()
"""

class TestErrFite(object):
    def test_add_multistring_fite(self, testbot):
        testbot.push_message("!new fitelist bar")
        testbot.push_message("!add fite bar old new")
        testbot.pop_message()
        print(testbot.pop_message())
