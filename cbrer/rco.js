arr = Array.prototype.slice.call(document.querySelectorAll('img')).filter(img=>img.style.length==0 && img.className=="")
urls = arr.map(img=>img.src).filter(url=>url.indexOf('gif')==-1) .reduce((a,b)=>a+' '+b, '')
console.log(urls.slice(1))
