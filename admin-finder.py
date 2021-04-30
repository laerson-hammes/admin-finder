import requests
from typing import List
from colorama import Fore, init, Style # type: ignore
import argparse


class FindDashboard(object):
   def __init__(self, /) -> None:
      options: List[str] = self.get_arguments()
      words: List[str] = self.read_wordlist(options[1])
      init(autoreset=True)
      self.get_status_code(words, options[0])


   def get_status_code(self, wordlist: List[str], hostname: str, /) -> None:
      try:
         url = "http://" + hostname
         for word in wordlist:
            result = requests.get(f"{url}/{word}")
            if result.status_code == 200:
               print(Fore.GREEN + f"[+] {result.status_code}: {url}/{word}")
            else:
               print(Fore.RED + f"[-] {result.status_code}: {url}/{word}")
      except Exception as e:
         raise Exception(e)

   
   def read_wordlist(self, file_name: str, /) -> List[str]:
      words: List[str] = []
      try:
         with open(file_name, "r") as f:
            for line in f.readlines():
               words.append(line.rstrip())
         return words
      except FileNotFoundError:
         raise Exception("[-] File not found error...")
      except Exception as e:
         raise Exception(e)
         
   
   def get_arguments(self, /) -> List[str]:
      parser = argparse.ArgumentParser()
      parser.add_argument("-hn", "--host", dest="host", help="Enter with the hostname")
      parser.add_argument("-w", "--wordlist", dest="wordlist", help="Enter with the path / filename from your wordlist")
      options = parser.parse_args()
      if not options.host:
         options.host = str(input("[+] Hostname: "))
      if not options.wordlist:
         options.wordlist = str(input("[+] Path / filename from your wordlist: "))
      return [options.host, options.wordlist]
   

if __name__ == "__main__":
   run = FindDashboard()
   

 