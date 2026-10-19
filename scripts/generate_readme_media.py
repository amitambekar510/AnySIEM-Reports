#!/usr/bin/env python3
"""Generate deterministic, self-hosted animated README GIFs with synthetic visuals.
Usage: python scripts/generate_readme_media.py
Requires Pillow; no network, credentials, or SOC data.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
OUT = Path(__file__).resolve().parents[1] / "assets" / "media"
OUT.mkdir(parents=True, exist_ok=True)
W,H = 1050,520
NAVY="#091126"; PANEL="#13233d"; WHITE="#f8f6f1"; GOLD="#d9b54d"; MUTED="#afbed0"
def font(sz,bold=False):
    paths = (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"] if bold else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"])
    for p in paths:
        if Path(p).exists(): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
def text(d,pos,s,sz=22,c=WHITE,b=False):d.text(pos,s,fill=c,font=font(sz,b))
def bg():
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    d.ellipse((775,-340,1430,335),fill="#151d33")
    d.ellipse((-325,320,280,855),fill="#101b30")
    return im,d
def rect(d,xy,fill,outline=None,r=17,width=2):d.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=width)
def finish(name,frames,duration):
    assert len(frames)>1
    file=OUT/name
    frames[0].save(file,format="GIF",save_all=True,append_images=frames[1:],duration=duration,loop=0,optimize=True,disposal=2)
    check=Image.open(file)
    assert getattr(check,"n_frames",1)>1, f"{name} lost its animation"
    print(name,check.n_frames,file.stat().st_size,"bytes")
steps=[("SELECT TEMPLATE","Choose from 38 designs"),("GUIDED QUESTIONS","Describe SOC context"),("VALIDATE EVIDENCE","Unknowns remain explicit"),("MAP FRAMEWORKS","Verify applicability"),("DELIVER PDF","Human-approved output")]
frames=[]
for selected in range(len(steps)):
    im,d=bg()
    text(d,(45,33),"AnySIEM-Reports  /  HOW IT WORKS",34,WHITE,True)
    text(d,(45,85),"An AI-guided workflow for SIEM-agnostic reporting",20,MUTED)
    for i,(label,desc) in enumerate(steps):
        x=43+i*205; y=182
        line = GOLD if i==selected else ("#57b9a4" if i<selected else "#38516c")
        rect(d,(x,y,x+189,y+182),PANEL,line,r=16,width=4 if i==selected else 2)
        rect(d,(x+16,y+17,x+51,y+52),line)
        text(d,(x+27,y+22),str(i+1),18,NAVY,True)
        parts=label.split(" ",1)
        for j,s in enumerate(parts):text(d,(x+12,y+77+28*j),s,15,WHITE,True)
        if i<4:text(d,(x+186,y+80),">",25,GOLD,True)
    rect(d,(43,411,1004,480),"#172843",r=12)
    text(d,(65,424),steps[selected][1],25,GOLD,True)
    text(d,(65,457),"Illustrative sequence • all input evidence requires human review",15,MUTED)
    frames.append(im)
finish("reporting-workflow.gif",frames,760)
reports=[
    ("SOC OPERATIONS","Deep winter blue","#20446e"),
    ("INCIDENT REPORT","Winter berry","#8f252a"),
    ("THREAT INTEL","Evergreen","#145840"),
    ("EVIDENCE PACK","Warm taupe","#9d806d")
]
frames=[]
for selected in range(len(reports)):
    im,d=bg()
    text(d,(45,33),"38 TEMPLATES  /  VISUAL GALLERY",32,WHITE,True)
    text(d,(45,84),"Illustrative report cover previews • synthetic examples only",18,MUTED)
    for i,(name,palette,c) in enumerate(reports):
        x=42+i*255; y=143
        rect(d,(x,y,x+238,y+309),"#ffffff",GOLD if selected==i else "#334a64",r=15,width=5 if selected==i else 2)
        rect(d,(x,y,x+238,y+79),c,r=15)
        d.rectangle((x,y+58,x+238,y+79),fill=c)
        text(d,(x+15,y+20),name,15,WHITE,True)
        for j in range(4):
            rect(d,(x+17,y+113+37*j,x+198-j*18,y+123+37*j),c if j==0 else "#e0e9f1",r=4)
        text(d,(x+17,y+263),"MOCKUP ONLY",13,c,True)
    text(d,(45,485),reports[selected][0]+"  |  "+reports[selected][1],18,GOLD,True)
    frames.append(im)
finish("template-gallery.gif",frames,900)
