// background.js

const API_URL = "http://127.0.0.1:5001/api/translate/batch";

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'translateBatch') {
        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                texts: request.texts,
                source_lang: 'en',
                target_lang: request.targetLang
            })
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => sendResponse({ success: true, data: data }))
            .catch(error => {
                console.error("Translation request failed:", error);
                sendResponse({ success: false, error: error.message });
            });

        return true; // Keep message channel open for async response
    }
});
