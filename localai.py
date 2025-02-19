
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

    mount_folders = "-v /var/lib/docker/volumes/midoriai_midori-ai-models/_data:/build/models"

    docker_command = f"{manager.command_base} {docker_run_command} -d {mount_folders} -p {port_to_use}:8080"

    print(manager.type)

    command_pre_list = []

    if "Purge".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image}")
        command_pre_list.append(f"{manager.command_base} rm {manager.image}")

    if "Start".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} start {manager.image}")

    if "Shutdown".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image}")
    
    if "Install".lower() in manager.type.lower():
        if manager.use_gpu:
            command_pre_list.append(f"{docker_command} --gpus all {full_image_name_command} -ti localai/localai:latest-aio-gpu-nvidia-cuda-11")
        else:
            command_pre_list.append(f"{docker_command} {full_image_name_command} -ti localai/localai:latest-aio-cpu")
        
    await run_commands_async(n, command_pre_list)

    manager.reset_image()