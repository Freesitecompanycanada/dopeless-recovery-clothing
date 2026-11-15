# Generates the static pages. Run: python build.py
import html
FORM = "https://formsubmit.co/doplesscloths@gmail.com"  # TODO: confirm Jason's inbox + activate FormSubmit
SITE = "https://freesitecompanycanada.github.io/dopeless-recovery-clothing/"

NAV = [("index.html","Home"),("shop.html","Collections"),("mission.html","Mission"),("about.html","About"),("contact.html","Contact")]
STROKE = 'stroke="rgba(239,230,210,.16)"'

def tee(fill="#171513", mono=True):
    m = '<image href="img/monogram.webp" x="72" y="52" width="56" height="55" style="mix-blend-mode:screen"/>' if mono else ''
    return f'<svg viewBox="0 0 200 200" role="img" aria-label="T-shirt concept"><path d="M62 20 L86 13 Q100 32 114 13 L138 20 L186 56 L166 88 L146 74 L146 182 L54 182 L54 74 L34 88 L14 56 Z" fill="{fill}" {STROKE}/><path d="M86 13 Q100 32 114 13" fill="none" stroke="rgba(239,230,210,.25)" stroke-width="3"/>{m}</svg>'

def hoodie(fill="#171513"):
    return f'<svg viewBox="0 0 200 200" role="img" aria-label="Hoodie concept"><path d="M64 26 Q100 -4 136 26 L180 58 L190 176 L162 180 L152 96 L152 186 L48 186 L48 96 L38 180 L10 176 L20 58 Z" fill="{fill}" {STROKE}/><path d="M72 28 Q100 62 128 28" fill="none" stroke="rgba(239,230,210,.25)" stroke-width="3"/><path d="M68 140 L132 140 L142 180 L58 180 Z" fill="none" stroke="rgba(239,230,210,.12)"/><image href="img/monogram.webp" x="75" y="62" width="50" height="49" style="mix-blend-mode:screen"/></svg>'

def cap(fill="#171513"):
    return f'<svg viewBox="0 0 200 200" role="img" aria-label="Hat concept"><path d="M34 128 Q30 54 100 48 Q170 54 166 128 Q100 112 34 128 Z" fill="{fill}" {STROKE}/><path d="M30 128 Q100 108 170 128 Q190 134 196 146 Q100 126 6 146 Q12 134 30 128 Z" fill="#0e0d0b" {STROKE}/><image href="img/monogram.webp" x="82" y="70" width="36" height="35" style="mix-blend-mode:screen"/></svg>'

def long(fill="#171513"):
    return f'<svg viewBox="0 0 200 200" role="img" aria-label="Long sleeve concept"><path d="M62 20 L86 13 Q100 32 114 13 L138 20 L180 50 L192 170 L168 174 L150 84 L146 74 L146 182 L54 182 L54 74 L50 84 L32 174 L8 170 L20 50 Z" fill="{fill}" {STROKE}/><image href="img/monogram.webp" x="75" y="54" width="50" height="49" style="mix-blend-mode:screen"/></svg>'

TICK = "".join('<span>Hope Not Dope</span><i>&#10022;</i><span>Recovery First</span><i>&#10022;</i><span>Change Looks Good On You</span><i>&#10022;</i><span>Your Past Doesn&#39;t Define Your Future</span><i>&#10022;</i>' for _ in range(4))

