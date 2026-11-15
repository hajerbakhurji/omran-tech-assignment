# Builds the website into the dist/ folder.
# Run:  python build.py

import json
import os
import shutil
from datetime import date
from html import escape

from content import *

OUT = "dist"
LANGS = ["en", "ar"]
FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900"
         "&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap")
AR_MONTHS = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
             "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
EN_MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load(name):
    with open(f"data/{name}.json", encoding="utf-8") as f:
        return json.load(f)


PROJECTS = load("projects")
POSTS = load("posts")
PAGES = load("pages")
POSTS.sort(key=lambda p: p["date"], reverse=True)


# ---------- small helpers ----------

ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "compass": '<path d="M12 3v3M5 21l7-15 7 15M7.5 15.5h9"/><circle cx="12" cy="6" r="1.5"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "beam": '<path d="M3 6h18M3 18h18M7 6v12M17 6v12M7 6l10 12M17 6L7 18"/>',
    "survey": '<path d="M12 3v10M8 21l4-8 4 8M5 21h14"/><rect x="8" y="3" width="8" height="5" rx="1"/>',
    "grid": '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17.5l9 5 9-5"/>',
    "wave": '<path d="M3 15c2 0 2-2 4.5-2S10 15 12 15s2.5-2 4.5-2 2.5 2 4.5 2"/><path d="M3 19c2 0 2-2 4.5-2S10 19 12 19s2.5-2 4.5-2 2.5 2 4.5 2"/><path d="M8 11V5a2 2 0 014 0M16 11V5"/>',
    "machine": '<rect x="3" y="8" width="18" height="10" rx="1"/><circle cx="8" cy="13" r="2.5"/><circle cx="16" cy="13" r="2.5"/><path d="M6 8V5h12v3M3 21h18"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0112 2.5a7 7 0 017 7C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "link": '<path d="M10 14a5 5 0 007 0l3-3a5 5 0 00-7-7l-1 1"/><path d="M14 10a5 5 0 00-7 0l-3 3a5 5 0 007 7l1-1"/>',
    "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8L19 15z"/>',
    "external": '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v5a1 1 0 01-1 1H5a1 1 0 01-1-1V7a1 1 0 011-1h5"/>',
    "send": '<path d="M4 12l16-8-6 16-2.5-6.5L4 12z"/>',
}

SOCIAL_ICONS = {
    "x": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3.1l-6.8 7.7L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
}


