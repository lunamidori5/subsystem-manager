## The goal of this rework is to remove the need for docker from all backends, things like AnythingLLM will not play nice with this
## But I am hopeing that we can get this worked out, only remove these comments if we have done this and this is live

import os
import sys

from nicegui import ui, app, native

from config import image_name
from config import image_download

from config import docker_command

from config import docker_run_command
from config import docker_run_rm_command

from config import docker_sock_command
from config import volumes, update_volume_config

from manager import Manager_mode

from update_repo import update_repo

### To add your own backends just import them here and format them like the others

from bigagi import bigagi
from bigagi import bigagi_two

from ollama import ollama
from localai import localai

from invokeai import invokeai

from anythingllm import anythingllm

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

manager = Manager_mode()

def handle_toggle_change(toggle):
    value = toggle.value
    if value == 'Update':
        manager.type = 'Update Install Purge'
    elif value == 'Install':
        manager.type = 'Install'
    elif value == 'Purge':
        manager.type = 'Purge'
    elif value == 'Start':
        manager.type = 'Start'
    elif value == 'Shutdown':
        manager.type = 'Shutdown'
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

def handle_gpu_type_toggle_change(toggle):
    value = str(toggle.value)
    if value.lower() == 'nvidia':
        manager.gpu_type = "nvidia"
    elif value.lower() == 'amd':
        manager.gpu_type = "amd"
    else:
        print(f"Unknown Var: {str(value)}")
        manager.gpu_type = "unknown"

ui.separator()

dark = ui.dark_mode(True)

with ui.row():
    ui.label('Switch mode:')
    ui.button('Dark', on_click=dark.enable)
    ui.button('Light', on_click=dark.disable)

ui.separator()

with ui.splitter(reverse=True) as splitter:
    with splitter.before:

        with ui.row():
            ui.label("Manager Mode:")
            toggle = ui.toggle(['Start', 'Install', 'Update', 'Shutdown', 'Uninstall'], value='Install')
            toggle.on_value_change(handle_toggle_change) 

        with ui.row():
            ui.label("Support GPU:")
            toggle_gpu = ui.toggle(['Use GPU', 'No GPU'], value='No GPU')
            toggle_gpu.on_value_change(handle_gput_toggle_change) 

        with ui.row():
            ui.label("GPU Type:")
            toggle_gpu_type = ui.toggle(['Nvidia', 'AMD'], value='Nvidia')
            toggle_gpu_type.on_value_change(handle_gpu_type_toggle_change) 

        with ui.row():
            markdown_box = ui.code(str(get_docker_json()))
            ui.update(markdown_box)

    with splitter.after:
        with ui.row():

            ui.label("Settings:")
            ui.input(label='Port Number', placeholder='Edit to change port', on_change=lambda e: manager.change_port(e.value))

        with ui.row():
            ui.label("Volume Mounts:")
        with ui.column():
            localai_box = ui.input(label='LocalAI', value=volumes['localai'])
            ollama_box = ui.input(label='Ollama', value=volumes['ollama'])
            invoke_box = ui.input(label='InvokeAI', value=volumes['invokeai'])
            ui.button("Save Mounts", on_click=lambda: update_volume_config({'localai': localai_box.value, 'ollama': ollama_box.value, 'invokeai': invoke_box.value}))

        ui.separator()

        with ui.row():

            ui.label("LRM / LLM Backends:")

            with ui.column():
                ui.button("LocalAI", on_click=lambda: localai(ui, manager, docker_run_command))

            with ui.column():
                ui.button("Ollama", on_click=lambda: ollama(ui, manager, docker_run_command))

        ui.separator()

        with ui.row():

            ui.label("Chat WebUi:")

            with ui.column():
                ui.button("AnythingLLM", on_click=lambda: anythingllm(ui, manager, docker_run_command))

            with ui.column():
                ui.button("Big-AGI V1 (Stable)", on_click=lambda: bigagi(ui, manager, docker_run_command))
                ui.button("Big-AGI V2 (Beta)", on_click=lambda: bigagi_two(ui, manager, docker_run_rm_command, docker_sock_command))

        ui.separator()

        with ui.row():

            ui.label("Photo Making:")

            with ui.column():
                ui.button("InvokeAI", on_click=lambda: invokeai(ui, manager, docker_run_command))

        ui.separator()

        with ui.row():
            ui.label("Mozilla AI (Blueprints):")

        ui.separator()

        #ui.button("3 - Update Backends in Subsystem", on_click=on_button_click)
        #ui.button("4 - Uninstall Backends from Subsystem", on_click=on_button_click)
        #ui.button("5 - Backend Programs (install models / edit backends)", on_click=on_button_click)
        #ui.button("6 - Subsystem and Backend News", on_click=on_button_click)

ui.run(reload=True, port=native.find_open_port())