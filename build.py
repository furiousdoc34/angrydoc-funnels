import html
BOOK="https://askangrydoc.com/"
def fv(n):
    return f"{n/1000:.1f}K".replace(".0K","K") if n>=1000 else str(n)
I={ # inline icons
'check':'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
'x':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#9aa3ad" stroke-width="2.2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
'spark':'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/></svg>',
'video':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="14" height="12" rx="2"/><path d="m16 10 6-3v10l-6-3"/></svg>',
'clock':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
'shield':'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/></svg>',
'brain':'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/></svg>',
'move':'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="13" cy="4" r="2"/><path d="m7 21 3-6 3 2v4M10 15l1-5 4 3 3-1M8 10l3-1"/></svg>',
'target':'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
'play':'<svg width="26" height="26" viewBox="0 0 24 24" fill="#0d1b2a"><path d="M8 5v14l11-7z"/></svg>',
}
P=[
dict(slug="sciatica",name="Sciatica",tl="Sciatica",
 hook="Sakit mula balakang <em>hanggang binti</em>? Hindi ka nag-iisa — at may paraan.",
 sub="Yung kirot na gumagapang pababa, yung manhid sa paa, yung hirap umupo nang matagal. Alamin kung ano talaga ang nangyayari, at ano ang tamang susunod na hakbang.",
 vids=[("g_50BRqdK3Q","Sciatica Consult: Bakit sumasakit ang likod at binti?",15000),("wC5FR30LyGY","Back pain/sciatica",233),("ytBWX85JMfM","Sciatica: Bakit Natutulog ang Muscle?",90)],
 sym=["Sakit o kirot mula puwit pababa sa likod ng hita o binti","Parang kuryente o hapdi kapag yumuyuko o umuubo","Manhid o tusok-tusok sa binti o paa","Hirap umupo nang matagal — kailangan laging tumayo","Mas masakit sa isang side lang","Paulit-ulit na bumabalik kahit ilang beses nang na-masahe"],
 why="Ang sciatica ay hindi diagnosis — sintomas ito. Madalas, ang sciatic nerve (o ang mga ugat nito sa lower back) ay naiirita dahil sa disc bulge, paninikip ng daanan ng nerve, o muscle na nag-proprotect. Ang magandang balita: karamihan ng kaso ay gumagaling sa tamang edukasyon at unti-unting paggalaw, hindi sa pagpapahinga lang.",
 faq=[("Kailangan ko ba ng MRI bago mag-consult?","Hindi kailangan. Kung meron ka nang X-ray o MRI, dalhin mo — titingnan natin. Kung wala, sasabihin namin kung kailangan talaga."),("Kailangan ba ng operasyon?","Karamihan ng sciatica ay hindi nangangailangan ng operasyon. Pag-uusapan natin kung kailan dapat mag-refer sa surgeon.")]),
dict(slug="pinched-nerve",name="Pinched Nerve",tl="Pinched Nerve / Disc Bulge",
 hook="\u201cNaipit daw ang ugat ko.\u201d <em>Ano ba talaga 'yan?</em>",
 sub="Ngalay sa leeg pababa sa braso, o sa likod pababa sa binti. Disc bulge, herniation, \u201cnaipit na nerve\u201d — linawin natin ang mga salitang 'yan at gawan ng plano.",
 vids=[("eyldzX2XCic","Pinched nerve?",13000),("8CAsn4Y9EIM","Angriest Podcast - Ep 2 (Clinic Experiences) Pinched nerves & Bell's Palsy and meeting famous folks.",1600),("mRxUTbSHUFU","Dr Ron talks about X-ray and nerve ipit -Doc Ron Ang Malakas",531)],
 sym=["Ngalay o kirot mula leeg pababa sa balikat at braso","Manhid o tusok-tusok sa kamay o daliri","Sakit sa likod na gumagapang pababa sa binti","Lumalala kapag nakayuko sa cellphone o laptop","Sinabihan ka na may disc bulge o herniation sa X-ray/MRI","Takot kang gumalaw dahil baka lumala"],
 why="Ang \u201cpinched nerve\u201d ay nangyayari kapag naiirita ang nerve root — puwedeng dahil sa disc bulge, pamamaga, o paninikip ng espasyo. Pero alam mo ba? Maraming tao ang may disc bulge sa MRI na walang nararamdamang sakit. Ang mahalaga ay kung paano gumagalaw at nag-aadjust ang katawan mo — at 'yon ang puwede nating i-train.",
 faq=[("Masama ba talaga ang disc bulge sa MRI ko?","Hindi laging masama. Maraming pain-free na tao ang may bulge. Titingnan natin kung tugma ba ito sa sintomas mo."),("Puwede ba sa leeg at likod?","Oo — cervical (leeg) at lumbar (likod) ay parehong pinag-uusapan sa consult.")]),
dict(slug="knee-pain",name="Knee Pain",tl="Knee Pain",
 hook="Masakit ang tuhod tuwing <em>aakyat ng hagdan</em>?",
 sub="Tumutunog, namamaga, kumikirot kapag tatayo mula sa upuan. Bago ka sumuko o magpa-inject, alamin kung ano pa ang puwedeng gawin.",
 vids=[("7DMElmO9GHY","I Can\u2019t Believe This Knee Procedure Exists",1400),("0nsHxDAK8tI","Tuhod Ang Issue\u2026Pero Palagutok Pa Rin Ng Likod?",745),("udRcIyBraaQ","Knee pain di gumaling sa PT sa hospital",460)],
 sym=["Sakit kapag umaakyat o bumababa ng hagdan","Hirap tumayo mula sa pagkakaupo o pag-squat","Tumutunog o parang may lumalagutok","Namamaga o naninigas sa umaga","Sinabihan kang may \u201carthritis\u201d o \u201cnasisira na ang tuhod\u201d","Iniiwasan mo nang maglakad nang malayo"],
 why="Ang tuhod ay naiipit sa pagitan ng balakang at bukung-bukong. Madalas, ang sakit ay galing sa kahinaan ng muscles sa paligid nito, maling load, o paninigas — hindi lang sa \u201cpagkasira.\u201d Kahit may arthritis, napapalakas pa rin ang tuhod sa tamang graded exercise.",
 faq=[("May arthritis na ako, may pag-asa pa ba?","Oo. Maraming may arthritis ang gumagaan ang pakiramdam sa tamang strengthening at load management."),("Kailangan ko ba ng knee replacement?","Hindi namin masasabi nang hindi ka natitingnan. Sa consult, aalamin natin ang opsyon mo bago ka magdesisyon.")]),
dict(slug="frozen-shoulder",name="Frozen Shoulder",tl="Frozen Shoulder",
 hook="Hindi na maitaas ang braso? <em>Hirap abutin ang likod?</em>",
 sub="Ang frozen shoulder ay mabagal, masakit, at nakakainip. Pero hindi ito dapat hulaan — at hindi ito dapat puro hot compress lang.",
 vids=[("nMCK7FtrjBg","Frozen shoulder di gumaling sa hospital PT",2300),("P9Q3JzIdKzs","Shoulder Pain Mystery: Is It Your Scapula or Clavicle?",18000),("EDI-L9I2qzw","Hindi Ganito Mag Treat ng Frozen Shoulder",291)],
 sym=["Hirap itaas ang braso o magsuklay","Hindi maabot ang likod o bra strap","Masakit sa gabi, lalo na kapag nakahiga sa side na 'yon","Unti-unting naninigas ang balikat sa loob ng ilang buwan","May diabetes o thyroid problem","Sinubukan na ang masahe pero bumabalik pa rin"],
 why="Sa frozen shoulder (adhesive capsulitis), ang kapsula ng balikat ay namamaga at naninikip. May mga yugto ito — masakit na yugto, naninigas na yugto, at paggaling. Iba-iba ang tamang approach sa bawat yugto, kaya mahalaga ang tamang assessment.",
 faq=[("Gaano katagal bago gumaling?","Iba-iba — madalas buwan ang inaabot. Ang layunin ng plano ay bawasan ang sakit at ibalik ang galaw nang mas mabilis at ligtas."),("Paano kung shoulder pain lang, hindi frozen?","Maraming sanhi ang shoulder pain. Sa consult, aalamin natin kung frozen shoulder ba talaga o iba.")]),
dict(slug="scoliosis",name="Scoliosis",tl="Scoliosis",
 hook="May scoliosis ka o ang anak mo? <em>Huwag mag-panic.</em>",
 sub="Ang kurba sa X-ray ay simula lang ng kuwento. Alamin kung ano talaga ang ibig sabihin nito para sa sakit, postura, at kinabukasan mo.",
 vids=[("PAQ4ctZhkUM","Let\u2019s talk about SCOLIOSIS",571),("4x9vzPQOsVo","Tama Ba Sinasabi Nya Sa Scoliosis?",435),("8N96YMWYqzk","Scoliosis Misdiagnosed in the Philippines -Doc Ron Ang Malakas",375)],
 sym=["Hindi pantay ang balikat o balakang","May umbok sa isang side ng likod kapag yumuyuko","Sakit o pagod sa likod pagkatapos tumayo nang matagal","Sinabihan kang may scoliosis sa X-ray","Nag-aalala ka para sa anak mong lumalaki pa","Hindi mo alam kung kailangan ng brace o operasyon"],
 why="Ang scoliosis ay kurba ng gulugod sa gilid. Hindi lahat ng kurba ay delikado, at hindi lahat ng back pain ay dahil sa kurba. Ang tamang plano ay depende sa edad, laki ng kurba, at sintomas — kaya kailangan ng maayos na pagsusuri, hindi takot.",
 faq=[("Para ba ito sa bata?","Oo, puwedeng pag-usapan ang scoliosis ng bata kasama ang magulang. Para sa mga lumalaking bata, mahalaga ang regular na monitoring."),("Kailangan ba ng brace?","Depende sa edad at sukat ng kurba. Ipapaliwanag namin ang opsyon at kung kailan kailangan ng specialist referral.")]),
]
TV={"uGMmPjFdg7Q":("Knee pain testimonial",61),"FSRWCpxXrDg":("Random testimony",60),"lzju12jCyBI":("Our patients after activelife knee procedure",553),"aknhg1aUqI4":("Amazing Knee Treatment Before & After",633),
"0bR1WBfnTNM":("Disc bulge patient\u2019s positive feedback",84),"3l-nb-WUxi8":("\u201c2 sessions pa lang, ok na ang back pain\u201d",94),"Mlgs3KSfywE":("Upper & lower back pain \u2014 after 1st session",33),
"LNU0PQKHsZE":("Knee pain treatment result",96),"z8RDNE5flRs":("Knee: before & after",42),"8Zl76BBDmyU":("Shoulder mobility: before & after",138),
"FboBrzu4vmg":("Scoliosis: 57\u00b0 to 24.8\u00b0 after therapy",56),"sAZ_xndjIog":("Scoliosis X-ray result (after)",42),"mvTF7vB6qbY":("CDO City Councilor Aimee Moreno at the clinic",94)}
TMAP={"sciatica":["3l-nb-WUxi8","Mlgs3KSfywE","0bR1WBfnTNM"],"pinched-nerve":["0bR1WBfnTNM","3l-nb-WUxi8","Mlgs3KSfywE"],"knee-pain":["LNU0PQKHsZE","uGMmPjFdg7Q","z8RDNE5flRs","lzju12jCyBI"],"frozen-shoulder":["8Zl76BBDmyU","FSRWCpxXrDg","mvTF7vB6qbY"],"scoliosis":["FboBrzu4vmg","sAZ_xndjIog","FSRWCpxXrDg"],"hub":["0bR1WBfnTNM","uGMmPjFdg7Q","FboBrzu4vmg","8Zl76BBDmyU"]}
def tvids(ids):
    return "".join(f'<div class="tv"><div class="vid v"><iframe src="https://www.youtube-nocookie.com/embed/{i}" title="{html.escape(TV[i][0])}" loading="lazy" allowfullscreen></iframe></div><p class="vmeta"><b>{html.escape(TV[i][0])}</b><br>~{fv(TV[i][1])} views</p></div>' for i in ids)
