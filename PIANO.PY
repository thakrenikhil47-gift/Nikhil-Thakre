import webbrowser
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from threading import Timer

HOST = "127.0.0.1"
PORT = 8000

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#fbf8f0">
<meta name="description" content="Nikhil Thakre — Electronics, technology and industrial operations portfolio.">
<title>Nikhil Thakre | Digital Portfolio</title>
<style>
:root{
 --paper:#fbf8f0;--white:#fffefa;--ink:#171711;--muted:#6e6a60;
 --gold:#bd8722;--gold2:#e9c66f;--gold-dark:#76500c;--line:rgba(167,117,25,.22);
 --shadow:0 24px 70px rgba(93,67,20,.10);--max:1240px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:92px}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,"SF Pro Display","Segoe UI",Arial,sans-serif;line-height:1.65;overflow-x:hidden}
body:before{content:"";position:fixed;inset:0;pointer-events:none;z-index:-2;background:radial-gradient(ellipse at 82% 12%,rgba(245,210,125,.22),transparent 31%),radial-gradient(ellipse at 5% 80%,rgba(226,193,117,.13),transparent 35%),linear-gradient(135deg,#fffdf8 0%,#f8f4e9 100%)}
a{color:inherit}
::selection{background:#e8c46b;color:#201805}
#progress{position:fixed;top:0;left:0;width:100%;height:3px;z-index:200;transform-origin:left;transform:scaleX(0);background:linear-gradient(90deg,#8b5b0b,#e8c46b,#fff0b4)}
header{position:fixed;top:0;left:0;right:0;z-index:100;transition:background .45s,box-shadow .45s,border-color .45s}
header.scrolled{background:rgba(255,254,250,.82);backdrop-filter:blur(20px);box-shadow:0 8px 30px rgba(71,52,14,.06);border-bottom:1px solid rgba(167,117,25,.12)}
.nav-wrap{max-width:var(--max);margin:auto;padding:20px 34px;display:flex;align-items:center;justify-content:space-between;gap:24px;transition:padding .35s}
header.scrolled .nav-wrap{padding-top:12px;padding-bottom:12px}
.brand{display:inline-flex;align-items:center;gap:11px;text-decoration:none;font-size:.82rem;font-weight:800;letter-spacing:3px;white-space:nowrap}
.brand-mark{width:28px;height:34px;display:grid;place-items:center;color:var(--gold);font-size:1.7rem;line-height:1}
.brand b{font-weight:800}
.brand b span{color:var(--gold)}
nav{display:flex;align-items:center;gap:clamp(8px,1.7vw,25px)}
nav a{position:relative;text-decoration:none;font-size:.83rem;color:#555248;padding:8px 0;transition:color .25s}
nav a:after{content:"";position:absolute;left:0;right:100%;bottom:2px;height:1px;background:var(--gold);transition:right .35s cubic-bezier(.2,.7,.2,1)}
nav a:hover,nav a.active{color:#9a690f}
nav a:hover:after,nav a.active:after{right:0}
.nav-cta,.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;padding:12px 20px;text-decoration:none;font-size:.83rem;font-weight:700;transition:transform .3s cubic-bezier(.2,.8,.2,1),box-shadow .3s,background .3s}
.nav-cta,.btn.gold{background:linear-gradient(115deg,#a56c0b,#e1b84e 55%,#b37b12);color:white;box-shadow:0 8px 22px rgba(169,117,16,.18);border:1px solid rgba(255,255,255,.55)}
.nav-cta:hover,.btn:hover{transform:translateY(-3px);box-shadow:0 14px 28px rgba(169,117,16,.22)}
.btn.light{border:1px solid rgba(145,100,15,.45);color:#65460e;background:rgba(255,255,255,.48)}
.menu-toggle{display:none;border:1px solid var(--line);background:rgba(255,255,255,.65);border-radius:50%;width:42px;height:42px;font-size:1.2rem}
.hero{min-height:100svh;position:relative;display:flex;align-items:center;overflow:hidden;padding:125px 34px 75px;isolation:isolate}
.hero-inner{max-width:var(--max);width:100%;margin:0 auto;display:grid;grid-template-columns:.88fr 1.12fr;align-items:center;gap:15px;position:relative;z-index:2}
.hero-copy{max-width:570px;padding:18px 0 30px}
.pill{display:inline-flex;align-items:center;gap:10px;padding:7px 14px;border:1px solid rgba(174,121,20,.38);border-radius:999px;background:rgba(255,255,255,.55);font-size:.74rem;letter-spacing:2px;text-transform:uppercase;color:#65502b}
.pill:before{content:"";width:6px;height:6px;background:var(--gold);border-radius:50%;box-shadow:0 0 0 4px rgba(189,135,34,.12)}
.hero h1{font-size:clamp(3.2rem,7.2vw,6.6rem);letter-spacing:-.075em;line-height:.98;margin:25px 0 22px;font-weight:760}
.hero h1 .gold-text{color:var(--gold);background:linear-gradient(110deg,#96610a,#e1b64d 55%,#9d6c13);background-clip:text;-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-subtitle{font-size:clamp(.92rem,1.25vw,1.08rem);letter-spacing:3px;line-height:1.8;text-transform:uppercase;max-width:420px}
.gold-rule{height:2px;width:54px;background:linear-gradient(90deg,var(--gold),#e9ce86);margin:23px 0}
.hero-desc{color:var(--muted);max-width:435px;font-size:.98rem}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}
.socials{display:flex;gap:17px;margin-top:28px;color:#504329;font-size:.82rem}
.socials a{text-decoration:none;border-bottom:1px solid transparent;transition:color .2s,border-color .2s}
.socials a:hover{color:var(--gold);border-color:var(--gold)}
.hero-visual{position:relative;min-height:600px;display:grid;place-items:center;perspective:1200px}
.visual-glow{position:absolute;width:min(43vw,560px);height:min(43vw,560px);border-radius:50%;background:radial-gradient(circle,rgba(246,208,113,.36),rgba(246,208,113,.08) 48%,transparent 70%);filter:blur(7px);animation:glowBreathe 6s ease-in-out infinite}
.chip-stage{position:relative;width:min(100%,650px);aspect-ratio:1.15;transform-style:preserve-3d;animation:stageFloat 7s ease-in-out infinite}
.circuit-svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.chip{position:absolute;left:50%;top:51%;width:51%;aspect-ratio:1.15;transform:translate(-50%,-50%) rotate(-13deg) skewY(2deg);border-radius:26px;background:linear-gradient(145deg,#39362d,#11110f 48%,#4c4027);border:2px solid #d7ad4e;box-shadow:0 30px 0 #b88622,0 39px 0 #8b641c,0 55px 55px rgba(99,65,8,.24),inset 0 2px 0 rgba(255,242,193,.75),inset 0 -8px 16px rgba(0,0,0,.55);display:grid;place-items:center;z-index:3}
.chip:before{content:"";position:absolute;inset:12px;border:1px solid rgba(232,194,96,.6);border-radius:17px}
.chip:after{content:"";position:absolute;inset:-13px;border-radius:31px;border:1px solid rgba(201,153,44,.42);transform:translateZ(-10px)}
.chip-label{text-align:center;color:#f4d78d;text-transform:uppercase;letter-spacing:2px;font-size:clamp(.55rem,1vw,.85rem);line-height:1.65;text-shadow:0 0 18px rgba(255,213,104,.25)}
.chip-label strong{display:block;font-size:1.25em;letter-spacing:3px}
.pin{position:absolute;z-index:2;background:linear-gradient(90deg,#94640e,#ffec9c,#b7831a);box-shadow:0 0 8px rgba(214,164,45,.45)}
.pin.top,.pin.bottom{height:12px;width:6%;left:47%;border-radius:2px}
.pin.top{top:-11px}.pin.bottom{bottom:-11px}
.pin.left,.pin.right{width:12px;height:6%;top:47%;border-radius:2px}
.pin.left{left:-11px}.pin.right{right:-11px}
.float-card{position:absolute;z-index:4;background:rgba(255,254,248,.73);backdrop-filter:blur(14px);border:1px solid rgba(191,143,38,.35);border-radius:16px;padding:15px 17px;box-shadow:0 16px 35px rgba(115,83,17,.11);font-size:.74rem;color:#625638;animation:cardFloat 5s ease-in-out infinite}
.float-card strong{display:block;color:#282317;font-size:.84rem;margin-bottom:3px}
.float-card.one{top:12%;left:4%;transform:rotate(-7deg)}
.float-card.two{right:0;top:24%;animation-delay:-2s;transform:rotate(5deg)}
.float-card.three{left:11%;bottom:11%;animation-delay:-1s}
.signal{height:28px;display:flex;align-items:center;gap:4px;margin-top:7px}
.signal i{display:block;width:4px;border-radius:4px;background:linear-gradient(#e4bc54,#a46f12);animation:signal 1s ease-in-out infinite alternate}
.signal i:nth-child(2n){animation-delay:.2s}.signal i:nth-child(3n){animation-delay:.4s}
.hero-index{position:absolute;right:28px;top:50%;transform:translateY(-50%);display:grid;gap:20px;font-size:.72rem;color:#8c7c5b}
.hero-index span:first-child{color:var(--gold);font-weight:800}
.scroll-cue{position:absolute;bottom:26px;left:max(34px,calc((100vw - var(--max))/2));display:flex;align-items:center;gap:12px;color:#93866c;font-size:.72rem;letter-spacing:1.5px;text-transform:uppercase}
.scroll-cue span{width:20px;height:31px;border:1px solid #b78a2d;border-radius:99px;position:relative}
.scroll-cue span:after{content:"";position:absolute;top:6px;left:8px;width:2px;height:6px;background:var(--gold);border-radius:2px;animation:wheel 1.5s infinite}
main{position:relative}
.section{padding:115px 34px;position:relative;scroll-margin-top:72px}
.section-inner{max-width:var(--max);margin:0 auto}
.section-kicker{color:#9a6a13;text-transform:uppercase;font-size:.72rem;letter-spacing:3px;font-weight:750;margin-bottom:13px}
.section-title{font-size:clamp(2.25rem,4.5vw,4.3rem);line-height:1.08;letter-spacing:-.06em;margin:0 0 25px;font-weight:700}
.section-title span{color:var(--gold)}
.section-intro{color:var(--muted);max-width:640px;font-size:1.04rem}
.reveal{opacity:0;transform:translateY(45px);filter:blur(5px);transition:opacity 1s cubic-bezier(.16,1,.3,1),transform 1s cubic-bezier(.16,1,.3,1),filter 1s cubic-bezier(.16,1,.3,1)}
.reveal.visible{opacity:1;transform:translateY(0);filter:blur(0)}
.about-section{background:linear-gradient(180deg,rgba(255,254,250,.9),rgba(248,242,226,.65))}
.about-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:clamp(35px,7vw,105px);align-items:center}
.portrait-card{min-height:440px;position:relative;border-radius:34px;background:linear-gradient(145deg,#f4e4b7,#fffdf7 52%,#e6c66f);border:1px solid rgba(182,130,27,.26);overflow:hidden;display:grid;place-items:center;box-shadow:var(--shadow)}
.portrait-card:before,.portrait-card:after{content:"";position:absolute;border:1px solid rgba(183,129,24,.35);border-radius:50%;width:75%;aspect-ratio:1;animation:orbit 24s linear infinite}
.portrait-card:after{width:94%;animation-duration:36s;animation-direction:reverse}
.portrait-initials{width:200px;height:200px;border-radius:50%;display:grid;place-items:center;font-size:4rem;font-weight:700;letter-spacing:-5px;color:#fff8e7;background:linear-gradient(145deg,#8b5d12,#e3bd5d 60%,#9c6b17);box-shadow:0 25px 55px rgba(133,91,14,.25);z-index:1}
.portrait-note{position:absolute;bottom:23px;left:23px;right:23px;z-index:2;padding:14px 17px;border-radius:15px;background:rgba(255,254,250,.76);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.85);font-size:.77rem;color:#665a3d}
.portrait-note strong{display:block;color:#292419;font-size:.95rem}
.about-copy p{color:var(--muted)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:30px 0}
.stat{padding:13px 0;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat strong{display:block;font-size:1.7rem;letter-spacing:-1px}
.stat span{font-size:.75rem;color:var(--muted)}
.capability-list{display:grid;gap:15px;margin-top:28px}
.capability{display:flex;align-items:center;gap:14px;padding:13px 15px;border:1px solid transparent;border-radius:14px;transition:background .3s,border-color .3s,transform .3s}
.capability:hover{background:rgba(255,255,255,.7);border-color:var(--line);transform:translateX(5px)}
.capability-icon{flex:0 0 42px;width:42px;height:42px;display:grid;place-items:center;border:1px solid rgba(183,129,24,.35);border-radius:50%;color:#9a6a13;background:rgba(255,255,255,.7);font-size:1.1rem}
.capability strong{display:block;font-size:.9rem}.capability small{color:var(--muted)}
.education-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:60px;align-items:center}
.education-card{position:relative;border:1px solid var(--line);border-radius:24px;background:rgba(255,254,250,.78);padding:30px;box-shadow:var(--shadow);overflow:hidden}
.education-card:after{content:"";position:absolute;right:-70px;top:-70px;width:190px;height:190px;border-radius:50%;background:radial-gradient(circle,rgba(230,190,86,.23),transparent 70%)}
.edu-top{display:flex;align-items:flex-start;gap:16px;position:relative;z-index:1}
.edu-icon{width:48px;height:48px;flex-shrink:0;border-radius:15px;background:#f7ebc9;color:#96640d;display:grid;place-items:center;font-size:1.35rem}
.education-card h3{font-size:1.12rem;margin:0 0 6px}.education-card p{color:var(--muted);margin:3px 0}
.edu-year{display:inline-block;margin-top:18px;color:#8b5e0c;font-size:.78rem;font-weight:750;letter-spacing:1px}
.skills-section{background:#f4eddd}
.skills-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:35px}
.skill-card{min-height:150px;border:1px solid rgba(164,117,26,.2);border-radius:18px;padding:22px;background:rgba(255,254,250,.74);transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s,border-color .35s}
.skill-card:hover{transform:translateY(-7px);box-shadow:0 20px 40px rgba(105,77,21,.1);border-color:rgba(164,117,26,.5)}
.skill-icon{font-size:1.45rem;color:#a57216;margin-bottom:15px}.skill-card h3{font-size:.95rem;margin:0 0 6px}.skill-card p{font-size:.79rem;color:var(--muted);margin:0}
.experience-layout{display:grid;grid-template-columns:.65fr 1.35fr;gap:60px}
.experience-list{display:grid;gap:15px}
.experience-card{display:grid;grid-template-columns:120px 1fr;gap:22px;padding:25px;border:1px solid var(--line);border-radius:20px;background:rgba(255,254,250,.8);transition:transform .3s,box-shadow .3s}
.experience-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.experience-date{font-size:.77rem;color:#95660e;font-weight:750;letter-spacing:1px}
.experience-card h3{margin:0 0 5px;font-size:1.06rem}.experience-card p{color:var(--muted);margin:0 0 8px;font-size:.9rem}
.experience-card ul{margin:8px 0 0;padding-left:18px;color:#5f5b51;font-size:.86rem}
.objective-panel{position:relative;overflow:hidden;border-radius:30px;padding:clamp(30px,6vw,70px);background:linear-gradient(115deg,#201b0e,#49330d 52%,#8d6417);color:#fff8e8}
.objective-panel:before{content:"";position:absolute;width:420px;height:420px;border:1px solid rgba(255,224,144,.2);border-radius:50%;right:-100px;top:-190px;box-shadow:0 0 0 35px rgba(255,224,144,.035),0 0 0 75px rgba(255,224,144,.025)}
.objective-panel .section-kicker{color:#e9c66f}.objective-panel .section-title{max-width:800px}.objective-panel p{max-width:720px;color:#e3d6b5}
footer{padding:35px 34px;border-top:1px solid var(--line);color:#83765c;font-size:.8rem}
.footer-inner{max-width:var(--max);margin:auto;display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap}
#top-button{position:fixed;right:24px;bottom:24px;width:47px;height:47px;border:1px solid rgba(255,255,255,.55);border-radius:50%;background:linear-gradient(145deg,#c18c21,#8c5e0c);color:#fff;font-size:1.2rem;box-shadow:0 10px 25px rgba(133,91,14,.25);cursor:pointer;z-index:80;opacity:0;pointer-events:none;transform:translateY(12px);transition:opacity .3s,transform .3s}
#top-button.show{opacity:1;pointer-events:auto;transform:translateY(0)}
#music-toggle{position:fixed;right:24px;bottom:82px;z-index:90;display:flex;align-items:center;gap:9px;border:1px solid rgba(189,135,34,.35);border-radius:999px;padding:11px 15px;background:rgba(255,254,248,.88);backdrop-filter:blur(14px);color:#76500c;font:600 .78rem Inter,"Segoe UI",Arial,sans-serif;box-shadow:0 10px 28px rgba(93,67,20,.12);cursor:pointer;transition:transform .25s,box-shadow .25s,background .25s}
#music-toggle:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(93,67,20,.17)}
#music-toggle .music-dot{width:7px;height:7px;border-radius:50%;background:#b98726;box-shadow:0 0 0 4px rgba(189,135,34,.12)}
#music-toggle.playing .music-dot{background:#4d8b58;box-shadow:0 0 0 4px rgba(77,139,88,.12);animation:musicPulse 1.8s ease-in-out infinite}
@keyframes musicPulse{50%{box-shadow:0 0 0 7px rgba(77,139,88,0)}}
@media(max-width:600px){#music-toggle{right:16px;bottom:76px;padding:10px 13px;font-size:.73rem}}
@keyframes stageFloat{0%,100%{transform:translateY(0) rotateX(0deg)}50%{transform:translateY(-12px) rotateX(2deg)}}
@keyframes glowBreathe{0%,100%{transform:scale(.92);opacity:.75}50%{transform:scale(1.08);opacity:1}}
@keyframes cardFloat{0%,100%{translate:0 0}50%{translate:0 -10px}}
@keyframes signal{from{height:5px}to{height:25px}}
@keyframes wheel{0%{transform:translateY(0);opacity:1}80%,100%{transform:translateY(9px);opacity:0}}
@keyframes orbit{to{transform:rotate(360deg)}}
@media(max-width:1000px){.hero-inner{grid-template-columns:1fr 1fr}.hero-visual{min-height:490px}.hero-index{display:none}.skills-grid{grid-template-columns:repeat(2,1fr)}.about-grid{gap:35px}.experience-layout{gap:30px}}
@media(max-width:760px){
 .nav-wrap{padding:14px 18px}.nav-cta{display:none}.menu-toggle{display:block}
 nav{display:none;position:absolute;top:100%;left:12px;right:12px;padding:14px;background:rgba(255,254,250,.96);backdrop-filter:blur(18px);border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);flex-direction:column;align-items:stretch;gap:3px}
 nav.open{display:flex}nav a{padding:10px 12px}
 .hero{padding:105px 22px 75px;min-height:auto}.hero-inner{grid-template-columns:1fr;gap:0}.hero-copy{padding:35px 0 0}.hero h1{font-size:clamp(3.2rem,15vw,5.4rem)}.hero-visual{min-height:360px;margin-top:-8px}.chip-stage{width:100%;max-width:500px}.float-card{padding:10px 12px;font-size:.65rem}.float-card.one{left:0}.float-card.two{right:0}.float-card.three{left:4%}.scroll-cue{left:22px;bottom:20px}
 .section{padding:78px 22px}.about-grid,.education-grid,.experience-layout{grid-template-columns:1fr}.portrait-card{min-height:350px;max-width:480px;width:100%;margin:auto}.stats{margin:22px 0}.education-grid{gap:28px}.experience-layout{gap:25px}.experience-card{grid-template-columns:1fr;gap:7px}.skills-grid{gap:10px}.skill-card{padding:17px;min-height:140px}.footer-inner{flex-direction:column}
}
@media(max-width:420px){.brand{font-size:.7rem;letter-spacing:2px}.hero-actions .btn{width:100%}.hero-visual{min-height:310px}.float-card.two{top:18%}.float-card.three{bottom:5%}.skills-grid{grid-template-columns:1fr 1fr}.skill-card{min-height:145px}.section-title{font-size:2.3rem}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}.reveal{opacity:1;transform:none;filter:none}}
</style>
</head>
<body>
<div id="progress" aria-hidden="true"></div>
<header id="site-header">
 <div class="nav-wrap">
  <a class="brand" href="#home" aria-label="Nikhil Thakre home"><span class="brand-mark">ϟ</span><b>NIKHIL <span>THAKRE</span></b></a>
  <button class="menu-toggle" id="menu-toggle" aria-label="Open navigation" aria-expanded="false">☰</button>
  <nav id="main-nav" aria-label="Main navigation">
   <a href="#home" class="active">Home</a><a href="#about">About</a><a href="#education">Education</a><a href="#skills">Skills</a><a href="#experience">Experience</a><a href="#objective">Objective</a>
  </nav>
  <a class="nav-cta" href="#experience"><span>↘</span> Explore Profile</a>
 </div>
</header>

<section class="hero" id="home">
 <div class="hero-inner">
  <div class="hero-copy">
   <div class="pill">Electronics · Technology · Innovation</div>
   <h1>NIKHIL<br><span class="gold-text">THAKRE</span></h1>
   <div class="hero-subtitle">Building a smarter tomorrow<br>with technology</div>
   <div class="gold-rule"></div>
   <p class="hero-desc">An Electronics & Telecommunication diploma holder and Computer Science Engineering student, interested in technology, industrial automation and practical problem-solving.</p>
   <div class="hero-actions"><a class="btn gold" href="#about">Discover My Profile <span>↗</span></a><a class="btn light" href="#experience">View Experience</a></div>
   <div class="socials"><a href="#skills">Technical Skills</a><a href="#education">Education</a><a href="#objective">Career Goal</a></div>
  </div>
  <div class="hero-visual" aria-label="Decorative gold electronics microchip illustration">
   <div class="visual-glow"></div>
   <div class="chip-stage">
    <svg class="circuit-svg" viewBox="0 0 700 600" fill="none" aria-hidden="true">
     <defs><linearGradient id="wire" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f7df9b"/><stop offset=".55" stop-color="#c28b1e"/><stop offset="1" stop-color="#fff1bd"/></linearGradient><filter id="softGlow"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
     <g stroke="url(#wire)" stroke-width="2" opacity=".9" filter="url(#softGlow)">
      <path d="M350 300 L350 65 L220 65 L170 115 L70 115"/><path d="M355 310 L580 310 L620 270 L660 270"/><path d="M335 340 L260 415 L260 480 L160 480"/><path d="M400 340 L470 410 L570 410 L625 465"/><path d="M305 280 L210 185 L110 185"/><path d="M415 270 L500 190 L610 190"/><path d="M320 375 L320 500 L380 545"/><path d="M435 320 L530 365 L640 365"/>
     </g>
     <g fill="#fff3bd" stroke="#c18b20" stroke-width="2"><circle cx="70" cy="115" r="5"/><circle cx="660" cy="270" r="5"/><circle cx="160" cy="480" r="5"/><circle cx="625" cy="465" r="5"/><circle cx="110" cy="185" r="5"/><circle cx="610" cy="190" r="5"/><circle cx="380" cy="545" r="5"/><circle cx="640" cy="365" r="5"/></g>
     <path d="M90 300 C140 240 210 240 270 300 S410 365 475 300 S575 235 630 290" stroke="#edc45c" stroke-width="1.5" stroke-dasharray="5 8" opacity=".75"/>
    </svg>
    <div class="chip">
     <span class="pin top"></span><span class="pin bottom"></span><span class="pin left"></span><span class="pin right"></span>
     <div class="chip-label"><strong>NT / 01</strong>Electronics<br> & Technology</div>
    </div>
    <div class="float-card one"><strong>01 / HARDWARE</strong>Circuits · Components · Systems</div>
    <div class="float-card two"><strong>LIVE SIGNAL</strong>System status <span style="color:#9b751d">● Online</span><div class="signal"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
    <div class="float-card three"><strong>ENGINEERING MINDSET</strong>Learn · Build · Improve</div>
   </div>
  </div>
 </div>
 <div class="hero-index"><span>01</span><span>02</span><span>03</span><span>04</span></div>
 <div class="scroll-cue"><span></span> Scroll to explore</div>
</section>

<main>
<section class="section about-section" id="about">
 <div class="section-inner about-grid reveal">
  <div class="portrait-card"><div class="portrait-initials">NT</div><div class="portrait-note"><strong>Nikhil Thakre</strong>Electronics · Operations · Technology</div></div>
  <div class="about-copy">
   <div class="section-kicker">01 / About me</div>
   <h2 class="section-title">Turning ideas into<br><span>practical solutions.</span></h2>
   <p>I am an Electronics and Telecommunication diploma holder and a Computer Science Engineering student with industrial experience in operations, inventory management and SAP MM.</p>
   <p>I am interested in electronics, information technology, industrial automation, IoT and cybersecurity. I enjoy learning how hardware, software and real-world operations work together.</p>
   <div class="stats"><div class="stat"><strong>69.20%</strong><span>Diploma score</span></div><div class="stat"><strong>2</strong><span>Technical pathways</span></div><div class="stat"><strong>∞</strong><span>Curiosity to learn</span></div></div>
   <a class="btn gold" href="#skills">Explore My Skills <span>↗</span></a>
  </div>
 </div>
</section>

<section class="section" id="education">
 <div class="section-inner education-grid reveal">
  <div><div class="section-kicker">02 / Education</div><h2 class="section-title">A foundation built<br>on <span>curiosity.</span></h2><p class="section-intro">My academic journey combines electronics fundamentals with ongoing computer science studies.</p></div>
  <div class="education-card">
   <div class="edu-top"><div class="edu-icon">✦</div><div><h3>Diploma in Electronics & Telecommunication Engineering</h3><p>Government Polytechnic, Nagpur</p><p>Final percentage: 69.20%</p><span class="edu-year">COMPLETED · 2025</span></div></div>
   <hr style="border:0;border-top:1px solid var(--line);margin:25px 0">
   <div class="edu-top"><div class="edu-icon">⌘</div><div><h3>B.Tech in Computer Science Engineering</h3><p>Direct Second Year (DSY)</p><p>Second year completed</p><span class="edu-year">COMPUTER SCIENCE</span></div></div>
  </div>
 </div>
</section>

<section class="section skills-section" id="skills">
 <div class="section-inner reveal">
  <div class="section-kicker">03 / Capabilities</div><h2 class="section-title">Tools I use.<br><span>Skills I build.</span></h2>
  <p class="section-intro">A growing set of practical skills across industrial operations, electronics and technology.</p>
  <div class="skills-grid">
   <article class="skill-card"><div class="skill-icon">⌘</div><h3>SAP MM</h3><p>Material movement and stock management</p></article>
   <article class="skill-card"><div class="skill-icon">▦</div><h3>Microsoft Excel</h3><p>Reporting, data handling and documentation</p></article>
   <article class="skill-card"><div class="skill-icon">ϟ</div><h3>Electronics</h3><p>Electronics fundamentals and troubleshooting</p></article>
   <article class="skill-card"><div class="skill-icon">⌁</div><h3>Industrial Automation</h3><p>Automation concepts and control systems</p></article>
   <article class="skill-card"><div class="skill-icon">◉</div><h3>IoT</h3><p>Connected devices and sensor concepts</p></article>
   <article class="skill-card"><div class="skill-icon">⌬</div><h3>Cybersecurity</h3><p>Foundational security concepts</p></article>
   <article class="skill-card"><div class="skill-icon">▤</div><h3>Inventory Control</h3><p>Receiving, tracking and stock accuracy</p></article>
   <article class="skill-card"><div class="skill-icon">↗</div><h3>Coordination</h3><p>Team communication and operations</p></article>
  </div>
 </div>
</section>

<section class="section" id="experience">
 <div class="section-inner experience-layout reveal">
  <div><div class="section-kicker">04 / Experience</div><h2 class="section-title">Real work.<br><span>Real learning.</span></h2><p class="section-intro">Industrial experience with a focus on store operations, inventory accuracy, systems and team coordination.</p></div>
  <div class="experience-list">
   <article class="experience-card"><div class="experience-date">INDUSTRY<br>OPERATIONS</div><div><h3>Supervisor Operations · Mahindra Logistics</h3><p>Store operations and material management in an industrial environment.</p><ul><li>Material receiving, quantity checks and inventory control.</li><li>SAP MM and stock management.</li><li>MS Excel reporting, documentation and dispatch coordination.</li><li>Store operations and team coordination.</li></ul></div></article>
   <article class="experience-card"><div class="experience-date">TECHNICAL<br>TRAINING</div><div><h3>Industrial Automation & IoT Exposure</h3><p>Training exposure to Arduino, ESP32, sensors, IoT concepts and automation projects.</p></div></article>
  </div>
 </div>
</section>

<section class="section" id="objective">
 <div class="section-inner reveal"><div class="objective-panel"><div class="section-kicker">05 / The direction</div><h2 class="section-title">Built to learn.<br>Driven to <span>make an impact.</span></h2><p>To build a career in electronics, information technology and industrial automation by applying my technical knowledge, practical experience and problem-solving skills while continuously learning new technologies.</p><a class="btn gold" href="#home">Back to the beginning ↑</a></div></div>
</section>
</main>

<footer><div class="footer-inner"><span>© 2026 Nikhil Thakre. Personal portfolio.</span><span>Designed with precision · Electronics × Technology</span></div></footer>
<button id="music-toggle" type="button" aria-pressed="false" aria-label="Play soft piano music"><span class="music-dot"></span><span id="music-label">Play piano</span> ♫</button>
<button id="top-button" aria-label="Back to top" title="Back to top">↑</button>

<script>
(() => {
 const header=document.getElementById('site-header');
 const progress=document.getElementById('progress');
 const topButton=document.getElementById('top-button');
 const nav=document.getElementById('main-nav');
 const menuToggle=document.getElementById('menu-toggle');
 const musicToggle=document.getElementById('music-toggle');
 const musicLabel=document.getElementById('music-label');
 const navLinks=[...nav.querySelectorAll('a')];
 const sections=[...document.querySelectorAll('main section[id]')];

 const reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

 // A quiet, piano-inspired ambient score made with Web Audio. Browsers require
 // a user gesture before audible playback, so music starts when the visitor taps.
 let audioContext=null, masterGain=null, musicTimer=null, musicOn=false, noteIndex=0;
 const pianoProgression=[
   [261.63,329.63,392.00,493.88], // Cmaj7
   [220.00,261.63,329.63,392.00], // Am7
   [174.61,220.00,261.63,329.63], // Fmaj7
   [196.00,246.94,293.66,392.00]  // G6
 ];
 function pianoNote(frequency, startAt, duration){
   if(!audioContext || !masterGain) return;
   const fundamental=audioContext.createOscillator();
   const body=audioContext.createOscillator();
   const noteGain=audioContext.createGain();
   const tone=audioContext.createBiquadFilter();
   fundamental.type='triangle'; fundamental.frequency.value=frequency;
   body.type='sine'; body.frequency.value=frequency*2.01;
   tone.type='lowpass'; tone.frequency.value=2600; tone.Q.value=.5;
   noteGain.gain.setValueAtTime(.0001,startAt);
   noteGain.gain.exponentialRampToValueAtTime(.12,startAt+.012);
   noteGain.gain.exponentialRampToValueAtTime(.0001,startAt+duration);
   fundamental.connect(tone); body.connect(tone); tone.connect(noteGain); noteGain.connect(masterGain);
   fundamental.start(startAt); body.start(startAt);
   fundamental.stop(startAt+duration+.03); body.stop(startAt+duration+.03);
 }
 function schedulePiano(){
   if(!musicOn || !audioContext) return;
   const chord=pianoProgression[Math.floor(noteIndex/4)%pianoProgression.length];
   const note=chord[noteIndex%4];
   const now=audioContext.currentTime+.03;
   pianoNote(note,now,2.7);
   if(noteIndex%4===0) pianoNote(chord[0]/2,now,3.2);
   noteIndex++;
 }
 async function startPiano(){
   try{
     const AudioCtx=window.AudioContext||window.webkitAudioContext;
     if(!AudioCtx) throw new Error('Audio is not supported in this browser.');
     if(!audioContext){audioContext=new AudioCtx();masterGain=audioContext.createGain();masterGain.gain.value=.22;masterGain.connect(audioContext.destination);}
     await audioContext.resume();
     if(musicOn) return;
     musicOn=true; noteIndex=0;
     schedulePiano(); musicTimer=window.setInterval(schedulePiano,680);
     musicToggle.classList.add('playing');musicToggle.setAttribute('aria-pressed','true');
     musicToggle.setAttribute('aria-label','Turn piano music off');musicLabel.textContent='Piano playing';
   }catch(error){musicLabel.textContent='Audio unavailable';window.setTimeout(()=>{musicLabel.textContent='Play piano';},2200);}
 }
 function stopPiano(){
   musicOn=false;if(musicTimer){window.clearInterval(musicTimer);musicTimer=null;}
   if(masterGain && audioContext){masterGain.gain.setTargetAtTime(.0001,audioContext.currentTime,.08);}
   musicToggle.classList.remove('playing');musicToggle.setAttribute('aria-pressed','false');
   musicToggle.setAttribute('aria-label','Play soft piano music');musicLabel.textContent='Play piano';
   // Restore the quiet default level for the next time the visitor presses play.
   if(masterGain && audioContext){window.setTimeout(()=>{if(!musicOn)masterGain.gain.value=.22;},350);}
 }
 musicToggle.addEventListener('click',()=>musicOn?stopPiano():startPiano());

 menuToggle.addEventListener('click',()=>{
   const open=nav.classList.toggle('open');
   menuToggle.setAttribute('aria-expanded',String(open));
   menuToggle.textContent=open?'×':'☰';
 });
 navLinks.forEach(link=>link.addEventListener('click',()=>{nav.classList.remove('open');menuToggle.setAttribute('aria-expanded','false');menuToggle.textContent='☰';}));

 function updateScrollUI(){
   const maxScroll=document.documentElement.scrollHeight-window.innerHeight;
   const ratio=maxScroll>0?window.scrollY/maxScroll:0;
   progress.style.transform=`scaleX(${ratio})`;
   header.classList.toggle('scrolled',window.scrollY>24);
   topButton.classList.toggle('show',window.scrollY>550);
 }
 window.addEventListener('scroll',updateScrollUI,{passive:true});
 updateScrollUI();
 topButton.addEventListener('click',()=>document.getElementById('home').scrollIntoView({behavior:reduceMotion?'auto':'smooth'}));

 if('IntersectionObserver' in window){
   const revealObserver=new IntersectionObserver(entries=>{
     entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');revealObserver.unobserve(entry.target);}});
   },{threshold:.12,rootMargin:'0px 0px -45px 0px'});
   document.querySelectorAll('.reveal').forEach(el=>revealObserver.observe(el));

   const activeObserver=new IntersectionObserver(entries=>{
     const candidates=entries.filter(e=>e.isIntersecting).sort((a,b)=>b.intersectionRatio-a.intersectionRatio);
     if(candidates.length){
       const id=candidates[0].target.id;
       navLinks.forEach(link=>link.classList.toggle('active',link.getAttribute('href')==='#'+id));
     }
   },{rootMargin:'-25% 0px -60% 0px',threshold:[0,.1,.25,.5]});
   sections.forEach(section=>activeObserver.observe(section));
 }else{
   document.querySelectorAll('.reveal').forEach(el=>el.classList.add('visible'));
 }

 // Gentle cursor-responsive tilt on the hero chip. Disabled for touch and reduced motion.
 const stage=document.querySelector('.chip-stage');
 if(stage && !reduceMotion && window.matchMedia('(pointer:fine)').matches){
   const visual=stage.parentElement;
   visual.addEventListener('pointermove',e=>{
     const r=visual.getBoundingClientRect();
     const x=(e.clientX-r.left)/r.width-.5;
     const y=(e.clientY-r.top)/r.height-.5;
     stage.style.animationPlayState='paused';
     stage.style.transform=`translate3d(${x*10}px,${y*8}px,0) rotateX(${-y*3}deg) rotateY(${x*4}deg)`;
   });
   visual.addEventListener('pointerleave',()=>{stage.style.transform='';stage.style.animationPlayState='running';});
 }
})();
</script>
</body>
</html>
"""

class PortfolioHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass

def open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}")

if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), PortfolioHandler)
    print("Nikhil Thakre Premium Portfolio is running!")
    print(f"Open: http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    Timer(1, open_browser).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nWebsite stopped.")
        server.server_close()