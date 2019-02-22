import os
import subprocess


def run_test_coverage():
    """
    Simple run coverage and do:
     - Runs the tests
     - Check your test coverage
     - Generates HTML coverage report under "htmlcov" directory.
    """
    py_test_command = "coverage run -m pytest"

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    try:
        subprocess.run(py_test_command.split())
        coverage_dir = os.path.join(CURRENT_DIR, "htmlcov")
        os.chdir(coverage_dir)
    except AttributeError:
        print("Please activate your local virtual environment and re-run this script.")


def run_http_server():
    """Up & Run Simple HTTP Server with 8080 port."""
    command = "python -m http.server 8080"
    subprocess.run(command.split())


if __name__ == "__main__":
    run_test_coverage()
    run_http_server()
