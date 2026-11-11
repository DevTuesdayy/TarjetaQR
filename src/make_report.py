from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

OUT = '/Users/tuesday/Desktop/Reporte-TarjetaQR.pdf'
W, H = letter
NAVY = colors.HexColor('#14233B')
ORANGE = colors.HexColor('#FF4B1F')
BLUE = colors.HexColor('#657895')
LIGHT = colors.HexColor('#F2F5F9')
LINE = colors.HexColor('#D7E0EC')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body2', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#182338')))
styles.add(ParagraphStyle(name='Label2', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=BLUE, tracking=1.2))
styles.add(ParagraphStyle(name='Head2', fontName='Helvetica-Bold', fontSize=22, leading=25, textColor=NAVY))
styles.add(ParagraphStyle(name='WhiteHead', fontName='Helvetica-Bold', fontSize=40, leading=41, textColor=colors.white))
styles.add(ParagraphStyle(name='Card2', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=NAVY))
styles.add(ParagraphStyle(name='Hero2', fontName='Helvetica', fontSize=11, leading=16, textColor=colors.HexColor('#D5DCE7')))

def P(text, style='Body2'):
    return Paragraph(text, styles[style])

def field(label, value, width=6.6*inch):
    t = Table([[P(label.upper(), 'Label2')], [P(value)], ['']], colWidths=[width], rowHeights=[18, 30, 5])
    t.setStyle(TableStyle([('LINEBELOW', (0,1), (-1,1), .8, LINE), ('LEFTPADDING',(0,0),(-1,-1),0), ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),0), ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    return t

def pills(items):
    cells = [P(x.upper(), 'Label2') for x in items]
    t = Table([cells], colWidths=[1.35*inch]*len(items))
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NAVY), ('TEXTCOLOR',(0,0),(-1,-1),colors.white), ('BOX',(0,0),(-1,-1),.5,colors.HexColor('#536783')), ('INNERGRID',(0,0),(-1,-1),.5,NAVY), ('ALIGN',(0,0),(-1,-1),'CENTER'), ('TOPPADDING',(0,0),(-1,-1),8), ('BOTTOMPADDING',(0,0),(-1,-1),8)]))
    return t

