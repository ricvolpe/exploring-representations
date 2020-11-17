// Setup variables
var lastSwitch = localStorage.getItem('lastSwitch')
var lastTimeStamp = localStorage.getItem('lastTimeStamp')
var el = document.getElementById("darkSheet");
var now = new Date();

// If user never switch the ligth or did it more than 12 hours ago
// We switch the ligth on only before after 6am and before 6pm
if (lastSwitch == null | (now - lastTimeStamp) > 1000 * 60 * 60 * 12) {
   if (now.getHours() < 18 & now.getHours() > 7) {
      ligthsOn()
   } else {
      ligthsOff()
   }
} else if (lastSwitch == 'dark') {
   ligthsOff()
} else if (lastSwitch == 'ligth') {
   ligthsOn()
}

function ligthsOff() {
   el.disabled = false;
   document.getElementById("ligthSwitch").textContent="ligthsOn";
   localStorage.setItem('lastSwitch', 'dark');
}

function ligthsOn() {
   el.disabled = true;
   document.getElementById("ligthSwitch").textContent="ligthsOff";
   localStorage.setItem('lastSwitch', 'ligth');
}

function switchLigth() {
    if (el.disabled) {
      ligthsOff()
    } else {
      ligthsOn()
    }
    localStorage.setItem('lastTimeStamp', new Date().getTime());
}

// Matomo code
var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
   var u="https://analytics.volpato.io/";
   _paq.push(['setTrackerUrl', u+'matomo.php']);
   _paq.push(['setSiteId', '1']);
   var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
   g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
})();