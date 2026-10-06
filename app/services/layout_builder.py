from typing import List
from app.models import ComicPanel


def build_comic_layout(
    outline,
    story,
    image_urls: List[str]
) -> List[ComicPanel]:

    panels = []
    story_panels = {}

    if isinstance(story, dict):
        for item in story.get("panels", []):
            story_panels[item.get("panel_number")] = item

    for index, panel in enumerate(
        outline.panels
        if hasattr(outline, "panels")
        else outline.get("panels", []),
        start=1
    ):

        panel_number = (
            panel.panel_number
            if hasattr(panel, "panel_number")
            else panel.get("panel_number", index)
        )

        title = (
            panel.title
            if hasattr(panel, "title")
            else panel.get("title", f"Panel {index}")
        )

        scene_description = (
            panel.scene_description
            if hasattr(panel, "scene_description")
            else panel.get("scene_description", "")
        )

        image_prompt = (
            panel.image_prompt
            if hasattr(panel, "image_prompt")
            else panel.get("image_prompt", "")
        )

        image_url = (
            image_urls[index - 1]
            if index - 1 < len(image_urls)
            else ""
        )

        story_data = story_panels.get(
            panel_number,
            {}
        )

        panels.append(
            ComicPanel(
                panel_number=panel_number,
                title=title,
                scene_description=scene_description,
                image_prompt=image_prompt,
                image_url=image_url,
                caption=story_data.get("caption", ""),
                narration=story_data.get("narration", "")
            )
        )

    return panels