#!/usr/bin/env python3
"""leibingerturkiye.com kategori sayfalarını üretir.
Kullanım: python3 _build/build.py  (repo kökünden)
Ürün verisi: _build/products.json (Kristal Diş Deposu, Otto Leibinger markası)
"""
import json, html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(ROOT, '_build')
SITE = 'https://leibingerturkiye.com'
KD = 'https://www.kristaldisdeposu.com'
IMG = KD + '/idea/hy/90/myassets/products/'
LB = 'https://www.leibinger-dental.de/wp-content/uploads/'
BRAND = KD + '/marka/otto-leibinger'

P = json.load(open(os.path.join(B, 'products.json'), encoding='utf-8'))
esc = html.escape

def model(p):
    return p['sku'].replace('OT.', '') if p['sku'] else ''

def by_cat(*cats):
    return [p for p in P if any(c in p['cats'] for c in cats)]

# ---------------- sayfa içerikleri ----------------
PAGES = [
 dict(
  slug='davye', nav='Davye',
  title='Davye Çeşitleri ve Numaraları | Alman Menşeli Leibinger Davyeler',
  desc='Alman menşeli Otto Leibinger davyeler: üst ve alt çene davyeleri, kök davyeleri, çocuk davye seti. Davye numaraları ve kullanım alanları. Türkiye resmî distribütörü Kristal Diş Deposu.',
  h1='Davye', h1em='çeşitleri', eyebrow='Diş çekim davyeleri · İngiliz tipi',
  hero=LB + '2025/02/20210708_Leibinger_0046.jpg',
  lead='Leibinger davyeleri Almanya, Mühlheim\'da paslanmaz cerrahi çelikten üretilir. Yetişkin ve çocuk davyeleri İngiliz tipi (English pattern) formdadır; her model belirli bir diş grubuna ve çeneye göre şekillendirilmiştir.',
  cats=('Davyeler',),
  guide_title='Davye numaraları ve kullanım alanları',
  guide_head=('Numara', 'Çene', 'Kullanım alanı'),
  guide=[('2','Üst','Premolar dişler'),('7','Üst','Kökler ve premolarlar'),('17','Üst','Sağ büyük azı dişleri'),('18','Üst','Sol büyük azı dişleri'),('51A / 51S','Üst','Kökler, dar gagalı'),('67A','Üst','Üçüncü büyük azılar (yirmilik)'),('13','Alt','Kökler ve premolarlar'),('22','Alt','Büyük azı dişleri'),('23','Alt','Büyük azı dişleri (boynuz gagalı)'),('33','Alt','Kökler'),('46L','Alt','Çok ince kökler'),('79','Alt','Üçüncü büyük azılar (yirmilik)'),('86A / 86C','Alt','Büyük azı dişleri')],
  guide_note='Tablo, Kristal Diş Deposu\'ndaki Leibinger davye modellerinin isimlerinden derlenmiştir. Model seçiminde hasta anatomisi ve klinik değerlendirme esas alınmalıdır.',
  faq=[('Üst çene davyesi ile alt çene davyesi nasıl ayırt edilir?','Üst çene davyelerinde gaga ile sap genellikle aynı doğrultuda ya da hafif açılıdır; alt çene davyelerinde gaga sapa göre belirgin şekilde dik açılıdır. Leibinger modellerinde çene ve diş grubu ürün adında belirtilir.'),
       ('İngiliz tipi (English pattern) davye nedir?','Avrupa\'da yaygın kullanılan, menteşesi yatay olan klasik davye formudur. Leibinger yetişkin ve çocuk davyeleri bu formdadır.'),
       ('Davye seti mi, tek davye mi almalıyım?','Muayenehaneyi yeni kuranlar için set, temel diş gruplarını tek seferde karşılar. Eksik ya da yıpranmış modelleri tamamlamak için tek davye almak daha ekonomiktir.'),
       ('Davyeler otoklavlanabilir mi?','Leibinger davyeleri paslanmaz cerrahi çelikten üretilir ve standart otoklav sterilizasyonuna uygundur. Üreticinin temizlik ve bakım talimatlarına uyulmalıdır.')],
  related=('el-aletleri','kuret','portegu'),
 ),
 dict(
  slug='kuret', nav='Küret',
  title='Gracey Küret Numaraları ve Periodontal Küretler | Leibinger',
  desc='Alman menşeli Leibinger Gracey küretler (1-2\'den 15-16\'ya), Lucas cerrahi küretler ve periodontal scaler\'lar. Küret numaraları hangi bölgede kullanılır?',
  h1='Küret', h1em='ve scaler', eyebrow='Periodontoloji · ColorIdent · SharpCut',
  hero=LB + '2025/02/20250203-Leibinger-018.jpg',
  lead='Leibinger Gracey küretleri, çift uçlu ve bölgeye özel açılandırılmış çalışma uçlarıyla subgingival temizlik ve kök yüzeyi düzleştirme için tasarlanmıştır. Leibinger küret ailesinde ColorIdent renk halkalı ve SharpCut kaplamalı seçenekler de bulunur.',
  cats=('Gracey Küretler','Küret ve Scaler'),
  guide_title='Gracey küret numaraları',
  guide_head=('Numara','Bölge','Yüzey'),
  guide=[('1-2','Ön dişler (kesici ve kanin)','Tüm yüzeyler'),('3-4','Ön dişler','Tüm yüzeyler'),('5-6','Ön dişler ve premolarlar','Tüm yüzeyler'),('7-8','Premolar ve molarlar','Bukkal ve lingual'),('9-10','Premolar ve molarlar','Bukkal ve lingual'),('11-12','Arka dişler','Mezial'),('13-14','Arka dişler','Distal'),('15-16','Arka dişler','Mezial (açılı)')],
  guide_note='Gracey küretler tek kesici kenarlıdır ve her numara belirli bir bölge ve yüzey için açılandırılmıştır. Üniversal scaler\'lar ise supragingival diş taşı temizliğinde kullanılır.',
  faq=[('Gracey küret ile üniversal küret arasındaki fark nedir?','Gracey küretlerin tek kesici kenarı vardır ve bölgeye özeldir; üniversal küretlerin iki kesici kenarı vardır ve ağzın her bölgesinde kullanılabilir.'),
       ('Hangi Gracey numaraları temel set için yeterlidir?','Birçok klinikte 5-6 (ön bölge), 7-8 (arka bukkal-lingual), 11-12 (arka mezial) ve 13-14 (arka distal) temel set olarak kullanılır. Leibinger Gracey seti tüm numaraları bir arada sunar.'),
       ('Küretler bilenmeli mi?','Evet, keskinliğini kaybeden küret etkinliğini yitirir. SharpCut kaplamalı modeller keskinliği daha uzun süre korumak için geliştirilmiştir.')],
  related=('davye','el-aletleri','portegu'),
 ),
 dict(
  slug='portegu', nav='Portegü',
  title='Portegü (İğne Tutucu) Çeşitleri | Mayo-Hegar, Mathieu, Crile-Wood | Leibinger',
  desc='Alman menşeli Leibinger portegüler: Mayo-Hegar, Mathieu, Crile-Wood ve tungsten karbid (TC) uçlu modeller; Kelly ve Halstead hemostatik pensler.',
  h1='Portegü', h1em='ve hemostatik pens', eyebrow='Cerrahi · Dikiş',
  hero=LB + '2025/02/20250203-Leibinger-059.jpg',
  lead='Leibinger portegüleri dikiş iğnesini sağlam ve dengeli tutmak için hassas ağızlarla üretilir. Tungsten karbid (TC) uçlu modeller, iğneyi kaydırmadan tutar ve uzun kullanım ömrü sunar; altın renkli halkalarından kolayca ayırt edilir.',
  cats=('Portegü',),
  guide_title='Hangi portegü?',
  guide_head=('Model','Özellik','Uzunluk'),
  guide=[('Mayo-Hegar','Klasik makas tutuşlu, kilitli portegü','14 · 16 · 18 cm'),('Mayo-Hegar TC','Tungsten karbid ağızlı','14 · 16 · 18 cm'),('Crile-Wood TC','İnce ağızlı, hassas dikiş için','15 · 18 cm'),('Mathieu','Avuç içi tutuşlu, hızlı açılıp kapanan','14 · 17 cm'),('Kelly','Hemostatik pens, düz ve eğri','—'),('Halstead Mosquito','İnce uçlu hemostatik pens, eğri','—')],
  guide_note='Uzunluklar Kristal Diş Deposu\'ndaki Leibinger modellerinden alınmıştır.',
  faq=[('TC (tungsten karbid) portegünün farkı nedir?','Ağızlarına tungsten karbid uç yerleştirilmiş portegüler iğneyi daha sıkı ve kaydırmadan tutar, ağız yüzeyi daha geç aşınır. Altın renkli halkalarından tanınırlar.'),
       ('Diş hekimliğinde hangi boy portegü kullanılır?','Ağız içi dikişte en yaygın kullanılan boylar 14–16 cm\'dir. Arka bölgelere erişim için daha uzun modeller tercih edilebilir.'),
       ('Mathieu portegü ne zaman tercih edilir?','Avuç içi tutuşlu Mathieu portegü, hızlı ve seri dikiş atmak isteyen hekimler tarafından tercih edilir.')],
  related=('cerrahi-makas','davye','kuret'),
 ),
 dict(
  slug='cerrahi-makas', nav='Cerrahi makas',
  title='Cerrahi Makas Çeşitleri | Iris, Lagrange, Locklin, Dean | Leibinger',
  desc='Alman menşeli Leibinger dental cerrahi makaslar: Iris (düz ve eğri), Lagrange, Locklin ve Dean gum makasları; paslanmaz çelik ve tungsten karbid (SC) seçenekleri.',
  h1='Cerrahi', h1em='makas', eyebrow='Cerrahi · Yumuşak doku',
  hero=LB + '2025/02/20250203-Leibinger-059.jpg',
  lead='Leibinger cerrahi makasları yumuşak doku, dikiş ve flep işlemleri için ince ve dengeli ağızlarla üretilir. SC (supercut) tungsten karbid kesici kenarlı modeller keskinliği daha uzun korur.',
  cats=('Cerrahi Makas',),
  guide_title='Makas modelleri',
  guide_head=('Model','Kullanım','Seçenek'),
  guide=[('Iris','İnce yumuşak doku ve dikiş kesimi','Düz · eğri · paslanmaz · SC'),('Lagrange','Çift eğri ağız, dikiş alma ve gingival işlemler','Paslanmaz · SC'),('Locklin','Açılı, tırtıklı ağız','16 cm'),('Dean Gum','Tırtıklı ağız, diş eti işlemleri','17 cm')],
  guide_note='SC (supercut) modellerin kesici kenarında tungsten karbid bulunur ve altın renkli halkalarından ayırt edilir.',
  faq=[('Iris makas ile Lagrange makas arasındaki fark nedir?','Iris makas düz ya da tek eğri ince ağızlıdır; Lagrange makasın ağzı çift eğridir ve dar alanlarda dikiş almak için uygundur.'),
       ('SC (tungsten karbid) makas neden tercih edilir?','Tungsten karbid kesici kenar daha sert olduğu için keskinliğini uzun süre korur ve dokuyu ezmeden keser.'),
       ('Cerrahi makaslar otoklavlanabilir mi?','Evet, paslanmaz çelik ve SC makaslar standart otoklav sterilizasyonuna uygundur; menteşe bölgesi düzenli temizlenmeli ve yağlanmalıdır.')],
  related=('portegu','davye','el-aletleri'),
 ),
 dict(
  slug='el-aletleri', nav='El aletleri',
  title='Diş Hekimliği El Aletleri | Alman Menşeli Leibinger',
  desc='Alman menşeli Otto Leibinger diş hekimliği el aletleri: davye, elevatör, küret, portegü, cerrahi makas, ayna, sond, ekskavatör, bistüri sapı, presel ve ortodonti pensleri.',
  h1='Diş hekimliği', h1em='el aletleri', eyebrow='Teşhisten cerrahiye · 200+ ürün',
  hero=LB + '2025/02/20250203-Leibinger-068.jpg',
  lead='Otto Leibinger, 1978\'den beri Almanya\'nın Tuttlingen bölgesinde, Mühlheim\'da diş hekimliği el aletleri üretiyor. Teşhis, restoratif tedavi, endodonti, periodontoloji, cerrahi, çekim, implantoloji ve ortodonti için 200\'ü aşkın Leibinger ürünü Kristal Diş Deposu\'nda.',
  cats=('El Aletleri','Aynalar','Pensetler'),
  guide_title=None,
  faq=[('Leibinger el aletleri nerede üretiliyor?','Otto Leibinger GmbH, Almanya\'nın Tuttlingen bölgesindeki Mühlheim an der Donau\'da üretim yapan bir aile şirketidir. Aletler Alman menşelidir.'),
       ('Leibinger ürünlerini Türkiye\'de nereden alabilirim?','Türkiye resmî distribütörü Kristal Diş Deposu\'dur. Ürünler kristaldisdeposu.com üzerinden diş hekimlerine satılır.'),
       ('Fiyatları neden göremiyorum?','Fiyatlar diş hekimlerine özeldir. Kristal Diş Deposu\'na ücretsiz üye olduktan sonra görünür.')],
  related=('davye','kuret','portegu','cerrahi-makas'),
 ),
]
PG = {p['slug']: p for p in PAGES}

