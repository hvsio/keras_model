var urls = [];
var count = 0;
[...document.querySelectorAll('.rg_i')].forEach((element, index) => {
    let el = element.parentElement.parentElement;
    el.click();
    count++;
    setTimeout(() => {
        let google_url = el.href;

        let start = google_url.indexOf('=', google_url.indexOf('imgurl')) + 1;
        let encoded = google_url.substring(start, google_url.indexOf('&', start));
        let url = decodeURIComponent(encoded);
        urls.push(url);
        console.log(count);
        if (--count == 0) {
            let textToSave = urls.join('\n');
            let hiddenElement = document.createElement('a');
            hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
            hiddenElement.target = '_blank';
            hiddenElement.download = 'urls.txt';
            hiddenElement.click();
        }

    }, 50);

});