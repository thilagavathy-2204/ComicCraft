import os
import json

from google import genai


def generate_outline(
    story_prompt: str,
    character_name: str,
    setting: str,
    tone: str,
    art_style: str
):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing from the .env file."
        )

    client = genai.Client(
        api_key=api_key
    )

    prompt = f"""
Create a structured 5-panel comic outline.

Story prompt:
{story_prompt}

Main character:
{character_name}

Setting:
{setting}

Tone:
{tone}

Art style:
{art_style}

For each of the 5 panels provide:

- panel_number
- title
- scene_description
- image_prompt

Return ONLY valid JSON in this format:

{{
  "panels": [
    {{
      "panel_number": 1,
      "title": "Panel title",
      "scene_description": "Scene description",
      "image_prompt": "Detailed image generation prompt"
    }}
  ]
}}

Make the five panels form one continuous story.
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

    data = json.loads(text)

    return data