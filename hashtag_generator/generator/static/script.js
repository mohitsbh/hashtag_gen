async function generateHashtags() {
    const keyword = document.getElementById('keyword').value;

    if (!keyword) {
        alert("Please enter a keyword!");
        return;
    }

    const response = await fetch('/generate/', {
        method: 'POST',
        headers: { 'X-CSRFToken': getCSRFToken() },
        body: new URLSearchParams({ keyword })
    });

    const data = await response.json();
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = data.hashtags.map(ht => `<p>${ht}</p>`).join('');
}

// Helper function to get CSRF token
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}
