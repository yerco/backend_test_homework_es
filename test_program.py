import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['program.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f"The file `{filename}` wasn't found in the repository root"

    try:
        import program
    except Exception as e:
        assert False, (
            'Failed to run `program.py`. '
            'Correct the mistakes:\\n'
            f'{e}'
        )
