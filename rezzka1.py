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
import ollama
from rich.table import Table
import PyInstaller
import subprocess
from PIL import Image
import platform
import socket



sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

def pc_time(cmd):
    new = datetime.datetime.now()
    print(f"Сейчас: {new}")

def cal(cmd):
  while True:
    res = input("ввод:")
    hi = eval(res)
    print(hi)
    if res == "exit":
        break

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

def msg(cmd):
    def water_pressure(cmdp):
        try:
            p = float(input("введите плостность жидкости:"))
            h = float(input("введите высоту столба жидкости:"))
            print("вычислеие....")
            time.sleep(2)
            print("гидростатическое давление равно:")
            res = p * h * 9.8
            oper = "wpr"
            print(res)

            


        except ValueError:
            print("ошибка")
        except ZeroDivisionError:
            print("ошибка")


    # давление твердого тела
    def solid_pressure(cmdp):
        try:
            f = float(input("введите силу в ньютонах(H):"))
            s = float(input("введите площадь поверхности:"))
            print("вычислеие....")
            time.sleep(2)
            print("давление твердого тела равно:")
            res = f / s
            oper = "spr"
            print(res)
          
        except ValueError:
            print("ошибка")
        except ZeroDivisionError:
            print("ошибка")
    # закон Гука
    def elastic_force(cmdp):
        try:
            k = float(input("введите коэффициент жесткости тела:"))
            l = float(input("введите удлинение или деформацию тела:"))
            print("вычислеие....")
            time.sleep(2)
            print("сила упругости равна:")
            res = k * l 
            oper = "elf" 
            print(res)
            
        except ValueError:
            print("ошибка")
        except ZeroDivisionError:
            print("ошибка")

    # плотность
        def density(cmdp):
            try:
                m = float(input("введите массу:"))
                v = float(input("введите объем:"))
                res = m/v 
                oper = "den"
                print("вычислеие....")
                time.sleep(2)
                print(res)
                
            except ValueError:
                print("ошибка")
            except ZeroDivisionError:
                print("ошибка")

    # сила тяжести
    def gravity(cmdp):
        try:
            m = float(input("введите массу:"))
            res = m * 10 
            oper = "grv"
            print("вычислеие....")
            time.sleep(2)
            print(res)
            
        except ValueError:
            print("ошибка")
        except ZeroDivisionError:
            print("ошибка")


    # скорость при прямом направлении
    def speed(cmdp):
        try:
            s = float(input("введите путь:"))
            t = float(input("введите время:"))
            res= s / t 
            oper = "spd"
            print("вычислеие....")
            time.sleep(2)
            print(res)
            history(f"Действие: {oper}||Результат: ", res)
        except ValueError:
            print("ошибка")
        except ZeroDivisionError:
            print("ошибка")
    print("доступные действия: \nwpr-water pressure\nspr-solid pressure\nelf-elastic pressure\nden-denisty\ngrv-gravity\nspd-speed")
    cmdp = input("введите действие:")
    if cmdp.lower() == "wpr":
         water_pressure(cmdp)
    elif cmdp.lower() == "spr":
         solid_pressure(cmdp)
    elif cmdp.lower() == "elf":
         elastic_force(cmdp)
    elif cmdp.lower() == "den":
           density(cmdp)
    elif cmdp.lower() == "grv":
            gravity(cmdp)
    elif cmdp.lower() == "spd":
            speed(cmdp)

        
