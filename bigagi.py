import os

from runcommand import run_commands_async

async def bigagi_install(ui, manager, docker_run_command):
    n = ui.notification(timeout=None)
    n.message = f'Starting... Please wait...'
    manager.change_image("midori-ai-big-agi")
    n.spinner = True

    if manager.port == 30000:
        local_port_offset = 3000
    else:
        local_port_offset = 0
    
    port_to_use = manager.port + local_port_offset
    full_image_name_command = f"--name {manager.image}"

    print(manager.type)

    command_pre_list = []

    if "Purge".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image} && {manager.command_base} rm {manager.image}")

    if "Install".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} {docker_run_command} -d -p {port_to_use}:3000 {full_image_name_command} -ti ghcr.io/enricoros/big-agi")
        
    await run_commands_async(n, command_pre_list)

    manager.reset_image()

async def bigagi_two_install(ui, manager, docker_run_command, docker_sock_command):
    n = ui.notification(timeout=None)
    n.message = f'Starting... Please wait...'
    runsh_path = os.path.join(".", "run.sh")
    manager.change_image("midori-ai-big-agi")
    n.spinner = True

    if manager.port == 30000:
        local_port_offset = 3000
    else:
        local_port_offset = 0
    
    image_download = "lunamidori5/pixelarch:amethyst"
    
    port_to_use = manager.port + local_port_offset
    full_image_name_command = f"--name {manager.image}"

    print(manager.type)

    starter_builder_command_list = [
        f"{manager.command_base} pull {image_download}",
        f"{manager.command_base} {docker_run_command} -d {docker_sock_command} -p {port_to_use}:3000 {full_image_name_command} {image_download} sleep infinity",
        f"{manager.dockerexec} yay -Syu --noconfirm nodejs nvm"
        ]
    
    command_pre_list = []
    builder_command_list = []

    if "Purge".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image}")
        command_pre_list.append(f"{manager.command_base} rm {manager.image}")
        
    if "Install".lower() in manager.type.lower():
        for command in starter_builder_command_list:
            command_pre_list.append(command)

        builder_command_list.append("git clone -b v2-dev https://github.com/enricoros/big-AGI.git")
        builder_command_list.append("cd big-AGI")
        builder_command_list.append("source /usr/share/nvm/init-nvm.sh")
        builder_command_list.append("nvm install 20.0 && nvm use 20.0")
        builder_command_list.append("npm ci")
        builder_command_list.append("npm run build")
        builder_command_list.append("next start --port 3000 &")

        with open(runsh_path, "w") as f:
            for line in builder_command_list:
                f.write(line)
                f.write("\n")
        
        command_pre_list.append(f"{manager.command_base} cp {runsh_path} {manager.image}:/home/midori-ai/run.sh")
        command_pre_list.append(f"{manager.dockerexec} chmod +x run.sh")
        command_pre_list.append(f"{manager.dockerexec} ls -lha")
        command_pre_list.append(f"{manager.dockerexec} bash ./run.sh")
        
    await run_commands_async(n, command_pre_list)

    os.remove(runsh_path)

    manager.reset_image()