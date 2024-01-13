import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = os.getenv('ROOT_DIR')


def execute_python_script(fn: str):
    subprocess.call(['python', fn])


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
    execute_python_script(os.path.join(ROOT_DIR, 'load_authors.py'))
    execute_python_script(os.path.join(ROOT_DIR, 'load_papers.py'))
    execute_python_script(os.path.join(ROOT_DIR, 'load_author_paper.py'))


if __name__ == '__main__':
    main()
