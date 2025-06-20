from modules.colors import GREEN, RESET

def helper():
    text = f"""\
    --command               Передача произвольной команды. Первыми параметром
                            необходимо передать файл txt или csv. Вторым 
                            параметром в кавычках передать команду. В фигурных
                            скобках {{}} необходимо указать server, как
                            переменную. Пример:
                            {GREEN}python3 controller.py --command server.txt "ls -l"
                            {RESET}
    
    --check-count           Параметр применяется к серверам для рассылки.
                            Отображает количество имейлов в базе и количество
                            отправленных писем. Более подробная информация в
                            ControllerVDS/README.md. Вторым параметром передать
                            файл csv или txt с серверами. Пример:
                            {GREEN}python3 controller.py --check-count server.txt{RESET}
                            
    --divide-base           Разделение одной базы на несколько. Первым параметром
                            передаем --divide-base, вторым - базу, которую делим,
                            последним параметром - количество баз, которые мы должны
                            получить. Пример:
                            {GREEN}python3 controller.py --divide-base Clutch.csv 10{RESET}

    --cp-base               Копирование баз из Base/ по серверам. Достаточно передать 
                            док с серверами вторым параметром. Отправленные базы будут
                            перемещены в Done/ 
                            Пример:
                            {GREEN}python3 controller.py --cp-base servers.txt{RESET}

    --add-key               Отправка ключа ssh на сервер. Вторым параметром передаем
                            файл с серверами, последним - сам ключ. Пример:
                            {GREEN}python3 controller.py --add-key servers.txt 'ssh-ed25519 key'{RESET}
    """
    return text
