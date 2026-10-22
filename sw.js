const CACHE = 'jovem-parlamentar-v1';
const FILES = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-maskable-192.png', './icon-maskable-512.png', './apple-touch-icon.png', './favicon-32.png', './fontes/bebas-neue.woff2', './fontes/montserrat.woff2'];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key !== CACHE).map(key => caches.delete(key)))).then(() => self.clients.claim()));
});
// Abre na hora com a cópia guardada e, ao mesmo tempo, busca a versão nova
// na internet para a próxima abertura (estratégia "stale-while-revalidate").
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET' || new URL(event.request.url).origin !== self.location.origin) return;
  event.respondWith(caches.open(CACHE).then(cache => cache.match(event.request, { ignoreSearch: true }).then(cached => {
    const rede = fetch(event.request).then(response => {
      if (response.ok) cache.put(event.request, response.clone());
      return response;
    }).catch(() => cached || cache.match('./index.html'));
    if (cached) { event.waitUntil(rede.catch(() => {})); return cached; }
    return rede;
  })));
});