# ---------------- şablon ----------------
def header():
    links = ''.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES)
    return f'''<header>
  <div class="wrap">
    <a class="logo" href="/"><img src="{LB}2025/01/cropped-cropped-1978-3-2-1-2.png" alt="Leibinger Dental"><span>TÜRKİYE</span></a>
    <nav aria-label="Kategoriler">{links}</nav>
    <a class="btn btn-green" href="{BRAND}">Ürünleri gör</a>
  </div>
</header>'''

FOOTER = f'''<footer>
  <div class="wrap">
    <img src="{KD}/idea/hy/90/themes/selftpl_68a31aa3a0c2a/assets/uploads/logo.png" alt="Kristal Diş Deposu">
    <div>Kristal Diş Deposu · Otto Leibinger Türkiye resmî distribütörü<br>Cumhuriyet Mah. Tennuri Sok. No:13/C, Melikgazi / Kayseri
      <div class="note">Kategoriler: {' · '.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES)}</div>
      <div class="note">Görseller ve video: Otto Leibinger GmbH, Mühlheim an der Donau.</div></div>
    <a href="{KD}">kristaldisdeposu.com</a>
  </div>
</footer>'''

def card(p):
    m = model(p)
    img = f'<img src="{IMG}{esc(p["img"])}" alt="{esc(p["name"])}" loading="lazy">' if p['img'] else ''
    return (f'<a class="p" href="{KD}/urun/{esc(p["slug"])}">{img}<div class="b">'
            f'{f"<small>Model {esc(m)}</small>" if m else ""}<h3>{esc(p["name"])}</h3></div></a>')

