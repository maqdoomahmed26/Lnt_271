// script.js
document.getElementById('login-form').addEventListener('Login.html', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    // Simple validation for demonstration purposes
    if (username === 'admin' && password === '123') {
        errorMessage.textContent = 'Login successful!';
        errorMessage.style.color = 'green';
        // Redirect or perform further actions here
    } else {
        errorMessage.textContent = 'Invalid username or password';
        errorMessage.style.color = 'red';
    }
});