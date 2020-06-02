import os


def format_title(path):
    filename = os.path.basename(path).replace('_', ' ').split('.')[0]
    print(filename)
    return filename


def read_description(description, file):

    dirname = os.path.dirname(file)
    desc = read_from_file(dirname)
    if desc is not None:
        description = desc
    return description


def read_from_file(dirname, filename='/description.md'):
    try:
        path = dirname + filename
        with open(path) as f:
            content = f.read()
        return content
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    format_title('/mnt/nfs/media/Capture/aero_complexes_exo_p1_1.mkv')
