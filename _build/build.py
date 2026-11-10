#!/usr/bin/env python3
"""leibingerturkiye.com kategori sayfalarını üretir.
Kullanım: python3 _build/build.py  (repo kökünden)
Ürün verisi: _build/products.json (Kristal Diş Deposu, Otto Leibinger markası)
"""
import json, html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.join(ROOT, '_build')
SITE = 'https://leibingerturkiye.com'
KD = 'https://www.kristaldisdeposu.com'
IMG = KD + '/idea/hy/90/myassets/products/'
LB = 'https://www.leibinger-dental.de/wp-content/uploads/'
BRAND = KD + '/marka/otto-leibinger'

from rehber import REHBER
P = json.load(open(os.path.join(B, 'products.json'), encoding='utf-8'))
esc = html.escape

def model(p):
    return p['sku'].replace('OT.', '') if p['sku'] else ''

def by_cat(*cats):
    return [p for p in P if any(c in p['cats'] for c in cats)]

# ---------------- sayfa içerikleri ----------------
PAGES = [
 dict(
  slug='davye', menu=True, nav='Davye',
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
  slug='kuret', menu=True, nav='Küret',
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
       ('SC (Supercut) makas nedir?','Supercut makasların kesici kenarları özel bir bileme ile çok keskin hale getirilir. Tek altın renkli halkasından ayırt edilir.'),
       ('Cerrahi makaslar otoklavlanabilir mi?','Evet, paslanmaz çelik ve SC makaslar standart otoklav sterilizasyonuna uygundur; menteşe bölgesi düzenli temizlenmeli ve yağlanmalıdır.')],
  related=('portegu','davye','el-aletleri'),
 ),
 dict(
  slug='el-aletleri', nav='El aletleri', menu=True,
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
 dict(
  slug='elevator', nav='Elevatör', menu=True,
  title='Elevatör ve Lüksatör Çeşitleri | Bein, Cryer, Heidbrink | Leibinger',
  desc='Alman menşeli Leibinger kök elevatörleri ve lüksatörler: Bein, Cryer, Heidbrink, Lindo-Levian, periost elevatörleri. Elevatör çeşitleri, ölçüleri ve kullanım alanları.',
  h1='Elevatör', h1em='ve lüksatör', eyebrow='Çekim · Kök elevatörleri · Lüksatörler',
  hero=LB + '2025/02/20210708_Leibinger_0053.jpg',
  lead='Leibinger kök elevatörleri ve lüksatörleri Almanya, Mühlheim\'da üretilir. Lüksatörlerle dişi kemiğe bağlayan periodontal lifler kesilip alveol genişletilir; böylece diş kemiğe zarar vermeden, daha nazik bir şekilde çıkarılabilir. Bu da implant öncesi çekimler için uygundur.',
  cats=('Kök Elavatörleri','Periost Elavatörleri','Periost Elevatörleri'), exclude=('OT.185/8MK',),
  guide_title='Elevatör tipleri ve kullanım alanları',
  guide_head=('Tip','Uç','Kullanım','Katalog no'),
  guide=[('Bein','Düz, oluklu uç · 2 · 3 · 4 mm','Kökleri gevşetmek ve kaldırmak için en yaygın düz elevatör','190/1 · 190/2 · 190/3'),
         ('Lüksatör','İnce, keskin uç · 2,5 – 5 mm · düz ve eğri','Periodontal lifleri kesip alveolü genişletme; atravmatik çekim','190/3ST … 190/5C'),
         ('Cryer','Üçgen uç · sağ ve sol','Alt molar kökleri, karşı kökü kaldırmak','190/13 · 190/14'),
         ('Heidbrink','İnce, açılı uç','Apikal kök parçaları','192/01 · 192/02 · 192/03'),
         ('Lindo-Levian','İnce kök elevatörü · 3,5 ve 4 mm','Dar alanlarda kök gevşetme','190/23 · 190/24'),
         ('Periost elevatörü (Molt 9, Prichard)','Geniş ve yuvarlak uç','Flep kaldırma, periostu kemikten ayırma','335/M9 · 335/PR3S')],
  guide_note='Tipler ve katalog numaraları Leibinger ana kataloğundan alınmıştır. Lüksatörlerin ErgoDesign saplı (-ED) ve renk kodlu (F) versiyonları da vardır.',
  faq=[('Elevatör ile lüksatör arasındaki fark nedir?','Elevatör kökü kaldırmak ve gevşetmek için kaldıraç gibi kullanılır. Lüksatörün ucu daha ince ve keskindir; kök ile kemik arasına girerek periodontal lifleri keser, kaldıraç olarak kullanılması önerilmez.'),
       ('Hangi ölçü elevatörle başlamalıyım?','Temel sette genellikle 2, 3 ve 4 mm Bein elevatörler bulunur. Dar kökler için ince, geniş kökler için kalın uçlu model seçilir. Leibinger Bein elevatörleri 3 parça set olarak da bulunur.'),
       ('Cryer elevatör neden sağ ve sol olarak satılır?','Cryer elevatörün üçgen ucu belirli bir yöne bakar. Alt çenede iki taraf için ayrı model gerektiği için sağ ve sol olarak ya da çift set halinde kullanılır.'),
       ('Lüksatör ucu nasıl korunur?','İnce uç darbeye ve kaldıraç kuvvetine hassastır. Kaldıraç olarak kullanılmamalı, sterilizasyonda diğer aletlerle çarpışmaması için kasette saklanmalıdır.')],
  related=('davye','cerrahi-makas','ekartor'),
 ),
 dict(
  slug='ortodonti-pensi', nav='Ortodonti', menu=True,
  title='Ortodonti Pensleri | Distal Uç Kesici, Tel Bükme, Aligner | Leibinger',
  desc='Alman menşeli Leibinger ortodonti pensleri: distal uç kesici, ligatür kesici, tel bükme pensleri, aligner pensleri. TC (tungsten karbid) uçlu kesiciler.',
  h1='Ortodonti', h1em='pensleri', eyebrow='Ortodonti · Tel kesme ve bükme · Aligner',
  hero=LB + '2025/02/20210708_Leibinger_0058.jpg',
  lead='Leibinger ortodonti pensleri tel bükme, tel ve ligatür kesme ile aligner (şeffaf plak) işlemleri için Almanya\'da üretilir. Kesicilerin TC versiyonlarında kesici kenarlarda tungsten karbid kullanılır.',
  cats=('Ortodonti',), skupre=('OT.63',),
  guide_title='Hangi pens ne için?',
  guide_head=('Pens','Kullanım','Kristal\'deki model'),
  guide=[('Distal uç kesici (Distal End Cutter)','Ark telinin distal ucunu ağız içinde keser ve kesilen ucu tutar','632/16TC · 632/19TC (mini)'),
         ('Ligatür kesici','Ligatür tellerini keser','632/3TC'),
         ('Flush cutter','Teli yüzeye yakın keser','632/24TC'),
         ('Tel kesme pensi','Kalın tel kesimi','632/15TC · 632/6 · 632/6TC'),
         ('Tel bükme pensleri','Yuvarlak ve açılı uçlarla tel bükme','630/11 · 630/4'),
         ('Aligner pensleri','Şeffaf plağa damla, dikey ve yatay çentik açma','630/84 · 630/82 · 630/81')],
  guide_note='Model numaraları Kristal Diş Deposu\'ndaki Leibinger ürünlerinden alınmıştır. Leibinger\'in ortodonti broşürünü Kataloglar sayfasında bulabilirsiniz.',
  faq=[('TC uçlu kesici ne demek?','TC (tungsten karbid) kesici kenarlar paslanmaz çelikten daha serttir. Bu yüzden sert ortodontik telleri keserken keskinliklerini daha uzun süre korurlar.'),
       ('Distal uç kesicide "safety hold" ne işe yarar?','Kesilen tel parçasını pensin ağzında tutar, böylece parça ağız içine düşmez.'),
       ('Aligner pensleri ne için kullanılır?','Şeffaf plaklara (aligner) kuvvet uygulamak ya da tutuculuk için damla, dikey veya yatay çentik açmakta kullanılır.')],
  related=('el-aletleri','kataloglar-link','davye'),
 ),
 dict(
  slug='rubberdam', nav='Rubberdam',
  title='Rubberdam Klempleri ve Rubberdam Seti | Klemp Numaraları | Leibinger',
  desc='Alman menşeli Leibinger rubberdam klempleri ve rubberdam seti. Klemp numaraları hangi diş için kullanılır? #00, #1, #2, #2A, #3, #7, #8, #8A, #9, #12A, #13A, #14A, #212.',
  h1='Rubberdam', h1em='klempleri', eyebrow='Endodonti · Restoratif · İzolasyon',
  hero=LB + '2025/02/20250203-Leibinger-044.jpg',
  lead='Leibinger rubberdam klempleri paslanmaz çelikten üretilir ve her numara belirli bir diş grubuna göre şekillendirilmiştir. Rubberdam seti; çocuk ve yetişkin çerçevesi, delme pensi, klemp pensi, 8 klemp ve klemp tutucusuyla gelir.',
  cats=('Rubberdam',),
  guide_title='Rubberdam klemp numaraları',
  guide_head=('Klemp','Diş grubu (Leibinger kataloğu)','Katalog no'),
  guide=[('#00','Alt kaninler ve premolarlar','316/RDC00'),('#1','Üst premolarlar','316/RDC1'),('#2 · #2A','Üst ve alt premolarlar','316/RDC2 · 316/RDC2A'),
         ('#3','Alt molarlar','316/RDC3'),('#7','Alt molarlar','316/RDC7'),('#8','Üst molarlar, büyük klemp','316/RDC8'),
         ('#8A','Üst ve alt molar kökleri','316/RDC8A'),('#9','Ön dişler','316/RDC9'),('#12A','Alt molarlar, sağ ve sol','316/RDC12A'),
         ('#13A','Alt molarlar, sol','316/RDC13A'),('#14A','Büyük molarlar','316/RDC14A'),('#212','Ön dişlerde labial kaviteler','316/RDC212')],
  guide_note='Açıklamalar Leibinger ana kataloğundan çevrilmiştir. Klemplerin siyah (-B) versiyonları da vardır. Rubberdam seti (316/SET) şu klempleri içerir: 00, 2, 2A, 7, 8, 8A, 9, 14A.',
  faq=[('Rubberdam setinde neler var?','Leibinger rubberdam setinde 1 çocuk çerçevesi, 1 yetişkin çerçevesi, 1 rubberdam delme pensi, 1 klemp pensi, 8 klemp (00, 2, 2A, 7, 8, 8A, 9, 14A) ve 1 klemp tutucusu bulunur.'),
       ('Kanatlı ve kanatsız klemp farkı nedir?','Kanatlı klemp rubberdam örtüsüyle birlikte tek seferde yerleştirilebilir. Kanatsız klempte önce klemp takılır, örtü sonra geçirilir. Klempin adındaki ve görselindeki forma bakarak seçebilirsiniz.'),
       ('Hangi klemplerle başlamalıyım?','Çoğu klinikte premolar için #2 veya #2A, molar için #7 veya #8, ön dişler için #9 ve #212 sık kullanılır. Rubberdam seti bu temel numaraları içerir.')],
  related=('ayna','el-aletleri','kataloglar-link'),
 ),
 dict(
  slug='ayna', nav='Ayna',
  title='Rodyum Mikro Ayna ve Dişçi Aynası Sapı | Leibinger',
  desc='Alman menşeli Leibinger rodyum mikro aynalar (Ø 3 mm, Ø 5 mm, 3×6 mm) ve ölçekli ayna sapı. Mikrocerrahi, endodonti ve implantoloji için ön yüzey (FS) aynalar.',
  h1='Rodyum', h1em='mikro ayna', eyebrow='Teşhis · Mikrocerrahi · Endodonti',
  hero=LB + '2024/12/20210708_Leibinger_0074.jpg',
  lead='Leibinger mikro aynaları yalnızca 0,6 mm kalınlığındadır ve mikrocerrahi için tasarlanmıştır. Ön yüzey (FS) rodyum kaplama, çift görüntü oluşturmayan net ve kontrastlı bir görüntü verir; yapışmayı azaltan yüzeyi kolay temizlenir.',
  cats=('Aynalar',),
  guide_title='Mikro ayna boyutları',
  guide_head=('Ayna','Kullanım (Leibinger kataloğu)','Katalog no'),
  guide=[('Ø 3 mm','Kanal ağızlarını bulma, apikal rezeksiyon','201/10'),('Ø 5 mm','Hazırlanmış kanalları, fissürleri ve inley kavitelerini kontrol etme','201/20'),
         ('3 × 6 mm','Doğrudan görülemeyen çürükleri bulma (ör. mine altında)','201/30'),('Ölçekli ayna sapı','Mikro aynalarla birlikte, ölçekli','200/51M')],
  guide_note='Kullanım alanları Leibinger ana kataloğundaki mikro ayna açıklamasından çevrilmiştir. Aynalar 12\'li kutu halinde de bulunur.',
  faq=[('Ön yüzey (FS) ayna nedir?','Yansıtıcı katmanın camın arkasında değil ön yüzeyinde olduğu aynadır. Çift görüntü oluşturmaz, daha net ve kontrastlı bir görüntü verir.'),
       ('Rodyum kaplamanın avantajı nedir?','Rodyum kaplama parlak ve doğru renkli bir görüntü sağlar. Leibinger\'in FS rodyum aynalarında yapışmayı azaltan bir yüzey de vardır, bu yüzden kolay temizlenir.'),
       ('Mikro ayna standart ayna sapına takılır mı?','Leibinger mikro aynaları ölçekli ayna sapıyla birlikte set olarak ya da yalnızca ayna olarak bulunur. Sap uyumluluğu için ürün sayfasındaki bilgiye bakın ya da bize WhatsApp\'tan yazın.')],
  related=('el-aletleri','rubberdam','kuret'),
 ),
 dict(
  slug='ekartor', nav='Ekartör',
  title='Cerrahi Ekartör Çeşitleri | Farabeuf, Langenbeck, Molt | Leibinger',
  desc='Alman menşeli Leibinger cerrahi ekartörler: Farabeuf, Kocher-Langenbeck, Wieder dil ekartörü, Molt ağız açacağı. Ölçüler ve kullanım alanları.',
  h1='Cerrahi', h1em='ekartörler', eyebrow='Cerrahi · Yara ve ağız ekartörleri',
  hero=LB + '2025/02/20250203-Leibinger-082.jpg',
  lead='Leibinger ekartörleri ağız içi cerrahide yanak, dudak, dil ve flebi uzaklaştırarak görüş alanı ve erişim sağlamak için Almanya\'da üretilir.',
  cats=('Ekartörler',),
  guide_title='Ekartör tipleri',
  guide_head=('Model','Ölçü','Kullanım','Katalog no'),
  guide=[('Farabeuf','125 · 150 mm (2\'li set)','Yanak, dudak ve flep ekartasyonu','353/8 · 353/9'),
         ('Kocher-Langenbeck','30×11 – 50×11 mm ağız · 22 cm','Derin cerrahi alanlarda flep ekartasyonu','355/11 – 355/15'),
         ('Wieder dil ekartörü','140 · 145 mm','Dili uzaklaştırma ve koruma','354/W1 · 354/W2'),
         ('Molt ağız açacağı','12 · 14 cm','Ağzı açık tutma','700/7 · 700/8')],
  guide_note='Ölçüler ve katalog numaraları Leibinger ana kataloğundan alınmıştır. Katalogda Minnesota, Obwegeser, Roux ve Middeldorpf ekartörleri de vardır; sormak için WhatsApp\'tan yazabilirsiniz.',
  faq=[('Farabeuf ekartör neden çift satılır?','Farabeuf ekartörün iki ucu farklı boyuttadır ve genellikle iki farklı uzunlukta set olarak kullanılır. Leibinger\'de 125 mm ve 150 mm\'lik iki parça set halinde bulunur.'),
       ('Langenbeck ekartörün ölçüsü nasıl seçilir?','Ağız genişliği ve derinliği cerrahi alana göre seçilir. Dar ve derin alanlar için 11 mm genişlikte uzun ağızlı modeller, daha geniş flepler için 14 – 16 mm modeller uygundur.'),
       ('Ekartörler otoklavlanabilir mi?','Evet, paslanmaz çelik ekartörler standart otoklav sterilizasyonuna uygundur. Üreticinin bakım talimatlarına uyulmalıdır.')],
  related=('elevator','cerrahi-makas','portegu'),
 ),
 dict(
  slug='implant-temizleme', nav='İmplant temizleme',
  title='Titanyum İmplant Küretleri ve Scaler\'lar | Leibinger',
  desc='Alman menşeli Leibinger titanyum küretler ve scaler\'lar: Langer 1-2, 3-4, 5-6, H6-H7, 204SD, Columbia 2RL ve 4RL. İmplant temizleme seti içeriği.',
  h1='Titanyum', h1em='implant küretleri', eyebrow='İmplantoloji · Periimplant bakım',
  hero=LB + '2025/02/20250203-Leibinger-018.jpg',
  lead='Leibinger titanyum küret ve scaler\'ları implant yüzeylerinin temizliği için üretilir. Titanyum uçlar, paslanmaz çelik aletlere göre titanyum implant yüzeyinde iz bırakma riskini azaltmak için tercih edilir.',
  cats=('İmpant Temizleme',),
  guide_title='İmplant temizleme seti içeriği',
  guide_head=('Model','Kullanım (Leibinger kataloğu)','Katalog no'),
  guide=[('Langer 1-2','Alt çene molar ve premolar','401/L1-2T-ED'),('Langer 3-4','Üst çene molar ve premolar','401/L3-4T-ED'),
         ('Langer 5-6','Ön dişler','401/L5-6T-ED'),('H6-H7','Üniversal scaler','401/H6-H7T-ED'),('204SD','Üniversal scaler','401/204SD-T-ED'),
         ('Easy Tray','5 alet için kaset, 180 × 70 × 30 mm','500/5')],
  guide_note='Set içeriği Leibinger ana kataloğundaki "Implant Cleaning Set" sayfasından alınmıştır. Tüm titanyum küretler ErgoDesign (-ED) saplıdır. Columbia 2RL ve 4RL titanyum küretler ayrıca bulunur.',
  faq=[('İmplant temizliğinde neden titanyum küret kullanılır?','Titanyum implant yüzeyi, daha sert paslanmaz çelik uçlarla çalışıldığında çizilebilir. Titanyum uçlu küret ve scaler\'lar bu riski azaltmak için tercih edilir.'),
       ('Langer küret ile Gracey küret arasındaki fark nedir?','Langer küretler Gracey\'nin açılı şaftını üniversal küretin iki kesici kenarıyla birleştirir. Böylece bir alet, belirli bir bölgede hem mezial hem distal yüzeyde kullanılabilir.'),
       ('İmplant temizleme seti tek tek alınabilir mi?','Evet. Set içindeki küret ve scaler\'lar Kristal Diş Deposu\'nda tek tek de bulunur.')],
  related=('kuret','alet-kaseti','el-aletleri'),
 ),
 dict(
  slug='kemik-pensi', nav='Kemik pensi',
  title='Kemik Pensi (Rongeur), Kemik Eğesi ve Diş Eti Bıçağı | Leibinger',
  desc='Alman menşeli Leibinger kemik pensleri (Friedmann, Mini Friedmann, Hartmann), Sugarman ve Miller kemik eğeleri, Kirkland ve Orban diş eti bıçakları.',
  h1='Kemik pensi', h1em='ve eğesi', eyebrow='Cerrahi · Periodontal cerrahi',
  hero=LB + '2025/02/20250203-Leibinger-059.jpg',
  lead='Kemik pensleri keskin kenarlı kemik çıkıntılarını düzeltmek ve kemik almak için; kemik eğeleri kemik yüzeyini düzeltmek için; diş eti bıçakları ise gingivektomi ve gingivoplasti için kullanılır. Leibinger bu aletleri Almanya, Mühlheim\'da üretir.',
  cats=('Kemik Pensleri','Kemik Eğesi ve Diş Eti Bıçağı'),
  guide_title='Modeller ve kullanım',
  guide_head=('Model','Tip','Ölçü / Not','Katalog no'),
  guide=[('Mini Friedmann','Kemik pensi','12 cm','136/01'),('Friedmann','Kemik pensi','14 cm','136/0'),('Hartmann','Kemik pensi','18 cm','136/4'),
         ('Sugarman','Kemik eğesi','1S-2S · 3S-4S · 9-10S','401/FS12 · FS34 · FS910'),('Miller','Kemik eğesi','—','338/3'),
         ('Kirkland','Diş eti bıçağı','Gingivektomi','401/K1'),('Orban','Diş eti bıçağı','İnterdental bölge','401/KO12')],
  guide_note='Ölçüler Leibinger ana kataloğundan ve Kristal Diş Deposu\'ndaki ürün adlarından alınmıştır. Katalogda Blumenthal ve Luer kemik pensleri de bulunur.',
  faq=[('Friedmann ile Mini Friedmann arasındaki fark nedir?','İkisi de aynı formda kemik pensidir. Mini Friedmann 12 cm, Friedmann 14 cm uzunluğundadır; dar alanlarda daha kısa model tercih edilir.'),
       ('Kirkland ve Orban bıçakları ne için kullanılır?','Kirkland bıçağı gingivektomide labial ve lingual yüzeylerde, Orban bıçağı ise interdental bölgelerde diş eti kesimi için kullanılır.')],
  related=('elevator','cerrahi-makas','ekartor'),
 ),
 dict(
  slug='penset', nav='Penset',
  title='Cerrahi Penset ve Presel Çeşitleri | Adson, London College | Leibinger',
  desc='Alman menşeli Leibinger Adson cerrahi doku pensleri, Adson mikro pensler ve London College preseller (elmas uçlu dahil).',
  h1='Penset', h1em='ve presel', eyebrow='Cerrahi · Doku tutma · Muayene',
  hero=LB + '2025/02/20210708_Leibinger_0058.jpg',
  lead='Leibinger Adson pensleri cerrahide doku tutmak ve dikiş sırasında flebi sabitlemek için; London College preseller ise muayene ve restoratif işlemlerde küçük malzemeleri taşımak için kullanılır.',
  cats=('Pensetler',), extra_sku=('OT.180/5',),
  guide_title='Modeller',
  guide_head=('Model','Uç','Uzunluk','Katalog no'),
  guide=[('Adson cerrahi doku pensi','Dişli','12 · 15 cm','183/61 · 183/62'),('Adson mikro cerrahi doku pensi','Dişli, ince','12 cm','183/63'),
         ('Adson mikro pens','İnce','12 cm','182/62 · 182/63'),('London College presel','Düz uç · elmas kaplı uç','15 cm','180/5 · 180/5D')],
  guide_note='Uzunluklar Kristal Diş Deposu\'ndaki Leibinger ürün adlarından alınmıştır.',
  faq=[('Elmas uçlu presel ne işe yarar?','Uçlardaki elmas kaplama tutuşu artırır; küçük ve kaygan parçalar daha güvenli tutulur.'),
       ('Dişli doku pensi neden tercih edilir?','Uçtaki küçük dişler dokuyu kaydırmadan tutar ve daha az kuvvetle sabitleme sağlar.')],
  related=('portegu','cerrahi-makas','el-aletleri'),
 ),
 dict(
  slug='alet-kaseti', nav='Alet kaseti',
  title='Otoklavlanabilir Alet Kaseti | Easy Tray, Wash Tray | Leibinger',
  desc='Leibinger otoklavlanabilir alet kasetleri: Easy Tray ve Wash Tray (5\'li ve 10\'lu). Ölçüler ve kaset kullanmanın avantajları.',
  h1='Alet', h1em='kasetleri', eyebrow='Saklama · Sterilizasyon',
  hero=LB + '2025/03/20210708_Leibinger_0008.jpg',
  lead='Leibinger alet kasetleri el aletlerini tedaviye göre düzenli tutmak, birlikte yıkamak ve otoklavlamak için tasarlanmıştır. Aletler kasette sabit durduğu için birbirine çarpmaz ve keskin uçlar daha güvenli taşınır.',
  cats=('Alet Kasetleri',),
  guide_title='Kaset ölçüleri',
  guide_head=('Model','Kapasite','Ölçü','Katalog no'),
  guide=[('Easy Tray','5 alet','180 × 70 × 30 mm','500/5'),('Easy Tray','10 alet','—','500/6'),
         ('Ergo-Clip Wash Tray','5 alet','184 × 110 × 25 mm','500/TK'),('Ergo-Clip Wash Tray','10 alet','184 × 150 × 25 mm','500/T')],
  guide_note='Ölçüler Leibinger ana kataloğundan alınmıştır. Katalogda 20 aletlik Ergo Cassette modelleri de bulunur.',
  faq=[('Alet kaseti kullanmanın avantajı nedir?','Leibinger kataloğuna göre: aletler tedavi türüne göre set halinde düzenlenir ve arama zamanı azalır; aletler güvenle saklanır; kasette sabitlendikleri için keskin uçlarla yaralanma riski azalır.'),
       ('Kasetler otoklava girer mi?','Evet, Easy Tray ve Wash Tray otoklavlanabilir kasetlerdir.')],
  related=('implant-temizleme','kuret','el-aletleri'),
 ),
]
PG = {p['slug']: p for p in PAGES}
MENU = ('davye','elevator','kuret','ortodonti-pensi','el-aletleri')