def tsec(ids):
    return f'<section class="sec alt"><div class="c"><span class="eyebrow">Real patient stories</span><h2>Mga kuwento ng pasyente</h2><p class="lead">Mga patient video mula sa YouTube channel ni Dr. Ronald, karamihan mula sa panahon niya sa ActiveLife clinics.</p><div class="tvrow">{tvids(ids)}</div><p class="vmeta">Patient videos as posted on the channel; results vary per person.</p></div></section>'
COMMON_FAQ=[("Magkano ang consult at gaano katagal?","₱500 para sa 15-minutong online consult kay Dr. Ronald sa Zoom. Pipili ka ng slot sa booking page."),("May libre bang option?","Oo — may libreng Staff Screening Line sa booking page para sa mabilisang tanong bago ka mag-book ng doctor consult."),("Paano ako magbabayad?","Sundin lang ang instructions sa booking page. Ang Zoom link ay ibibigay kapag confirmed na ang bayad."),("Puwede ba ito kapalit ng hospital o ER?","Hindi. Kung may red-flag symptoms ka (tingnan sa ibaba), pumunta agad sa ER.")]

def pic(n,alt,w,h,cls="",eager=False):
    ld='fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<picture class="{cls}"><source srcset="img/{n}.webp" type="image/webp"><img src="img/{n}.jpg" alt="{alt}" width="{w}" height="{h}" {ld} decoding="async"></picture>'
