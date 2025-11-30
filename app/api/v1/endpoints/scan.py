from fastapi import APIRouter, HTTPException, Depends
from app.schemas import ScanTarget, PortScanResult, HttpScanResult, HttpScanIssue
from app.core.security import require_api_key
from app.services.scan_service import run_command, parse_nmap_ports
router = APIRouter()

@router.post('/port', response_model=PortScanResult)
async def port_scan(payload: ScanTarget, ok: bool = Depends(require_api_key)):
    target = payload.target.strip()
    timeout = payload.timeout or 30
    if not target:
        raise HTTPException(status_code=400, detail='Missing target')
    cmd = ['nmap','-Pn','-sT','-p','1-1024','-T4',target]
    code, out, err = await run_command(cmd, timeout=timeout)
    if code == -2:
        raise HTTPException(status_code=503, detail='nmap not available')
    if code < 0:
        raise HTTPException(status_code=500, detail=f'scan failed: {err}')
    ports = parse_nmap_ports(out)
    return PortScanResult(target=target, open_ports=ports, raw=out)
