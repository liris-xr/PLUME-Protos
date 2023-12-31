import pathlib
from shutil import which, rmtree
import subprocess

if which('protoc') is None:
    print("protoc not found. Ensure that you installed and added it to your PATH.")
    exit()

protos = [str(path.relative_to("./").as_posix()) for path in pathlib.Path('./').rglob('*.proto')]

rmtree(pathlib.Path("./generated/python"), ignore_errors=True)
pathlib.Path("./generated/python").mkdir(parents=True, exist_ok=True)

proc = subprocess.run(["protoc", "--proto_path=./", "--python_out=generated/python", *protos])