
import os
import socket

import configparser

from halo import Halo

image_download = "lunamidori5/pixelarch:subsystem"
image_name = "midori_ai_subsystem_pixelarch"

spinner = Halo(text='Loading', spinner='dots', color='green')

config = configparser.ConfigParser()
config.read('config.ini')

docker_socket = config['docker']['sock']
docker_command = config['docker']['command']

docker_sock_command = f"-v {docker_socket}:/var/run/docker.sock"

docker_run_command = "run --restart always"

if not os.path.exists(docker_socket):
    print("Docker socket not found at:", docker_socket)
    needs_sudo = True
else:
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            s.connect(docker_socket)
            s.send(b"GET /info HTTP/1.0\r\n\r\n")
            response = s.recv(4096)
            if b"HTTP/1.1 200 OK" in response:
                needs_sudo = False
            else:
                needs_sudo = True
    except PermissionError:
        needs_sudo = True
    except Exception as e:
        print(f"An error occurred: {e}")
        needs_sudo = True

if needs_sudo:
    docker_command = "sudo " + docker_command