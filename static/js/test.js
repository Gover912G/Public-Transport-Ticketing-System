// const form = document.getElementById('form');
// const username = document.getElementById('username');
// const email = document.getElementById('email');
// const phone = document.getElementById('phone');
// const password = document.getElementById('password');
// const password2 = document.getElementById('password2');

// form.addEventListener('submit', e => {
//     e.preventDefault();

//     validateInputs();
// });

// const setError = (element, message) => {
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay.innerText = message;
//     inputControl.classList.add('error');
//     inputControl.classList.remove('success');
// }

// const setSuccess = element => {
//     const inputControl = element.parentElement;
//     const errorDisplay = inputControl.querySelector('.error');

//     errorDisplay = '';
//     inputControl.classList.add('success');
//     inputControl.classList.remove('error');
// };


// const isValidEmail = email => {
//     const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//     return re.test(String(email).toLowerCase());
// }


// const validateInputs = () => {
//     const usernameValue = username.value.trim();
//     const emailValue = email.value.trim();
//     const phoneValue = phone.value.trim();
//     const passwordValue = password.value.trim();
//     const password2Value = password2.value.trim();

//     if (usernameValue === '') {
//         setError(username, 'username is required');
//     } else {
//         setSuccess(username);
//     }

//     if (emailValue === '') {
//         setError(email, "email is required");
//     } else if (!isValidEmail(emailValue)) {
//         setError(email, "Provide a valid email");
//     }else {
//         setSuccess(email);
//     }

//     if (phoneValue === '') {
//         setError(phone, 'enter your phone number');
//     } else {
//         setSuccess(phone);
//     }


//     if (passwordValue === '') {
//         setError(password, 'password cannot be empty');
//     } else if (passwordValue.length < 8) {
//         setError(password, 'password must contain atleast 8 characters');
//     } else {
//         setSuccess(password);
//     }

//     if (password2Value === '') {
//         setError(password2, 'please confirm your message');
//     } else if (password2Value !== passwordValue) {
//         setError(password2, 'passwords do not match');
//     } else {
//         setSuccess(password2);
//     }
// }




// // login js