HS_ALT="Dr. Ronald Samaniego, PT, DPT — The Angry Doc — professional headshot in navy suit"
ST_ALT="Dr. Ronald Samaniego in The Angry Doc studio, in front of the illuminated The Angry Doc sign with red and blue neon lights"

API="https://askangrydoc.com/api/subscribe"
def optin(src):
    return f'''<section class="sec alt optin" id="tips"><div class="c optin-g"><div><span class="eyebrow">Libre · Free</span><h2>Libreng pain tips, diretso sa text.</h2><p class="lead">Get free pain tips by text from Dr. Ronald — maikli, diretso, walang spam. Kasama ang abiso kapag may bukas na consult slots.</p></div>
<form class="card optin-form" data-api="{API}" data-source="funnel:{src}" novalidate><label>Pangalan / Name<input name="name" type="text" autocomplete="name" required maxlength="80" placeholder="Juan Dela Cruz"></label>
<label>Mobile number<input name="phone" type="tel" inputmode="tel" autocomplete="tel" required placeholder="09XX XXX XXXX"></label>
<label>Concern <small>(optional)</small><input name="concern" type="text" maxlength="200" placeholder="hal. sciatica, knee pain"></label>
<div class="hp" aria-hidden="true"><label>Website<input name="website" type="text" tabindex="-1" autocomplete="off"></label></div>
<label class="oc"><input type="checkbox" name="consent" required> <span>I agree to receive SMS updates and promos from Athletic Therapy Center / The Angry Doc. Reply STOP to opt out. <a href="https://askangrydoc.com/privacy">Privacy Notice</a></span></label>
<p class="oerr" role="alert" hidden></p><button class="btn" type="submit">I-text mo ako ng tips</button><p class="ook" role="status" hidden>Salamat! Nasa listahan ka na. Reply STOP anytime, o <a href="https://askangrydoc.com/optout">mag-unsubscribe dito</a>.</p></form></div></section>'''
def page(p):
    v0=p["vids"][0]
    vids="".join(f'''<div class="rv"><div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/{i}" title="{html.escape(t)}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div><p class="vmeta"><b>{html.escape(t)}</b><br>~{fv(n)} views sa YouTube</p></div>''' for i,t,n in p["vids"])
    sym="".join(f"<li>{I['check']}<span>{s}</span></li>" for s in p["sym"])
    faq="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in p["faq"]+COMMON_FAQ)
    cta=lambda txt="Book Online Consult",cls="btn": f'<a class="{cls} book" href="{BOOK}">{txt} <span aria-hidden="true">→</span></a>'
    return f'''<!doctype html><html lang="fil"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p["tl"]} — Online Consult with Dr. Ronald Samaniego, DPT | The Angry Doc</title>
<meta name="description" content="{p["tl"]}: 15-minute online consult with Dr. Ronald Samaniego, Doctor of Physical Therapy. ₱500 via Zoom. Athletic Therapy Center, Bacoor.">
<meta property="og:title" content="{p["tl"]} — The Angry Doc"><meta property="og:image" content="img/dr-ronald-headshot.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<!-- Meta Pixel: paste your Meta Pixel base code here (replace YOUR_PIXEL_ID). No real ID included. -->
</head><body>
<nav class="top"><div class="c"><a class="brand" href="index.html">The Angry Doc<small>Athletic Therapy Center · Bacoor</small></a>{cta("Book Consult","btn sm")}</div></nav>
<header class="hero"><div class="c grid"><div>
<span class="eyebrow">{p["tl"]} · Online Consult</span>
<h1>{p["hook"]}</h1><p class="sub">{p["sub"]}</p>
<div class="ctas">{cta()}<a class="btn ghost" href="#video">Panoorin muna</a></div>
<div class="trust"><span>{I['video']} 15-min Zoom</span><span>{I['clock']} ₱500 doctor consult</span><span>{I['shield']} Doctor of Physical Therapy</span></div>
</div><figure class="doc-hero rv">{pic("dr-ronald-headshot",HS_ALT,835,1000,"",True)}<figcaption><b>Dr. Ronald Samaniego, PT, DPT</b><span>Ang iyong doktor · The Angry Doc</span></figcaption></figure></div></header>

<section class="sec alt" id="video"><div class="c"><span class="eyebrow">Mula sa YouTube channel</span><h2>Panoorin si Dr. Ronald na ipaliwanag ito</h2><p class="lead">Mga totoong video mula sa The Angry Doc channel tungkol sa {p["name"].lower()}.</p><div class="cards c2" style="margin-top:28px">{vids}</div></div></section>

<section class="sec"><div class="c"><span class="eyebrow">Kilala mo ba 'to?</span><h2>Kung tumatango ka sa ilan dito, para sa'yo ang page na 'to.</h2><ul class="check rv">{sym}</ul>{cta("Pag-usapan natin — Book Online Consult")}</div></section>

<section class="sec alt"><div class="c"><div class="cards c2"><div class="rv"><span class="eyebrow">Bakit ito nangyayari</span><h2>Simpleng paliwanag</h2><p class="lead">{p["why"]}</p></div>
<div class="cards"><div class="card rv"><div class="ico">{I['brain']}</div><h3>Ang sakit ay signal, hindi sira</h3><p>Ang pain ay paraan ng nervous system na protektahan ka. Kapag naintindihan mo ito, nababawasan ang takot — at mas gumagaan ang paggalaw.</p></div></div></div></div></section>

<section class="sec dark"><div class="c"><span class="eyebrow">Ibang approach</span><h2>Bakit hindi gumagaling sa hot compress at TENS lang</h2><p class="lead">Ang passive treatment ay puwedeng magpagaan pansamantala. Pero kung walang plano para palakasin at ibalik ang tiwala ng katawan mo sa paggalaw, madalas bumabalik ang sakit.</p>
<div class="vs" style="margin-top:30px"><div class="card rv"><h3>{I['x']} Karaniwang approach</h3><ul class="no"><li>Hot compress, TENS, ultrasound — tapos uwi</li><li>\u201cMagpahinga ka muna\u201d nang walang plano</li><li>Walang malinaw na paliwanag kung bakit masakit</li><li>Paulit-ulit na session, parehong resulta</li></ul></div>
<div class="card rv"><h3><span style="color:#f08a8f">{I['spark']}</span> Approach ni Angry Doc</h3><ul class="yes"><li><b>Pain education</b> — maiintindihan mo ang kondisyon mo</li><li><b>Graded movement</b> — unti-unting dagdag na galaw at lakas</li><li><b>Assessment-based</b> — hinahanap ang tunay na pinanggagalingan</li><li><b>Malinaw na plano</b> at kailan dapat mag-refer</li></ul></div></div></div></section>

<section class="sec" id="consult"><div class="c"><span class="eyebrow">Ano ang mangyayari</span><h2>Ang iyong 15-minutong online consult</h2>
<div class="steps" style="margin-top:28px"><div class="card rv"><h3>Pumili ng slot</h3><p>Buksan ang booking page at pumili ng oras na swak sa'yo.</p></div><div class="card rv"><h3>Magbayad ng ₱500</h3><p>Sundin ang payment instructions. Makukuha mo ang Zoom link kapag confirmed.</p></div><div class="card rv"><h3>Mag-Zoom kay Dr. Ronald</h3><p>Ikukuwento mo ang sintomas; may simpleng movement checks gamit ang camera.</p></div><div class="card rv"><h3>Umalis nang may plano</h3><p>Malinaw na paliwanag, unang hakbang na exercises, at susunod na gagawin.</p></div></div>
<div class="price rv"><div><small>Doctor consult</small><div class="amt">₱500</div><small>15 minuto · Zoom · kasama si Dr. Ronald</small></div><div>{cta()}<p class="vmeta" style="margin-top:4px">May tanong muna? May <b>libreng Staff Screening Line</b> sa booking page.</p></div></div></div></section>

<section class="sec dark"><div class="c about about-ph"><figure class="studio rv">{pic("dr-ronald-studio",ST_ALT,1000,914)}<figcaption>As seen on <b>The Angry Doc</b></figcaption></figure><div class="rv"><span class="eyebrow">Meet your doctor · Tungkol kay Dr. Ronald</span><h2>Dr. Ronald Samaniego, PT, DPT</h2>
<p>Doctor of Physical Therapy na nag-practice sa Chicago, USA bago bumalik sa Pilipinas para dalhin ang modern physical therapy. Siya ang \u201cThe Angry Doc\u201d — kilala sa diretso at walang-paligoy na paliwanag tungkol sa sakit ng katawan. Ngayon ay nasa Athletic Therapy Center, Bacoor, at tumatanggap ng online consults sa buong Pilipinas.</p>
<div class="stats"><div><b>19.3K</b><span>YouTube subscribers</span></div><div><b>200+</b><span>long-form videos sa YouTube</span></div></div>
<p style="font-size:.85rem">Napanood sa: <a href="https://www.youtube.com/@Angry_Doc456">YouTube · The Angry Doc</a> · <a href="https://www.facebook.com/search/top?q=The%20Angry%20Doc">Facebook · The Angry Doc</a></p></div></div></section>

{tsec(TMAP[p["slug"]])}

<section class="sec"><div class="c" style="max-width:780px"><span class="eyebrow">FAQ</span><h2>Mga madalas itanong</h2>{faq}
<div class="red" style="margin-top:34px"><h3>⚠ Kailan dapat pumunta agad sa ER</h3><p style="margin:0">Huwag nang maghintay ng online consult kung may:</p><ul><li>Hindi makontrol ang ihi o dumi (bladder/bowel)</li><li>Pamamanhid sa \u201csaddle area\u201d (singit, puwit, ari)</li><li>Lumalalang panghihina ng binti o braso</li><li>Sakit na may kasamang lagnat, biglang pagbaba ng timbang, o matapos ang matinding aksidente</li><li>Matinding sakit sa dibdib, hirap huminga, o biglang pamamaga at pamumula</li></ul></div>
<p class="vmeta" style="margin-top:18px">Ang page na ito ay para sa edukasyon lamang at hindi kapalit ng medical advice, diagnosis, o treatment. Ang online consult ay hindi pang-emergency.</p></div></section>

{optin(p["slug"])}
<section class="sec dark final"><div class="c"><h2>Huwag mo nang tiisin.</h2><p class="lead">15 minuto lang, malalaman mo na kung ano ang susunod mong gagawin.</p><div class="ctas" style="justify-content:center">{cta()}</div></div></section>
<footer><div class="c">© 2026 The Angry Doc · Athletic Therapy Center, Bacoor · <a href="index.html">Lahat ng kondisyon</a><br>Educational content only — not medical advice.</div></footer>
<div class="sticky"><div><b>{p["name"]} consult</b><br>₱500 · 15 min · Zoom</div>{cta("Book Now")}</div>
<script src="funnel.js" defer></script></body></html>'''

