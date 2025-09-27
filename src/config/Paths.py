from pathlib import Path

class Paths:
    """Centralized file paths configuration"""
    
    def __init__(self, base_dir: str = None):
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent.parent
        else:
            self.base_dir = Path(base_dir)
    
    @property
    def path_config(self) -> str:
        return str(self.base_dir / "src" / "config")

    @property
    def file_config(self) -> str:
        return str(self.base_dir / "src" / "config" / "Config.py")