def page(pg):
    prods = by_cat(*pg['cats'])
    url = f'{SITE}/{pg["slug"]}/'
    guide = ''
    if pg.get('guide_title'):
        rows = ''.join('<tr>' + ''.join(f'<td>{esc(c)}</td>' for c in r) + '</tr>' for r in pg['guide'])
        head = ''.join(f'<th>{esc(h)}</th>' for h in pg['guide_head'])
        guide = f'''<section class="guide-s"><div class="wrap">
  <span class="eyebrow">Seçim rehberi</span>
  <h2 style="margin-top:12px">{esc(pg["guide_title"])}</h2>
  <div class="tbl-wrap"><table class="gt"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
  <p class="note2">{esc(pg["guide_note"])}</p>
</div></section>'''
    hub = ''
    if pg['slug'] == 'el-aletleri':
        cards = ''.join(f'<a class="hubc" href="/{PG[s]["slug"]}/"><img src="{PG[s]["hero"]}" alt="" loading="lazy"><span>{PG[s]["nav"]}</span></a>' for s in ('davye','kuret','portegu','cerrahi-makas'))
        hub = f'<section style="padding-bottom:0"><div class="wrap"><span class="eyebrow">Kategoriler</span><h2 style="margin-top:12px">Gruba göre <em>incele</em></h2><div class="hub">{cards}</div></div></section>'
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in pg['faq'])
    rel = ''.join(f'<a class="btn btn-ghost" href="/{s}/">{PG[s]["nav"]}</a>' for s in pg['related'])
    ld = [
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Leibinger Dental Türkiye","item":SITE+'/'},
        {"@type":"ListItem","position":2,"name":pg['nav'],"item":url}]},
      {"@context":"https://schema.org","@type":"ItemList","name":pg['h1']+' '+pg['h1em'],"itemListElement":[
        {"@type":"ListItem","position":i+1,"item":{"@type":"Product","name":p['name'],"sku":model(p) or None,
          "brand":{"@type":"Brand","name":"Otto Leibinger"},"image":IMG+p['img'] if p['img'] else None,
          "url":f'{KD}/urun/{p["slug"]}',"countryOfOrigin":"DE"}} for i, p in enumerate(prods)]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in pg['faq']]},
    ]
    ld_s = '\n'.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    count = f'{len(prods)} ürün' if prods else ''
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(pg["title"])}</title>
<meta name="description" content="{esc(pg["desc"])}">
<link rel="canonical" href="{url}">
<link rel="icon" href="{LB}2025/01/cropped-cropped-1978-3-2-1-2.png">
<meta property="og:title" content="{esc(pg["title"])}">
<meta property="og:description" content="{esc(pg["desc"])}">
<meta property="og:image" content="{pg["hero"]}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="tr_TR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="/style.css">
{ld_s}
</head>
<body>
{header()}
<main>
<section class="phero">
  <div class="wrap phero-grid">
    <div class="txt">
      <nav class="crumb" aria-label="Konum"><a href="/">Leibinger Türkiye</a> / <span>{esc(pg["nav"])}</span></nav>
      <span class="de"><span class="flag" aria-hidden="true"></span>Made in Germany · Alman menşeli</span>
      <span class="eyebrow">{esc(pg["eyebrow"])}</span>
      <h1>{esc(pg["h1"])} <em>{esc(pg["h1em"])}</em></h1>
      <p class="lead">{esc(pg["lead"])}</p>
      <div class="cta"><a class="btn btn-green" href="#urunler">Modelleri gör</a><a class="btn btn-ghost" href="{KD}/uye-ol">Üye olun, fiyatları görün</a></div>
    </div>
    <img class="phero-img" src="{pg["hero"]}" alt="Leibinger {esc(pg["nav"].lower())} aletleri">
  </div>
