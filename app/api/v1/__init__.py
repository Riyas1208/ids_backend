from fastapi import APIRouter
from app.api.v1.endpoints import analysis, packets, scan, pentest, auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
api_router.include_router(packets.router, prefix="/packets", tags=["packets"])
api_router.include_router(scan.router, prefix="/scan", tags=["scan"])
api_router.include_router(pentest.router, prefix="/pentest", tags=["pentest"])
