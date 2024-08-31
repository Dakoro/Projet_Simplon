import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.getcwd()
BDD_PATH = os.path.join(ROOT_DIR, 'scripts', 'bdd', 'bdd.db')
BDD_SQL_SCRIPT = os.path.join(ROOT_DIR, 'scripts', 'bdd', 'create_tables.sql')


def execute_python_script(fn: str):
    fp = os.path.join(ROOT_DIR, 'scripts', 'bdd', fn)
    try:
        subprocess.call(['python', fp])
    except Exception:
        subprocess.call(["python3", fp])


def create_bdd(fp):
    """Create the database with an sql script

    Args:
        fp (str): path to database
    """
    if os.path.exists(fp):
        os.remove(fp)
    command = f"cat {BDD_SQL_SCRIPT} | sqlite3 {BDD_PATH}"
    subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def main():
    """Main function that execute multiple scripts
    """
    create_bdd(BDD_PATH)
    execute_python_script('load_papers.py')
    execute_python_script('load_authors.py')
    execute_python_script('load_paper_author.py')


if __name__ == '__main__':
    main()
