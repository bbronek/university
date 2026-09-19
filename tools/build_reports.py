from pathlib import Path

import reportlab
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Table,
    TableStyle,
)

FONT_DIRECTORY = Path(reportlab.__file__).parent / "fonts"
pdfmetrics.registerFont(TTFont("ReportSans", str(FONT_DIRECTORY / "Vera.ttf")))
pdfmetrics.registerFont(TTFont("ReportSans-Bold", str(FONT_DIRECTORY / "VeraBd.ttf")))
pdfmetrics.registerFontFamily(
    "ReportSans",
    normal="ReportSans",
    bold="ReportSans-Bold",
    italic="ReportSans",
    boldItalic="ReportSans-Bold",
)

ROOT = Path(__file__).resolve().parents[1]
INK = colors.HexColor("#152B3C")
TEAL = colors.HexColor("#087F8C")
LIGHT = colors.HexColor("#EDF5F6")
styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ReportTitle",
        fontName="ReportSans-Bold",
        fontSize=27,
        leading=31,
        textColor=INK,
        spaceAfter=9,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportSubtitle",
        fontName="ReportSans",
        fontSize=10,
        leading=14,
        textColor=TEAL,
        spaceAfter=19,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportHeading",
        fontName="ReportSans-Bold",
        fontSize=12,
        leading=16,
        textColor=TEAL,
        spaceBefore=14,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="ReportBody",
        fontName="ReportSans",
        fontSize=10,
        leading=14,
        textColor=INK,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="Cell", fontName="ReportSans", fontSize=9, leading=12, textColor=INK
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderCell",
        fontName="ReportSans-Bold",
        fontSize=9,
        leading=12,
        textColor=colors.white,
    )
)


def paragraph(text, style="ReportBody"):
    return Paragraph(text, styles[style])


def table(rows, widths):
    content = [
        [paragraph(str(cell), "HeaderCell" if index == 0 else "Cell") for cell in row]
        for index, row in enumerate(rows)
    ]
    result = Table(content, colWidths=widths, repeatRows=1, hAlign="LEFT")
    result.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), INK),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [LIGHT, colors.white]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("LINEBELOW", (0, -1), (-1, -1), 0.5, TEAL),
            ]
        )
    )
    return result


def page_number(canvas, document):
    canvas.setFont("ReportSans", 8)
    canvas.setFillColor(INK)
    canvas.drawRightString(A4[0] - 46, 26, str(document.page))


def build(path, title, story):
    document = SimpleDocTemplate(
        str(ROOT / path),
        pagesize=A4,
        rightMargin=46,
        leftMargin=46,
        topMargin=39,
        bottomMargin=42,
        title=title,
        author="Bartosz Bronikowski",
    )
    document.build(story, onFirstPage=page_number, onLaterPages=page_number)


def machine_learning_report():
    story = [
        paragraph("Swiss house-type classification", "ReportTitle"),
        paragraph("MACHINE LEARNING PROJECT  /  06-DUMAUI0 2021/SL", "ReportSubtitle"),
        paragraph("Objective", "ReportHeading"),
        paragraph(
            "Predict the type of a Swiss residential property from its price, floor area, number of rooms, and location."
        ),
        paragraph("Data", "ReportHeading"),
        paragraph(
            "The original report records 16,701 examples: 13,361 for training and 3,340 for testing. Missing numerical values were replaced with the mean; missing categorical values were replaced with the most frequent value."
        ),
        paragraph(
            'Source: <link href="https://www.kaggle.com/datasets/etiennekaiser/switzerland-house-price-prediction-data" color="#087F8C">Switzerland House Price Prediction Data, Etienne Kaiser / Kaggle</link>.'
        ),
        paragraph("Models described in the original report", "ReportHeading"),
        paragraph(
            "<b>Logistic regression, with and without L2 regularization.</b> The report describes third-degree polynomial features and mini-batch gradient descent with batches of 100."
        ),
        paragraph(
            "<b>Gaussian naive Bayes.</b> Class-conditional features were modeled with normal distributions."
        ),
        paragraph(
            "<b>Neural network.</b> One hidden layer with 32 ReLU units, a softmax output layer, and the Adam optimizer."
        ),
        paragraph("Recorded results", "ReportHeading"),
        table(
            [
                ["Model", "Accuracy", "Precision", "Recall", "F1 score"],
                ["Logistic regression + L2", "0.5862", "0.4092", "0.5862", "0.4625"],
                [
                    "Logistic regression, no regularization",
                    "0.5877",
                    "0.4331",
                    "0.5877",
                    "0.4866",
                ],
                ["Gaussian naive Bayes", "0.3051", "0.5529", "0.3051", "0.3737"],
                ["Neural network", "0.6686", "0.7140", "0.6686", "0.6007"],
            ],
            [191, 77, 79, 77, 79],
        ),
        paragraph("Conclusions", "ReportHeading"),
        paragraph(
            "The neural network achieved the highest recorded values for all four metrics. The two logistic regression models performed similarly. Naive Bayes had lower accuracy but higher precision than either logistic regression model."
        ),
        paragraph("Reproducibility", "ReportHeading"),
        paragraph(
            "These values are translated historical results, not a new benchmark. The archived script used standard scikit-learn logistic regression without polynomial feature expansion or the stated mini-batch optimizer. The refactored script retains the implemented model families and now fits preprocessing only on training data. The source CSV is not included, so these scores have not been reproduced. An 80/20 scikit-learn split of 16,701 rows produces 13,360 training and 3,341 test rows, differing from the counts recorded above."
        ),
    ]
    build(
        "semester7/machine-learning/project/report.pdf",
        "Swiss House-Type Classification",
        story,
    )


