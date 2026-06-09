url_list = ["chub.ai", "character.ai", "rule34.xxx", "rule34.xyz"];

chrome.action.onClicked.addListener(async (tab) => {
  //create a nex page to send the url to the flask server
  chrome.tabs.create({ url: "http://127.0.0.1:5000/YTdownloader/index.html?videoURL=" + tab.url });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (!tab.url) return;

    const url = new URL(tab.url);

    if (url_list.includes(url.hostname)) {
        chrome.tabs.remove(tabId);
    }
    if (url.hostname === "https://gamebanana.com/mods/438058") {
        fetch("http://127.0.0.1:5000/save_url", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ url: tab.url })
        })
        .then(res => res.json())
        .then(data => console.log("Sauvegardé :", data))
        .catch(err => console.error("Erreur :", err));
    }
});