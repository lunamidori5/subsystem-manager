
import asyncio

from config import spinner

async def run_commands_async(n, command_pre_list):
    for command_str in command_pre_list:
        print(command_str)
        spinner.start(text=f'Running: {command_str}')
        n.message = f'Running: {command_str}'
        command_list = command_str.split()

        process = await asyncio.create_subprocess_exec(
            *command_list,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        while True:
            stdout, stderr = await process.communicate()

            output = stdout.decode('utf-8')
            command_outerr = stderr.decode('utf-8')

            if process.returncode is not None:
                spinner.succeed(text=f"Output: {output}")
                print(output)
                await asyncio.sleep(2)
                break
            else:
                spinner.fail(text=f"Output: {output} : {command_outerr}")
                print(output)
                await asyncio.sleep(2)
                break

    await asyncio.sleep(5)

    n.message = 'Done!'
    n.spinner = False
    #markdown_box.update()
    await asyncio.sleep(25)

    n.dismiss()