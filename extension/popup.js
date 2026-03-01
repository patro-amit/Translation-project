document.addEventListener('DOMContentLoaded', () => {
    const translateBtn = document.getElementById('translateBtn');
    const targetLangSelect = document.getElementById('targetLang');
    const statusEl = document.getElementById('status');
    const btnText = translateBtn.querySelector('.btn-text');
    const loader = translateBtn.querySelector('.loader');

    // Load saved preference
    chrome.storage.local.get(['targetLang'], (result) => {
        if (result.targetLang) {
            targetLangSelect.value = result.targetLang;
        }
    });

    translateBtn.addEventListener('click', async () => {
        const targetLang = targetLangSelect.value;

        // Save preference
        chrome.storage.local.set({ targetLang });

        // UI update
        btnText.textContent = 'Translating...';
        loader.style.display = 'block';
        translateBtn.disabled = true;
        statusEl.textContent = 'Contacting content script...';
        statusEl.className = 'status-message';

        try {
            // Send a message to the active tab's content script to start translation
            const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

            if (!tab) throw new Error("No active tab found");

            // Check if it's a restricted page
            if (tab.url.startsWith('chrome://') || tab.url.startsWith('edge://') || tab.url.startsWith('about:')) {
                throw new Error("Cannot translate browser internal pages.");
            }

            chrome.tabs.sendMessage(tab.id, {
                action: 'translatePage',
                targetLang: targetLang
            }, (response) => {
                if (chrome.runtime.lastError) {
                    // Content script might not be injected
                    statusEl.textContent = 'Error: Refresh the page and try again.';
                    statusEl.className = 'status-message error';
                } else if (response && response.success) {
                    statusEl.textContent = 'Translation started! Check the page.';
                    statusEl.className = 'status-message success';
                } else {
                    const errorMsg = response ? response.error : 'Unknown error';
                    statusEl.textContent = `Error: ${errorMsg}`;
                    statusEl.className = 'status-message error';
                }

                // Reset UI
                btnText.textContent = 'Translate Page';
                loader.style.display = 'none';
                translateBtn.disabled = false;
            });

        } catch (err) {
            statusEl.textContent = `Error: ${err.message}`;
            statusEl.className = 'status-message error';
            btnText.textContent = 'Translate Page';
            loader.style.display = 'none';
            translateBtn.disabled = false;
        }
    });
});
