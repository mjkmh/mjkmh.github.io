/* Sitefinity düzenleme ekranında EN sayfayı TR içerikten doldurma yardımcıları */
window.__trEn = async function (trPath) {
  var t = await fetch(trPath + (trPath.indexOf('?') < 0 ? '?' : '&') + 'v=' + Date.now()).then(function (r) { return r.text(); });
  var dd = new DOMParser().parseFromString(t, 'text/html');
  var bl = [].slice.call(dd.querySelectorAll('.sfContentBlock')).filter(function (b) {
    return !/footer__|Bilgi İşlem/.test(b.innerHTML) && b.innerHTML.length > 500;
  }).sort(function (a, b) { return b.innerHTML.length - a.innerHTML.length; });
  return window.__cevir(bl[0].innerHTML);
};
window.__docks = function (re) {
  return [].slice.call(document.querySelectorAll('.RadDock')).filter(function (x) {
    return x.offsetParent && re.test(x.textContent.replace(/\s+/g, ' ').trim());
  });
};
window.__legacyFill = async function (html, i) {
  var d = window.__docks(/^Content blockEditMore/)[i || 0];
  [].slice.call(d.querySelectorAll('a')).filter(function (a) { return a.textContent.trim() === 'Edit'; })[0].click();
  await new Promise(function (r) { setTimeout(r, 4500); });
  var fr = document.querySelectorAll('iframe');
  for (var k = 0; k < fr.length; k++) {
    var w; try { w = fr[k].contentWindow; if (!(w.Telerik && w.$telerik)) continue; } catch (e) { continue; }
    var eds = w.$telerik.radControls.filter(function (c) { return c.set_html; });
    if (eds.length) {
      eds[0].set_html(html);
      await new Promise(function (r) { setTimeout(r, 500); });
      var s = [].slice.call(fr[k].contentDocument.querySelectorAll('a,button,input,span')).filter(function (x) {
        return (x.textContent || x.value || '').trim() === 'Save' && x.offsetParent;
      });
      if (s[0]) s[0].click();
      return ['legacy', eds[0].get_html().length, s.length];
    }
  }
  /* MVC (kendo) editör */
  var ed = window.$ && $('[data-role=editor]').map(function (i, e) { return $(e).data('kendoEditor'); }).get().filter(Boolean)[0];
  if (ed) { ed.value(html); ed.trigger('change'); return ['mvc', ed.value().length, 'Save butonuna elle basılmalı']; }
  return 'editör yok';
};
window.__deleteDock = async function (re) {
  var d = window.__docks(re)[0]; if (!d) return 'yok';
  [].slice.call(d.querySelectorAll('a')).filter(function (a) { return /More/.test(a.textContent); })[0].click();
  await new Promise(function (r) { setTimeout(r, 600); });
  var del = [].slice.call(document.querySelectorAll('a')).filter(function (a) { return a.textContent.trim() === 'Delete' && a.offsetParent; });
  if (del[0]) del[0].click();
  await new Promise(function (r) { setTimeout(r, 1500); });
  return del.length;
};