</section>
{hub}
<section id="urunler">
  <div class="wrap">
    <div class="head"><div><span class="eyebrow">Kristal Diş Deposu'nda · {count}</span><h2>Leibinger <em>{esc(pg["nav"].lower())}</em> modelleri</h2>
    <p class="lead">Her ürün Kristal Diş Deposu'ndaki sayfasına gider. Fiyatlar diş hekimlerine özeldir ve üye girişinden sonra görünür.</p></div>
    <a class="btn btn-ghost" href="{BRAND}">Tüm Leibinger ürünleri</a></div>
    <div class="grid pgrid">{''.join(card(p) for p in prods)}</div>
  </div>
</section>
{guide}
<section class="faq-s">
  <div class="wrap">
    <span class="eyebrow">Sık sorulan sorular</span>
    <h2 style="margin-top:12px">{esc(pg["nav"])} hakkında</h2>
    <div class="faq">{faq}</div>
    <div class="rel"><span>Diğer kategoriler:</span>{rel}</div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="cta-band">
      <div><span class="eyebrow">Diş hekimlerine özel fiyat</span>
        <h2 style="margin-top:10px">Alman menşeli Leibinger aletlerini resmî distribütörden alın</h2>
        <p>Fiyatlar yalnızca diş hekimi üyelere açıktır. Kristal Diş Deposu'na ücretsiz üye olun, tüm Leibinger ürünlerinin fiyatlarını görün ve sipariş verin.</p></div>
      <div class="acts"><a class="btn btn-green" href="{KD}/uye-ol">Üye ol</a><a class="btn btn-ghost" href="{BRAND}">Leibinger ürünlerine git</a></div>
    </div>
  </div>
