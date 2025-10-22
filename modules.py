# modules.py на GitHub

def clean_temp():
    import subprocess
    subprocess.run("del /q/f/s %TEMP%\\*", shell=True)
    subprocess.run("del /q/f/s C:\\Windows\\Temp\\*", shell=True)
    return "Временные файлы удалены!"

def disable_telemetry():
    import subprocess
    services = ["DiagTrack", "dmwappushservice"]
    for service in services:
        subprocess.run(f"sc stop {service}", shell=True)
        subprocess.run(f"sc config {service} start=disabled", shell=True)
    return "Телеметрия отключена!"

def optimize_network():
    import subprocess
    subprocess.run("netsh int tcp set global autotuninglevel=normal", shell=True)
    subprocess.run("netsh int tcp set global chimney=enabled", shell=True)
    return "Сеть оптимизирована!"

def fps_boost():
    import subprocess
    subprocess.run("powercfg -setactive SCHEME_MIN", shell=True)
    return "Режим высокой производительности включен!"

def disable_defender():
    import subprocess
    subprocess.run("sc stop WinDefend", shell=True)
    subprocess.run("sc config WinDefend start=disabled", shell=True)
    return "Windows Defender отключен!"
