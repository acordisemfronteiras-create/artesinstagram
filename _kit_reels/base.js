// Motor de animação dos Reels @tiagoassessorxp.
// A página define cenas <div class="scene" id="ID"> e elementos com:
//   data-in="fade-up|fade|pop|left|right|grow-y|grow-x|draw|down"  efeito de entrada
//   data-at="1.2" (s após o início da cena) ou "L2+0.3" (início da 2ª legenda da cena + 0,3 s)
//   data-dur="0.7"   duração (padrão 0,7 s)
//   data-out="L3"    some nesse instante (opcional)
//   data-float="8"   flutua em loop (amplitude px)
//   data-at também aceita "@deixa+0.2" (deixa = {nome} marcado dentro da fala no roteiro.json)
//   data-cin="L2" (classe .cin): texto cinético, palavra a palavra no ritmo da fala; <em> = palavra de destaque;
//       data-cin-hold (s na tela depois da fala) ou data-cin-out="@deixa"; "legenda_na_tela": false no roteiro esconde a legenda de baixo
//   window.onSeek(t): função opcional da página, chamada a cada quadro (câmera, grades, partículas)
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
    const c = spec.match(/^@(\w+)([+-][\d.]+)?$/);   // "@deixa+0.2": deixa marcada com {deixa} na fala
    if (c) {
      if (!(c[1] in (TL.cues || {}))) throw new Error('deixa inexistente: ' + c[1]);
      return TL.cues[c[1]] + parseFloat(c[2] || 0);
    }
    return cena(sid).ini + parseFloat(spec);
  }
  window.cue = (nome, d) => { if (!(nome in (TL.cues || {}))) throw new Error('deixa inexistente: ' + nome); return TL.cues[nome] + (d || 0); };
  window.ease = k => { k = Math.max(0, Math.min(1, k)); return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; };
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
  const counters = [], cins = [];
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
          el.animate([{ opacity: 1 }, { opacity: 0 }], { delay: at(sid, el.dataset.out) * 1000, duration: 220, fill: 'forwards', composite: 'replace' });
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
    // texto cinético: <div class="cin" data-cin="L2">imagina uma equipe inteira de <em>agentes</em></div>
    // as palavras entram uma a uma no ritmo da fala L2 da cena (ou data-cin="@deixa" data-cin-dur="2.4")
    document.querySelectorAll('.scene').forEach(sc => sc.querySelectorAll('[data-cin]').forEach(el => {
      const spec = el.dataset.cin, m = spec.match(/^L(\d+)$/);
      let ini, fim;
      if (m) { const l = legs(sc.id)[+m[1] - 1]; ini = l.ini; fim = l.fim; }
      else { ini = at(sc.id, spec); fim = ini + parseFloat(el.dataset.cinDur || 2); }
      const words = [];
      (function split(node) {
        [...node.childNodes].forEach(n => {
          if (n.nodeType === 3) {
            const frag = document.createDocumentFragment();
            n.textContent.split(/(\s+)/).forEach(w => {
              if (!w.trim()) { frag.appendChild(document.createTextNode(w)); return; }
              const sp = document.createElement('span'); sp.className = 'w'; sp.textContent = w; frag.appendChild(sp); words.push(sp);
            });
            n.replaceWith(frag);
          } else if (n.nodeType === 1 && n.tagName !== 'BR') split(n);
        });
      })(el);
      const sai = el.dataset.cinOut ? at(sc.id, el.dataset.cinOut) : fim + parseFloat(el.dataset.cinHold || 0.3);
      cins.push({ el, words, ini, fim, sai });
    }));
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
    cins.forEach(c => {
      const vis = t >= c.ini - 0.05 && t < c.sai + 0.2;
      c.el.style.opacity = !vis ? 0 : Math.max(0, Math.min(1, (c.sai + 0.2 - t) / 0.2));
      if (!vis) return;
      const span = Math.max(0.3, c.fim - c.ini - 0.15);
      c.words.forEach((w, i) => {
        const k = Math.max(0, Math.min(1, (t - (c.ini + span * i / c.words.length)) / 0.16));
        const e = 1 - Math.pow(1 - k, 3);
        w.style.opacity = e; w.style.transform = `translateY(${(1 - e) * 26}px)`; w.style.filter = k < 1 ? `blur(${(1 - e) * 7}px)` : 'none';
      });
    });
    if (TL.sem_legenda) document.getElementById('cap').style.display = 'none';
    caption(t);
    document.querySelector('#bar i').style.width = (100 * Math.min(1, t / TL.duracao)) + '%';
    if (window.onSeek) window.onSeek(t);   // gancho para animação contínua (câmera, grade etc.)
  };
  window.addEventListener('DOMContentLoaded', () => { setup(); window.seek(0); window.__ready = true; });
})();
