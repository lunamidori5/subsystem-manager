

import configparser

from halo import Halo

image_download = "lunamidori5/pixelarch:subsystem"
image_name = "midori_ai_subsystem_pixelarch"

spinner = Halo(text='Loading', spinner='dots', color='green')

config = configparser.ConfigParser()
config.read('config.ini')

docker_command = config['docker']['command']
docker_sock = config['docker']['sock']

docker_sock_command = f"-v {docker_sock}:/var/run/docker.sock"

docker_run_command = "run --restart always"