# ---------------- şablon ----------------
def header():
    links = ''.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in (PG[x] for x in MENU)) + '<a href="/kataloglar/">Kataloglar</a><a href="/rehber/">Rehber</a>'
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
      <div class="note">Kategoriler: {' · '.join(f'<a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES)} · <a href="/kataloglar/">Kataloglar</a> · <a href="/rehber/">Rehber</a> · <a href="/neden-leibinger/">Neden Leibinger?</a></div>
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
    if pg.get('extra_sku'):
        prods += [p for p in P if p['sku'] in pg['extra_sku'] and p not in prods]
    if pg.get('exclude'):
        prods = [p for p in prods if p['sku'] not in pg['exclude']]
    if pg.get('skupre'):
        prods = [p for p in prods if p['sku'].startswith(pg['skupre'])]
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
        cards = ''.join(f'<a class="hubc" href="/{PG[s]["slug"]}/"><img src="{PG[s]["hero"]}" alt="" loading="lazy"><span>{PG[s]["nav"]}</span></a>' for s in ('davye','elevator','kuret','implant-temizleme','portegu','cerrahi-makas','kemik-pensi','ekartor','penset','rubberdam','ayna','ortodonti-pensi','alet-kaseti'))
        hub = f'<section style="padding-bottom:0"><div class="wrap"><span class="eyebrow">Kategoriler</span><h2 style="margin-top:12px">Gruba göre <em>incele</em></h2><div class="hub">{cards}</div></div></section>'
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in pg['faq'])
    rel = ''.join(('<a class="btn btn-ghost" href="/kataloglar/">Kataloglar</a>' if s == 'kataloglar-link' else f'<a class="btn btn-ghost" href="/{s}/">{PG[s]["nav"]}</a>') for s in pg['related'])
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
.art{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:clamp(24px,5vw,64px);align-items:start}
.art article{max-width:720px}
.art article h2{font-size:clamp(1.3rem,2.4vw,1.7rem);margin:28px 0 10px}
.art article p{font-size:1.06rem;line-height:1.7;margin:0 0 12px}
.art .rel{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.art aside{position:sticky;top:96px;border:1.5px solid var(--green);border-radius:16px;padding:18px 20px;background:#fff}
.art aside h3{margin:0 0 10px;font-size:1rem}
.art aside ul{margin:0;padding-left:18px;display:grid;gap:8px}
@media (max-width:860px){.art{grid-template-columns:1fr}.art aside{position:static}}

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

def _head(title, desc, url, og_img=None, ld=()):
    ld_s = '\n'.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    ogi = f'<meta property="og:image" content="{og_img}">' if og_img else ''
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" href="{LB}2025/01/cropped-cropped-1978-3-2-1-2.png">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta property="og:locale" content="tr_TR">{ogi}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hind:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="/style.css">
{ld_s}
{LD_STORE}
</head>
<body>
{header()}'''

def rehber_page(a):
    url = f'{SITE}/rehber/{a["slug"]}/'
    img = LB + a['hero']
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Leibinger Dental Türkiye","item":SITE+'/'},
            {"@type":"ListItem","position":2,"name":"Rehber","item":SITE+'/rehber/'},
            {"@type":"ListItem","position":3,"name":a['title'],"item":url}]},
          {"@context":"https://schema.org","@type":"Article","headline":a['title'],"description":a['desc'],"image":img,
           "inLanguage":"tr","mainEntityOfPage":url,"author":{"@type":"Organization","name":"Kristal Diş Deposu"},
           "publisher":{"@type":"Organization","name":"Kristal Diş Deposu"}}]
    body = ''.join(f'<h2>{esc(h)}</h2><p>{esc(t)}</p>' for h, t in a['body'])
    links = ''.join(f'<a class="btn btn-ghost" href="{u}">{esc(t)}</a>' for u, t in a['links'])
    others = ''.join(f'<li><a href="/rehber/{b["slug"]}/">{esc(b["title"])}</a></li>' for b in REHBER if b is not a)
    return _head(a['title'], a['desc'], url, img, ld) + f'''
<main>
<section class="phero">
  <div class="wrap phero-grid">
    <div class="txt">
      <nav class="crumb" aria-label="Konum"><a href="/">Leibinger Türkiye</a> / <a href="/rehber/">Rehber</a></nav>
      <span class="eyebrow">Rehber</span>
      <h1>{esc(a["h1"])} <em>{esc(a["h1em"])}</em></h1>
      <p class="lead">{esc(a["lead"])}</p>
    </div>
    <img class="phero-img" src="{img}" alt="">
  </div>
</section>
<section>
  <div class="wrap art">
    <article>{body}
      <p class="note2">Bu yazı genel bilgilendirme amaçlıdır. Klinik kararlar hekimin değerlendirmesine, bakım ve sterilizasyon üretici talimatlarına göre verilmelidir.</p>
      <div class="rel">{links}</div>
    </article>
    <aside><h3>Diğer rehberler</h3><ul>{others}</ul></aside>
  </div>
</section>
</main>
{CONTACT_HTML}
{FOOTER}
</body>
</html>
'''

def rehber_index():
    url = f'{SITE}/rehber/'
    title = 'Diş Hekimliği El Aletleri Rehberi | Leibinger Dental Türkiye'
    desc = 'Davye seçimi, Gracey küret numaraları, el aletleri bakımı ve sterilizasyonu hakkında pratik rehberler.'
    cards = ''.join(f'<a class="hubc" href="/rehber/{a["slug"]}/"><img src="{LB}{a["hero"]}" alt="" loading="lazy"><span>{esc(a["title"])}</span></a>' for a in REHBER)
    return _head(title, desc, url) + f'''
<main>
<section class="phero"><div class="wrap"><div class="txt" style="display:grid;gap:14px;justify-items:start;max-width:760px">
  <nav class="crumb" aria-label="Konum"><a href="/">Leibinger Türkiye</a> / <span>Rehber</span></nav>
  <h1>El aletleri <em>rehberi</em></h1>
  <p class="lead">Doğru aleti seçmek ve uzun süre kullanmak için kısa, pratik yazılar.</p>
</div></div></section>
<section><div class="wrap"><div class="hub">{cards}</div></div></section>
</main>
{CONTACT_HTML}
{FOOTER}
</body>
</html>
'''

def about_page():
    url = f'{SITE}/neden-leibinger/'
    title = 'Neden Leibinger? Alman Menşeli Diş Hekimliği El Aletleri'
    desc = 'Otto Leibinger 1978\'den beri Almanya, Mühlheim\'da (Tuttlingen bölgesi) diş hekimliği el aletleri üretiyor. Üretim yeri, ürün gamı ve Leibinger teknolojileri.'
    img = LB + '2024/12/20210708_Leibinger_0086.jpg'
    ld = [{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Leibinger Dental Türkiye","item":SITE+'/'},
            {"@type":"ListItem","position":2,"name":"Neden Leibinger?","item":url}]}]
    body = [
     ('1978\'den beri aile şirketi', 'Otto Leibinger GmbH 1978\'de kuruldu. Şirkete adını veren kurucusu, alet üretiminde uzun bir geleneği olan bir aileden geliyor. Leibinger bugün de aile şirketi olarak yönetiliyor.'),
     ('Tıbbi teknolojinin merkezinde üretim', 'Leibinger\'in üretim yeri Mühlheim an der Donau, Almanya\'nın Tuttlingen bölgesinde. Leibinger, cerrahi ve tıbbi alet üretiminin dünya merkezi olarak bilinen bu bölgeyi yüksek kaliteli diş hekimliği el aletleri üretmek için en iyi koşullar olarak tanımlıyor. Aletler Alman menşelidir.'),
     ('Teşhisten ortodontiye geniş ürün gamı', 'Leibinger kataloğu teşhis, restoratif tedavi, endodonti, periodontoloji, çekim, dental cerrahi, dental elektrotlar, ölçü kaşıkları, implantoloji, saklama ve sterilizasyon, protetik ve ortodonti gruplarını kapsar.'),
     ('Leibinger teknolojileri', 'ColorIdent renk halkalarıyla aletleri numarasına bakmadan tanıma; ErgoDesign geniş ve hafif saplarla ergonomi; Deep Scale Gracey küretlerde derin cepler için daha uzun şaft ve daha kısa uç; titanyum küretlerle implant yüzeyleri için ayrı bir seri; FS rodyum mikro aynalarla mikrocerrahide net görüntü.'),
     ('Türkiye\'de Leibinger', 'Kristal Diş Deposu, Otto Leibinger\'in Türkiye distribütörüdür. Leibinger ürünleri kristaldisdeposu.com üzerinden diş hekimlerine satılır; fiyatlar üye girişinden sonra görünür. Model seçimi ve set içerikleri için WhatsApp\'tan yazabilirsiniz.'),
    ]
    b = ''.join(f'<h2>{esc(h)}</h2><p>{esc(t)}</p>' for h, t in body)
    cats = ''.join(f'<li><a href="/{p["slug"]}/">{esc(p["nav"])}</a></li>' for p in PAGES)
    return _head(title, desc, url, img, ld) + f'''
<main>
<section class="phero">
  <div class="wrap phero-grid">
    <div class="txt">
      <nav class="crumb" aria-label="Konum"><a href="/">Leibinger Türkiye</a> / <span>Neden Leibinger?</span></nav>
      <span class="de"><span class="flag" aria-hidden="true"></span>Made in Germany · Alman menşeli</span>
      <h1>Neden <em>Leibinger?</em></h1>
      <p class="lead">1978\'den beri Almanya\'da, tıbbi alet üretiminin merkezinde üretilen diş hekimliği el aletleri.</p>
    </div>
    <img class="phero-img" src="{img}" alt="Leibinger üretimi">
  </div>
</section>
<section>
  <div class="wrap art">
    <article>{b}
      <p class="note2">Kaynak: Otto Leibinger GmbH ana kataloğu ve leibinger-dental.de.</p>
    </article>
    <aside><h3>Kategoriler</h3><ul>{cats}</ul></aside>
  </div>
</section>
</main>
{CONTACT_HTML}
{FOOTER}
</body>
</html>
'''

def notfound_page():
    return _head('Sayfa bulunamadı | Leibinger Dental Türkiye', 'Aradığınız sayfa bulunamadı.', SITE + '/404.html') + f'''
<main>
<section class="phero"><div class="wrap"><div class="txt" style="display:grid;gap:14px;justify-items:start;max-width:760px">
  <h1>Sayfa <em>bulunamadı</em></h1>
  <p class="lead">Aradığınız sayfa taşınmış ya da hiç olmamış olabilir. Aşağıdaki kategorilerden devam edebilirsiniz.</p>
  <div class="cta">{''.join(f'<a class="btn btn-ghost" href="/{p["slug"]}/">{esc(p["nav"])}</a>' for p in PAGES)}</div>
</div></div></section>
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
    os.makedirs(os.path.join(ROOT,'neden-leibinger'), exist_ok=True)
    open(os.path.join(ROOT,'neden-leibinger','index.html'),'w',encoding='utf-8').write(about_page())
    open(os.path.join(ROOT,'404.html'),'w',encoding='utf-8').write(notfound_page())
    os.makedirs(os.path.join(ROOT,'rehber'), exist_ok=True)
    open(os.path.join(ROOT,'rehber','index.html'),'w',encoding='utf-8').write(rehber_index())
    for a in REHBER:
        d = os.path.join(ROOT,'rehber',a['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(rehber_page(a))
    urls = [SITE + '/'] + [f'{SITE}/{p["slug"]}/' for p in PAGES] + [SITE + '/kataloglar/', SITE + '/neden-leibinger/', SITE + '/rehber/'] + [f'{SITE}/rehber/{a["slug"]}/' for a in REHBER]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>\n'
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
    for pg in PAGES:
        print(pg['slug'], 'ok')

if __name__ == '__main__':
    main()
