from pathlib import Path
from datetime import datetime

from fpdf import FPDF


def save_pdf(layout) -> str:

    output_dir = Path("static") / "exports"

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"comic_{timestamp}.pdf"
    )

    output_path = output_dir / filename

    pdf = FPDF()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    for panel in layout:

        pdf.add_page()

        pdf.set_font(
            "Arial",
            "B",
            18
        )

        pdf.cell(
            0,
            12,
            f"Panel {panel.panel_number}: "
            f"{panel.title}",
            ln=True
        )

        pdf.ln(5)

        pdf.set_font(
            "Arial",
            "",
            12
        )

        pdf.multi_cell(
            0,
            8,
            f"Scene:\n"
            f"{panel.scene_description}"
        )

        pdf.ln(5)

        if panel.caption:

            pdf.set_font(
                "Arial",
                "B",
                12
            )

            pdf.multi_cell(
                0,
                8,
                f"Caption: {panel.caption}"
            )

            pdf.ln(3)

        if panel.narration:

            pdf.set_font(
                "Arial",
                "",
                12
            )

            pdf.multi_cell(
                0,
                8,
                f"Narration: {panel.narration}"
            )

    pdf.output(
        str(output_path)
    )

    return f"/{output_path.as_posix()}"