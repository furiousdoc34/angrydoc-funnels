// UTM passthrough: append utm_* (and fbclid) from page URL to every booking link
(function(){var q=new URLSearchParams(location.search),k=[];q.forEach(function(v,n){if(/^utm_|^fbclid$/.test(n))k.push([n,v])});
var src=location.pathname.split('/').pop().replace('.html','')||'index';
document.querySelectorAll('a.book').forEach(function(a){var u=new URL(a.href);k.forEach(function(p){u.searchParams.set(p[0],p[1])});if(!u.searchParams.has('utm_content'))u.searchParams.set('utm_content',src);a.href=u.toString();
a.addEventListener('click',function(){if(window.fbq)fbq('track','Lead',{content_name:src})})});
var io='IntersectionObserver'in window&&new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.rv').forEach(function(el){io?io.observe(el):el.classList.add('in')});})();
// SMS opt-in -> askangrydoc.com/api/subscribe (CORS-allowed). Consent box must be ticked.
document.querySelectorAll('form.optin-form').forEach(function(f){f.addEventListener('submit',function(ev){ev.preventDefault();
var er=f.querySelector('.oerr'),ok=f.querySelector('.ook'),b=f.querySelector('button');function say(m){er.textContent=m||'';er.hidden=!m}say('');
var d={name:f.name.value.trim(),phone:f.phone.value,concern:f.concern.value,website:f.website.value,consent:f.consent.checked,source:f.dataset.source};
if(d.name.length<2)return say('Pakilagay ang pangalan mo.');
if(!/^(\+?63|0)?9\d{9}$/.test(d.phone.replace(/[\s\-().]/g,'')))return say('Pakilagay ang valid na PH mobile number (hal. 0917 123 4567).');
if(!d.consent)return say('Paki-tick ang box para pumayag na makatanggap ng texts.');
b.disabled=true;fetch(f.dataset.api,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(function(r){return r.json().catch(function(){return{}}).then(function(j){if(!r.ok)throw new Error(j.error||'May error. Subukan ulit.');
[].forEach.call(f.elements,function(el){el.disabled=true});b.hidden=true;ok.hidden=false;if(window.fbq)fbq('track','Subscribe',{content_name:d.source})})}).catch(function(e){say(e.message||'May error. Subukan ulit.');b.disabled=false})})});
