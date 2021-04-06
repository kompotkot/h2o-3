import os
import zipfile

here = os.path.abspath(os.path.dirname(__file__))


def readTxtFromWhl(name, fallback):
    if here.endswith(".whl/h2o"):
        with zipfile.ZipFile(here[:-4]) as whl:
            with whl.open(name) as f:
                return f.read().decode("utf8")
    else:
        return fallback


try:
    with open(os.path.join(here, "buildinfo.txt"), encoding="utf-8") as f:
        __buildinfo__ = f.read()
except:
    try:
        __buildinfo__ = readTxtFromWhl("h2o/buildinfo.txt", "unknown")
    except:
        __buildinfo__ = "unknown"

try:
    with open(os.path.join(here, "version.txt"), encoding="utf-8") as f:
        __version__ = f.read()
except:
    try:
        __version__ = readTxtFromWhl("h2o/version.txt", "0.0.local")
    except:
        __version__ = "0.0.local"
