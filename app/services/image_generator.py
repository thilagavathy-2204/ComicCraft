from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def generate_image(prompt: str, panel_number: int) -> str:
    output_dir = Path("static") / "panels"
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"panel_{panel_number}.png"
    output_path = output_dir / filename

    width = 1200
    height = 800

    image = Image.new("RGB", (width, height), "#f4ead7")
    draw = ImageDraw.Draw(image)

    draw.rectangle(
        (30, 30, width - 30, height - 30),
        outline="#6b2f2f",
        width=12
    )

    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
        text_font = ImageFont.truetype("arial.ttf", 28)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    title = f"COMIC PANEL {panel_number}"

    draw.text(
        (width // 2, 80),
        title,
        fill="#6b2f2f",
        font=title_font,
        anchor="mm"
    )

    draw.ellipse(
        (420, 230, 780, 590),
        fill="#d9a441",
        outline="#6b2f2f",
        width=8
    )

    draw.ellipse(
        (510, 330, 550, 370),
        fill="black"
    )

    draw.ellipse(
        (650, 330, 690, 370),
        fill="black"
    )

    draw.arc(
        (535, 380, 665, 500),
        start=0,
        end=180,
        fill="#6b2f2f",
        width=8
    )

    caption = f"Panel {panel_number}: AI Comic Scene"

    draw.text(
        (width // 2, 680),
        caption,
        fill="#6b2f2f",
        font=text_font,
        anchor="mm"
    )

    image.save(output_path)

    return f"/static/panels/{filename}"