from fastapi.templating import Jinja2Templates

async def generate_content_from_payload(params, request, templates):
    return templates.TemplateResponse("basic_response.html", {"request": request, "payloads": params})