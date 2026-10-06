from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.models import PromptRequest

from app.services.gemini_flash import generate_outline
from app.services.gemini_pro import generate_story
from app.services.image_generator import generate_image
from app.services.layout_builder import build_comic_layout
from app.services.exporters import save_pdf


router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)


def generate_complete_comic(
    data: PromptRequest
):

    outline = generate_outline(
        story_prompt=data.story_prompt,
        character_name=data.character_name,
        setting=data.setting,
        tone=data.tone,
        art_style=data.art_style
    )

    story = generate_story(
        outline=outline,
        character_name=data.character_name,
        tone=data.tone
    )

    image_urls = []

    for panel in outline.panels:

        image_url = generate_image(
            prompt=panel.image_prompt,
            panel_number=panel.panel_number
        )

        image_urls.append(image_url)

    layout = build_comic_layout(
        outline=outline,
        story=story,
        image_urls=image_urls
    )

    pdf_url = save_pdf(layout)

    return layout, pdf_url


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate_form(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    data = PromptRequest(
        story_prompt=story_prompt,
        character_name=character_name,
        setting=setting,
        tone=tone,
        art_style=art_style
    )

    try:

        panels, pdf_url = generate_complete_comic(data)

        return templates.TemplateResponse(
            request=request,
            name="comic_preview.html",
            context={
                "panels": [
                    panel.model_dump()
                    for panel in panels
                ],
                "pdf_url": pdf_url
            }
        )

    except Exception as exc:

        return HTMLResponse(
            content=f"""
            <html>
            <body>
                <h1>ComicCraft Error</h1>
                <pre>{type(exc).__name__}: {exc}</pre>
            </body>
            </html>
            """,
            status_code=500
        )


@router.get("/health")
async def health():

    return {
        "status": "ok"
    }
