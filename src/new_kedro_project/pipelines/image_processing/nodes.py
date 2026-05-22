from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter


def process_image(
    input_path,
    output_path,
    rotation_angle,
    filter_name,
    watermark_text,
):
    image = Image.open(input_path)

    # Rotar la imagen y expandir el lienzo para que se note el giro
    rotated = image.rotate(rotation_angle, expand=True)

    filters = {
        "EMBOSS": ImageFilter.EMBOSS,
        "FIND_EDGES": ImageFilter.FIND_EDGES,
        "BLUR": ImageFilter.BLUR,
    }

    selected_filter = filters.get(
        filter_name,
        ImageFilter.EMBOSS
    )

    filtered = rotated.filter(selected_filter)

    draw = ImageDraw.Draw(filtered)

    draw.text(
        (20, 20),
        watermark_text,
        fill="white"
    )

    filtered.save(output_path)

    return output_path