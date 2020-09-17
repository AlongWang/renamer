import os
import argparse
import re


def getFileList(path, subdirectories=False):
    files = []
    for f in os.listdir(path):
        filePath = os.path.join(path, f)
        if os.path.isdir(filePath):
            if subdirectories:
                files.extend(getFileList(filePath))
        else:
            if not f.startswith('.'):
                files.append(filePath)
    return files


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--directory', '-d',
        help='the directory where files need to be renamed',
        required=True
    )
    parser.add_argument(
        '--target', '-t',
        help='the characters need to be replaced',
        required=True
    )
    parser.add_argument(
        '--replace', '-r',
        help='the replacement characters',
        required=True
    )
    parser.add_argument(
        '--subdirectory',
        help='include files in subdirectories',
        action='store_true',
        default=False
    )
    parser.add_argument(
        '--regex',
        help='the characters which match regex need to be replaced, if use this option, the --target/-t option will be ignored',
        required=True
    )
    return parser.parse_args()


def rename(file, target, regexPattern, replace):
    if not os.path.isfile(file):
        return
    fpath, fname = os.path.split(file)

    if regexPattern is None:
        nfname = fname.replace(target, replace)
    else:
        nfname = re.sub(regexPattern, replace, fname)

    if nfname == fname:
        return
    os.renames(os.path.join(fpath, fname), os.path.join(fpath, nfname))
    return os.path.join(fpath, nfname)


if __name__ == '__main__':
    args = parseArgs()
    files = getFileList(args.directory, args.subdirectory)
    for file in files:

        result = rename(file, args.target, args.regex, args.replace)
        if result is None:
            pass
        else:
            print(file, '  ->  ', result)
