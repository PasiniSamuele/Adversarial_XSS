from fastapi import APIRouter, status, HTTPException, Request
from app.request_models.basic_request import BasicRequest
from fastapi.responses import HTMLResponse
import logging
from app.services import payload_service

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post(
    "/",
    status_code = status.HTTP_200_OK
)
async def vuln_request(request: Request,params:BasicRequest):
    template = await payload_service.generate_content_from_payload(params.payload, request, request.app.package["templates"])
    return template

@router.get(
    "/{payload}",
    status_code = status.HTTP_200_OK
)
async def vuln_request(request: Request,payload:str):
    template = await payload_service.generate_content_from_payload([payload], request, request.app.package["templates"])
    return template