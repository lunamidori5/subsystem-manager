from runcommand import run_commands_async

async def anythingllm_install(ui, manager, docker_run_command):
    n = ui.notification(timeout=None)
    n.message = f'Starting... Please wait...'
    manager.change_image("midori-ai-anythingllm")
    n.spinner = True

    if manager.port == 30000:
        local_port_offset = 3001
    else:
        local_port_offset = 0
    
    port_to_use = manager.port + local_port_offset
    full_image_name_command = f"--name {manager.image}"

    print(manager.type)
    
    command_pre_list = []

    if "Purge".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} stop {manager.image}")
        command_pre_list.append(f"{manager.command_base} rm {manager.image}")
        
    if "Install".lower() in manager.type.lower():
        command_pre_list.append(f"{manager.command_base} {docker_run_command} -d -p {port_to_use}:3001 {full_image_name_command} --cap-add SYS_ADMIN -v anythingllm:/app/server/storage -e STORAGE_DIR=\"/app/server/storage\" mintplexlabs/anythingllm")
        
    await run_commands_async(n, command_pre_list)

    manager.reset_image()