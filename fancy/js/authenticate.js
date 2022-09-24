const login = document.getElementById('login');

login.addEventListener('submit', function(e) {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    e.preventDefault();
    fetch("http://localhost:8000/api/v1/auth/login/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            password: password,
        })

}).then((response) => alert(response.json())).catch((error) => alert(error));
});