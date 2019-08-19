import os
import sys
import unittest
import logging
import re
import threading

# test will run running make which lives one directory above src
scriptdir = os.path.join(os.getcwd(), 'src')
libdir = os.path.join(scriptdir, 'lib')
sys.path.insert(0, libdir)
test_dir = os.path.join(scriptdir, 'tests')
sys.path.insert(0, test_dir)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)-2s] %(message)s')
handler.setFormatter(formatter)

# 1 get all tests under test folder: all test are in a folder which name start by test_*.py
def get_test_files():
    pattern = "^test_"
    files = []
    for file in os.listdir(test_dir):
        if re.match(pattern, file):
                files.append(file)
    return files


def run_tests(test_file, result):
    logging.info('Running tests on file: {}'.format(test_file))
    test_loader = unittest.defaultTestLoader.discover(test_dir, test_file)
    test_runner = unittest.TextTestRunner()
    result[test_file] = test_runner.run(test_loader)



if __name__ == '__main__':
    result = {}
    files = get_test_files()
    logging.info('Running tests on files: {}'.format(files))
    for file in files:
        t = threading.Thread(target=run_tests, args=(file, result))
        t.start()
        t.join()

    for k, v in result.items():
        if not v.wasSuccessful():
            sys.exit(1)