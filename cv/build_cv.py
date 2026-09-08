"""Generate the two-page academic CV. Edit the content below, then rerun."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,
    HRFlowable, PageBreak, KeepTogether,
)
from PIL import Image as PILImage
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Embed Times New Roman when installed (matching the reference CV).
# On other platforms, ReportLab's standard Times family is the fallback.
font_dir = Path("/System/Library/Fonts/Supplemental")
for alias, filename in {
    "Times-Roman": "Times New Roman.ttf",
    "Times-Bold": "Times New Roman Bold.ttf",
    "Times-Italic": "Times New Roman Italic.ttf",
    "Times-BoldItalic": "Times New Roman Bold Italic.ttf",
}.items():
    if (font_dir / filename).exists():
        pdfmetrics.registerFont(TTFont(alias, str(font_dir / filename)))
pdfmetrics.registerFontFamily("Times-Roman", normal="Times-Roman",
                             bold="Times-Bold", italic="Times-Italic",
                             boldItalic="Times-BoldItalic")

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "files" / "CV_HyunkyuKang.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
WIDTH = A4[0] - 76

body = ParagraphStyle("Body", fontName="Times-Roman", fontSize=10.5,
                      leading=12.7, spaceAfter=3.5, textColor=colors.black)
bold = ParagraphStyle("Bold", parent=body, fontName="Times-Bold", spaceAfter=2)
italic = ParagraphStyle("Italic", parent=body, fontName="Times-Italic", spaceAfter=3)
bullet = ParagraphStyle("Bullet", parent=body, leftIndent=12, firstLineIndent=0,
                        bulletIndent=0, spaceAfter=3)
caption = ParagraphStyle("Caption", parent=italic, fontSize=9.3, leading=11,
                         alignment=TA_CENTER, spaceBefore=5, spaceAfter=5)
heading = ParagraphStyle("Heading", parent=bold, fontSize=12, leading=14,
                         spaceBefore=12, spaceAfter=3, keepWithNext=True)
name = ParagraphStyle("Name", parent=bold, fontSize=19, leading=22, alignment=TA_CENTER)
contact = ParagraphStyle("Contact", parent=body, fontSize=10, leading=12,
                         alignment=TA_CENTER, spaceAfter=0)

story = []

def p(text, style=body):
    return Paragraph(text, style)

def add(text, style=body):
    story.append(p(text, style))

def section(text):
    story.append(p(text.upper(), heading))
    rule = HRFlowable(width="100%", thickness=0.55, color=colors.black, spaceAfter=5)
    rule.keepWithNext = True
    story.append(rule)

def entry(left, right=""):
    table = Table([[p(left, bold), p(right, ParagraphStyle(
        "Date", parent=bold, alignment=2))]], colWidths=[WIDTH*.72, WIDTH*.28])
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(table)

def bullets(*items):
    for text in items:
        story.append(Paragraph(text, bullet, bulletText="•"))

def figure(filename, width, text):
    path = ROOT / "images" / "research" / filename
    with PILImage.open(path) as im:
        ratio = im.height / im.width
    story.append(KeepTogether([
        Spacer(1, 4),
        Image(str(path), width=width, height=width*ratio, hAlign="CENTER"),
        p(text, caption),
    ]))

def repo(name, label="Code"):
    return f'<link href="https://github.com/khk0606/{name}" color="#174c92"><u>{label}</u></link>'

add("Hyunkyu Kang", name)
add('<link href="mailto:khk0606khk@gmail.com">khk0606@gmail.com</link>'
    ' | <link href="https://github.com/khk0606">github.com/khk0606</link>'   
    ' | South Korea', contact)
add('<link href="https://khk0606.github.io">khk0606.github.io</link>', contact)

section("Research Interests")
add("My research interests lie in human–scene interaction, affordance-aware motion generation, "
    "Robotics, and embodied AI. I study how language, spatial relationships, and interaction "
    "history can guide context-appropriate behavior, with an emphasis on reliable data "
    "pipelines and reproducible evaluation.")

section("Education")
entry("Chung-Ang University", "March 2021 - February 2027(Expected)")
add("Bachelor of School of Art and Technology", italic)
add("Bachelor of Science in Cyber Security (Convergence Major)", italic)

section("Research Experience")
entry("Chung-Ang University", "Jul 2026 – Current")
add("Coexistent Reality and Intelligent Agents Lab | Advisor: Prof. Taeil Jin", italic)
bullets(
    "Worked on language-based 3D scene understanding and purpose- and history-conditioned affordance maps.",
    "Designed a scene-point/body-part representation and implemented motion preprocessing, "
    "coordinate validation, and teacher–student training and evaluation components.",
)

section("Representative Research")
add("Purpose- and History-Conditioned Affordance-Aware Motion Generation", bold)
add("Ongoing research | " + repo("ADM-MoE-Teacher"), italic)
bullets(
    "Designed an affordance representation over 8,192 scene points and six body parts, "
    "combining purpose, scene geometry, and interaction history.",
    "Implemented teacher adaptation, contact supervision, point-alignment checks, and "
    "checkpoint auditing within an ADM/LoRA and mixture-of-experts research workflow.",
    "Established strict multi-object evaluation gates and documented checkpoint limitations; "
    "end-to-end performance remains under evaluation.",
)
figure("relafford-dual-weight-moe.png", 480,
       "Proposed teacher–student pipeline for purpose- and history-conditioned affordances. "
       "End-to-end performance remains under evaluation.")

story.append(PageBreak())
section("Research and Projects")
add("Video2Unity: Transformer-Based Motion Refinement", bold)
add("AI &amp; ML course project, Fall 2025 | " + repo("AI_ML_Video2Unity-Final"), italic)
bullets(
    "Developed a video-to-animation pipeline using BlazePose 3D landmarks and a "
    "TensorFlow/Keras Transformer encoder to refine 33-joint poses from 30-frame sequences.",
    "Applied root-centered normalization, denoising training, Savitzky-Golay smoothing, "
    "and floor alignment to address temporal jitter and grounding artifacts.",
    "Integrated refined motion into a Unity dance performance with motion interpolation, "
    "scripted camera tracking, and lighting; evaluated motion smoothness and foot-contact "
    "behavior on a held-out video.",
)

story.append(Spacer(1, 6))
add("Video-to-Robot Motion Transfer", bold)
add("Simulation prototype | " + repo("Zero-Shot-Video-to-Robot-Motion-Transfer"), italic)
bullets(
    "Connected reference-video interpretation to structured motion specifications, JAX reward "
    "functions, and Dial-MPC control for a Unitree Go2 model in MuJoCo/MJX.",
    "Worked on startup holds, velocity ramps, warm starts, and joint-limit safeguards. "
    "Validation is simulation-based, not a physical-robot deployment.",
)

story.append(Spacer(1, 6))
add("Korean Hate-Speech Robustness under Text Obfuscation", bold)
add("NLP evaluation | " + repo("Korean-Hate-Speech-Robustness-under-Text-Obfuscation"), italic)
bullets(
    "Evaluated a balanced 500-comment K-MHaS subset across five variants "
    "(2,500 predictions per system), comparing character-based, KoELECTRA, and Qwen-based pipelines.",
    "Measured normalization and calibration trade-offs; normalization + character TF-IDF MLP "
    "achieved 0.772 worst-condition balanced accuracy on the evaluated benchmark.",
)

section("Technical Experience")
add("<b>Programming and ML:</b> Python, PyTorch, NumPy, scikit-learn, Hugging Face Transformers")
add("<b>Motion and simulation:</b> HumanML263, Unity/YBot motion processing, MuJoCo/MJX, JAX")
add("<b>Research workflows:</b> Git, Linux, LoRA adaptation, experiment auditing, visualization")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 8)
    canvas.setFillColor(colors.HexColor("#666666"))
    canvas.drawString(32, 19, "Hyunkyu Kang | Curriculum Vitae")
    canvas.drawRightString(A4[0]-32, 19, str(doc.page))
    canvas.restoreState()

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, rightMargin=32, leftMargin=32,
    topMargin=27, bottomMargin=31, title="Hyunkyu Kang — Curriculum Vitae",
    author="Hyunkyu Kang", subject="Academic curriculum vitae",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
