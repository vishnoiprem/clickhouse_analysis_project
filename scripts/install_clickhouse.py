# scripts/install_clickhouse.py
import os
import platform

def install_clickhouse():
    os_name = platform.system().lower()
    if os_name == 'linux':
        os.system('source ~/.zprofile')
        os.system('sudo apt-get install -y clickhouse-server clickhouse-client')
        os.system('sudo service clickhouse-server start')
    elif os_name == 'darwin':
        os.system('source ~/.zprofile')
        os.system('brew install clickhouse-server clickhouse-client')
        os.system('brew services start clickhouse-server')

if __name__ == "__main__":
    install_clickhouse()
    print("ClickHouse installed and started.")