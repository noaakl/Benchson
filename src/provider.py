import subprocess
import sys


class Provider:

    @staticmethod
    def install_dependency(package):
        """Installs a package dynamically if missing."""
        if package.startswith("src.") or "." in package:
            return  # Skip local imports
        try:
            __import__(package)
        except ImportError:
            print(f"Installing missing dependency: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
