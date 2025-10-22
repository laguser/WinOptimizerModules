# modules.py - продвинутый оптимизатор
# Категории: Очистка, Система, Сеть, Производительность, Безопасность

# --- Очистка ---
def clean_temp():
    import subprocess
    subprocess.run("del /q/f/s %TEMP%\\*", shell=True)
    subprocess.run("del /q/f/s C:\\Windows\\Temp\\*", shell=True)
    return "Временные файлы удалены!"

def clean_cache():
    import subprocess
    subprocess.run("del /q/f/s %LOCALAPPDATA%\\Microsoft\\Windows\\INetCache\\*", shell=True)
    return "Кэш браузеров и приложений очищен!"

def clean_logs():
    import subprocess
    subprocess.run("del /q/f/s C:\\Windows\\Logs\\*", shell=True)
    return "Системные логи очищены!"

# --- Система ---
def disable_telemetry():
    import subprocess
    services = ["DiagTrack", "dmwappushservice"]
    for service in services:
        subprocess.run(f"sc stop {service}", shell=True)
        subprocess.run(f"sc config {service} start=disabled", shell=True)
    return "Телеметрия отключена!"

def disable_search_indexing():
    import subprocess
    subprocess.run("sc stop WSearch", shell=True)
    subprocess.run("sc config WSearch start=disabled", shell=True)
    return "Поиск Windows отключен!"

def visual_effects_off():
    import subprocess
    subprocess.run("SystemPropertiesPerformance.exe", shell=True)
    return "Визуальные эффекты отключены!"

# --- Сеть ---
def optimize_network():
    import subprocess
    subprocess.run("netsh int tcp set global autotuninglevel=normal", shell=True)
    subprocess.run("netsh int tcp set global chimney=enabled", shell=True)
    subprocess.run("netsh int tcp set global congestionprovider=ctcp", shell=True)
    return "Сетевые параметры оптимизированы!"

def disable_ipv6():
    import subprocess
    subprocess.run("netsh interface ipv6 set disabled", shell=True)
    return "IPv6 отключен!"

# --- Производительность ---
def fps_boost():
    import subprocess
    subprocess.run("powercfg -setactive SCHEME_MIN", shell=True)
    return "Режим высокой производительности включен!"

def memory_cleaner():
    import ctypes
    ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
    return "Память очищена!"

def disable_background_apps():
    import subprocess
    subprocess.run("powershell \"Get-Process | Where-Object {$_.MainWindowHandle -eq 0} | Stop-Process\"", shell=True)
    return "Фоновые приложения остановлены!"

# --- Безопасность ---
def disable_defender():
    import subprocess
    subprocess.run("sc stop WinDefend", shell=True)
    subprocess.run("sc config WinDefend start=disabled", shell=True)
    return "Windows Defender отключен!"

def firewall_on():
    import subprocess
    subprocess.run("netsh advfirewall set allprofiles state on", shell=True)
    return "Брандмауэр включен!"

def firewall_off():
    import subprocess
    subprocess.run("netsh advfirewall set allprofiles state off", shell=True)
    return "Брандмауэр выключен!"
