
from config import image_name
from config import docker_command

class Manager_mode:
    def __init__(self):
        self.type = "Install"
        self.command_base = docker_command
        self.image = image_name
        self.dockerexec = f"{self.command_base} exec {self.image}"
        self.dockerbuilder = f"{self.dockerexec}" 
        self.port = 30000
        self.use_gpu = False
    
    def check_type(self, command_in):
        if self.type == "Update Install Purge":
            print("Updating")
        elif self.type == 'Install':
            print("Installing")
        elif self.type == 'Purge':
            print("Purging")
    
    def change_port(self, port):
        try:
            self.port = int(port)
        except Exception as error:
            self.port = 30000
    
    def reset_image(self):
        self.image = image_name
        self.dockerexec = f"{self.command_base} exec {self.image}"
        self.dockerbuilder = f"{self.dockerexec}" 
    
    def change_image(self, new_image):
        self.image = new_image
        self.dockerexec = f"{self.command_base} exec {self.image}"
        self.dockerbuilder = f"{self.dockerexec}" 