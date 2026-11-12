// Motor de animação dos Reels @tiagoassessorxp.
// A página define cenas <div class="scene" id="ID"> e elementos com:
//   data-in="fade-up|fade|pop|left|right|grow-y|grow-x|draw|down"  efeito de entrada
//   data-at="1.2" (s após o início da cena) ou "L2+0.3" (início da 2ª legenda da cena + 0,3 s)
//   data-dur="0.7"   duração (padrão 0,7 s)
//   data-out="L3"    some nesse instante (opcional)
//   data-float="8"   flutua em loop (amplitude px)
//   data-count="5.65" data-from="5.56" data-dec="2" data-pre="R$ " data-suf=""  contador
// O render.py chama window.seek(t) a cada quadro.
(function () {
  const TL = window.TL;
  const cena = id => TL.cenas.find(c => c.id === id);
  const legs = id => TL.legendas.filter(l => l.cena === id);
  function at(sid, spec) {
    spec = String(spec ?? '0');
    const m = spec.match(/^L(\d+)([+-][\d.]+)?$/);
    if (m) return legs(sid)[+m[1] - 1].ini + parseFloat(m[2] || 0);
    return cena(sid).ini + parseFloat(spec);
  }
  const E = 'cubic-bezier(.2,.8,.2,1)';
  const FX = {
    'fade-up': [{ opacity: 0, transform: 'translateY(50px)' }, { opacity: 1, transform: 'translateY(0)' }],
    'down': [{ opacity: 0, transform: 'translateY(-50px)' }, { opacity: 1, transform: 'translateY(0)' }],
    'fade': [{ opacity: 0 }, { opacity: 1 }],
    'pop': [{ opacity: 0, transform: 'scale(.55)' }, { opacity: 1, transform: 'scale(1.07)', offset: .7 }, { opacity: 1, transform: 'scale(1)' }],
    'left': [{ opacity: 0, transform: 'translateX(-140px)' }, { opacity: 1, transform: 'translateX(0)' }],
    'right': [{ opacity: 0, transform: 'translateX(140px)' }, { opacity: 1, transform: 'translateX(0)' }],
    'grow-y': [{ transform: 'scaleY(0)' }, { transform: 'scaleY(1)' }],
    'grow-x': [{ transform: 'scaleX(0)' }, { transform: 'scaleX(1)' }],
    'tilt': [{ transform: 'rotate(0deg)' }, { transform: 'rotate(-9deg)' }],
    'zoom': [{ opacity: 0, transform: 'scale(1.25)' }, { opacity: 1, transform: 'scale(1)' }],
  };
  const counters = [];
  function setup() {
    // moldura
    const st = document.getElementById('stage');
    st.insertAdjacentHTML('beforeend', `<div id="grain"></div>
      <div id="top"><span class="k">${TL.kicker || 'Entenda em 1 minuto'}</span><span class="h">@tiagoassessorxp</span></div>
      <div id="bar"><i></i></div><div id="cap"><p></p></div>`);
    document.querySelectorAll('.scene').forEach(sc => {
      const sid = sc.id;
      sc.querySelectorAll('[data-in]').forEach(el => {
        const t0 = at(sid, el.dataset.at), dur = parseFloat(el.dataset.dur || .7) * 1000;
        let kf = FX[el.dataset.in];
        if (el.dataset.in === 'draw') {
          const len = el.getTotalLength();
          el.style.strokeDasharray = len;
          kf = [{ strokeDashoffset: len }, { strokeDashoffset: 0 }];
        }
        el.animate(kf, { delay: t0 * 1000, duration: dur, fill: 'both', easing: E });
        if (el.dataset.out) {
          el.animate([{ opacity: 1 }, { opacity: 0 }], { delay: at(sid, el.dataset.out) * 1000, duration: 350, fill: 'forwards', composite: 'replace' });
        }
      });
      sc.querySelectorAll('[data-float]').forEach((el, i) => {
        const a = parseFloat(el.dataset.float);
        el.animate([{ transform: `translateY(${-a}px)` }, { transform: `translateY(${a}px)` }],
          { duration: 1800 + i * 370, iterations: Infinity, direction: 'alternate', easing: 'ease-in-out' });
      });
      sc.querySelectorAll('[data-count]').forEach(el => counters.push({
        el, t0: at(sid, el.dataset.at), dur: parseFloat(el.dataset.dur || 1.4),
        from: parseFloat(el.dataset.from || 0), to: parseFloat(el.dataset.count),
        dec: parseInt(el.dataset.dec || 0), pre: el.dataset.pre || '', suf: el.dataset.suf || ''
      }));
    });
    document.getAnimations().forEach(a => a.pause());
  }
  const fmt = (v, d) => v.toLocaleString('pt-BR', { minimumFractionDigits: d, maximumFractionDigits: d });
  let capIdx = -2;
  function caption(t) {
    const L = TL.legendas;
    let i = L.findIndex(l => t >= l.ini - 0.05 && t < l.fim + 0.25);
    const p = document.querySelector('#cap p');
    if (i !== capIdx) {
      capIdx = i;
      p.innerHTML = i < 0 ? '' : L[i].texto.split(' ').map(w =>
        `<span data-h="${/[\d$%]/.test(w) ? 1 : 0}">${w}</span>`).join(' ');
    }
    if (i < 0) return;
    const l = L[i], sp = p.querySelectorAll('span');
    const prog = Math.min(1, (t - l.ini) / Math.max(.3, l.fim - l.ini - .15));
    const n = Math.ceil(prog * sp.length + 0.001);
    sp.forEach((s, k) => { s.className = k < n ? (s.dataset.h === '1' ? 'on hl' : 'on') : ''; });
  }
  window.seek = function (t) {
    document.getAnimations().forEach(a => { a.currentTime = t * 1000; });
    TL.cenas.forEach(c => {
      const el = document.getElementById(c.id); if (!el) return;
      const fi = 0.3;
      let o = 0;
      if (t >= c.ini - fi / 2 && t <= c.fim + fi / 2) {
        o = Math.min(1, (t - (c.ini - fi / 2)) / fi, ((c.fim + fi / 2) - t) / fi);
        if (c === TL.cenas[0]) o = Math.min(1, ((c.fim + fi / 2) - t) / fi);
        if (c === TL.cenas[TL.cenas.length - 1]) o = Math.min(1, (t - (c.ini - fi / 2)) / fi);
      }
      el.style.opacity = Math.max(0, o);
      const k = (t - c.ini) / Math.max(1, c.fim - c.ini);
      el.style.transform = `scale(${1 + 0.025 * Math.max(0, Math.min(1, k))})`;
    });
    counters.forEach(c => {
      const k = Math.max(0, Math.min(1, (t - c.t0) / c.dur));
      const e = 1 - Math.pow(1 - k, 3);
      c.el.textContent = c.pre + fmt(c.from + (c.to - c.from) * e, c.dec) + c.suf;
    });
    caption(t);
    document.querySelector('#bar i').style.width = (100 * Math.min(1, t / TL.duracao)) + '%';
  };
  window.addEventListener('DOMContentLoaded', () => { setup(); window.seek(0); window.__ready = true; });
})();
