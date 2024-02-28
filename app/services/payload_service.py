from app.exceptions.xss_exception import XSSException

async def generate_content_from_payload(params, request, templates, validator):
    sanitized_els = []
    # print("Generating content from payload...")
    # print(params, request, templates, validator)

    for param in params:
        valid, sanitized = validator.validate(param)
        print("Non-sanitized", param)
        print("Sanitized", sanitized)
        if not valid:
            raise XSSException()
        sanitized_els.append(sanitized)
    return templates.TemplateResponse("basic_response.html", {"request": request, "payloads": sanitized_els})
