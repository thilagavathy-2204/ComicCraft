from app.models import ComicOutline


def generate_outline(
    story_prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
) -> ComicOutline:

    panels = []

    for i in range(1, 6):
        panels.append({
            "panel_number": i,
            "title": f"Panel {i}",
            "scene_description": (
                f"{character_name} in a {setting} setting. "
                f"Story idea: {story_prompt}"
            ),
            "image_prompt": (
                f"{art_style} illustration of {character_name} "
                f"in a {setting}. {story_prompt}. "
                f"{tone} mood."
            ),
            "caption": f"Panel {i}",
            "narration": ""
        })

    return ComicOutline(
        panels=panels
    )