def page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, H-3.55*inch, W, 3.55*inch, fill=1, stroke=0)
    canvas.setFillColor(ORANGE)
    canvas.circle(W+10, H+6, 105, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#3B2931'))
    canvas.circle(W-10, H-235, 85, fill=1, stroke=0)
    canvas.setFillColor(ORANGE)
    canvas.rect(0, H-3.62*inch, W, 5, fill=1, stroke=0)
    canvas.setFillColor(ORANGE)
    canvas.roundRect(.58*inch, H-.95*inch, .42*inch, .42*inch, 7, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont('Helvetica-Bold', 18)
    canvas.drawCentredString(.79*inch, H-.81*inch, 'R')
    canvas.setFont('Helvetica-Bold', 16)
    canvas.drawString(1.12*inch, H-.80*inch, 'RHINA')
    canvas.setFillColor(ORANGE)
    canvas.drawString(1.72*inch, H-.80*inch, 'CRED')
    canvas.setStrokeColor(LINE)
    canvas.line(.58*inch, .55*inch, W-.58*inch, .55*inch)
    canvas.setFillColor(BLUE)
    canvas.setFont('Helvetica', 8.5)
    canvas.drawString(.58*inch, .33*inch, 'https://devtuesdayy.github.io/TarjetaQR/')
    canvas.drawRightString(W-.58*inch, .33*inch, 'github.com/DevTuesdayy/TarjetaQR')
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=.58*inch, rightMargin=.58*inch, topMargin=.55*inch, bottomMargin=.75*inch)
story = [Spacer(1,.58*inch), P('ACTIVIDAD INDIVIDUAL', 'Label2'), Spacer(1,.18*inch), P('TARJETA DIGITAL<br/><font color="#FF4B1F">DEL EMPLEADO</font>', 'WhiteHead'), Spacer(1,.20*inch), P('Aplicación web para generar y consultar una tarjeta digital profesional con información del empleado y código QR.', 'Hero2'), Spacer(1,.12*inch), pills(['Vue 3', 'PrimeVue', 'GitHub Pages']), Spacer(1,.25*inch), P('DATOS DE PRESENTACIÓN', 'Head2'), Spacer(1,.16*inch), field('Universidad', 'Universidad Nacional Autónoma de Chiapas'), Spacer(1,.06*inch), field('Facultad', 'Escuela de Tecnologías Digitales Aplicadas Campus IV'), Spacer(1,.06*inch)]

two = Table([[field('Licenciatura', 'Ingeniería en Desarrollo y Tecnologías de Software', 3.25*inch), field('Semestre y grupo', '7°A', 3.05*inch)]], colWidths=[3.45*inch,3.05*inch])
two.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
story += [two, Spacer(1,.10*inch), field('Materia', 'Desarrollo de Aplicaciones Web y Móviles'), Spacer(1,.10*inch), field('Alumno(a)', 'Alan Cervantes de la Cruz'), Spacer(1,.10*inch)]
two2 = Table([[field('Matrícula', '100017455', 3.25*inch), field('Lugar y fecha de entrega', '8 de noviembre de 2026, Tapachula, Chiapas', 3.05*inch)]], colWidths=[3.45*inch,3.05*inch])
two2.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
story += [two2, PageBreak(), Spacer(1,.65*inch), P('EVIDENCIA', 'Label2'), Spacer(1,.08*inch), P('SITIO PUBLICADO', 'Head2'), Spacer(1,.28*inch)]

box = Table([[P('RHINACRED  ·  TARJETA QR', 'Card2')], [P('TARJETA DIGITAL DEL EMPLEADO', 'Head2')], [P('Aplicación publicada y accesible desde GitHub Pages.', 'Body2')], [pills(['Sitio activo'])]], colWidths=[6.15*inch], rowHeights=[.42*inch,.52*inch,.42*inch,.45*inch])
box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('BOX',(0,0),(-1,-1),.8,LINE),('LEFTPADDING',(0,0),(-1,-1),.28*inch),('RIGHTPADDING',(0,0),(-1,-1),.28*inch),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
story += [box, Spacer(1,.18*inch), P('La aplicación fue construida con Vue 3 y PrimeVue, compilada con Vite y desplegada automáticamente mediante GitHub Actions.', 'Body2'), Spacer(1,.28*inch)]

links = Table([[P('SITIO PUBLICADO', 'Label2'), P('REPOSITORIO EN GITHUB', 'Label2')], [P('devtuesdayy.github.io/TarjetaQR/', 'Card2'), P('github.com/DevTuesdayy/TarjetaQR', 'Card2')]], colWidths=[3.05*inch,3.05*inch], rowHeights=[.35*inch,.68*inch])
links.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT),('BOX',(0,0),(-1,-1),.8,LINE),('INNERGRID',(0,0),(-1,-1),.8,LINE),('LEFTPADDING',(0,0),(-1,-1),.22*inch),('RIGHTPADDING',(0,0),(-1,-1),.18*inch),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
story += [links, Spacer(1,.25*inch), P('TECNOLOGÍAS UTILIZADAS', 'Head2'), Spacer(1,.14*inch), pills(['Vue 3', 'PrimeVue', 'Vite', 'GitHub Pages']), Spacer(1,.25*inch), P('DESCRIPCIÓN DE LA EVIDENCIA', 'Label2'), Spacer(1,.06*inch), P('La evidencia documenta la publicación del proyecto TarjetaQR, incluyendo la dirección pública del sitio y el repositorio donde se encuentra el código fuente. El despliegue se realiza automáticamente al actualizar la rama principal.', 'Body2'), Spacer(1,.12*inch), field('Docente', 'Dr. Christian Mauricio Castillo Estrada')]

doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUT)
