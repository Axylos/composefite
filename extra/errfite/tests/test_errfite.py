import os
from errbot.backends.test import testbot
from errfite.fitedb.fite_client import FiteClient

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

class TestErrfite(object):
    extra_plugin_dir = '.'

    def test_add_multistring_fite(self, testbot):
        """
        really stupid setup but trying to use normal
        setup methods and interfacing with the testbot
        is pita.  prob should just manually interact with
        mongo but don't give a shit
        """
        testbot.push_message('!toggle test')
        testbot.pop_message()


        testbot.push_message("!new fitelist warbar")
        assert "Fite Created" in testbot.pop_message()

        testbot.push_message("!add fite warbar | foo fuck | wtf omg")
        assert "foo fuck" in testbot.pop_message()
        #print(testbot.pop_message())


