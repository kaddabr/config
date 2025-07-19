import os

# Очистка файла .xsession-errors
os.system("cat /dev/null > .xsession-errors")

# Установка атрибута "immutable" для файла .xsession-errors
os.system("sudo chattr +i .xsession-errors")

# Увеличение swap файла
os.system("sudo swapoff /swapfile")  # Отключение swap файла
os.system("sudo fallocate -l 8G /swapfile")  # Установка размера swap файла (например, 2G)
os.system("sudo mkswap /swapfile")  # Форматирование swap файла
os.system("sudo swapon /swapfile")  # Включение swap файла

# Добавление строк в конец файла /etc/modprobe.d/alsa-base.conf
with open('/etc/modprobe.d/alsa-base.conf', 'a') as f:
    f.write("# micro\n")
    f.write("options snd-hda-intel model=generic\n")

# Команды для редактирования файла default.pa и отключения Bluetooth
os.system("sudo sed -Ei '/load-module module-bluetooth*/s/^/#/' /etc/pulse/default.pa")  # Закомментировать строку
os.system("sudo systemctl disable --now bluetooth")  # Отключить Bluetooth
