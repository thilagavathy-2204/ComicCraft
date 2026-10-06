import os
import json

from dotenv import load_dotenv

load_dotenv()

from google import genai
def generate_story(
    outline,
    character_name: str,
    tone: str
):
    if hasattr(outline, "model_dump"):
        outline_data = outline.model_dump()
    else:
        outline_data = outline

    panels = outline_data.get("panels", [])

    story_panels = []

    for panel in panels:

        panel_number = panel.get(
            "panel_number",
            len(story_panels) + 1
        )

        story_panels.append({
            "panel_number": panel_number,
            "caption": panel.get(
                "caption",
                f"Panel {panel_number}"
            ),
            "narration": (
                f"{character_name} continues "
                f"the adventure in a {tone} way."
            ),
            "dialogue": (
                f"{character_name}: "
                f"What an amazing adventure!"
            )
        })

    return {
        "panels": story_panels
    }