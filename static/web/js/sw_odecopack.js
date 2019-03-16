importScripts('./cache-polyfill.js');

self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open('odecopack').then(function (cache) {
            return cache.addAll([
                './index.html'
            ]);
        })
    );
});

self.addEventListener('fetch', function (event) {
    console.log('siiii');
    console.log(event.request.url);
});
