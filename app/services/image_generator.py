import os
import re
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def generate_image(prompt: str, panel_number: int) -> str:

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing from the .env file."
        )

    output_dir = Path("static") / "panels"
    output_dir.mkdir(parents=True, exist_ok=True)

    safe_prompt = re.sub(
        r"[^a-zA-Z0-9_-]+",
        "_",
        prompt
    )[:50]

    filename = f"panel_{panel_number}_{safe_prompt}.png"
    output_path = output_dir / filename

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"]
        )
    )

    for part in response.parts:
        if part.inline_data is not None:
            image = part.as_image()
            image.save(output_path)
            return f"/static/panels/{filename}"

    raise RuntimeError(
        "Gemini did not return an image."
    )