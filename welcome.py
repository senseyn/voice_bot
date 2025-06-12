import platform
import os
import shutil
import psutil


def print_start_banner():
    line_1 = r"========================================================================="

    line_2 = r"========================================================================="

    ascii_logo = r'''
    ██╗   ██╗ ██████╗ ██╗ ██████╗███████╗    ██████╗  ██████╗ ████████╗
    ██║   ██║██╔═══██╗██║██╔════╝██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██║   ██║██║   ██║██║██║     █████╗      ██████╔╝██║   ██║   ██║   
    ╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝      ██╔══██╗██║   ██║   ██║   
     ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗    ██████╔╝╚██████╔╝   ██║   
      ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                         -  V O I C E  B O T  -
'''

    # Получаем системную информацию
    os_name = platform.system()
    os_version = platform.release()
    python_ver = platform.python_version()
    cpu = platform.processor() or "Unknown CPU"

    #получение памяти диска
    path = '/'  # Указываем путь к корню файловой системы.  
    disk_info = shutil.disk_usage(path)  # Вызываем метод shutil.disk_usage() с указанным путём.  

    # Получение памяти RAM (Linux only)
    if "linux" in os_name.lower():
        mem = psutil.virtual_memory()
        mem_total = round(mem.total / (1024 ** 3), 2)
        mem_used = round(mem.used / (1024 ** 3), 2)
    elif "windows" in os_name.lower() or "darwin" in os_name.lower():
        mem = psutil.virtual_memory()
        mem_total = round(mem.total / (1024 ** 3), 2)
        mem_used = round(mem.used / (1024 ** 3), 2)
    else:
        mem_total = "False"
        mem_used = "False"

    installed_packages = len(os.popen("pip list").readlines()) - 2

    # Блок информации
    info_block = f"""
      OS:        {os_name} {os_version}
      Версия:    {platform.version().split()[0]}
      PIP:       {installed_packages}
      Версия:    Python {python_ver}
      Программа: voice_bot
      CPU:       {cpu}
      RAM:       {mem_used} MiB / {mem_total} MiB
      ПАМЯТЬ НА ДИСКЕ:
      -- Всего:        {disk_info.total / 1_000_000:.2f} MB
      -- Использовано: {disk_info.used / 1_000_000:.2f} MB
      -- Свободно:     {disk_info.free / 1_000_000:.2f} MB
    """

    # Печать цветом (ANSI ESC-коды)
    print("\033[1;35m" + line_1 + "\033[0m")
    print("\033[1;35m" + ascii_logo + "\033[0m")  # logo
    print("\033[1;35m" + info_block + "\033[1;35m")  # Green info
    print("\033[1;35m" + line_2 + "\033[0m")


if __name__ == "__main__":
    print_start_banner()
