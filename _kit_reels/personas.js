// Personas genéricas (sem pessoas reais) no estilo flat escuro + dourado.
// persona({tipo, pele, terno, cabelo}) -> string SVG (viewBox 0 0 240 380)
// tipos: 'executivo' (gravata), 'investidor' (pasta + selo de globo), 'empresario' (caixa),
//        'produtor' (chapéu + camisa xadrez), 'assessor' (gravata dourada)
window.persona = function (o) {
  o = Object.assign({ tipo: 'executivo', pele: '#c9a07a', terno: '#2b2f38', cabelo: '#2a1f17' }, o || {});
  const g = [];
  g.push(`<svg viewBox="0 0 240 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;overflow:visible">`);
  g.push(`<ellipse cx="120" cy="370" rx="78" ry="9" fill="#000" opacity=".55"/>`);
  // pernas
  g.push(`<rect x="86" y="268" width="30" height="100" rx="12" fill="#17191e"/><rect x="124" y="268" width="30" height="100" rx="12" fill="#17191e"/>`);
  // tronco
  const camisa = o.tipo === 'produtor';
  const corpo = camisa ? '#5a4a33' : o.terno;
  g.push(`<path d="M60 175 Q60 140 95 135 L145 135 Q180 140 180 175 L176 285 Q120 296 64 285 Z" fill="${corpo}"/>`);
  if (camisa) {
    for (let x = 70; x < 176; x += 18) g.push(`<line x1="${x}" y1="140" x2="${x}" y2="288" stroke="#c9a45c" stroke-opacity=".22" stroke-width="3"/>`);
    for (let y = 160; y < 286; y += 22) g.push(`<line x1="62" y1="${y}" x2="178" y2="${y}" stroke="#c9a45c" stroke-opacity=".16" stroke-width="3"/>`);
    g.push(`<path d="M104 135 L120 160 L136 135" fill="none" stroke="#3a2f20" stroke-width="5"/>`);
  } else {
    g.push(`<path d="M100 135 L120 175 L140 135 Z" fill="#e9e2d4"/>`);
    const gr = o.tipo === 'assessor' || o.tipo === 'executivo' ? '#c9a45c' : '#7b6a4c';
    g.push(`<path d="M116 146 L124 146 L128 205 L120 216 L112 205 Z" fill="${gr}"/>`);
    g.push(`<path d="M100 135 L112 190 L96 180 Z M140 135 L128 190 L144 180 Z" fill="#000" opacity=".18"/>`);
  }
  // braços
  g.push(`<rect x="38" y="150" width="28" height="118" rx="14" fill="${corpo}" transform="rotate(8 52 150)"/>`);
  g.push(`<rect x="174" y="150" width="28" height="118" rx="14" fill="${corpo}" transform="rotate(-8 188 150)"/>`);
  g.push(`<circle cx="44" cy="272" r="14" fill="${o.pele}"/><circle cx="196" cy="272" r="14" fill="${o.pele}"/>`);
  // pescoço + cabeça
  g.push(`<rect x="108" y="112" width="24" height="28" rx="8" fill="${o.pele}"/>`);
  g.push(`<circle cx="120" cy="84" r="46" fill="${o.pele}"/>`);
  g.push(`<path d="M74 82 Q76 36 120 36 Q166 36 166 80 Q150 58 120 60 Q92 60 74 82 Z" fill="${o.cabelo}"/>`);
  g.push(`<circle cx="104" cy="88" r="4.5" fill="#1a1410"/><circle cx="136" cy="88" r="4.5" fill="#1a1410"/>`);
  g.push(`<path d="M106 106 Q120 116 134 106" fill="none" stroke="#1a1410" stroke-width="3.5" stroke-linecap="round"/>`);
  // acessórios
  if (o.tipo === 'produtor') {
    g.push(`<ellipse cx="120" cy="50" rx="78" ry="14" fill="#8f7240"/><path d="M84 50 Q86 12 120 12 Q154 12 156 50 Z" fill="#a4864f"/><rect x="85" y="40" width="70" height="8" fill="#5a4626"/>`);
  }
  if (o.tipo === 'investidor') {
    g.push(`<rect x="176" y="262" width="62" height="46" rx="6" fill="#4a3a22" stroke="#c9a45c" stroke-width="2"/><rect x="196" y="252" width="22" height="12" rx="4" fill="none" stroke="#c9a45c" stroke-width="3"/>`);
    g.push(`<circle cx="152" cy="168" r="13" fill="#0f1620" stroke="#c9a45c" stroke-width="2"/><ellipse cx="152" cy="168" rx="5" ry="13" fill="none" stroke="#c9a45c" stroke-width="1.5"/><line x1="139" y1="168" x2="165" y2="168" stroke="#c9a45c" stroke-width="1.5"/>`);
  }
  if (o.tipo === 'empresario') {
    g.push(`<rect x="150" y="226" width="80" height="64" rx="4" fill="#6b5634" stroke="#c9a45c" stroke-width="2"/><line x1="150" y1="246" x2="230" y2="246" stroke="#c9a45c" stroke-width="2"/><line x1="190" y1="226" x2="190" y2="246" stroke="#c9a45c" stroke-width="2"/>`);
  }
  g.push(`</svg>`);
  return g.join('');
};
// ícones simples (viewBox 0 0 100 100), traço dourado
window.icone = function (nome) {
  const s = 'fill="none" stroke="#c9a45c" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"';
  const I = {
    container: `<rect x="12" y="30" width="76" height="46" rx="3" ${s}/><path d="M24 36v34M36 36v34M48 36v34M60 36v34M72 36v34" ${s} stroke-width="2.5"/>`,
    saco: `<path d="M28 26h44l6 58H22z" ${s}/><path d="M32 18h36l-4 8H36z" ${s}/><path d="M38 52h24M38 62h24" ${s} stroke-width="3"/>`,
    divida: `<rect x="20" y="12" width="60" height="76" rx="5" ${s}/><path d="M32 30h36M32 44h36M32 58h20" ${s} stroke-width="3"/><text x="66" y="80" font-size="22" fill="#c9a45c" font-family="Fraunces,serif" text-anchor="middle">$</text>`,
    cupula: `<path d="M10 70h80" ${s}/><path d="M22 70 Q50 40 78 70" ${s}/><path d="M36 70 Q50 92 64 70" ${s}/><path d="M50 40V18" ${s}/><path d="M18 82h64" ${s} stroke-width="3"/>`,
    casa: `<path d="M14 48 L50 16 L86 48" ${s}/><path d="M24 42v44h52V42" ${s}/><rect x="42" y="60" width="16" height="26" ${s} stroke-width="3"/>`,
  };
  return `<svg viewBox="0 0 100 100" style="width:100%;height:100%">${I[nome]}</svg>`;
};
