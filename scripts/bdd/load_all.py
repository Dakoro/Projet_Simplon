import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.getcwd()


def execute_python_script(fn: str):
    fp = os.path.join(ROOT_DIR, 'scripts', 'bdd', fn)
    try:
        subprocess.call(['python', fp])
    except:
        subprocess.call(["python3", fp])


def create_bdd(fp):
    if os.path.exists(fp):
        os.remove(fp)
    command = "cat create_tables.sql | sqlite3 bdd.db"
    subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def main():
    create_bdd(os.path.join(ROOT_DIR, 'bdd.db'))
    execute_python_script('load_papers.py')
    execute_python_script('load_authors.py')
    execute_python_script('load_paper_author.py')


if __name__ == '__main__':
    main()
