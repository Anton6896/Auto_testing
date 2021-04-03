import os

if __name__ == '__main__':
    driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
    print(f"driver ::  {driver_path}")
