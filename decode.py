#!/usr/bin/python
# -*- coding: utf-8 -*-

# Created by Brilyan Okta Firmansyah // fourtyonesec
# Team : Team Pencari Proxy
# IP : 191.168.1.1
# User-Agent : Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36


import marshal
import time
import sys
import os


def decode_py3():
    try:
        output = input("[*] File output: ")
        # Paste Code Marshall in Here !!!
        # Dari tanda tanda ( sampai tanda ) ambil isi dari marshall codenya didalam marshal.loads
        # lalu pastekan disini ikuti alur nya kalau anda ingin mendapatkan sesuatu
        try:
            # Example b'\xe3\x00\x00\x00\x00\x00\'
            data = marshal.loads(
                ())  # Paste here marcode !
            xx = decompile(3.7, data, sys.stdout)
            os.system("clear")
            with open(output, "w", encoding="utf-8") as f:
                f.write(str(xx.text))
                pass
            print("[+] Successfully added file '{}' ...".format(output))
            time.sleep(2)
            print("[*] Result saved file as {}".format(output))
        except TypeError:
            print(
                "[!] a bytes-like object is required, not str please check your marcode!")
            sys.exit(1)
            pass
        pass
    except KeyboardInterrupt:
        print("[!] CTRL + C Detected !!")
        sys.exit(1)
        pass


def decode_py2():
    try:
        output = raw_input("[*] File output: ")
        try:
            # Example 'c\xe3\x00\x00\x00\x00\x00\'
            data = marshal.loads(())  # Paste here marcode !
            result = decompile(2.7, data, sys.stdout)
            os.system("clear")
            with open(output, "w") as f:
                f.write(str(result.text))
                pass
            print("[+] Successfully added file '{}' ...".format(output))
            time.sleep(2)
            print("[*] Result saved file as {}".format(output))
            pass
        except TypeError:
            print(
                "[!] a bytes-like object is required, not str please check your marcode!")
            sys.exit(1)
            pass
        pass
    except KeyboardInterrupt:
        print("[!] CTRL + C Detected !!")
        sys.exit(1)
        pass
    pass


if (sys.version[0] in "3"):
    try:
        from uncompyle6.main import decompile
        decode_py3()
        pass
    except ModuleNotFoundError:
        print(
            "[!] No module named 'uncompyle6', please install 'python3 -m pip install uncompyle6'")
        sys.exit(1)
        pass
    pass
elif (sys.version[0] in "2"):
    try:
        from uncompyle6.main import decompile
        decode_py2()
        pass
    except ImportError:
        print(
            "[!] No module named 'uncompyle6', please install 'python2 -m pip install uncompyle6'")
        sys.exit(1)
        pass
    pass
    pass
