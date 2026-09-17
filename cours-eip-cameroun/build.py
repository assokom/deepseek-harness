# -*- coding: utf-8 -*-
"""Génère cours_eip_cameroun.tex (source LaTeX) et cours_eip_cameroun.pdf.

    python3 build.py            -> les deux fichiers
    python3 build.py --tex      -> LaTeX seulement (aucune dépendance)

Le PDF est produit avec ReportLab, car aucune distribution TeX n'est disponible
dans cet environnement. Le .tex produit est autonome et compilable avec
pdflatex/lualatex sur une machine disposant de TeX Live.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from content import CONTENT, SOURCES, DATE_MAJ  # noqa: E402

TITLE = "Le Président de la République et le Parlement au Cameroun"
SUBTITLE = "Cours complet de droit constitutionnel"
AUDIENCE = "Préparation au concours de la Police — Élève Inspecteur de Police (EIP)"

BOX_LABEL = {
    "key": "À retenir",
    "warn": "Point de vigilance",
    "method": "Méthode concours",
    "def": "Définition",
}

# ══════════════════════════════════════════════════════════════════════
#  LaTeX
# ══════════════════════════════════════════════════════════════════════

LATEX_SPECIALS = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
    "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
    "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def tex_escape(s):
    return "".join(LATEX_SPECIALS.get(c, c) for c in s)


def tex_inline(s):
    """Échappe puis rend **gras** et les repères [S1]."""
    out = tex_escape(s)
    out = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", out, flags=re.S)
    out = re.sub(r"\[(S\d+)\]", r"\\src{\1}", out)
    return out


def tex_doc():
    L = []
    a = L.append
    a(r"% !TEX TS-program = pdflatex")
    a(r"% Cours EIP — Président de la République et Parlement du Cameroun")
    a(r"% Généré par build.py à partir de content.py. Données arrêtées au " + DATE_MAJ + ".")
    a(r"\documentclass[11pt,a4paper,oneside]{report}")
    a(r"\usepackage[utf8]{inputenc}")
    a(r"\usepackage[T1]{fontenc}")
    a(r"\usepackage[french]{babel}")
    a(r"\usepackage[a4paper,margin=2.2cm,headheight=15pt]{geometry}")
    a(r"\usepackage{lmodern}")
    a(r"\usepackage{microtype}")
    a(r"\usepackage{booktabs,tabularx,longtable,array}")
    a(r"\usepackage{enumitem}")
    a(r"\usepackage{xcolor}")
    a(r"\usepackage[most]{tcolorbox}")
    a(r"\usepackage{titlesec}")
    a(r"\usepackage{fancyhdr}")
    a(r"\usepackage{lastpage}")
    a(r"\usepackage{hyperref}")
    a(r"\usepackage{xurl}")
    a("")
    a(r"\definecolor{navy}{HTML}{12304A}")
    a(r"\definecolor{bluec}{HTML}{1F5A83}")
    a(r"\definecolor{gold}{HTML}{C9962E}")
    a(r"\definecolor{redc}{HTML}{A73535}")
    a(r"\definecolor{greenc}{HTML}{2E6B4F}")
    a(r"\definecolor{paleblue}{HTML}{E7F0F5}")
    a(r"\definecolor{palegold}{HTML}{FBF5E7}")
    a(r"\definecolor{palered}{HTML}{FBEDED}")
    a(r"\definecolor{palegrey}{HTML}{F1F4F6}")
    a("")
    a(r"\hypersetup{colorlinks=true,linkcolor=navy,urlcolor=bluec,")
    a(r"  pdftitle={" + tex_escape(TITLE) + r"},pdfauthor={Préparation EIP},")
    a(r"  pdfsubject={Droit constitutionnel camerounais}}")
    a(r"\setlength{\parindent}{0pt}")
    a(r"\setlength{\parskip}{5pt}")
    a(r"\setlist[itemize]{leftmargin=1.4em,itemsep=2pt,topsep=3pt}")
    a(r"\setlist[enumerate]{leftmargin=1.9em,itemsep=2pt,topsep=3pt}")
    a(r"\renewcommand{\arraystretch}{1.25}")
    a("")
    a(r"\newcommand{\src}[1]{\textcolor{bluec}{\scriptsize[#1]}}")
    a(r"\newtcolorbox{keybox}[1][]{enhanced,breakable,colback=paleblue,colframe=bluec,"
      r"boxrule=.6pt,arc=2pt,fonttitle=\bfseries\color{navy},#1}")
    a(r"\newtcolorbox{warnbox}[1][]{enhanced,breakable,colback=palered,colframe=redc,"
      r"boxrule=.6pt,arc=2pt,fonttitle=\bfseries\color{redc},#1}")
    a(r"\newtcolorbox{methodbox}[1][]{enhanced,breakable,colback=palegold,colframe=gold,"
      r"boxrule=.6pt,arc=2pt,fonttitle=\bfseries\color{navy},#1}")
    a(r"\newtcolorbox{defbox}[1][]{enhanced,breakable,colback=palegrey,colframe=greenc,"
      r"boxrule=.6pt,arc=2pt,fonttitle=\bfseries\color{greenc},#1}")
    a("")
    a(r"\titleformat{\chapter}[display]{\normalfont\sffamily\bfseries\color{navy}}"
      r"{\filleft\large\chaptertitlename\ \thechapter}{6pt}{\Huge\filright}"
      r"[\vspace{5pt}{\color{gold}\titlerule[1.2pt]}]")
    a(r"\titlespacing*{\chapter}{0pt}{-12pt}{20pt}")
    a(r"\titleformat{\section}{\normalfont\sffamily\Large\bfseries\color{bluec}}{\thesection}{.6em}{}")
    a(r"\titleformat{\subsection}{\normalfont\sffamily\large\bfseries\color{navy}}{\thesubsection}{.6em}{}")
    a("")
    a(r"\pagestyle{fancy}")
    a(r"\fancyhf{}")
    a(r"\fancyhead[L]{\sffamily\small Préparation EIP · Institutions du Cameroun}")
    a(r"\fancyhead[R]{\sffamily\small\nouppercase{\leftmark}}")
    a(r"\fancyfoot[L]{\sffamily\scriptsize Données arrêtées au " + DATE_MAJ + r"}")
    a(r"\fancyfoot[R]{\sffamily\scriptsize\thepage\ / \pageref{LastPage}}")
    a(r"\renewcommand{\chaptermark}[1]{\markboth{#1}{}}")
    a(r"\renewcommand{\headrulewidth}{.4pt}")
    a("")
    a(r"\begin{document}")
    # couverture
    a(r"\begin{titlepage}\centering\vspace*{2.5cm}")
    a(r"{\sffamily\large\color{navy}RÉPUBLIQUE DU CAMEROUN\\[2pt]Paix — Travail — Patrie}\\[1.4cm]")
    a(r"{\color{gold}\rule{\textwidth}{2pt}}\\[.8cm]")
    a(r"{\sffamily\bfseries\color{navy}\Huge " + tex_escape(TITLE) + r"}\\[.9cm]")
    a(r"{\color{gold}\rule{\textwidth}{2pt}}\\[1.2cm]")
    a(r"{\sffamily\Large " + tex_escape(SUBTITLE) + r"}\\[.5cm]")
    a(r"{\sffamily\large " + tex_escape(AUDIENCE) + r"}")
    a(r"\vfill")
    a(r"{\sffamily\small Édition de travail — données arrêtées au " + DATE_MAJ + r"\\[3pt]")
    a(r"Constitution du 2 juin 1972 révisée en 1996, 2008 et 2026 · Code électoral · "
      r"Assemblée nationale · Sénat}")
    a(r"\end{titlepage}")
    a(r"\tableofcontents")
    a(r"\clearpage")

    for block in CONTENT:
        kind = block[0]
        if kind == "chapter":
            a(r"\chapter{" + tex_escape(block[1]) + "}")
        elif kind == "section":
            a(r"\section{" + tex_escape(block[1]) + "}")
        elif kind == "subsection":
            a(r"\subsection{" + tex_escape(block[1]) + "}")
        elif kind == "p":
            a(tex_inline(block[1]))
            a("")
        elif kind in ("ul", "ol"):
            env = "itemize" if kind == "ul" else "enumerate"
            a(r"\begin{" + env + "}")
            for it in block[1]:
                a(r"  \item " + tex_inline(it))
            a(r"\end{" + env + "}")
        elif kind == "table":
            heads, rows, widths = block[1], block[2], block[3]
            spec = " ".join(
                r">{\raggedright\arraybackslash}p{%.3f\textwidth}" % (w * 0.93) for w in widths)
            a(r"\begin{longtable}{" + spec + "}")
            a(r"\toprule")
            a(" & ".join(r"\textbf{\color{navy}" + tex_inline(h) + "}" for h in heads) + r" \\")
            a(r"\midrule\endhead")
            for row in rows:
                a(" & ".join(tex_inline(c) for c in row) + r" \\")
                a(r"\addlinespace[1pt]")
            a(r"\bottomrule")
            a(r"\end{longtable}")
        elif kind == "box":
            genre, title, text = block[1], block[2], block[3]
            env = {"key": "keybox", "warn": "warnbox",
                   "method": "methodbox", "def": "defbox"}[genre]
            a(r"\begin{" + env + "}[title={" + tex_escape(BOX_LABEL[genre]) +
              " — " + tex_escape(title) + "}]")
            for i, para in enumerate(text.split("\n")):
                if i:
                    a("")
                a(tex_inline(para))
            a(r"\end{" + env + "}")
        elif kind == "qcm":
            a(r"\begin{enumerate}[label=\textbf{Q\arabic*.},leftmargin=2.4em]")
            for q, opts in block[1]:
                letters = ["A", "B", "C", "D"]
                line = r"  \item " + tex_inline(q) + r"\\" + "\n  "
                line += r" \quad ".join(
                    r"\textbf{%s.} %s" % (letters[i], tex_inline(o)) for i, o in enumerate(opts))
                a(line)
            a(r"\end{enumerate}")
        elif kind == "dl":
            a(r"\begin{description}[style=nextline,leftmargin=3.2cm,labelwidth=2.9cm]")
            for term, definition in block[1]:
                a(r"  \item[" + tex_escape(term) + "] " + tex_inline(definition))
            a(r"\end{description}")

    # sources
    a(r"\chapter{Sources et vérification}")
    a("Les règles exposées proviennent des textes normatifs ci-dessous. Les données "
      "d'actualité (titulaires de fonctions) sont issues de sources de presse concordantes et "
      "sont datées dans le corps du document. Avant l'épreuve, vérifier la dernière version "
      "publiée au Journal officiel.")
    a("")
    a(r"\begin{description}[style=nextline,leftmargin=1.3cm,labelwidth=1cm]")
    for sid, desc, url in SOURCES:
        a(r"  \item[" + sid + "] " + tex_escape(desc) + r" \\ \url{" + url + "}")
    a(r"\end{description}")
    a(r"\begin{keybox}[title={À retenir — dernier conseil}]")
    a("Le jour du concours : si la question porte sur un titulaire ou une composition "
      "politique, préciser la date de référence. Si elle porte sur une compétence, citer "
      "l'article de la Constitution. La précision juridique vaut mieux qu'une réponse longue.")
    a(r"\end{keybox}")
    a(r"\end{document}")
    return "\n".join(L) + "\n"


# ══════════════════════════════════════════════════════════════════════
#  PDF (ReportLab)
# ══════════════════════════════════════════════════════════════════════

def build_pdf(path):
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                    Table, TableStyle, KeepTogether, PageBreak)
    from reportlab.platypus.tableofcontents import TableOfContents

    F = "/usr/share/fonts/truetype/dejavu/"
    pdfmetrics.registerFont(TTFont("DJ", F + "DejaVuSerif.ttf"))
    pdfmetrics.registerFont(TTFont("DJ-B", F + "DejaVuSerif-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("DJS", F + "DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DJS-B", F + "DejaVuSans-Bold.ttf"))
    for base, bold in (("DJ", "DJ-B"), ("DJS", "DJS-B")):
        pdfmetrics.registerFontFamily(base, normal=base, bold=bold,
                                      italic=base, boldItalic=bold)

    NAVY = colors.HexColor("#12304A")
    BLUE = colors.HexColor("#1F5A83")
    GOLD = colors.HexColor("#C9962E")
    RED = colors.HexColor("#A73535")
    GREEN = colors.HexColor("#2E6B4F")
    GREY = colors.HexColor("#5C6B77")
    PALE = {"key": colors.HexColor("#E7F0F5"), "warn": colors.HexColor("#FBEDED"),
            "method": colors.HexColor("#FBF5E7"), "def": colors.HexColor("#F1F4F6")}
    EDGE = {"key": BLUE, "warn": RED, "method": GOLD, "def": GREEN}

    body = ParagraphStyle("body", fontName="DJ", fontSize=9.3, leading=13.6,
                          alignment=TA_JUSTIFY, spaceAfter=5, textColor=colors.HexColor("#1B252D"))
    h1 = ParagraphStyle("h1", fontName="DJS-B", fontSize=19, leading=23,
                        textColor=NAVY, spaceAfter=2)
    h2 = ParagraphStyle("h2", fontName="DJS-B", fontSize=12.6, leading=16,
                        textColor=BLUE, spaceBefore=13, spaceAfter=4)
    h3 = ParagraphStyle("h3", fontName="DJS-B", fontSize=10.5, leading=14,
                        textColor=NAVY, spaceBefore=9, spaceAfter=3)
    li = ParagraphStyle("li", parent=body, spaceAfter=2.5)
    boxtitle = ParagraphStyle("bt", fontName="DJS-B", fontSize=9.6, leading=13, spaceAfter=3)
    boxbody = ParagraphStyle("bb", parent=body, fontSize=9.1, leading=13.2, spaceAfter=3)
    cellh = ParagraphStyle("ch", fontName="DJS-B", fontSize=8.8, leading=11.6,
                           textColor=colors.white)
    cell = ParagraphStyle("cl", fontName="DJ", fontSize=8.5, leading=11.6)
    toc_ch = ParagraphStyle("tc", fontName="DJS-B", fontSize=10, leading=17,
                            textColor=NAVY, spaceBefore=5)
    toc_se = ParagraphStyle("ts", fontName="DJ", fontSize=8.8, leading=13.4,
                            leftIndent=14, textColor=colors.HexColor("#33414C"))

    def esc(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def fmt(s):
        out = esc(s)
        out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out, flags=re.S)
        out = re.sub(r"\[(S\d+)\]",
                     r'<font size="7" color="#1F5A83">[\1]</font>', out)
        return out

    def P(txt, st=body):
        return Paragraph(fmt(txt), st)

    PW, PH = A4
    LM = RM = 19 * mm
    TM, BM = 22 * mm, 18 * mm
    FW = PW - LM - RM

    state = {"chapter": ""}

    def deco(canvas, doc, cover=False):
        canvas.saveState()
        if not cover:
            canvas.setFont("DJS", 7.4)
            canvas.setFillColor(GREY)
            canvas.drawString(LM, PH - TM + 9, "Préparation EIP · Institutions du Cameroun")
            canvas.drawRightString(PW - RM, PH - TM + 9, state["chapter"][:58])
            canvas.setStrokeColor(GOLD)
            canvas.setLineWidth(0.7)
            canvas.line(LM, PH - TM + 5, PW - RM, PH - TM + 5)
            canvas.setStrokeColor(colors.HexColor("#C9CFD4"))
            canvas.setLineWidth(0.4)
            canvas.line(LM, BM - 6, PW - RM, BM - 6)
            canvas.setFont("DJS", 7.2)
            canvas.drawString(LM, BM - 15, "Données arrêtées au " + DATE_MAJ)
            canvas.setFillColor(NAVY)
            canvas.setFont("DJS-B", 8)
            canvas.drawRightString(PW - RM, BM - 15, str(doc.page))
        canvas.restoreState()

    class Doc(BaseDocTemplate):
        def afterFlowable(self, flowable):
            if hasattr(flowable, "_toc"):
                lvl, text = flowable._toc
                if lvl == 0:
                    state["chapter"] = text
                self.notify("TOCEntry", (lvl, text, self.page))

    doc = Doc(path, pagesize=A4, leftMargin=LM, rightMargin=RM,
              topMargin=TM, bottomMargin=BM, title=TITLE,
              author="Préparation EIP", subject="Droit constitutionnel camerounais")
    frame = Frame(LM, BM, FW, PH - TM - BM, id="n",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame],
                     onPage=lambda c, d: deco(c, d, cover=True)),
        PageTemplate(id="main", frames=[frame], onPage=deco),
    ])

    S = []

    # ── couverture ───────────────────────────────────────────────
    center = ParagraphStyle("c", fontName="DJS", fontSize=11, leading=16, alignment=TA_CENTER)
    S.append(Spacer(1, 26 * mm))
    S.append(Paragraph('<font name="DJS-B" size="12" color="#12304A">RÉPUBLIQUE DU CAMEROUN</font>'
                       '<br/><font name="DJS" size="10" color="#5C6B77">Paix — Travail — Patrie</font>',
                       center))
    S.append(Spacer(1, 14 * mm))
    S.append(Table([[""]], colWidths=[FW], rowHeights=[2.4],
                   style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)])))
    S.append(Spacer(1, 9 * mm))
    S.append(Paragraph('<font name="DJS-B" size="25" color="#12304A">'
                       'LE PRÉSIDENT DE LA RÉPUBLIQUE<br/>ET LE PARLEMENT<br/>AU CAMEROUN</font>',
                       ParagraphStyle("t", alignment=TA_CENTER, fontName="DJS-B",
                                      fontSize=25, leading=32)))
    S.append(Spacer(1, 9 * mm))
    S.append(Table([[""]], colWidths=[FW], rowHeights=[2.4],
                   style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)])))
    S.append(Spacer(1, 12 * mm))
    S.append(Paragraph('<font name="DJS-B" size="13" color="#1F5A83">' + esc(SUBTITLE) + "</font>",
                       ParagraphStyle("s", alignment=TA_CENTER, fontSize=13, leading=18)))
    S.append(Spacer(1, 4 * mm))
    S.append(Paragraph('<font name="DJS" size="11">' + esc(AUDIENCE) + "</font>", center))
    S.append(Spacer(1, 40 * mm))
    S.append(Table(
        [[Paragraph('<font name="DJS-B" size="9" color="#12304A">Édition de travail</font>'
                    '<font name="DJS" size="9"> — données institutionnelles arrêtées au '
                    + DATE_MAJ + '.</font><br/>'
                    '<font name="DJ" size="8.6">Textes de référence : Constitution du 2 juin 1972 '
                    'révisée par la loi n° 96/06 du 18 janvier 1996, la loi n° 2008/001 du '
                    '14 avril 2008 et la révision promulguée le 14 avril 2026 ; loi n° 2012/001 '
                    'portant Code électoral ; documents officiels de l’Assemblée nationale et du '
                    'Sénat.</font>',
                    ParagraphStyle("cv", fontName="DJ", fontSize=9, leading=13,
                                   alignment=TA_CENTER))]],
        colWidths=[FW],
        style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F1F4F6")),
            ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#C9CFD4")),
            ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ])))
    S.append(PageBreak())

    # ── sommaire ────────────────────────────────────────────────
    S.append(Paragraph('<font name="DJS-B" size="17" color="#12304A">Sommaire</font>',
                       ParagraphStyle("toch", spaceAfter=10)))
    toc = TableOfContents()
    toc.levelStyles = [toc_ch, toc_se]
    S.append(toc)
    S.append(PageBreak())

    def bullets(items, ordered=False):
        rows = []
        for i, it in enumerate(items):
            mark = ("%d." % (i + 1)) if ordered else "•"
            rows.append([Paragraph('<font name="DJS-B" color="#1F5A83">%s</font>' % mark,
                                   ParagraphStyle("m", fontName="DJS-B", fontSize=9,
                                                  leading=13.6, textColor=BLUE)),
                         P(it, li)])
        t = Table(rows, colWidths=[13 if not ordered else 18, FW - (13 if not ordered else 18)])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (0, -1), 4), ("LEFTPADDING", (1, 0), (1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
        ]))
        return t

    def make_table(heads, rows, widths):
        cw = [w * FW for w in widths]
        data = [[Paragraph(fmt(h), cellh) for h in heads]]
        for r in rows:
            data.append([Paragraph(fmt(c), cell) for c in r])
        t = Table(data, colWidths=cw, repeatRows=1)
        st = [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C2CBD2")),
            ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
            ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                st.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F5F8FA")))
        t.setStyle(TableStyle(st))
        return t

    def make_box(genre, title, text):
        inner = [Paragraph('<font color="%s">%s — %s</font>'
                           % ("#" + EDGE[genre].hexval()[2:], esc(BOX_LABEL[genre]), esc(title)),
                           boxtitle)]
        for para in text.split("\n"):
            inner.append(P(para, boxbody))
        t = Table([[inner]], colWidths=[FW])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALE[genre]),
            ("BOX", (0, 0), (-1, -1), 0.5, EDGE[genre]),
            ("LINEBEFORE", (0, 0), (0, -1), 3, EDGE[genre]),
            ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]))
        return [Spacer(1, 3), t, Spacer(1, 6)]

    def heading(text, level):
        if level == 0:
            p = Paragraph(esc(text), h1)
            p._toc = (0, text)
            rule = Table([[""]], colWidths=[FW], rowHeights=[1.6],
                         style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)]))
            return [PageBreak(), p, Spacer(1, 3), rule, Spacer(1, 8)]
        if level == 1:
            p = Paragraph(esc(text), h2)
            p._toc = (1, text)
            return [p]
        return [Paragraph(esc(text), h3)]

    for block in CONTENT:
        kind = block[0]
        if kind == "chapter":
            S += heading(block[1], 0)
        elif kind == "section":
            S += heading(block[1], 1)
        elif kind == "subsection":
            S += heading(block[1], 2)
        elif kind == "p":
            S.append(P(block[1]))
        elif kind == "ul":
            S.append(bullets(block[1]))
            S.append(Spacer(1, 4))
        elif kind == "ol":
            S.append(bullets(block[1], ordered=True))
            S.append(Spacer(1, 4))
        elif kind == "table":
            S.append(Spacer(1, 3))
            S.append(make_table(block[1], block[2], block[3]))
            S.append(Spacer(1, 6))
        elif kind == "box":
            S += make_box(block[1], block[2], block[3])
        elif kind == "qcm":
            letters = ["A", "B", "C", "D"]
            for i, (q, opts) in enumerate(block[1], 1):
                choices = "&nbsp;&nbsp;".join(
                    '<font name="DJS-B" color="#1F5A83">%s.</font> %s' % (letters[j], esc(o))
                    for j, o in enumerate(opts))
                S.append(KeepTogether([
                    Paragraph('<font name="DJS-B" color="#12304A">Q%d.</font> %s' % (i, fmt(q)),
                              ParagraphStyle("q", parent=body, spaceAfter=1)),
                    Paragraph(choices, ParagraphStyle("o", parent=body, fontSize=8.8,
                                                      leading=12.6, leftIndent=16, spaceAfter=6)),
                ]))
        elif kind == "dl":
            rows = [[Paragraph('<font name="DJS-B" color="#12304A">%s</font>' % esc(t), cell),
                     Paragraph(fmt(d), cell)] for t, d in block[1]]
            t = Table(rows, colWidths=[0.28 * FW, 0.72 * FW])
            t.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -2), 0.3, colors.HexColor("#DDE3E8")),
                ("LEFTPADDING", (0, 0), (-1, -1), 2), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            S.append(t)

    # ── sources ─────────────────────────────────────────────────
    S += heading("Sources et vérification", 0)
    S.append(P("Les règles exposées dans ce cours proviennent des textes normatifs listés "
               "ci-dessous. Les données d'actualité (titulaires de fonctions) reposent sur des "
               "sources de presse concordantes et sont datées dans le corps du document. "
               "Avant l'épreuve, vérifier la dernière version publiée au Journal officiel."))
    rows = []
    for sid, desc, url in SOURCES:
        rows.append([Paragraph('<font name="DJS-B" color="#1F5A83">%s</font>' % sid, cell),
                     Paragraph(esc(desc) + '<br/><font size="7.4" color="#1F5A83">'
                               + esc(url) + "</font>", cell)])
    t = Table(rows, colWidths=[0.07 * FW, 0.93 * FW])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, colors.HexColor("#DDE3E8")),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
    ]))
    S.append(t)
    S += make_box("key", "Dernier conseil",
                  "Le jour du concours : si la question porte sur un titulaire ou une composition "
                  "politique, préciser la date de référence. Si elle porte sur une compétence, "
                  "citer l'article de la Constitution. La précision juridique vaut mieux qu'une "
                  "réponse longue et vague.")

    doc.multiBuild(S)


def main():
    tex_path = os.path.join(HERE, "cours_eip_cameroun.tex")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_doc())
    print("écrit :", tex_path)
    if "--tex" not in sys.argv:
        pdf_path = os.path.join(HERE, "cours_eip_cameroun.pdf")
        build_pdf(pdf_path)
        print("écrit :", pdf_path)


if __name__ == "__main__":
    main()
