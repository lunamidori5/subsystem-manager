
from runcommand import run_commands_async

async def localai_install(ui, manager, docker_run_command):
    n = ui.notification(timeout=None)
    n.message = f'Starting... Please wait...'
    manager.change_image("midori-ai-local-ai")
    n.spinner = True

    if manager.port == 30000:
        local_port_offset = 8080
    else:
        local_port_offset = 0
    
    port_to_use = manager.port + local_port_offset
    full_image_name_command = f"--name {manager.image}"

    print(manager.type)

    command_pre_list = []

    if "Purge".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image} && {manager.command_base} rm {manager.image}")
    
    if "Install".lower() in manager.type.lower():
        if manager.use_gpu:
            command_pre_list.append(f"{manager.command_base} {docker_run_command} -d --gpus all -p {port_to_use}:8080 {full_image_name_command} -ti localai/localai:latest-aio-gpu-nvidia-cuda-11")
        else:
            command_pre_list.append(f"{manager.command_base} {docker_run_command} -d -p {port_to_use}:8080 {full_image_name_command} -ti localai/localai:latest-aio-cpu")
        
    await run_commands_async(n, command_pre_list)

    manager.reset_image()