def flight_report():
    story = [
        paragraph("Flight delay analysis", "ReportTitle"),
        paragraph(
            "DATABASES  /  BARTOSZ BRONIKOWSKI  /  30 APRIL 2021", "ReportSubtitle"
        ),
        paragraph("Overview", "ReportHeading"),
        paragraph(
            "English edition of the recorded database-query results. Delay values are in minutes."
        ),
        table(
            [
                ["Measure", "Recorded value"],
                ["Average arrival delay", "15.9115212681785"],
                ["Maximum arrival delay", "1,895"],
                [
                    "Pearson correlation: arrival and departure delays",
                    "0.971705844958789",
                ],
            ],
            [340, 163],
        ),
        paragraph("Flight with the longest arrival delay", "ReportHeading"),
        paragraph(
            "American Airlines (AA), 26 July 2017: Kona, HI to Los Angeles, CA. Arrival delay: 1,895 minutes."
        ),
        paragraph("Average arrival delay by weekday", "ReportHeading"),
        table(
            [
                ["Weekday", "Delay (minutes)"],
                *zip(
                    [
                        "Friday",
                        "Monday",
                        "Wednesday",
                        "Thursday",
                        "Saturday",
                        "Tuesday",
                        "Sunday",
                    ],
                    [
                        "20.8074719",
                        "18.0480054",
                        "16.1051434",
                        "15.6469562",
                        "15.2187565",
                        "12.8805641",
                        "12.776057",
                    ],
                ),
            ],
            [340, 163],
        ),
        PageBreak(),
        paragraph("Average arrival delay by airline", "ReportHeading"),
        table(
            [
                ["Airline", "Delay (minutes)"],
                *zip(
                    [
                        "JetBlue Airways (B6)",
                        "ExpressJet Airlines Inc. (EV)",
                        "Frontier Airlines Inc. (F9)",
                        "American Airlines Inc. (AA)",
                        "Spirit Air Lines (NK)",
                        "United Air Lines Inc. (UA)",
                        "SkyWest Airlines Inc. (OO)",
                        "Virgin America (VX)",
                        "Southwest Airlines Co. (WN)",
                        "Delta Air Lines Inc. (DL)",
                        "Alaska Airlines Inc. (AS)",
                        "Hawaiian Airlines Inc. (HA)",
                    ],
                    [
                        "28.8411481",
                        "19.2545055",
                        "18.9802997",
                        "18.3753142",
                        "18.0657512",
                        "16.9504026",
                        "16.8082728",
                        "13.964467",
                        "13.8239826",
                        "12.2587877",
                        "7.4539275",
                        "4.2027194",
                    ],
                ),
            ],
            [340, 163],
        ),
        paragraph("Reproduction", "ReportHeading"),
        paragraph(
            "The source queries are in analysis.Rmd. Re-running them requires the original Flight_delays, Weekdays, and Airlines tables and an ODBC connection. No database queries were rerun while translating this report."
        ),
    ]
    build(
        "semester2/databases/flight-analysis/analysis.pdf",
        "Flight Delay Analysis",
        story,
    )


if __name__ == "__main__":
    machine_learning_report()
    flight_report()
