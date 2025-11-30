import asyncio, re
from typing import Tuple, List

async def run_command(cmd: list, timeout: int = 30) -> Tuple[int, str, str]:
    try:
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            return -1, '', 'timeout'
        return proc.returncode, stdout.decode(errors='ignore'), stderr.decode(errors='ignore')
    except FileNotFoundError:
        return -2, '', f'tool-not-found: {cmd[0]}'
    except Exception as e:
        return -3, '', str(e)

def parse_nmap_ports(output: str) -> List[int]:
    ports = []
    for line in output.splitlines():
        m = re.match(r'^(\d{1,5})/tcp\s+open', line)
        if m:
            try:
                ports.append(int(m.group(1)))
            except:
                pass
    return sorted(list(set(ports)))
