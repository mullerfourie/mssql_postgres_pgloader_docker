import os
import subprocess

os.system('docker-compose up -d')

mssqlIP = subprocess.Popen(['docker', 'inspect', '-f', '\'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}\'', 'sql-server-db'])

postgresIP = os.system(['docker', 'inspect', '-f', '\'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}\'', 'postgres'])

cmd = 'docker run --security-opt seccomp=unconfined \
           --rm \
           --name pgloader \
           dimitri/pgloader:latest pgloader \
           mysql://user:pass@%s/dbname postgresql://user:pass@%s/dbname' % (mssqlIP, postgresIP)
os.system(cmd)