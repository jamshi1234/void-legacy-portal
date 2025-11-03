"""Legacy dev portal (stub)."""
from config import load_config

def main():
    cfg = load_config()
    print(f"Starting legacy portal on :{cfg.get('port', 8080)}")

if __name__ == "__main__":
    main()
