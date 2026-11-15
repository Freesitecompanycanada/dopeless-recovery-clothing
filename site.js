(function () {
  var b = document.querySelector('.burger'), h = document.querySelector('.bar');
  b.addEventListener('click', function () {
    var o = h.classList.toggle('open');
    b.setAttribute('aria-expanded', o);
  });
  document.querySelectorAll('.nav a').forEach(function (a) {
    a.addEventListener('click', function () { h.classList.remove('open'); });
  });
  addEventListener('scroll', function () { h.classList.toggle('stuck', scrollY > 30); }, { passive: true });
  var els = document.querySelectorAll('main section:not(.hero) .wrap');
  if ('IntersectionObserver' in window) {
    document.documentElement.classList.add('js');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.06 });
    els.forEach(function (e) { io.observe(e); });
  }
})();