for p in P: open(p["slug"]+".html","w").write(page(p))
cards="".join(f'<a class="card rv" href="{p["slug"]}.html"><img src="https://i.ytimg.com/vi/{p["vids"][0][0]}/hqdefault.jpg" alt="" loading="lazy"><span class="eyebrow">{p["tl"]}</span><h3>{p["hook"].replace("<em>","").replace("</em>","")}</h3><p class="vmeta">Alamin pa →</p></a>' for p in P)
open("index.html","w").write(f'''<!doctype html><html lang="fil"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Angry Doc — Online PT Consult | Dr. Ronald Samaniego, DPT</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="styles.css">
<!-- Meta Pixel: paste your Meta Pixel base code here (replace YOUR_PIXEL_ID). --></head><body>
<nav class="top"><div class="c"><a class="brand" href="index.html">The Angry Doc<small>Athletic Therapy Center · Bacoor</small></a><a class="btn sm book" href="{BOOK}">Book Consult</a></div></nav>
<header class="hero"><div class="c grid"><div><span class="eyebrow">Online Physical Therapy Consult</span><h1>Sakit ng katawan? <em>Alamin ang totoo.</em></h1><p class="sub">15-minutong Zoom consult kay Dr. Ronald Samaniego, Doctor of Physical Therapy — ₱500. Pumili ng kondisyon mo para magsimula.</p><div class="ctas"><a class="btn book" href="{BOOK}">Book Online Consult →</a></div></div><figure class="doc-hero rv">{pic("dr-ronald-headshot",HS_ALT,835,1000,"",True)}<figcaption><b>Dr. Ronald Samaniego, PT, DPT</b><span>Doctor of Physical Therapy · The Angry Doc</span></figcaption></figure></div></header>
<section class="sec dark"><div class="c about about-ph"><figure class="studio rv">{pic("dr-ronald-studio",ST_ALT,1000,914)}<figcaption>As seen on <b>The Angry Doc</b></figcaption></figure><div class="rv"><span class="eyebrow">Meet your doctor</span><h2>Dr. Ronald Samaniego, PT, DPT</h2><p>Doctor of Physical Therapy na nag-practice sa Chicago, USA. Siya ang \u201cThe Angry Doc\u201d — diretso at walang-paligoy na paliwanag tungkol sa sakit ng katawan. Online consults sa buong Pilipinas mula sa Athletic Therapy Center, Bacoor.</p><div class="stats"><div><b>19.3K</b><span>YouTube subscribers</span></div><div><b>200+</b><span>long-form videos</span></div></div></div></div></section>
<section class="sec"><div class="c"><div class="cards c3 hub">{cards}</div></div></section>
{tsec(TMAP["hub"])}
{optin('index')}
<footer><div class="c">© 2026 The Angry Doc · Educational content only — not medical advice.</div></footer>
<div class="sticky"><div><b>Online consult</b><br>₱500 · 15 min · Zoom</div><a class="btn book" href="{BOOK}">Book Now</a></div>
<script src="funnel.js" defer></script></body></html>''')
