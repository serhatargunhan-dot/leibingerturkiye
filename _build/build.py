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
  guide_head=('Fig.', 'Çene', 'Kullanım alanı (Leibinger kataloğu)', 'Model'),
  guide=[('2','Üst','Kesici ve kanin dişler','600/2 · 604/2 ED'),('7','Üst','Premolar dişler','600/7 · 604/7 ED'),('17','Üst','Sağ büyük azı dişleri','600/17 · 604/17 ED'),('18','Üst','Sol büyük azı dişleri','600/18 · 604/18 ED'),('67A','Üst','Yirmi yaş dişleri, geniş','600/67A · 604/67A ED'),('51A','Üst','Ön bölge kökleri, dar gagalı','600/51A · 604/51A ED'),('51S','Üst','Kökler (çocuk serisi)','600/51S · 604/51S ED'),('13','Alt','Kanin ve premolar dişler','600/13 · 604/13 ED'),('22','Alt','Büyük azı dişleri, her iki taraf','600/22 · 604/22 ED'),('33','Alt','Kökler','600/33 · 604/33 ED'),('46L','Alt','Çok ince kökler, derin kavrama','600/46L · 604/46L ED'),('79','Alt','Yirmi yaş dişleri','600/79 · 604/79 ED'),('86A / 86C','Alt','Büyük azılar, derin ve yandan kavrama','600/86A · 600/86C'),('44X · 45X · 51X','Alt / her iki / üst','Kırık kök kalıntıları için “troubleshooter” davyeler','604/44X · 604/45X · 604/51X')],
  guide_note='Açıklamalar Leibinger ana kataloğundaki (İngiliz formu davyeler) tanımlardan çevrilmiştir. 604 serisi ErgoDesign saplıdır. Çocuk serisi (37, 39, 29S, 13S, 22S, 33S) 7 parçalı pedo set olarak da bulunur. Model seçiminde hasta anatomisi ve klinik değerlendirme esas alınmalıdır.',
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
  guide_head=('Numara','Bölge (Leibinger kataloğu)','Yüzey','Model'),
  guide=[('1-2','Ön dişler','Fasiyal ve oral','400/1-2 · 400/1-2ED'),('3-4','Ön dişler','Lingual / bukkal','400/3-4 · 400/3-4ED'),('5-6','Ön dişler','Fasiyal ve oral','400/5-6 · 400/5-6ED'),('7-8','Yan dişler','Fasiyal ve oral','400/7-8 · 400/7-8ED'),('9-10','Yan dişler','Lingual / bukkal','400/9-10 · 400/9-10ED'),('11-12','Premolar ve molarlar','Mezial','400/11-12 · 400/11-12ED'),('13-14','Premolar ve molarlar','Distal','400/13-14 · 400/13-14ED'),('15-16','Premolar ve molarlar','Mezial','400/15-16 · 400/15-16ED')],
  guide_note='ED = ErgoDesign sap. Deep Scale (M) Gracey modellerinde (1-2M, 5-6M, 7-8M, 11-12M, 13-14M) ilk şaft 3 mm daha uzun, çalışma ucu %50 daha kısadır; derin ve dar cepler ile kök yüzeyi düzleştirme için tasarlanmıştır. ColorIdent serisi (404/…) renk kodlu halkalarıyla numarayı uzaktan tanımayı kolaylaştırır.',
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
  guide_head=('Model','Özellik','Uzunluk','Katalog no'),
  guide=[('Mayo-Hegar','Klasik halka tutuşlu, kilitli portegü','14 · 16 · 18 cm','175/71 · 175/72 · 175/73'),('Olsen-Hegar','Portegü ve makas bir arada','14 cm','175/6'),('Crile-Wood','İnce ağızlı, hassas dikiş için','15 · 18 cm','175/61 · 175/62'),('Mathieu','Avuç içi tutuşlu, hızlı açılıp kapanan','14 · 17 cm','175/3 · 175/2'),('TC versiyonlar','Tungsten karbid (TC) uçlu, daha sert ve uzun ömürlü','Tüm modellerde','… TC')],
  guide_note='Uzunluk ve katalog numaraları Leibinger ana kataloğundan alınmıştır; listelenen modeller 3/0–4/0 dikiş iplikleri için uygundur. TC uçlu portegüler kimyasallara daha hassastır, üretici bakım talimatına uyulmalıdır.',
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
  guide_head=('Model','Uzunluk','Ağız','Katalog no'),
  guide=[('Iris','11 cm','Düz · eğri','220/2 · 220/1 (SC)'),('La Grange','11,5 cm','Çift eğri','245/1 (SC)'),('Goldman-Fox','13 cm','Düz · eğri, tırtıklı','240/1 · 240/2 (SC)'),('Kelly','16 cm','Düz · eğri','250/1 · 250/0 (SC)'),('Wagner','12 cm','Düz · eğri','230/1 · 230/2'),('Joseph','14,5 cm','Düz · eğri','235/3 · 235/4'),('Spencer (dikiş makası)','9 cm','—','—'),('Mikro makas','15 · 18 cm','Düz · eğri','251/31–251/34')],
  guide_note='SC = Supercut: özel bileme ile çok keskin kesici kenarlar; tek altın renkli halkasından ayırt edilir. Uzunluk ve katalog numaraları Leibinger ana kataloğundan alınmıştır.',
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
    links = ''.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES) + '<a href="/kataloglar/">Kataloglar</a>'
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
      <div class="note">Kategoriler: {' · '.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES)} · <a href="/kataloglar/">Kataloglar</a></div>
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
{LD_STORE}
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
{CONTACT_HTML}
{FOOTER}
</body>
</html>
'''

CONTACT_HTML = '<section class="contact" id="iletisim">\n  <div class="wrap contact-grid">\n    <div>\n      <span class="eyebrow">İletişim</span>\n      <h2 style="margin-top:12px">Leibinger ürünleri için <em>bize ulaşın</em></h2>\n      <p class="lead">Model seçimi, set içerikleri ve sipariş için doğrudan yazabilir ya da arayabilirsiniz.</p>\n      <a class="btn btn-wa" href="https://wa.me/905340867700?text=Merhaba%2C%20leibingerturkiye.com%20%C3%BCzerinden%20ula%C5%9F%C4%B1yorum.%20Leibinger%20%C3%BCr%C3%BCnleri%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." target="_blank" rel="noopener"><svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.2-3.8 1.2 1.2-3.7-.3-.4c-1.2-1.8-1.8-3.8-1.8-5.9C5 9.9 10 5.2 16 5.2s11 4.7 11 10.6-5 10.6-11 10.6zm6-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1c-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg><span>WhatsApp\'tan ulaşın</span></a>\n    </div>\n    <dl class="cinfo">\n      <div><dt>Yetkili</dt><dd>Serhat Argunhan · Kristal Diş Deposu</dd></div>\n      <div><dt>Telefon</dt><dd><a href="tel:+905340867700">0534 086 77 00</a></dd></div>\n      <div><dt>WhatsApp</dt><dd><a href="https://wa.me/905340867700?text=Merhaba%2C%20leibingerturkiye.com%20%C3%BCzerinden%20ula%C5%9F%C4%B1yorum.%20Leibinger%20%C3%BCr%C3%BCnleri%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." target="_blank" rel="noopener">0534 086 77 00</a></dd></div>\n      <div><dt>E-posta</dt><dd><a href="mailto:serhatarg@hotmail.com">serhatarg@hotmail.com</a></dd></div>\n      <div><dt>Adres</dt><dd>Cumhuriyet Mah. Tennuri Sok. No:13/C<br>Melikgazi / Kayseri</dd></div>\n    </dl>\n  </div>\n</section>\n<a class="wa-float" href="https://wa.me/905340867700?text=Merhaba%2C%20leibingerturkiye.com%20%C3%BCzerinden%20ula%C5%9F%C4%B1yorum.%20Leibinger%20%C3%BCr%C3%BCnleri%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum." target="_blank" rel="noopener" aria-label="WhatsApp\'tan ulaşın"><svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.2-3.8 1.2 1.2-3.7-.3-.4c-1.2-1.8-1.8-3.8-1.8-5.9C5 9.9 10 5.2 16 5.2s11 4.7 11 10.6-5 10.6-11 10.6zm6-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1c-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.7s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg><span>WhatsApp\'tan ulaşın</span></a>\n'
LD_STORE = '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Store", "name": "Kristal Diş Deposu – Leibinger Dental Türkiye", "url": "https://leibingerturkiye.com/", "telephone": "+90 534 086 77 00", "email": "serhatarg@hotmail.com", "address": {"@type": "PostalAddress", "streetAddress": "Cumhuriyet Mah. Tennuri Sok. No:13/C", "addressLocality": "Melikgazi", "addressRegion": "Kayseri", "addressCountry": "TR"}, "brand": {"@type": "Brand", "name": "Otto Leibinger"}, "contactPoint": {"@type": "ContactPoint", "telephone": "+90 534 086 77 00", "contactType": "sales", "availableLanguage": ["Turkish"]}}</script>'
EXTRA_CSS = '''
.katlist{display:grid;gap:12px;max-width:900px}
.kat{display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center;border:1.5px solid var(--green);border-radius:16px;padding:18px 20px;text-decoration:none;background:#fff;transition:transform .15s ease}
.kat:hover{transform:translateY(-2px)}
.kat-ic{font-family:var(--f-mono);font-size:.8rem;background:var(--green);color:#fff;border-radius:10px;padding:14px 10px}
.kat h3{font-size:1.2rem;font-weight:600;text-transform:uppercase}
.kat p{margin:2px 0 4px;color:var(--muted);font-size:.93rem}
.kat small{font-family:var(--f-mono);font-size:.76rem;color:var(--green-d)}
.kat-go{font-weight:600;color:var(--green-d)}

/* ---- iletişim ve WhatsApp ---- */
.contact{background:var(--green-soft);border-top:3px solid var(--green)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,64px);align-items:center}
.contact-grid > div:first-child{display:grid;gap:16px;justify-items:start}
.cinfo{margin:0;background:#fff;border:1.5px solid var(--green);border-radius:18px;padding:8px 24px}
.cinfo div{display:grid;grid-template-columns:110px 1fr;gap:12px;padding:14px 0;border-bottom:1px solid var(--green-soft)}
.cinfo div:last-child{border-bottom:0}
.cinfo dt{font-family:var(--f-mono);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--green-d);padding-top:3px}
.cinfo dd{margin:0;font-weight:500}
.cinfo a{color:var(--ink);text-decoration-color:var(--green)}
.btn-wa{background:#25d366;color:#fff;gap:10px}
.btn-wa:hover{background:#1ebe5b}
.wa-float{position:fixed;right:max(18px,env(safe-area-inset-right,0px));bottom:calc(18px + env(safe-area-inset-bottom,0px));z-index:50;display:inline-flex;align-items:center;gap:10px;background:#25d366;color:#fff;text-decoration:none;font-weight:600;padding:12px 18px 12px 14px;border-radius:999px;box-shadow:0 8px 24px rgba(0,0,0,.2)}
.wa-float:hover{background:#1ebe5b}
@media (max-width:600px){.wa-float span{display:none}.wa-float{padding:14px}}
@media (max-width:860px){.contact-grid{grid-template-columns:1fr}}

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

KATALOGLAR = [
 ('Ana katalog 2023','Otto Leibinger\'in tüm diş hekimliği el aletleri ürün gamı: teşhis, restoratif, endodonti, periodontoloji, cerrahi, çekim, implantoloji ve ortodonti.','2025/02/ol_gk_2023_dl.pdf','18 MB','Almanca / İngilizce'),
 ('Ortodonti broşürü','Tel bükme pensleri, distal uç kesiciler, ligatür pensleri ve aligner pensleri.','2025/01/2021-katalog_ol_kfo.pdf','4,3 MB','Almanca / İngilizce'),
 ('2025 yenilikleri','Leibinger\'in 2025 yılı öne çıkan ürünleri.','2025/02/OL_NEWSFLYER_2025_DL.pdf','2,5 MB','Almanca'),
 ('Rubberdam seti','Rubberdam klempleri, klemp pensi ve set içeriği.','2025/02/ol_newsflyer_rubberdam_online.pdf','0,4 MB','Almanca'),
 ('Tünel tekniği aletleri','Periodontal ve mukogingival tünel tekniği için aletler.','2025/02/tunneling-instruments.pdf','0,1 MB','İngilizce'),
 ('ErgoDesign titanyum küretler','ErgoDesign saplı titanyum küretler.','2025/02/titan-kueretten-flyer.pdf','0,1 MB','Almanca'),
 ('HI TECH alet bakım yağı','El aletlerinin menteşe ve eklem bakımı için yağ.','2025/02/hitech-oel.pdf','küçük','Almanca'),
]

def katalog_page():
    url = f'{SITE}/kataloglar/'
    title = 'Leibinger Katalog (PDF) | Otto Leibinger Dental Ürün Katalogları'
    desc = 'Otto Leibinger diş hekimliği el aletleri ana kataloğu, ortodonti broşürü ve ürün broşürleri (PDF). Türkiye resmî distribütörü Kristal Diş Deposu.'
    items = ''.join(f'''<a class="kat" href="{LB}{f}" target="_blank" rel="noopener"><span class="kat-ic">PDF</span><div><h3>{esc(t)}</h3><p>{esc(d)}</p><small>{esc(sz)} · {esc(lang)}</small></div><span class="kat-go">Aç</span></a>''' for t,d,f,sz,lang in KATALOGLAR)
    ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Leibinger Dental Türkiye","item":SITE+'/'},{"@type":"ListItem","position":2,"name":"Kataloglar","item":url}]}
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="{LB}2025/01/cropped-cropped-1978-3-2-1-2.png">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:locale" content="tr_TR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{LD_STORE}
</head>
<body>
{header()}
<main>
<section class="phero">
  <div class="wrap">
    <div class="txt" style="display:grid;gap:14px;justify-items:start;max-width:760px">
      <nav class="crumb" aria-label="Konum"><a href="/">Leibinger Türkiye</a> / <span>Kataloglar</span></nav>
      <span class="de"><span class="flag" aria-hidden="true"></span>Made in Germany · Alman menşeli</span>
      <h1>Leibinger <em>kataloglar</em></h1>
      <p class="lead">Otto Leibinger\'in güncel ürün kataloğu ve broşürleri. PDF\'ler Leibinger\'in kendi sitesinden açılır. Katalogda gördüğünüz bir modeli sormak için WhatsApp\'tan model numarasını yazmanız yeterli.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap"><div class="katlist">{items}</div>
  <p class="note2">Kataloglar Otto Leibinger GmbH tarafından hazırlanmıştır. Fiyat ve stok bilgisi için Kristal Diş Deposu\'na üye girişi yapın ya da bize ulaşın.</p></div>
</section>
</main>
{CONTACT_HTML}
{FOOTER}
</body>
</html>
'''

def main():
    base = open(os.path.join(B, 'base.css'), encoding='utf-8').read()
    open(os.path.join(ROOT, 'style.css'), 'w', encoding='utf-8').write(base + EXTRA_CSS)
    for pg in PAGES:
        d = os.path.join(ROOT, pg['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(pg))
    os.makedirs(os.path.join(ROOT,'kataloglar'), exist_ok=True)
    open(os.path.join(ROOT,'kataloglar','index.html'),'w',encoding='utf-8').write(katalog_page())
    urls = [SITE + '/'] + [f'{SITE}/{p["slug"]}/' for p in PAGES] + [SITE + '/kataloglar/']
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    for pg in PAGES:
        print(pg['slug'], len(by_cat(*pg['cats'])), 'ürün')

if __name__ == '__main__':
    main()
