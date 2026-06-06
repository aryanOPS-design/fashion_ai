from .renderer import slide_1, slide_2, slide_3, slide_4, slide_5
from .template import TEMPLATES
import os


def build_carousel(content, template_name, output_dir):

    theme = TEMPLATES[template_name]

    os.makedirs(output_dir, exist_ok=True)

    slide_1(content, theme, f"{output_dir}/slide_1.jpg")
    slide_2(content, theme, f"{output_dir}/slide_2.jpg")
    slide_3(content, theme, f"{output_dir}/slide_3.jpg")
    slide_4(content, theme, f"{output_dir}/slide_4.jpg")
    slide_5(content, theme, f"{output_dir}/slide_5.jpg")