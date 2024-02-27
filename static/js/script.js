// Access the Testimonials

let testSlide = document.querySelectorAll('.testItem');

// Access the indicators
let dots = document.querySelectorAll('.dot');

var counter = 0;

// Adding click event to the indicators

function switchText(currentTest) {
    currentTest.classList.add('active');
    var testId = currentTest.getAttribute('attr');
    if (testId > counter) {
        testSlide[counter].style.animation = 'next1 0.5s ease-in forwards';
        counter = testId;
        testSlide[counter].style.animation = 'next2 0.5s ease-in forwards';

    }
    else if (testId == counter) { return; }
    else {
        testSlide[counter].style.animation = 'prev1 0.5s ease-in forwards';
        counter = testId;
        testSlide[counter].style.animation = 'prev2 0.5s ease-in forwards';

    }
    indicators();
}

// add and remove active class from indicators

function indicators() {
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(' active', '');
    }
    dots[counter].className += ' active';
}

// code for auto sliding

function slideNext() {
    testSlide[counter].style.animation = 'next1 0.5s ease-in forwards';
    if (counter >= testSlide.length - 1) {
        counter = 0;
    }
    else {
        counter++
    }
    testSlide[counter].style.animation = 'next2 0.5s ease-in forwards';

}
function autoSliding() {
    deleteInterval = setInterval(timer, 2000);
    function timer() {
        slideNext();
        indicators();
    }
}
autoSliding();

// Stop auto sliding when mouse is over the indicators
const container = document.querySelector('.indicators');
container.addEventListener('mouseover', pause);
function pause() {
    clearInterval(deleteInterval);
}

//  Resume sliding when mouse is out of the indicators
container.addEventListener('mouseout', autoSliding);




