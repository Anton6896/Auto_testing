from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMEDRIVER = BASE_DIR.joinpath('chromedriver')

if __name__ == '__main__':
    print(CHROMEDRIVER)
