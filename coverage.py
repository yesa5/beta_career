import subprocess


def run_test_coverage():
    """
    Simple run coverage and do:
     - Runs the tests
     - Check your test coverage
     - Generate an HTML coverage report.
    """
    command = "coverage run -m pytest"
    try:
        subprocess.run(command.split())
    except AttributeError:
        print("Please activate your local virtual environment and re-run this script.")


def run_http_server():
    pass


def deactivate_venv():
    pass


if __name__ == "__main__":
    run_test_coverage()
    deactivate_venv()
    run_http_server()
