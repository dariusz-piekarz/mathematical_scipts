/* One connection per live page, including background tabs. No unload beacon required. */
(() => {
  let socket=null, leaving=false, unmanaged=false, reconnect=null, failures=0;
  function connect(){
    if(leaving||unmanaged||socket?.readyState===WebSocket.OPEN||socket?.readyState===WebSocket.CONNECTING)return;
    clearTimeout(reconnect);
    const current=new WebSocket(`${location.protocol==='https:'?'wss':'ws'}://${location.host}/api/lifecycle/socket`);
    socket=current;
    current.onmessage=event=>{
      const message=JSON.parse(event.data);
      if(message.managed===false)unmanaged=true;
      else failures=0;
    };
    current.onclose=()=>{
      if(socket!==current)return;
      socket=null;
      if(leaving||unmanaged)return;
      if(failures++<5){reconnect=setTimeout(connect,Math.min(2000,250*2**failures));return;}
      const status=document.getElementById('dbStatus');
      if(status){status.textContent='Aplikacja zakończona — uruchom start.cmd';status.classList.remove('connected');}
    };
  }
  window.addEventListener('pagehide',()=>{
    leaving=true;clearTimeout(reconnect);
    socket?.close(1000,'Page closed');
  });
  window.addEventListener('pageshow',()=>{leaving=false;connect();});
  connect();
})();
