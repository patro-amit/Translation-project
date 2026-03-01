// content.js

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'translatePage') {
        // Respond immediately so the popup UI updates
        sendResponse({ success: true });

        // Start the heavy translation workload in the background
        startTranslation(request.targetLang).catch(console.error);
        return false;
    }
});

async function startTranslation(targetLang) {
    console.log(`Starting translation to ${targetLang}`);

    // Elements we want to traverse
    const walker = document.createTreeWalker(
        document.body,
        NodeFilter.SHOW_TEXT,
        {
            acceptNode: function (node) {
                const parent = node.parentNode;
                // Skip style, script, noscript, code blocks, etc.
                if (parent && ['STYLE', 'SCRIPT', 'NOSCRIPT', 'CODE', 'PRE'].includes(parent.nodeName)) {
                    return NodeFilter.FILTER_REJECT;
                }
                // Skip empty text
                if (!node.nodeValue || !node.nodeValue.trim()) {
                    return NodeFilter.FILTER_SKIP;
                }
                // Skip text that is too short or doesn't have alphabetic characters
                if (node.nodeValue.trim().length < 2 || !/[a-zA-Z]/.test(node.nodeValue)) {
                    return NodeFilter.FILTER_SKIP;
                }
                return NodeFilter.FILTER_ACCEPT;
            }
        },
        false
    );

    let textNodes = [];
    let currentNode;
    while (currentNode = walker.nextNode()) {
        textNodes.push(currentNode);
    }

    console.log(`Found ${textNodes.length} text nodes to translate.`);

    // Translate in smaller batches so the user sees progress instead of waiting a minute for a massive batch
    const BATCH_SIZE = 10;
    for (let i = 0; i < textNodes.length; i += BATCH_SIZE) {
        const batchNodes = textNodes.slice(i, i + BATCH_SIZE);
        const originalTexts = batchNodes.map(node => node.nodeValue.trim());

        try {
            const translatedTexts = await translateBatch(originalTexts, targetLang);
            if (translatedTexts && translatedTexts.length === originalTexts.length) {
                for (let j = 0; j < batchNodes.length; j++) {
                    batchNodes[j].nodeValue = batchNodes[j].nodeValue.replace(originalTexts[j], translatedTexts[j]);
                }
            }
        } catch (e) {
            console.error("Translation error for batch", e);
        }
    }

    console.log("Translation complete for available nodes.");
}

function translateBatch(texts, targetLang) {
    return new Promise((resolve) => {
        chrome.runtime.sendMessage(
            { action: 'translateBatch', texts: texts, targetLang: targetLang },
            (response) => {
                if (chrome.runtime.lastError) {
                    console.error("Runtime error:", chrome.runtime.lastError.message);
                    resolve(null);
                } else if (response && response.success && response.data && response.data.translated_texts) {
                    resolve(response.data.translated_texts);
                } else {
                    if (response && response.error) {
                        console.error("Backend error:", response.error);
                    }
                    resolve(null);
                }
            }
        );
    });
}