</section>
</main>
{FOOTER}
</body>
</html>
'''

EXTRA_CSS = '''
/* ---- kategori sayfaları ---- */
.phero{background:var(--green-soft);border-bottom:6px solid var(--green);padding-block:clamp(36px,6vw,72px)}
.phero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,5vw,64px);align-items:center}
.phero .txt{display:grid;gap:14px;justify-items:start;min-width:0}
.phero h1{font-size:clamp(2.4rem,5.6vw,4.4rem);font-weight:600;text-transform:uppercase;line-height:1.02}
.phero h1 em{font-style:normal;color:var(--green)}
.phero-img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:20px;outline:3px solid var(--green);outline-offset:4px}
.phero .de{background:#fff;border-color:var(--green);color:var(--ink)}
.phero .cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:6px}
.crumb{font-size:.85rem;color:var(--muted)}
.crumb a{color:var(--green-d)}
@media (max-width:860px){.phero-grid{grid-template-columns:1fr}}
.pgrid{grid-template-columns:repeat(4,1fr)}
.pgrid .p img{aspect-ratio:1;object-fit:contain;background:#fff}
.pgrid .p h3{font-family:var(--f-body);text-transform:none;font-size:.95rem;font-weight:600;line-height:1.35}
@media (max-width:960px){.pgrid{grid-template-columns:repeat(2,1fr)}}
.guide-s{background:var(--paper)}
.tbl-wrap{overflow-x:auto;margin-top:28px;background:#fff;border:1.5px solid var(--green);border-radius:16px}
.gt{width:100%;border-collapse:collapse;font-size:.97rem}
.gt th{background:var(--green);color:#fff;text-align:left;padding:12px 16px;font-weight:600}
.gt td{padding:12px 16px;border-top:1px solid var(--green-soft)}
.gt td:first-child{font-family:var(--f-mono);font-weight:500;white-space:nowrap;color:var(--green-d)}
.note2{color:var(--muted);font-size:.9rem;margin-top:12px;max-width:80ch}
.faq{display:grid;gap:10px;margin-top:28px;max-width:860px}
.faq details{border:1.5px solid var(--green);border-radius:14px;padding:14px 18px;background:#fff}
.faq summary{cursor:pointer;font-weight:600}
.faq p{margin:.6em 0 0;color:var(--muted)}
.rel{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:28px}
.rel span{color:var(--muted);font-size:.92rem;margin-right:4px}
.hub{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px}
.hubc{position:relative;border-radius:16px;overflow:hidden;aspect-ratio:4/3;display:block;outline:2px solid var(--green);text-decoration:none}
.hubc img{width:100%;height:100%;object-fit:cover}
.hubc span{position:absolute;left:12px;bottom:12px;background:var(--green);color:#fff;font-weight:600;padding:6px 14px;border-radius:999px}
@media (max-width:860px){.hub{grid-template-columns:repeat(2,1fr)}}
header{position:sticky}
footer .note a{color:var(--green-d)}
'''

def main():
    base = open(os.path.join(B, 'base.css'), encoding='utf-8').read()
    open(os.path.join(ROOT, 'style.css'), 'w', encoding='utf-8').write(base + EXTRA_CSS)
    for pg in PAGES:
        d = os.path.join(ROOT, pg['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(pg))
    urls = [SITE + '/'] + [f'{SITE}/{p["slug"]}/' for p in PAGES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    for pg in PAGES:
        print(pg['slug'], len(by_cat(*pg['cats'])), 'ürün')

if __name__ == '__main__':
    main()
