from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class AnalyzeSummary(BaseModel):
    file: str
    total_rows: int
    attack_count: int
    normal_count: int
    timestamp: datetime

class PacketOut(BaseModel):
    id: str
    timestamp: str
    src: str
    dst: str
    status: str
    meta: Dict[str, Any]

class ScanTarget(BaseModel):
    target: str = Field(..., description='IP or hostname')
    timeout: Optional[int] = Field(30, ge=5, le=300)

class PortScanResult(BaseModel):
    target: str
    open_ports: List[int]
    raw: Optional[str] = None

class HttpScanIssue(BaseModel):
    url: str
    issue: str
    severity: Optional[str] = 'medium'

class HttpScanResult(BaseModel):
    target: str
    issues: List[HttpScanIssue]
    raw: Optional[str] = None

class PentestResult(BaseModel):
    target: str
    tool: str
    summary: Dict[str, Any]
    raw: Optional[str] = None