def head(title, desc, page):
    nav = "".join(f'<a href="{h}"{" class=on" if h==page else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website"><meta property="og:image" content="{SITE}img/og.jpg">
<meta name="theme-color" content="#050403">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;0,6..96,800;1,6..96,400&family=Archivo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head><body>
<div class="ticker" aria-hidden="true"><div class="ticker-track">{TICK}</div></div>
<header class="bar"><a class="mark" href="index.html" aria-label="Dopeless Recovery Clothing home"><img src="img/monogram.webp" alt=""><b>DOPELESS</b></a>
<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
<nav class="nav">{nav}<a class="cta" href="index.html#drop">Get early access</a></nav></header>
<main>'''

def signup(id_="drop", heading="Be first through the door.", sub="Join the list for first access to samples, drops and the launch.", src="signup"):
    return f'''<section class="drop" id="{id_}"><div class="wrap narrow"><p class="eyebrow">Pre-launch &middot; Winnipeg, MB</p><h2>{heading}</h2><p class="lede">{sub}</p>
<form class="signup" action="{FORM}" method="POST"><input type="hidden" name="_subject" value="Dopeless - new early-access signup"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
<input type="hidden" name="_next" value="{SITE}thanks.html"><input type="hidden" name="source" value="{src}">
<div class="row"><input type="email" name="email" placeholder="Your email" required aria-label="Email"><button class="btn" type="submit">Notify me</button></div>
<p class="micro">Interested in: <label><input type="checkbox" name="interest" value="Tees"> Tees</label> <label><input type="checkbox" name="interest" value="Hoodies"> Hoodies</label> <label><input type="checkbox" name="interest" value="Hats"> Hats</label> <label><input type="checkbox" name="interest" value="Luxury collection"> Luxury</label></p>
<p class="micro dim">No spam. Unsubscribe any time.</p></form></div></section>'''

def foot():
    f = "".join(f'<a href="{h}">{t}</a>' for h,t in NAV)
    return f'''</main>
<footer><div class="wrap foot"><img class="flogo" src="img/logo.webp" alt="Dopeless Recovery Clothing" loading="lazy">
<div class="fcols"><div><h4>Explore</h4>{f}</div><div><h4>Partner</h4><a href="contact.html#partner">Sponsorships</a><a href="contact.html#partner">Collaborations</a><a href="contact.html#partner">Wholesale</a></div><div><h4>Dopeless</h4><p>Winnipeg, Manitoba, Canada<br>Shipping across Canada soon.</p></div></div>
<p class="legal">&copy; 2026 Dopeless Recovery Clothing&trade;. Recovery-inspired streetwear. Not a treatment provider &mdash; if you or someone you know needs support, call or text <a href="https://988.ca" rel="noopener">9-8-8</a> (Canada).</p></div></footer>
<script src="site.js"></script></body></html>'''

pages = {}

pages["index.html"] = head("Dopeless Recovery Clothing - Hope Not Dope","Recovery-inspired luxury streetwear from Winnipeg. Recovery first. Join the list for first access to the debut collection.","index.html") + f'''
<section class="hero"><div class="hero-glow"></div><div class="hero-in">
<img class="hero-logo" src="img/logo.webp" alt="Dopeless Recovery Clothing - Recovery first so the things I love don't come second" width="1400" height="933" fetchpriority="high">
<h1 class="sr">Dopeless Recovery Clothing</h1>
<p class="hero-line">Change looks good on you.</p>
<div class="hero-cta"><a class="btn" href="#drop">Get early access</a><a class="btn ghost" href="shop.html">See the collection</a></div></div>
<a class="scroll" href="#manifesto" aria-label="Scroll"><span></span></a></section>

<section class="manifesto" id="manifesto"><div class="wrap narrow"><p class="eyebrow">The brand</p>
<h2 class="big">Your past doesn't define your future.<br><em>Wear it like it's true.</em></h2>
<p class="lede">Dopeless is luxury streetwear with a reason behind it. Premium heavyweight pieces, made for people who've done the work &mdash; and for everyone who believes in second chances.</p></div></section>

<section class="pieces"><div class="wrap"><div class="shead"><div><p class="eyebrow">Debut collection</p><h2>Samples in progress</h2></div><a class="link" href="shop.html">All pieces &rarr;</a></div>
<div class="grid">
<a class="card" href="shop.html#tees"><div class="art">{tee()}</div><div class="meta"><h3>The Crown Tee</h3><p>Heavyweight tee &middot; DR monogram</p></div><span class="tag">Coming soon</span></a>
<a class="card" href="shop.html#hoodies"><div class="art">{hoodie()}</div><div class="meta"><h3>Recovery First Hoodie</h3><p>Heavyweight fleece</p></div><span class="tag">Sampling</span></a>
<a class="card" href="shop.html#hats"><div class="art">{cap()}</div><div class="meta"><h3>The Monogram Cap</h3><p>Structured, embroidered</p></div><span class="tag">Coming soon</span></a>
<a class="card" href="shop.html#tees"><div class="art">{long("#1d1a17")}</div><div class="meta"><h3>Hope Not Dope Long Sleeve</h3><p>Premium cotton</p></div><span class="tag">Concept</span></a>
</div><p class="note">Concept renders shown. Final production samples, photography and pricing to follow.</p></div></section>

<section class="slogans"><div class="wrap"><div class="s"><span>01</span><b>Hope Not Dope</b></div><div class="s"><span>02</span><b>Recovery First</b></div><div class="s"><span>03</span><b>Change Looks Good On You</b></div><div class="s"><span>04</span><b>Your Past Doesn't Define Your Future</b></div></div></section>

<section class="split"><div class="wrap two"><div><p class="eyebrow">Why it exists</p><h2>Something positive,<br>made from something heavy.</h2></div>
<div><p>Addiction has touched almost every family. We're not trying to make it look fashionable &mdash; we're building a brand that makes recovery something you can wear with pride.</p><p>Every piece is designed first as clothing you'd want to wear anyway. The meaning is there when you look closer.</p><a class="link" href="mission.html">Read the mission &rarr;</a></div></div></section>
{signup()}''' + foot()

def sec(id_, title, sub, items):
    cards = "".join(f'<div class="card static"><div class="art">{a}</div><div class="meta"><h3>{n}</h3><p>{d}</p></div><span class="tag">{t}</span></div>' for n,d,a,t in items)
    return f'<section class="coll" id="{id_}"><div class="wrap"><div class="shead"><div><p class="eyebrow">{sub}</p><h2>{title}</h2></div></div><div class="grid">{cards}</div></div></section>'

pages["shop.html"] = head("Collections - Dopeless Recovery Clothing","Tees, long sleeves, hoodies, hats and the luxury collection. Preview the Dopeless debut and register your interest.","shop.html") + f'''
<section class="phead"><div class="wrap narrow"><p class="eyebrow">Collections</p><h1>The debut drop.</h1><p class="lede">Pieces are in sampling now. Register interest and you'll hear first &mdash; online store opening soon.</p></div></section>
{sec("tees","Tees & Long Sleeves","Essentials",[("The Crown Tee","Heavyweight &middot; DR monogram",tee(),"Coming soon"),("Hope Not Dope Tee","Boxy fit &middot; back print",tee("#1d1a17",False),"Concept"),("Hope Not Dope Long Sleeve","Premium cotton",long("#1d1a17"),"Concept"),("Change Looks Good Long Sleeve","Sleeve print",long(),"Concept")])}
{sec("hoodies","Hoodies & Sweatshirts","Heavyweight",[("Recovery First Hoodie","Heavyweight fleece",hoodie(),"Sampling"),("Crown Crewneck","Embroidered chest crest",hoodie("#1d1a17"),"Concept")])}
{sec("hats","Hats & Accessories","Details",[("The Monogram Cap","Structured &middot; embroidered",cap(),"Coming soon"),("Dopeless Beanie","Folded cuff &middot; woven label",cap("#1d1a17"),"Concept")])}
<section class="coll lux"><div class="wrap narrow center"><p class="eyebrow">Luxury streetwear</p><h2>The Dopeless Luxe line</h2><p class="lede">Elevated cuts, premium fabrics, limited runs. A future collection for those who want the full expression of the brand.</p><span class="tag solo">In development</span></div></section>
{signup("drop","Get the drop link first.","Tell us what you want and we'll email you the moment it's live.","shop")}''' + foot()

pages["mission.html"] = head("Our Mission - Dopeless Recovery Clothing","Dopeless exists to make recovery something worth representing with pride - hope, resilience and second chances, in clothing worth wearing.","mission.html") + f'''
<section class="phead"><div class="wrap narrow"><p class="eyebrow">Our mission</p><h1>Recovery is worth representing with pride.</h1></div></section>
<section class="prose"><div class="wrap narrow">
<p class="lede">Dopeless Recovery Clothing is a recovery-inspired streetwear and lifestyle brand based in Winnipeg, Manitoba. We make clothing that stands for resilience, hope, personal growth &mdash; and the belief that people can change their lives.</p>
<blockquote>We aren't trying to make addiction look fashionable.<br>We're making something positive out of a subject that has affected so many lives.</blockquote>
<h3>Who it's for</h3><ul class="ticks"><li>People in recovery and people rebuilding their lives.</li><li>People personally affected by addiction.</li><li>Families and friends who've lived through it.</li><li>Anyone who believes in second chances and positive change.</li><li>Streetwear fans who appreciate clothing with meaning.</li></ul>
<h3>What we stand for</h3><div class="vals"><div><b>Hope Not Dope</b><p>A simple choice, made daily.</p></div><div><b>Recovery First</b><p>So the things I love don't come second.</p></div><div><b>Change Looks Good On You</b><p>Growth is the best fit you'll ever wear.</p></div><div><b>Your Past Doesn't Define Your Future</b><p>Where you've been isn't where you're going.</p></div></div>
</div></section>
{signup("drop","Wear the message.","Join the list and be there at launch.","mission")}''' + foot()

pages["about.html"] = head("About - Dopeless Recovery Clothing","Founded by Jason Roorda in Winnipeg, Dopeless is a recovery-inspired luxury streetwear brand built from the ground up.","about.html") + f'''
<section class="phead"><div class="wrap narrow"><p class="eyebrow">About</p><h1>Built from the ground up.</h1></div></section>
<section class="prose"><div class="wrap narrow">
<p class="lede">Dopeless was founded in Winnipeg by Jason Roorda, who has been developing the brand, logos, clothing concepts and graphics himself &mdash; a premium label that happens to stand for something meaningful.</p>
<p>It's streetwear first: clean, bold and professional. The message is there for those who know &mdash; it isn't shouted at everyone else.</p>
<div class="timeline"><div><span>Now</span><b>Sampling &amp; pre-launch</b><p>Finalizing production-ready artwork and first samples.</p></div><div><span>Next</span><b>Debut collection + online store</b><p>Tees, hoodies, hats &mdash; direct purchase across Canada.</p></div><div><span>Then</span><b>Luxe line &amp; collaborations</b><p>Limited runs, partnerships and expansion into the US and beyond.</p></div></div>
<p><a class="btn" href="contact.html#partner">Partner with Dopeless</a></p></div></section>
{signup("drop","Follow the build.","Be the first to see samples and release dates.","about")}''' + foot()

pages["contact.html"] = head("Contact - Dopeless Recovery Clothing","Get in touch with Dopeless Recovery Clothing in Winnipeg - questions, partnerships, sponsorships and collaborations.","contact.html") + f'''
<section class="phead"><div class="wrap narrow"><p class="eyebrow">Contact</p><h1>Let's talk.</h1><p class="lede">Questions, partnerships, sponsorships or collaborations &mdash; we read everything.</p></div></section>
<section class="prose" id="partner"><div class="wrap narrow">
<form class="cform" action="{FORM}" method="POST"><input type="hidden" name="_subject" value="Dopeless - website message"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table"><input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off"><input type="hidden" name="_next" value="{SITE}thanks.html">
<label>Name<input name="name" required></label><label>Email<input type="email" name="email" required></label>
<label>I'm reaching out about<select name="topic"><option>General question</option><option>Partnership / collaboration</option><option>Sponsorship</option><option>Wholesale / stockist</option><option>Press</option></select></label>
<label>Message<textarea name="message" rows="6" required></textarea></label><button class="btn" type="submit">Send message</button></form>
<p class="micro dim" style="margin-top:28px">Winnipeg, Manitoba, Canada</p></div></section>''' + foot()

pages["thanks.html"] = head("You're on the list - Dopeless","Thanks - you're on the Dopeless list.","") + '''
<section class="phead tall"><div class="wrap narrow center"><img class="tlogo" src="img/monogram.webp" alt=""><h1>You're in.</h1><p class="lede">Thanks &mdash; we'll be in touch. Recovery first.</p><a class="btn" href="index.html">Back to home</a></div></section>''' + foot()

pages["404.html"] = head("Not found - Dopeless","Page not found.","") + '''<section class="phead tall"><div class="wrap narrow center"><h1>Lost the trail.</h1><p class="lede">That page doesn't exist.</p><a class="btn" href="index.html">Home</a></div></section>''' + foot()

for n, c in pages.items():
    open(n, "w", encoding="utf-8").write(c)
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in ["", "shop.html", "mission.html", "about.html", "contact.html"]) + "</urlset>")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
