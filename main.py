## The goal of this rework is to remove the need for docker from all backends, things like AnythingLLM will not play nice with this
## But I am hopeing that we can get this worked out, only remove these comments if we have done this and this is live

import os
import sys

from nicegui import ui, app, native

from config import image_name, image_download
from config import docker_command, docker_run_command, docker_sock_command

from update_repo import update_repo

### To add your own backends just import them here and format them like the others

from bigagi import bigagi_install
from bigagi import bigagi_two_install

from localai import localai_install

from anythingllm import anythingllm_install

### End of backends imports

temp_menu = False

if update_repo():
    sys.exit(0)

def get_docker_json():
    temp_file = "docker_ps_output.md"
    format_info = str("""{{.Names}}: ID - {{.ID}} Command - {{.Command}} \\n""")
    
    os.system(f"{docker_command} ps -a --format \"{format_info}\" > {temp_file}")

    with open(temp_file, "r") as f:
        data = f.read()
        
    os.remove(temp_file)
    return data

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

manager = Manager_mode()

def handle_toggle_change(toggle):
    value = toggle.value
    if value == 'Update':
        manager.type = 'Update Install Purge'
    elif value == 'Install':
        manager.type = 'Install'
    elif value == 'Purge':
        manager.type = 'Purge'
    else:
        print(f"Unknown Var: {str(value)}")
        manager.type = 'Install'

def handle_gput_toggle_change(toggle):
    value = toggle.value
    if value == 'Use GPU':
        manager.use_gpu = True
    elif value == 'No GPU':
        manager.use_gpu = False
    else:
        print(f"Unknown Var: {str(value)}")
        manager.use_gpu = False

ui.separator()

dark = ui.dark_mode(True)

with ui.row():
    ui.label('Switch mode:')
    ui.button('Dark', on_click=dark.enable)
    ui.button('Light', on_click=dark.disable)

ui.separator()

ui.label("To install a backend please click Install Below")

with ui.row():
    ui.label("Manager Mode:")
    toggle = ui.toggle(['Install', 'Update', 'Purge'], value='Install')
    toggle_gpu = ui.toggle(['Use GPU', 'No GPU'], value='No GPU')
    toggle.on_value_change(handle_toggle_change) 
    toggle_gpu.on_value_change(handle_gput_toggle_change) 

ui.separator()

with ui.row():
    markdown_box = ui.code(str(get_docker_json()))
    ui.update(markdown_box)
    with ui.column():
        with ui.row():
            ui.label("Manage Backends:")

        with ui.row():
            ui.input(label='Port Number', placeholder='Edit to change port', on_change=lambda e: manager.change_port(e.value))
            with ui.column():
                ui.label("LocalAI:")
                ui.button("LocalAI", on_click=lambda: localai_install(ui, manager, docker_run_command))

            with ui.column():
                ui.label("AnythingLLM:")
                ui.button("AnythingLLM", on_click=lambda: anythingllm_install(ui, manager, docker_run_command))

            with ui.column():
                ui.label("Big AGI:")
                ui.button("Big-AGI V1 (Stable)", on_click=lambda: bigagi_install(ui, manager, docker_run_command))
                ui.button("Big-AGI V2 (Beta - MUST REINSTALL EACH REBOOT)", on_click=lambda: bigagi_two_install(ui, manager, docker_run_command, docker_sock_command))

            with ui.column():
                ui.label("Mozilla AI (Blueprints):")

        #ui.button("3 - Update Backends in Subsystem", on_click=on_button_click)
        #ui.button("4 - Uninstall Backends from Subsystem", on_click=on_button_click)
        #ui.button("5 - Backend Programs (install models / edit backends)", on_click=on_button_click)
        #ui.button("6 - Subsystem and Backend News", on_click=on_button_click)

ui.run(reload=False, port=native.find_open_port())