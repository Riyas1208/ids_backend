from fastapi import APIRouter
from typing import List
from app.schemas import PacketOut
import random, uuid, datetime
router = APIRouter()

def simulate_packet():
    rnd = random.Random()
    pkt_id = str(uuid.uuid4())[:8]
    ts = datetime.datetime.utcnow().isoformat()
    src = f'192.168.{rnd.randint(0,255)}.{rnd.randint(1,254)}'
    dst = f'10.0.{rnd.randint(0,255)}.{rnd.randint(1,254)}'
    status = 'attack' if rnd.random() < 0.14 else 'normal'
    meta = {'proto': rnd.choice(['TCP','UDP','ICMP']), 'size': rnd.randint(40,1500), 'score': round(rnd.random(),3)}
    return {"id": pkt_id, "timestamp": ts, "src": src, "dst": dst, "status": status, "meta": meta}

@router.get('/', response_model=List[PacketOut])
def recent_packets(limit: int = 20):
    limit = max(1, min(200, limit))
    return [simulate_packet() for _ in range(limit)]
