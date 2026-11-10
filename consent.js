/* Çerez onayı + Google Analytics (yalnızca onay verilirse yüklenir) */
(function(){
  var GA='G-3ZNSB7R3Q5', KEY='lt_cerez';
  function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
  function set(v){try{localStorage.setItem(KEY,v)}catch(e){}}
  function loadGA(){
    if(window.__ltga)return;window.__ltga=1;
    var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id='+GA;document.head.appendChild(s);
    window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
    gtag('js',new Date());gtag('config',GA,{anonymize_ip:true});
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a');if(!a||!window.gtag)return;
    var h=a.getAttribute('href')||'';
    if(h.indexOf('wa.me')>-1)gtag('event','whatsapp_click',{page_path:location.pathname});
    else if(h.indexOf('tel:')===0)gtag('event','phone_click',{page_path:location.pathname});
    else if(h.indexOf('kristaldisdeposu.com')>-1)gtag('event','kristal_click',{link_url:h,page_path:location.pathname});
  },true);
  var c=get();
  if(c==='evet'){loadGA();return}
  if(c==='hayir')return;
  function banner(){
    var d=document.createElement('div');d.className='cerez';d.setAttribute('role','dialog');d.setAttribute('aria-label','Çerez bildirimi');
    d.innerHTML='<p>Sitenin nasıl kullanıldığını anlamak için, onay verirseniz Google Analytics çerezlerini kullanıyoruz. Onay vermezseniz analiz çerezi kullanılmaz.</p><div><button type="button" data-v="hayir">Reddet</button><button type="button" data-v="evet">Kabul et</button></div>';
    d.addEventListener('click',function(e){var v=e.target.getAttribute&&e.target.getAttribute('data-v');if(!v)return;set(v);d.remove();if(v==='evet')loadGA();});
    document.body.appendChild(d);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',banner);else banner();
})();