def files(cmd):
    disk = input("введите название вашего диска, к примеру: C,D,Anoron\nввод:")
    print("доступные действия:\n создать директорию-mkdir \n создать файл-mkfile\n rm-удаление\n редактировать файл-edit\n all-все файлы в директории\n cd,cd!,cd?,cd.-переход по деректориям\n rn-переименовать\n rc-переместить")
    while True:
        cmdf = input("введите действие:")
        
        if cmdf == "mkdir":
            name = input("введите название:")

            try:
                os.makedirs(name, exist_ok=True)
                print(f"Готово! Папка '{name}' создана (или уже была).")
            except OSError as e:
                print(f"Ошибка при создании: {e}")


        elif cmdf == "mkfile":



            def create_custom_file():
                folder = input(" Введите имя папки: ").strip()
                if not os.path.exists(folder):
                    os.makedirs(folder, exist_ok=True)

                filename = input(" Введите имя файла: ").strip()
                extension = input(" Введите расширение: ").strip()
                
                if not extension.startswith("."):
                    extension = "." + extension

                full_name = filename + extension
                full_path = os.path.join(folder, full_name)

                try:
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write("")
                    
                    print(f" Готово: {os.path.abspath(full_path)}")
                    
                except Exception as e:
                    print(f" Ошибка: {e}")

            if __name__ == "__main__":
                create_custom_file()



        elif cmdf == "edit":

        
            print("режимы:\n r-чтение\n w-запись в файл с полной его очисткой\n a-запись в файл")
            gon = input("введите что хотите сделать(r,w,a):")
            if gon == "a":
                fileo = input("введите какой файл октрыть:")
                texta = input("введите что записать в файл:")
                with open(f'{fileo}', 'a', encoding='utf-8') as file:
                    file.write(texta)
                    print("текст записан")

            elif gon == "w":
                fileo = input("введите какой файл октрыть:")
                textw = input("введите что записать в файл:")
                with open(f'{fileo}', 'w', encoding='utf-8') as file:
                    file.write(textw)
                    print("текст записан")

            elif gon == "r":
                fileo = input("введите какой файл октрыть:")
                with open(f'{fileo}', 'r', encoding='utf-8') as file:
                    txt=file.read()
                    print(f"содержимое файла:\n {txt}")

            elif gon == "clear":
                clear(cmd)

        elif cmdf == "all":
            all = os.listdir('.')  
            print(f"список файлов в текущей директории:\n {all}") 

        elif cmdf == "cd":
            cd = os.chdir(fr"{disk}:\Rezzka")
        elif cmdf == 'cd.':
            cd = os.chdir(fr"{disk}:\\")
        elif cmdf == "cd!":
            i = input("введите навзание или путь:")
            cd = os.chdir(i)
        elif cmdf == "cd?":
            i = os.getcwd()
            print(i)   
        
        elif cmdf == "rn":
            rn = input("введите для переименованя\ndir-папка\nfile-файл\nввод:")
            if rn.lower() == "file":
                a = input("введите файл:")
                b = input("введите новое название :")
                res = os.rename(a,b)
                print(res)
            elif rn.lower() == "dir":
                a = input("введите папку:")
                b = input("введите новое название:")
                res = os.rename(a,b)
                print("done")

        elif cmdf == "rc":
            rc = input("Введите для перемещения:\ndir — папка\nfile — файл\nВвод: ")
                
            if rc.lower() in ["file", "dir"]:
                a = input("Введите исходный путь: ")
                b = input("Введите путь назначения: ")
                try:     
                    os.replace(a, b)
                    print("Done!")
                except FileNotFoundError:
                    print("Ошибка: указанный путь не найден.")
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            elif rc.lower == "clear":
                clear(cmd)
            else:
                print("Неверный выбор. Используйте 'dir' или 'file'.")

        elif cmdf.lower() == "rm":
          try:
            a = input("введите файл для удаления:")
            os.remove(a)
            print("done")
          except PermissionError:
            print("ошибка")

        
        elif cmdf == "clear":
            clear(cmd)
        elif cmdf == "back":
            break
        
def ping(cmd):
    it = input("ввод:")
    res = subprocess.run(["ping", "-n", "1", f"{it}"], capture_output=True, text=True)
    if res.returncode == 0:
        print("Узел доступен")
    else:
        print("Узел недоступен")

