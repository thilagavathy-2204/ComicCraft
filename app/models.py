from pydantic import BaseModel
from typing import List


class PromptRequest(BaseModel):
    story_prompt: str
    character_name: str
    setting: str
    tone: str
    art_style: str


class ComicPanel(BaseModel):
    panel_number: int
    title: str
    scene_description: str
    image_prompt: str
    caption: str = ""
    narration: str = ""


class ComicOutline(BaseModel):
    panels: List[ComicPanel]


class GenerateResponse(BaseModel):
    panels: List[ComicPanel]
    pdf_url: str