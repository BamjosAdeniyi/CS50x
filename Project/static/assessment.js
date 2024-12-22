// Array to hold questions
const questions = [];

// Function to initialize the assessment
function initializeAssessment(questionsData) {
    questions.push(...questionsData); // Populate the questions array

    // Get references to DOM elements
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    const questionContainers = document.querySelectorAll('.question-container');
    const progressDisplay = document.getElementById('progress');
    const alertMessage = document.getElementById('alertMessage');

    let currentIndex = 0; // Track the current question index

    // Function to update the progress display
    function updateProgress() {
        progressDisplay.textContent = `Question ${currentIndex + 1} of ${questionContainers.length}`;
    }

    // Function to update button states
    function updateButtons() {
        prevBtn.disabled = currentIndex === 0; // Disable "Previous" on the first question
        nextBtn.style.display = currentIndex === questionContainers.length - 1 ? 'none' : 'inline'; // Hide "Next" on the last question
        submitBtn.style.display = currentIndex === questionContainers.length - 1 ? 'inline' : 'none'; // Show "Submit" on the last question
    }

    // Event listener for "Previous" button
    prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
            questionContainers[currentIndex].classList.remove('active');
            currentIndex--;
            questionContainers[currentIndex].classList.add('active');
            alertMessage.style.display = 'none'; // Hide alert on navigating back
        }
        updateButtons();
        updateProgress();
    });

    // Event listener for "Next" button
    nextBtn.addEventListener('click', () => {
        // Ensure the current question is answered before proceeding
        const selectedOption = document.querySelector(`input[name="responses[${questions[currentIndex].id}]"]:checked`);
        if (!selectedOption) {
            alertMessage.style.display = 'block'; // Show alert if no option is selected
            return;
        } else {
            alertMessage.style.display = 'none'; // Hide alert if an option is selected
        }

        if (currentIndex < questionContainers.length - 1) {
            questionContainers[currentIndex].classList.remove('active');
            currentIndex++;
            questionContainers[currentIndex].classList.add('active');
        }
        updateButtons();
        updateProgress();
    });

    // Initial setup
    questionContainers[currentIndex].classList.add('active'); // Show the first question
    updateButtons();
    updateProgress();
}

// DOMContentLoaded listener to initialize the assessment
document.addEventListener('DOMContentLoaded', () => {
    const questionsDataElement = document.getElementById('questionsData');
    if (questionsDataElement) {
        const questionsData = JSON.parse(questionsDataElement.textContent); // Parse questions data
        console.log('Questions data:', questionsData); // Debugging output
        initializeAssessment(questionsData);
    } else {
        console.error('Questions data not found.');
    }
});

document.querySelector('form').addEventListener('submit', (event) => {
    console.log('Submitting form data:', new FormData(event.target));
});


document.querySelector('form').addEventListener('submit', (event) => {
    console.log('Submitting form data:', new FormData(event.target));
});

document.addEventListener("DOMContentLoaded", () => {
    const questions = document.querySelectorAll(".question-container");
    const progressBar = document.getElementById("progress-bar");
    const progressText = document.getElementById("progress");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const submitBtn = document.getElementById("submitBtn");
    const alertMessage = document.getElementById("alertMessage");

    let currentQuestionIndex = 0;
    const totalQuestions = questions.length;

    // Object to store user responses temporarily
    const responses = {};

    function updateProgressBar() {
        const percentage = ((currentQuestionIndex + 1) / totalQuestions) * 100;
        progressBar.style.width = `${percentage}%`;
        progressBar.textContent = `${Math.round(percentage)}%`;
        progressText.textContent = `Question ${currentQuestionIndex + 1} of ${totalQuestions}`;
    }

    function updateButtons() {
        prevBtn.disabled = currentQuestionIndex === 0;
        nextBtn.style.display = currentQuestionIndex === totalQuestions - 1 ? "none" : "inline-block";
        submitBtn.style.display = currentQuestionIndex === totalQuestions - 1 ? "inline-block" : "none";
    }

    function showQuestion(index) {
        questions.forEach((question, i) => {
            question.classList.toggle("active", i === index);
            if (i === index) {
                restoreResponse(question); // Restore response when question becomes active
            }
        });
        updateProgressBar();
        updateButtons();
        alertMessage.style.display = "none"; // Hide alert message when question changes
    }

    function isOptionSelected() {
        const currentQuestion = questions[currentQuestionIndex];
        const options = currentQuestion.querySelectorAll("input[type='radio']");
        return [...options].some((option) => option.checked);
    }

    function saveResponse() {
        const currentQuestion = questions[currentQuestionIndex];
        const options = currentQuestion.querySelectorAll("input[type='radio']");
        options.forEach((option) => {
            if (option.checked) {
                responses[currentQuestion.dataset.index] = option.value; // Save selected value
            }
        });
    }

    function restoreResponse(question) {
        const index = question.dataset.index;
        const savedValue = responses[index];
        if (savedValue) {
            const options = question.querySelectorAll("input[type='radio']");
            options.forEach((option) => {
                option.checked = option.value === savedValue; // Restore the saved value
            });
        }
    }

    prevBtn.addEventListener("click", () => {
        saveResponse(); // Save response before navigating
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            showQuestion(currentQuestionIndex);
        }
    });

    nextBtn.addEventListener("click", () => {
        if (isOptionSelected()) {
            saveResponse(); // Save response before navigating
            if (currentQuestionIndex < totalQuestions - 1) {
                currentQuestionIndex++;
                showQuestion(currentQuestionIndex);
            }
        } else {
            alertMessage.style.display = "block"; // Show alert message
        }
    });

    // Initialize
    showQuestion(currentQuestionIndex);
});
