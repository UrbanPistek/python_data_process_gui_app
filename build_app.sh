#!/bin/zsh

while getopts "f:" flag; do
    case ${flag} in
        f )
            source venv/bin/activate
            FILE_NAME=${OPTARG}
            echo "File: $FILE_NAME"
            pyinstaller --onefile $FILE_NAME
            echo "==> Executable Created"
            ;;
        * ) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
done