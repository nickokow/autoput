'''Файл hosts.csv должен лежать рядом со скриптом. Список хостов вписать после блока IP в столбец в файле hosts.csv '''
import paramiko
import csv
local_file = '/path/to/file.foo' #тут указать название с которым он копируется
remote_path = '/remote/path/to/file.foo' #Тут полный путь к файлу
with open('hosts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ssh_host = row['IP']
        print(ssh_host)
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.load_system_host_keys('/path/to/ssh_pub_key')
        ssh_client.connect(
        row['IP'],
        username='username',
        )
        ftp_client=ssh_client.open_sftp()
        ftp_client.put(local_file,remote_path)
        ftp_client.close()
        command = 'hostname'
        (stdin, stdout, stderr) = ssh_client.exec_command(command)
        for line in stdout.readlines():
                print(line, end = '')
        ssh_client.close()
