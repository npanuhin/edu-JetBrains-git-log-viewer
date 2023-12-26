const endpoint = 'https://npanuhin.me:2096';

const container = document.getElementById('gitLog');

var messages;

fetch(endpoint)
    .then(response => response.text())
    .then(data => container.textContent = data)
    .catch(error => alert(`Error fetching Git log from server ${endpoint}`, error));