def icon(name, css_class=""):
    return (f'<svg class="{css_class}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


ARROW = '<svg class="arrow" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


def format_date(iso, lang):
    d = date.fromisoformat(iso)
    month = AR_MONTHS[d.month - 1] if lang == "ar" else EN_MONTHS[d.month - 1]
    return f"{d.day} {month} {d.year}"


def first_paragraph(body, max_length=150):
    for block in body:
        text = block.get("p", "") if isinstance(block, dict) else ""
        if len(text) > 40:
            if len(text) > max_length:
                text = text[:max_length].rsplit(" ", 1)[0] + "…"
            return text
    return ""


def render_body(body, page):
    """Turns a list like [{"h": ...}, {"p": ...}, {"list": [...]}] into HTML."""
    html = []
    first = True
    for block in body:
        if "h" in block:
            html.append(f"<h2>{escape(block['h'])}</h2>")
        elif "p" in block:
            css = ' class="intro"' if first else ""
            html.append(f"<p{css}>{escape(block['p'])}</p>")
            first = False
        elif "list" in block:
            css = ' class="cols"' if len(block["list"]) > 6 else ""
            items = "".join(f"<li>{escape(item)}</li>" for item in block["list"])
            html.append(f"<ul{css}>{items}</ul>")
        elif "video" in block:
            html.append(f'<div class="lgs-media" style="aspect-ratio:16/9"><video src="{page.link(block["video"])}" '
                        f'muted loop playsinline controls preload="metadata"></video></div>')
    return "\n".join(html)


def filter_name(tag, lang):
    for key, en, ar in FILTERS:
        if key == tag:
            return en if lang == "en" else ar
    return ""


def projects_in(lang):
    return [p for p in PROJECTS if p[lang]]


def posts_in(lang, post_type=None):
    return [p for p in POSTS if p[lang] and (post_type is None or p["type"] == post_type)]


# ---------- page layout ----------

class Page:
    """Holds the language and path of the page being built, and makes links relative to it."""

    def __init__(self, lang, path):
        self.lang = lang
        self.path = path              # e.g. "projects/cafe.html"
        self.t = TEXT[lang]
        self.ai = AI[lang]
        self.root = "../" * (path.count("/") + 1)

    def url(self, path, lang=None):
        return f"{self.root}{lang or self.lang}/{path}"

    def link(self, file):
        return self.root + file


def header(page, other_path):
    t, ai = page.t, page.ai
    section = page.path.split("/")[0].replace(".html", "")
    if section == "departments":
        section = "services"

    nav = ""
    mobile_nav = ""
    for key, label in t["nav"]:
        current = ' aria-current="page"' if key == section else ""
        nav += f'<a href="{page.url(key + ".html")}"{current}>{escape(label)}</a>'
        mobile_nav += f'<a class="m-link" href="{page.url(key + ".html")}"{current}>{escape(label)}{ARROW}</a>'

    mobile_nav += f'''<a class="m-link m-link--ai" href="{page.url("ai.html")}">
      <span>{icon("spark", "ai-ic")} {escape(ai["nav"])} <span class="ai-badge">{escape(ai["badge"])}</span></span></a>'''

    return f'''<a class="skip-link" href="#main">{escape(t["skip"])}</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{page.url("index.html")}" aria-label="{escape(t["brand"])}">
      <img src="{page.link(LOGO)}" alt="" width="77" height="48">
      <span class="brand-name">{escape(t["brand"])}<small>{escape(t["tagline"])}</small></span>
    </a>
    <nav class="main-nav" aria-label="Main">{nav}</nav>
    <div class="header-actions">
      <a class="ai-pill" href="{page.url("ai.html")}" aria-label="{escape(ai["nav"])}">{icon("spark")}<span>{escape(ai["nav"])}</span><span class="ai-dot"></span></a>
      <a class="lang-switch" href="{page.url(other_path, t["other"])}" lang="{t["other"]}">{escape(t["other_name"])}</a>
      <a class="btn btn--sm" href="{page.url("contact.html")}">{escape(t["start_project"])}</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="{escape(t["menu"])}"
              data-open="{escape(t["menu"])}" data-close="{escape(t["close"])}"><span></span></button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  {mobile_nav}
  <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
</nav>'''


def footer(page):
    t = page.t
    links = "".join(f'<li><a href="{page.url(key + ".html")}">{escape(label)}</a></li>' for key, label in t["nav"])
    links += f'<li><a href="{page.url("ai.html")}">{escape(page.ai["nav"])}</a></li>'
    branches = "".join(f'<li class="branch"><b>{escape(name)}</b>{escape(address)}</li>' for name, address in BRANCHES[page.lang])
    phones = "".join(f'<li><a class="ltr" href="tel:{p}">{p}</a></li>' for p in COMPANY["phones"])
    hours = "".join(f'<div><span>{escape(day)}</span><span class="ltr">{time}</span></div>' for day, time in t["hours_list"])
    socials = ""
    for name_en, name_ar, x_url, instagram_url in COMPANY["social"]:
        name = name_en if page.lang == "en" else name_ar
        socials += f'''<div class="social-row">
  <span>{escape(name)}</span>
  <a href="{x_url}" target="_blank" rel="noopener" aria-label="{escape(name)} on X">{SOCIAL_ICONS["x"]}</a>
  <a href="{instagram_url}" target="_blank" rel="noopener" aria-label="{escape(name)} on Instagram">{SOCIAL_ICONS["instagram"]}</a>
</div>'''
    socials += f'<div class="social-row"><span>Linktree</span><a href="{COMPANY["linktree"]}" target="_blank" rel="noopener" aria-label="Linktree">{icon("link")}</a></div>'

    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="{page.url("index.html")}"><img src="{page.link(LOGO)}" alt="{escape(t["brand"])}" width="77" height="48"><span class="brand-name">{escape(t["brand"])}</span></a>
        <p>{escape(t["footer_text"])}</p>
        <h4>{escape(t["follow"])}</h4>
        <div class="socials">{socials}</div>
      </div>
      <div><h4>{escape(t["links"])}</h4><ul>{links}</ul></div>
      <div><h4>{escape(t["branches"])}</h4><ul>{branches}</ul></div>
      <div>
        <h4>{escape(t["phone"])}</h4><ul>{phones}</ul>
        <h4 class="mt-28">{escape(t["email"])}</h4><ul><li><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></li></ul>
        <h4 class="mt-28">{escape(t["hours"])}</h4><div class="hours">{hours}</div>
      </div>
    </div>
  </div>
  <div class="wrap"><div class="footer-word" aria-hidden="true">{escape(t["short_name"])}</div></div>
  <div class="wrap footer-bottom">
    <span>© <span id="year">2025</span> {escape(t["brand"])}. {escape(t["rights"])}</span>
    <span class="ltr">{COMPANY["email"]}</span>
  </div>
</footer>
<a class="fab" href="tel:{COMPANY["phones"][0]}" aria-label="{escape(t["phone"])}">{icon("phone")}</a>'''


def layout(page, title, description, body, other_path, image=None):
    t = page.t
    if title != t["brand"]:
        title = f"{title} | {t['brand']}"
    return f'''<!doctype html>
<html lang="{page.lang}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{page.link(image or HERO_IMAGE)}">
<meta name="theme-color" content="#0c0e11">
<link rel="alternate" hreflang="{t["other"]}" href="{page.url(other_path, t["other"])}">
<link rel="icon" href="{page.link(LOGO)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{page.link("assets/styles.css")}">
</head>
<body>
{header(page, other_path)}
<main id="main">
{body}
</main>
{footer(page)}
<script src="{page.link("assets/main.js")}" defer></script>
</body>
</html>'''


# ---------- shared sections ----------

def page_hero(page, kicker, title, intro=None, image=None, crumbs=()):
    t = page.t
    trail = f'<a href="{page.url("index.html")}">{escape(t["nav"][0][1])}</a>'
    for label, href in crumbs:
        trail += '<span aria-hidden="true">/</span>'
        trail += f'<a href="{href}">{escape(label)}</a>' if href else f"<span>{escape(label)}</span>"

    background = ""
    css = "page-hero blueprint"
    if image:
        background = f'<div class="bg"><img src="{page.link(image)}" alt="" fetchpriority="high"></div>'
        css = "page-hero page-hero--img"

    intro_html = f'<p class="lead">{escape(intro)}</p>' if intro else ""
    return f'''<section class="{css}">{background}
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">{trail}</nav>
    <span class="kicker">{escape(kicker)}</span>
    <h1>{escape(title)}</h1>
    {intro_html}
  </div>
</section>'''


def section_head(kicker, title, side=""):
    return f'''<div class="section-head">
      <div><span class="kicker">{escape(kicker)}</span><h2>{title}</h2></div>
      {side}
    </div>'''


def call_to_action(page):
    t = page.t
    return f'''<section class="section section--tight cta-band">
  <div class="wrap cta-inner">
    <div class="reveal"><h2>{escape(t["cta_title"])}</h2><p>{escape(t["cta_text"])}</p></div>
    <div class="cta-actions reveal" data-delay="1">
      <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
      <a class="btn btn--ghost" href="tel:{COMPANY["phones"][2]}"><span class="ltr">{COMPANY["phones"][2]}</span></a>
    </div>
  </div>
</section>'''


def department_cards(page):
    cards = ""
    for i, dep in enumerate(DEPARTMENTS):
        name, company, summary = dep[page.lang]
        cards += f'''<a class="dept-card reveal" data-delay="{i % 3}" href="{page.url("departments/" + dep["slug"] + ".html")}">
  <img src="{page.link(dep["image"])}" alt="" loading="lazy">
  <span class="dept-num">0{i + 1}</span>
  <span class="tag">{escape(company)}</span>
  <h3>{escape(name)}</h3>
  <p>{escape(summary)}</p>
  <span class="link-arrow">{escape(page.t["learn_more"])} {ARROW}</span>
</a>'''
    return f'<div class="dept-grid">{cards}</div>'


def service_cards(page):
    cards = ""
    for i, service in enumerate(SERVICES):
        name, summary = service[page.lang]
        cards += f'''<a class="svc reveal" data-delay="{i % 4}" href="{page.url("services/" + service["slug"] + ".html")}">
  <div class="svc-top">{icon(service["icon"], "svc-icon")}<span class="svc-index">{i + 1:02d}</span></div>
  <h3>{escape(name)}</h3>
  <p>{escape(summary)}</p>
  <span class="link-arrow">{escape(page.t["learn_more"])} {ARROW}</span>
</a>'''
    return f'<div class="svc-grid">{cards}</div>'


def process_section(page):
    t = page.t
    steps = ""
    for i, (title, text) in enumerate(PROCESS[page.lang]):
        steps += f'''<div class="step reveal" data-delay="{i}">
  <div class="step-num">{i + 1:02d}</div>
  <div><h3>{escape(title)}</h3><p>{escape(text)}</p></div>
</div>'''
    return f'''<section class="section steel blueprint">
  <div class="wrap">
    {section_head(t["process_kicker"], escape(t["process_title"]))}
    <div class="process">{steps}</div>
  </div>
</section>'''


def project_card(page, project, delay=0):
    title = project[page.lang]["title"]
    if project["tags"]:
        label = filter_name(project["tags"][0], page.lang)
    else:
        label = page.t["projects_page"]
    return f'''<a class="proj-card reveal" data-delay="{delay}" data-tags="{" ".join(project["tags"])}" href="{page.url("projects/" + project["slug"] + ".html")}">
  <img src="{page.link(project["image"])}" alt="{escape(title)}" loading="lazy">
  <div class="proj-meta">
    <div><div class="cat">{escape(label)}</div><h3>{escape(title)}</h3></div>
    <span class="proj-go">{ARROW}</span>
  </div>
</a>'''


def post_card(page, post, delay=0):
    item = post[page.lang]
    label = page.t["articles_page"] if post["type"] == "articles" else page.t["news_page"]
    return f'''<a class="news-card reveal" data-delay="{delay}" href="{page.url(post["type"] + "/" + post["slug"] + ".html")}">
  <div class="news-thumb"><img src="{page.link(post["image"])}" alt="" loading="lazy"></div>
  <div class="news-date"><span class="pill">{escape(label)}</span><time datetime="{post["date"]}">{format_date(post["date"], page.lang)}</time></div>
  <h3>{escape(item["title"])}</h3>
  <p>{escape(first_paragraph(item["body"]))}</p>
</a>'''


def gallery(page, images, group, title):
    if len(images) < 2:
        return ""
    buttons = ""
    for i, image in enumerate(images):
        buttons += (f'<button data-lightbox="{group}" data-full="{page.link(image)}" data-alt="{escape(title)}" '
                    f'aria-label="{escape(title)} {i + 1}"><img src="{page.link(image)}" alt="" loading="lazy"></button>')
    return f'<h2 class="h3 gallery-title">{escape(page.t["gallery"])}</h2><div class="gallery">{buttons}</div>'


def ai_section(page):
    ai = page.ai
    points = "".join(f"<li>{icon('spark')}<span>{escape(p)}</span></li>" for p in ai["points"])
    messages = ""
    for i, question in enumerate(ai["chat_questions"]):
        messages += f'<div class="ai-msg ai-msg--user" style="--d:{0.3 + i * 0.9:.1f}s">{escape(question)}</div>'
    typing_delay = 0.3 + len(ai["chat_questions"]) * 0.9

    return f'''<section class="section ai-band" aria-labelledby="ai-title">
  <div class="wrap ai-grid">
    <div class="reveal">
      <span class="kicker">{escape(ai["kicker"])}</span>
      <h2 id="ai-title">{ai["title"]}</h2>
      <p class="lead mt-20">{escape(ai["text"])}</p>
      <ul class="ai-points">{points}</ul>
      <a class="btn ai-btn" href="{page.url("ai.html")}">{icon("spark")} {escape(ai["button"])}</a>
    </div>
    <a class="ai-chat reveal" data-delay="1" href="{page.url("ai.html")}" aria-label="{escape(ai["button"])}">
      <div class="ai-chat-head">
        <span class="ai-avatar">{icon("spark")}</span>
        <div><b>{escape(ai["chat_name"])}</b><small><i class="ai-online"></i>{escape(ai["chat_status"])}</small></div>
      </div>
      <div class="ai-chat-body" aria-hidden="true">
        {messages}
        <div class="ai-msg ai-msg--bot ai-typing" style="--d:{typing_delay:.1f}s"><i></i><i></i><i></i></div>
      </div>
      <div class="ai-chat-input" aria-hidden="true"><span>{escape(ai["chat_input"])}</span><span class="ai-send">{icon("send")}</span></div>
    </a>
  </div>
</section>'''


# ---------- pages ----------

def home_page(page):
    t = page.t
    projects = projects_in(page.lang)

    stats = ""
    for number, label in t["stats"]:
        plus = ""
        if number == "projects":
            number = str(len(projects))
            plus = "<sup>+</sup>"
        stats += f'<div class="stat"><div class="stat-num"><span data-count="{number}">{number}</span>{plus}</div><div class="stat-label">{escape(label)}</div></div>'

    techs = "".join(f'<span class="marquee-item">{escape(x)}</span>' for x in t["techs"])

    featured = [p for slug in FEATURED_PROJECTS for p in projects if p["slug"] == slug]
    featured_html = "".join(project_card(page, p, i % 3) for i, p in enumerate(featured))

    benefits = "".join(f"<li>{escape(b)}</li>" for b in LGS_BENEFITS[page.lang])

    reviews = ""
    for i, (quote, name) in enumerate(TESTIMONIALS[page.lang]):
        reviews += f'''<figure class="testi reveal" data-delay="{i}">
  <div class="testi-mark" aria-hidden="true">“</div>
  <blockquote>{escape(quote)}</blockquote>
  <figcaption><span class="avatar" aria-hidden="true">{escape(name[0])}</span>{escape(name)}<span class="stars" aria-label="5/5">★★★★★</span></figcaption>
</figure>'''

    logos = "".join(f'<div class="logo-tile"><img src="{page.link(img)}" alt="" loading="lazy"></div>' for img in PARTNERS)

    certificates = ""
    for i, (img, en, ar) in enumerate(CERTIFICATES):
        name = en if page.lang == "en" else ar
        certificates += f'''<button class="cert reveal" data-delay="{i % 4}" data-lightbox="certs" data-full="{page.link(img)}" data-alt="{escape(name)}">
  <span class="cert-img"><img src="{page.link(img)}" alt="{escape(name)}" loading="lazy"></span><span>{escape(name)}</span>
</button>'''

    news = "".join(post_card(page, p, i) for i, p in enumerate(posts_in(page.lang, "news")[:3]))

    view_projects = f'<div><p class="lead mb-24">{escape(t["projects_intro"])}</p><a class="btn btn--ghost" href="{page.url("projects.html")}">{escape(t["view_all"])} {ARROW}</a></div>'
    view_news = f'<div><a class="btn btn--ghost" href="{page.url("news.html")}">{escape(t["view_all"])} {ARROW}</a></div>'

    body = f'''
<section class="hero">
  <div class="hero-media"><img src="{page.link(HERO_IMAGE)}" alt="" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-content">
      <span class="kicker">{escape(t["hero_kicker"])}</span>
      <h1>{t["hero_title"]}</h1>
      <p class="lead">{escape(t["hero_text"])}</p>
      <div class="hero-ctas">
        <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
        <a class="btn btn--ghost" href="{page.url("projects.html")}">{escape(t["hero_button"])}</a>
      </div>
    </div>
    <div class="hero-stats">{stats}</div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{techs}{techs}</div></div>

{ai_section(page)}

<section class="section">
  <div class="wrap">
    {section_head(t["dept_kicker"], escape(t["dept_title"]), f'<p class="lead">{escape(t["dept_text"])}</p>')}
    {department_cards(page)}
  </div>
</section>

<section class="section light">
  <div class="wrap">
    {section_head(t["services_kicker"], escape(t["services_title"]), f'<p class="lead">{escape(t["services_intro"])}</p>')}
    {service_cards(page)}
  </div>
</section>

{process_section(page)}

<section class="section">
  <div class="wrap">
    {section_head(t["projects_kicker"], escape(t["projects_title"]), view_projects)}
    <div class="proj-grid proj-grid--featured">{featured_html}</div>
  </div>
</section>

<section class="section steel">
  <div class="wrap lgs">
    <div class="lgs-media reveal">
      <video data-autoplay src="{page.link(LGS_VIDEO)}" poster="{page.link(LGS_POSTER)}" muted loop playsinline preload="none"></video>
      <div class="lgs-badge"><span>150+</span><small>{escape(t["lgs_badge"])}</small></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="kicker">{escape(t["lgs_kicker"])}</span>
      <h2>{escape(t["lgs_title"])}</h2>
      <p class="lead mt-20">{escape(t["lgs_text"])}</p>
      <ul class="adv-list">{benefits}</ul>
      <a class="btn mt-32" href="{page.url("departments/factory.html")}">{escape(t["learn_more"])} {ARROW}</a>
    </div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    {section_head(t["reviews_kicker"], escape(t["reviews_title"]))}
    <div class="testi-grid">{reviews}</div>
  </div>
</section>

<section class="section section--tight concrete">
  <div class="wrap"><h2 class="h3 partners-title">{escape(t["partners_title"])}</h2></div>
  <div class="logo-strip"><div class="logo-track">{logos}{logos}</div></div>
</section>

<section class="section concrete certs-section">
  <div class="wrap">
    {section_head(t["certs_kicker"], escape(t["certs_title"]))}
    <div class="cert-grid">{certificates}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {section_head(t["news_kicker"], escape(t["news_title"]), view_news)}
    <div class="news-grid">{news}</div>
  </div>
</section>

{call_to_action(page)}'''
    return layout(page, t["brand"], t["hero_text"], body, "index.html")


def about_page(page):
    t = page.t
    about = ABOUT[page.lang]
    paragraphs = "".join(f"<p>{escape(p)}</p>" for p in about["paragraphs"])
    values = ""
    for i, (name, text) in enumerate(about["values"]):
        values += f'<div class="value reveal" data-delay="{i}"><span class="value-num">0{i + 1}</span><h3>{escape(name)}</h3><p>{escape(text)}</p></div>'

    body = f'''{page_hero(page, t["brand"], t["about_title"], image=ABOUT_IMAGES[0], crumbs=[(t["nav"][1][1], None)])}

<section class="section">
  <div class="wrap split">
    <div class="split-media reveal">
      <img src="{page.link(ABOUT_IMAGES[1])}" alt="" loading="lazy">
      <img src="{page.link(ABOUT_IMAGES[2])}" alt="" loading="lazy">
    </div>
    <div class="prose prose-lg reveal" data-delay="1">
      <span class="kicker">{escape(t["nav"][1][1])}</span>
      {paragraphs}
      <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
    </div>
  </div>
</section>

<section class="section steel blueprint pt-0">
  <div class="wrap vm-grid">
    <div class="vm reveal"><h3>{escape(t["vision"])}</h3><p>{escape(about["vision"])}</p></div>
    <div class="vm reveal" data-delay="1"><h3>{escape(t["mission"])}</h3><p>{escape(about["mission"])}</p></div>
  </div>
</section>

<section class="section light">
  <div class="wrap">
    {section_head(t["brand"], escape(t["values"]))}
    <div class="values">{values}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {section_head(t["dept_kicker"], escape(t["dept_title"]), f'<p class="lead">{escape(t["dept_text"])}</p>')}
    {department_cards(page)}
  </div>
</section>

{process_section(page)}
{call_to_action(page)}'''
    return layout(page, t["nav"][1][1], about["paragraphs"][0], body, "about.html")


def services_page(page):
    t = page.t
    body = f'''{page_hero(page, t["services_kicker"], t["services_page"], t["services_intro"], crumbs=[(t["services_page"], None)])}

<section class="section light"><div class="wrap">{service_cards(page)}</div></section>

<section class="section">
  <div class="wrap">
    {section_head(t["dept_kicker"], escape(t["dept_title"]), f'<p class="lead">{escape(t["dept_text"])}</p>')}
    {department_cards(page)}
  </div>
</section>

{process_section(page)}
{call_to_action(page)}'''
    return layout(page, t["services_page"], t["services_intro"], body, "services.html")


def side_menu(page, items, heading):
    t = page.t
    links = ""
    for name, path in items:
        current = ' aria-current="page"' if path == page.path else ""
        links += f'<li><a href="{page.url(path)}"{current}>{escape(name)}{ARROW}</a></li>'
    return f'''<div class="aside-card"><h4>{escape(heading)}</h4><ul>{links}</ul></div>
<div class="aside-card aside-cta">
  <h3>{escape(t["cta_title"])}</h3><p>{escape(t["cta_text"])}</p>
  <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
</div>'''


def detail_page(page, slug, kicker, title, intro, image, menu, section_name):
    t = page.t
    content = PAGES[slug]
    body = f'''{page_hero(page, kicker, title, intro, image, [(section_name, page.url("services.html")), (title, None)])}

<section class="section">
  <div class="wrap detail">
    <article class="rich reveal">
      {render_body(content[page.lang], page)}
      {gallery(page, content["gallery"], "g", title)}
    </article>
    <aside class="detail-aside">{menu}</aside>
  </div>
</section>

<section class="section section--tight steel blueprint">
  <div class="wrap">
    <span class="kicker">{escape(t["why_us"])}</span>
    <p class="lead why-us">{escape(t["why_us_text"])}</p>
  </div>
</section>

{call_to_action(page)}'''
    return layout(page, title, intro, body, page.path, image)


def service_page(page, service):
    name, summary = service[page.lang]
    items = [(s[page.lang][0], f"services/{s['slug']}.html") for s in SERVICES]
    menu = side_menu(page, items, page.t["services_page"])
    return detail_page(page, service["slug"], page.t["service"], name, summary, service["image"], menu, page.t["services_page"])


def department_page(page, dep):
    name, company, summary = dep[page.lang]
    items = [(d[page.lang][0], f"departments/{d['slug']}.html") for d in DEPARTMENTS]
    menu = side_menu(page, items, page.t["dept_kicker"])
    return detail_page(page, dep["slug"], company, name, summary, dep["image"], menu, page.t["dept_kicker"])


def projects_page(page):
    t = page.t
    projects = projects_in(page.lang)

    buttons = f'<button class="filter-btn" data-filter="all" aria-pressed="true">{escape(t["all"])}<span class="count">{len(projects)}</span></button>'
    for tag, en, ar in FILTERS:
        count = len([p for p in projects if tag in p["tags"]])
        if count:
            name = en if page.lang == "en" else ar
            buttons += f'<button class="filter-btn" data-filter="{tag}" aria-pressed="false">{escape(name)}<span class="count">{count}</span></button>'

    cards = "".join(project_card(page, p, i % 3) for i, p in enumerate(projects))
    body = f'''{page_hero(page, t["projects_kicker"], t["projects_page"], t["projects_intro"], crumbs=[(t["projects_page"], None)])}

<section class="section pt-0">
  <div class="wrap">
    <div class="filters" data-filters role="group">{buttons}</div>
    <div class="proj-grid">{cards}</div>
  </div>
</section>

{call_to_action(page)}'''
    return layout(page, t["projects_page"], t["projects_intro"], body, "projects.html")


def project_page(page, project):
    t = page.t
    lang = page.lang
    item = project[lang]
    title = item["title"]
    projects = projects_in(lang)
    index = projects.index(project)
    previous = projects[index - 1]
    following = projects[(index + 1) % len(projects)]

    related = [p for p in projects if p is not project and set(p["tags"]) & set(project["tags"])][:3]
    if not related:
        related = [p for p in projects if p is not project][:3]
    related_html = "".join(project_card(page, p, i) for i, p in enumerate(related))

    tags = "".join(f'<a class="chip" href="{page.url("projects.html")}#{tag}">{escape(filter_name(tag, lang))}</a>' for tag in project["tags"])

    facts = ""
    if item.get("facts"):
        rows = "".join(f"<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>" for label, value in item["facts"])
        facts = f'<div class="aside-card"><h4>{escape(t["project_details"])}</h4><dl class="facts">{rows}</dl></div>'

    if project[t["other"]]:
        other_path = page.path
    else:
        other_path = "projects.html"

    body = f'''{page_hero(page, t["projects_page"], title, image=project["image"], crumbs=[(t["projects_page"], page.url("projects.html")), (title, None)])}

<section class="section">
  <div class="wrap detail">
    <article class="reveal">
      <div class="rich">{render_body(item["body"], page)}</div>
      <div class="proj-facts">{tags}</div>
      {gallery(page, project["gallery"], "p", title)}
      <nav class="pager" aria-label="Projects">
        <a href="{page.url("projects/" + previous["slug"] + ".html")}"><small>{escape(t["previous"])}</small><b>{escape(previous[lang]["title"])}</b></a>
        <a class="next" href="{page.url("projects/" + following["slug"] + ".html")}"><small>{escape(t["next"])}</small><b>{escape(following[lang]["title"])}</b></a>
      </nav>
    </article>
    <aside class="detail-aside">
      {facts}
      <div class="aside-card aside-cta">
        <h3>{escape(t["cta_title"])}</h3><p>{escape(t["cta_text"])}</p>
        <a class="btn" href="{page.url("contact.html")}">{escape(t["start_project"])} {ARROW}</a>
      </div>
    </aside>
  </div>
</section>

<section class="section section--tight steel">
  <div class="wrap">
    <div class="row-between mb-32"><h2>{escape(t["more_projects"])}</h2><a class="link-arrow" href="{page.url("projects.html")}">{escape(t["view_all"])} {ARROW}</a></div>
    <div class="proj-grid">{related_html}</div>
  </div>
</section>

{call_to_action(page)}'''
    description = first_paragraph(item["body"]) or t["projects_intro"]
    return layout(page, title, description, body, other_path, project["image"])


def posts_page(page, post_type):
    t = page.t
    if post_type == "articles":
        title, intro = t["articles_page"], t["articles_intro"]
    else:
        title, intro = t["news_page"], t["news_intro"]
    cards = "".join(post_card(page, p, i % 3) for i, p in enumerate(posts_in(page.lang, post_type)))
    body = f'''{page_hero(page, t["news_kicker"], title, intro, crumbs=[(title, None)])}
<section class="section light"><div class="wrap"><div class="news-grid">{cards}</div></div></section>
{call_to_action(page)}'''
    return layout(page, title, intro, body, f"{post_type}.html")


def post_page(page, post):
    t = page.t
    item = post[page.lang]
    post_type = post["type"]
    label = t["articles_page"] if post_type == "articles" else t["news_page"]
    short_title = item["title"] if len(item["title"]) <= 40 else item["title"][:40] + "…"

    more = [p for p in posts_in(page.lang, post_type) if p is not post][:3]
    more_html = ""
    if more:
        cards = "".join(post_card(page, p, i) for i, p in enumerate(more))
        more_html = f'''<section class="section light">
  <div class="wrap">
    <div class="row-between mb-32"><h2>{escape(label)}</h2><a class="link-arrow" href="{page.url(post_type + ".html")}">{escape(t["view_all"])} {ARROW}</a></div>
    <div class="news-grid">{cards}</div>
  </div>
</section>'''

    other_path = page.path if post[t["other"]] else f"{post_type}.html"

    body = f'''<section class="page-hero blueprint">
  <div class="wrap article">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="{page.url("index.html")}">{escape(t["nav"][0][1])}</a><span aria-hidden="true">/</span>
      <a href="{page.url(post_type + ".html")}">{escape(label)}</a><span aria-hidden="true">/</span>
      <span>{escape(short_title)}</span>
    </nav>
    <div class="news-date"><span class="pill">{escape(label)}</span><time datetime="{post["date"]}">{format_date(post["date"], page.lang)}</time></div>
    <h1 class="h2 mt-12">{escape(item["title"])}</h1>
  </div>
</section>

<section class="section pt-0">
  <div class="wrap article">
    <div class="article-cover"><img src="{page.link(post["image"])}" alt="" fetchpriority="high"></div>
    <div class="rich">{render_body(item["body"], page)}</div>
  </div>
</section>

{more_html}
{call_to_action(page)}'''
    return layout(page, item["title"], first_paragraph(item["body"]) or label, body, other_path, post["image"])


def ai_page(page):
    ai = page.ai
    suggestions = "".join(f'<button type="button" class="chat-chip">{escape(q)}</button>' for q in ai["suggestions"])

    # texts the chat script needs (error messages etc.), passed as JSON
    settings = json.dumps({"maxQuestions": 10, "errors": ai["errors"]}, ensure_ascii=False)

    body = f'''{page_hero(page, ai["kicker"], ai["page_title"], ai["page_intro"], crumbs=[(ai["nav"], None)])}

<section class="section pt-0">
  <div class="wrap chat-wrap">
    <div class="chat-card">
      <div class="chat-head">
        <span class="ai-avatar">{icon("spark")}</span>
        <div><b>{escape(ai["chat_name"])}</b><small><i class="ai-online"></i>{escape(ai["chat_status"])}</small></div>
        <button type="button" class="btn btn--sm btn--ghost chat-new" id="chat-new">{escape(ai["new_chat"])}</button>
      </div>

      <div class="chat-messages" id="chat-messages" aria-live="polite">
        <div class="chat-msg chat-msg--bot">{escape(ai["welcome"])}</div>
      </div>

      <div class="chat-suggestions" id="chat-suggestions">
        <span>{escape(ai["suggestions_title"])}</span>
        {suggestions}
      </div>

      <form class="chat-form" id="chat-form">
        <label class="visually-hidden" for="chat-input">{escape(ai["placeholder"])}</label>
        <textarea id="chat-input" rows="1" maxlength="500" placeholder="{escape(ai["placeholder"])}" required></textarea>
        <button class="chat-send" type="submit" aria-label="{escape(ai["send"])}">{icon("send")}</button>
      </form>
    </div>

    <p class="chat-note"><span id="chat-left">10</span> {escape(ai["questions_left"])} · {escape(ai["disclaimer"])}</p>
  </div>
</section>

<script id="chat-settings" type="application/json">{settings}</script>

{call_to_action(page)}'''
    return layout(page, ai["page_title"], ai["page_intro"], body, "ai.html")


def contact_page(page):
    t = page.t

    def text_field(name, label, kind="text", required=False, full=False):
        css = "field field--full" if full else "field"
        req = " required" if required else ""
        return f'<div class="{css}"><label for="{name}">{escape(label)}</label><input id="{name}" name="{name}" type="{kind}"{req}></div>'

    def yes_no(name, label, first=None, second=None):
        first = first or t["yes"]
        second = second or t["no"]
        return f'''<fieldset class="field"><legend>{escape(label)}</legend><div class="radios">
  <label><input type="radio" name="{name}" value="{escape(first)}" required> {escape(first)}</label>
  <label><input type="radio" name="{name}" value="{escape(second)}"> {escape(second)}</label>
</div></fieldset>'''

    def branch_field(name):
        options = "".join(f"<option>{escape(b)}</option>" for b in t["form_branches"])
        return (f'<div class="field"><label for="{name}">{escape(t["branch"])}</label>'
                f'<select id="{name}" name="{name}" required><option value="">{escape(t["choose"])}</option>{options}</select></div>')

    def text_area(name, label):
        return f'<div class="field field--full"><label for="{name}">{escape(label)}</label><textarea id="{name}" name="{name}"></textarea></div>'

    def contact_fields(prefix):
        return (text_field(prefix + "name", t["name"], required=True)
                + text_field(prefix + "phone", t["phone_number"], "tel", required=True)
                + text_field(prefix + "email", t["email"], "email", full=True))

    forms = {
        "office": contact_fields("o_") + yes_no("o_plans", t["has_plans"]) + yes_no("o_designed", t["is_designed"])
                  + branch_field("o_branch") + text_area("o_message", t["message"]),
        "contracting": contact_fields("c_") + yes_no("c_planned", t["is_planned"]) + branch_field("c_branch")
                       + text_area("c_message", t["message"]),
        "lgs": contact_fields("l_") + yes_no("l_factory", t["has_factory"]) + yes_no("l_entity", t["entity"], t["company"], t["individual"])
               + text_field("l_company", t["company_name"]) + yes_no("l_training", t["wants_training"]) + branch_field("l_branch"),
        "feedback": contact_fields("f_") + text_field("f_service", t["your_service"], full=True) + text_field("f_responsible", t["responsible"])
                    + text_field("f_heard", t["heard_from"]) + text_area("f_opinion", t["opinion"])
                    + yes_no("f_problems", t["difficulties"]) + text_area("f_suggestions", t["suggestions"]),
    }

    tabs = ""
    panels = ""
    for i, (key, label) in enumerate(t["form_tabs"]):
        selected = "true" if i == 0 else "false"
        hidden = "" if i == 0 else " hidden"
        tabs += f'<button class="tab" role="tab" id="tab-{key}" data-key="{key}" aria-controls="panel-{key}" aria-selected="{selected}" tabindex="{0 if i == 0 else -1}">{escape(label)}</button>'
        panels += f'''<div class="tab-panel" role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{hidden}>
  <form data-mailto="{COMPANY["email"]}" data-subject="{escape(t["brand"])}: {escape(label)}" novalidate>
    <div class="form-grid">{forms[key]}</div>
    <div class="form-foot"><button class="btn" type="submit">{escape(t["send"])} {ARROW}</button><small>{escape(t["form_note"])}</small></div>
  </form>
</div>'''

    phones = "".join(f'<li><a class="ltr" href="tel:{p}">{p}</a></li>' for p in COMPANY["phones"])
    branches = "".join(f"<li><b>{escape(name)}</b>: {escape(address)}</li>" for name, address in BRANCHES[page.lang])
    hours = "".join(f'<div><span>{escape(day)}</span><span class="ltr">{time}</span></div>' for day, time in t["hours_list"])
    ai = page.ai

    body = f'''{page_hero(page, t["nav"][-1][1], t["contact_page"], t["contact_intro"], crumbs=[(t["contact_page"], None)])}

<section class="section pt-0">
  <div class="wrap contact">
    <div class="info-list reveal">
      <div class="info-row"><span class="info-ic">{icon("phone")}</span><div><h3>{escape(t["phone"])}</h3><ul>{phones}</ul></div></div>
      <div class="info-row"><span class="info-ic">{icon("mail")}</span><div><h3>{escape(t["email"])}</h3>
        <p><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></p>
        <p><a href="{COMPANY["linktree"]}" target="_blank" rel="noopener">Linktree</a></p></div></div>
      <div class="info-row"><span class="info-ic">{icon("pin")}</span><div><h3>{escape(t["branches"])}</h3><ul>{branches}</ul></div></div>
      <div class="info-row"><span class="info-ic">{icon("spark")}</span><div><h3>{escape(ai["contact_title"])}</h3><p>{escape(ai["contact_text"])}</p>
        <p class="mt-12"><a class="btn btn--sm ai-btn" href="{page.url("ai.html")}">{escape(ai["button"])}</a></p></div></div>
      <div class="info-row"><span class="info-ic">{icon("clock")}</span><div><h3>{escape(t["hours"])}</h3><div class="hours">{hours}</div></div></div>
    </div>
    <div class="form-card reveal" data-delay="1">
      <div class="tabs" role="tablist" aria-label="{escape(t["contact_page"])}">{tabs}</div>
      {panels}
    </div>
  </div>
</section>'''
    return layout(page, t["contact_page"], t["contact_intro"], body, "contact.html")


# ---------- write everything ----------

def save(lang, path, html):
    file = os.path.join(OUT, lang, path)
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)


def copy_files():
    # Remove old pages but keep dist/media, OneDrive sometimes locks it while syncing.
    for folder in ["en", "ar", "assets"]:
        shutil.rmtree(os.path.join(OUT, folder), ignore_errors=True)
    shutil.copytree("assets", os.path.join(OUT, "assets"), dirs_exist_ok=True)
    shutil.copytree("media", os.path.join(OUT, "media"), dirs_exist_ok=True)

    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write('''<!doctype html>
<html><head><meta charset="utf-8"><title>Omran Tech Group | مجموعة عمران تك</title>
<script>
  var lang = (navigator.language || "").toLowerCase().startsWith("ar") ? "ar" : "en";
  location.replace(lang + "/index.html");
</script>
<meta http-equiv="refresh" content="0; url=en/index.html"></head>
<body><a href="en/index.html">English</a> · <a href="ar/index.html">العربية</a></body></html>''')


def main():
    copy_files()
    count = 0
    for lang in LANGS:
        pages = {
            "index.html": home_page,
            "about.html": about_page,
            "services.html": services_page,
            "projects.html": projects_page,
            "contact.html": contact_page,
            "ai.html": ai_page,
            "news.html": lambda page: posts_page(page, "news"),
            "articles.html": lambda page: posts_page(page, "articles"),
        }
        for path, make in pages.items():
            save(lang, path, make(Page(lang, path)))
            count += 1

        for service in SERVICES:
            path = f"services/{service['slug']}.html"
            save(lang, path, service_page(Page(lang, path), service))
            count += 1

        for dep in DEPARTMENTS:
            path = f"departments/{dep['slug']}.html"
            save(lang, path, department_page(Page(lang, path), dep))
            count += 1

        for project in projects_in(lang):
            path = f"projects/{project['slug']}.html"
            save(lang, path, project_page(Page(lang, path), project))
            count += 1

        for post in posts_in(lang):
            path = f"{post['type']}/{post['slug']}.html"
            save(lang, path, post_page(Page(lang, path), post))
            count += 1

    print(f"Done: {count} pages in {OUT}/")


if __name__ == "__main__":
    main()
