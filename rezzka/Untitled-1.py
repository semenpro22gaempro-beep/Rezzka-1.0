from rich.console import Console
import pyfiglet
import sys
import io
import datetime
import psutil
import time
import platform
import socket
import os
from rich.table import Table

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

def pc_time(cmd):
    new = datetime.datetime.now()
    print(f"Сейчас: {new}")

def cal(cmd):
  try:
    num1 = float(input("введите 1 число:"))
    num2 = float(input("введите 2 число:"))
    go = input("введите действие(*,+,-,/,**):")
    print("считаем...")
    time.sleep(2)
    if go == "+":
        res1 = num1 + num2
        print(res1)
    elif go == "-":
        res3 = num1 - num2
        print(res3)
    elif go == "*":
        res4 = num1 * num2
        print(res4)
    elif go == "/":
        res5 = num1 / num2
        print(res5)
    elif go == "**":
        res6 = num1 ** num2
        print(res6)

  except ValueError:
    print("Ошибка, введите числа")
  except ZeroDivisionError:
    print("Ошибка, на ноль нельзя делить")

def cpu(cmd):
    print(f"Нагрузка CPU: {psutil.cpu_percent(interval=1)}%")
    time.sleep(2)
    print(f"По ядрам: {psutil.cpu_percent(interval=1, percpu=True)}")
                          

def notes(cmd):
    print("файл с текстом по умолчанию notes.txt")
    print("режимы:\n r-чтение\n w-запись в файл с полной его очисткой\n a-запись в файл")
    gon = input("введите что хотите сделать(r,w,a):")
    if gon == "a":
        texta = input("введите что записать в файл:")
        with open('notes.txt', 'a', encoding='utf-8') as file:
            file.write(texta)
            print("текст записан")
    if gon == "w":
        textw = input("введите что записать в файл:")
        with open('notes.txt', 'w', encoding='utf-8') as file:
            file.write(textw)
            print("текст записан")
    if gon == "r":
        with open('notes.txt', 'r', encoding='utf-8') as file:
           txt=file.read()
           print(f"содержимое файла:\n {txt}")
            
def ip(cmd):
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Имя хоста: {hostname}")
    print(f"Локальный IP: {ip_address}")

def clear(cmd):
    os.system('cls' if os.name == 'nt' else 'clear')
    



console = Console()



ascii_text = pyfiglet.figlet_format("Rezzka")
console.print(ascii_text, style="bold white")
table = Table(title="[bold magenta] [/bold magenta]", show_header=False, border_style="white")
table.add_row("Операционка", f"[green]{platform.system()} {platform.release()}[/green]")
table.add_row("Процессор", f"[yellow]{platform.processor()}[/yellow]")
table.add_row("Имя ПК", f"[cyan]{platform.node()}[/cyan]")
table.add_row("Локальный IP", f"[white]{socket.gethostbyname(socket.gethostname())}[/white]")

console.print(table)


console.print("\n[bold white]ДОСТУПНЫЕ КОМАНДЫ:[/bold white]")
console.print("  [cyan]•[/cyan] time   [cyan]•[/cyan] calcul [cyan]•[/cyan] cpu")
console.print("  [cyan]•[/cyan] notes  [cyan]•[/cyan] ip     [cyan]•[/cyan] msg")
console.print("  [cyan]•[/cyan] clear  [cyan]•[/cyan] exit\n")


while True: 
    cmd = input(f"{platform.node()} :")
    if cmd == "time":
        pc_time(cmd)
    if cmd == "clear":
        clear(cmd)
    elif cmd == "calcul":
        cal(cmd)
    elif cmd == "cpu":
        cpu(cmd)
    elif cmd == "notes":
        notes(cmd)
    elif cmd == "ip":
        ip(cmd)
    elif cmd == "msg":
        msg(cmd)
    elif cmd == "exit":
        break




    else:
        print("такой команды нет")
    


