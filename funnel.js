// UTM passthrough: append utm_* (and fbclid) from page URL to every booking link
(function(){var q=new URLSearchParams(location.search),k=[];q.forEach(function(v,n){if(/^utm_|^fbclid$/.test(n))k.push([n,v])});
var src=location.pathname.split('/').pop().replace('.html','')||'index';
document.querySelectorAll('a.book').forEach(function(a){var u=new URL(a.href);k.forEach(function(p){u.searchParams.set(p[0],p[1])});if(!u.searchParams.has('utm_content'))u.searchParams.set('utm_content',src);a.href=u.toString();
a.addEventListener('click',function(){if(window.fbq)fbq('track','Lead',{content_name:src})})});
var io='IntersectionObserver'in window&&new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.rv').forEach(function(el){io?io.observe(el):el.classList.add('in')});})();