def doc(cmd):
    console = Console()
    console.print("\n[bold]           ДОКУМЕНТАЦИЯ К КОМАНДАМ           [bold]")
    console.print("[bold]time[bold]-выводит время")
    console.print("[bold]clear[bold]-очищает терминал")
    console.print("[bold]calcul[bold]-калькулятор")
    console.print("[bold]ip[bold]-выводит ip адрес")
    console.print("[bold]exit[bold]-выходит из программы")
    console.print("[bold]cpu[bold]-показывает нагрзку")
    console.print("[bold]phcalcul[bold]-физический калькулятор")
    console.print("[bold]files[bold]-работа с файлами")
    console.print("[bold]ping[bold]-проверка на доступность узла")
    console.print("[bold]help[bold]-выводит доступные команды")
    console.print("[bold]info[bold]-информация")
def helpy(cmd):
        console = Console()
        console.print("\n[bold white]ДОСТУПНЫЕ КОМАНДЫ:[/bold white]")
        console.print("  [cyan]•[/cyan] time   [cyan]•[/cyan] calcul [cyan]•[/cyan] cpu       [cyan]•[/cyan] ping   [cyan]•[/cyan]docum")
        console.print("  [cyan]•[/cyan] notes  [cyan]•[/cyan] ip     [cyan]•[/cyan] phcalcul  [cyan]•[/cyan] help   ")
        console.print("  [cyan]•[/cyan] clear  [cyan]•[/cyan] exit   [cyan]•[/cyan] files     [cyan]•[/cyan] info   ")

def inf(cmd):


        ORANGE = "\033[38;5;208m"
        BLUE = "\033[1;34m"
        RESET = "\033[0m"

        logo = [
            r"      _______   ",
            r"     /  __   \  ",
            r"    /  /_/  /   ",
            r"   /  __   /    ",
            r"  /  /  \  \    ",
            r" /  /    \  \   ",
            r"/__/      \__\  "
        ]
        info = [
            f"Rezzka .PY",
            f"-------------------",
            f"{BLUE}OS{RESET}: {platform.system()}, {platform.release()}",
            f"{BLUE}CPU{RESET}: {platform.processor()}",
            f"{BLUE}PC{RESET}: {platform.node()}",
            f"{BLUE}Local{RESET}: {socket.gethostbyname(socket.gethostname())}"
        ]
        for i in range(max(len(logo), len(info))):
            left = logo[i] if i < len(logo) else " " * 16
            right = info[i] if i < len(info) else ""
            print(f"{ORANGE}{left}{RESET} {right}")

        

# ----------------------------------------------------------------
ORANGE = "\033[38;5;208m"
BLUE = "\033[1;34m"
RESET = "\033[0m"
CYAN = "\033[36m"
logo = [
r"      _______   ",
r"     /  __   \  ",
r"    /  /_/  /   ",
r"   /  __   /    ",
r"  /  /  \  \    ",
r" /  /    \  \   ",
r"/__/      \__\  "
]
info = [

f"___________________",
f"\033[1m{CYAN} Rezzka Py{CYAN}\033[1m",
f"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾",
f"{BLUE}OS{RESET}: {platform.system()}, {platform.release()}",
f"{BLUE}CPU{RESET}: {platform.processor()}",
f"{BLUE}PC{RESET}: {platform.node()}",
f"{BLUE}Local{RESET}: {socket.gethostbyname(socket.gethostname())}"
]
for i in range(max(len(logo), len(info))):
    left = logo[i] if i < len(logo) else " " * 16
    right = info[i] if i < len(info) else ""
    print(f"{ORANGE}{left}{RESET} {right}")




commands = {
    "time": pc_time,
    "calcul": cal,
    "cpu": cpu,
    "notes": notes,
    "ip": ip,
    "phcalcul": msg,
    "files": files,
    "clear": clear,
    "ping": ping,
    "help": helpy,
    "info": inf,
    "docum": doc
}


while True:
    user_input = input(f"{platform.node()} :").strip().lower()
    if not user_input:
        continue
    if user_input in commands:
        commands[user_input](user_input)
        if user_input == "clear":
         print("")

    elif user_input in ["exit", "quit"]:
        print("Выход из программы...")
        break
    else:
        print(f"Ошибка: команда '{user_input}' не найдена. Доступные: {', '.join(commands.keys())}")


        
            

        






    


