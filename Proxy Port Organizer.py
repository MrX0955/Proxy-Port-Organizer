import os,sys
if sys.platform == "win32": os.system("cls")
elif sys.platform == "linux": os.system("clear")
print("""\n                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                                        █░██░██░██░██░██░██░██░██░██░░░░░░░░░░█
                                        █░██░██░██░██░██░██░██░██░██░░░░░░░░░░█
                                        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ░░█░░░░█▀▀▀█░█▀▀█░█▀▀▄░▀█▀░█▄░░█░█▀▀█░░
                                        ░░█░░░░█░░░█░█▄▄█░█░░█░░█░░█░█░█░█░▄▄░░
                                        ░░█▄▄█░█▄▄▄█░█░░█░█▄▄▀░▄█▄░█░░▀█░█▄▄█░░
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")
os.system("pip install pystyle")
os.system("pip install colorama")
os.system("pip install pywin32-ctypes")
os.system("start https://discord.gg/7d2mE3j8WK")
if sys.platform == "win32": os.system("cls")
elif sys.platform == "linux": os.system("clear")
from pystyle    import Colors, Colorate
from colorama   import Fore
import ctypes

class Raymond:
    ctypes.windll.kernel32.SetConsoleTitleW("Raymond & MrX | Proxy Port Range Organizer | Developer: MrX#3051 |")
    print(Colorate.Horizontal(Colors.purple_to_red,"""
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                        ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
                                        ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
                                        ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
                                        ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
                                        ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
                                        ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
                                        ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
                                        ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
                                        ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
                                        ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
                                        ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
                                        ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
                                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",1))
    ip = input(f"\n {Fore.YELLOW}> "+Colorate.Diagonal(Colors.rainbow,"Ip Gir ~ MrX#3051: ",3))
    port = int(input(f"\n {Fore.YELLOW}> "+Colorate.Diagonal(Colors.rainbow,"Port gir ~ MrX#3051: ",4))) -1
    max = int(input(f"\n {Fore.YELLOW}> "+Colorate.Diagonal(Colors.rainbow, "Kaçıncı Porta Kadar Oluşturacaksın?: ",4)))
    proxy = ""
    z = int(max)-int(port)-1
    while port < max:
        port += 1
        proxy += ip + ":" + str(port) + "\n"
    with open(f"{z}x IPv6[{ip}].txt", "a") as MrX: MrX.write(proxy.strip())
