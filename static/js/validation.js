// //login form validation
// const form = document.querySelector('form'),
// eField = form.querySelector('.email'),
// eInput = eField.querySelector('input'),
// pField = form.querySelector('.password'),
// pInput = pField.querySelector('input');

// form.onsubmit = (e)=>{
//     e.preventDefault();

//     if(eInput.value == ''){
//         eField.classList.add('shake', 'error');
//     }else{
//         checkEmail();
//     }
//     if(pInput.value == ''){
//         pField.classList.add('shake','error');
//     }

//     setTimeout(()=>{//to remove shake after 500ms
//         eField.classList.remove('shake');
//         pField.classList.remove('shake');
//     },500);
    

//     eInput.onkeyup = ()=>{
//         checkEmail();
//     }

//     function checkEmail(){
//         let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
//         if(!eInput.value.match(pattern)){
//             eField.classList.add("error");
//             let errortxt = eField.querySelector('.error-txt');
//             (eInput.value != "") ? errortxt.innerHTML = 'Enter a valid email address': errortxt.innerHTML = "email can'tbe blank";
//         }else{
//             eField.classList.remove("error");
//         }
//     }

//     pInput.onkeyup = ()=>{
//     if(pInput.value == ''){
//         pField.classList.add("error");
//     }else{
//         pField.classList.remove("error");
//     }
// }



// if(!eField.classList.contains('error') && !pField.classList.contains('error')){
//     window.location.href = "#"; //#to removed and replaced with the url to where the submission will be done
//     //alternative link on the action section in the form and replace the above # with .href = form.getAttribute("action");
// }
// }

// // end of form of login validations