import { input_loader } from './input_loader.js';

const form = document.querySelector('form');
const results = document.querySelector('#results');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Retrieve user input
    const input_data = await input_loader();
    const age = parseInt(document.querySelector('#age').value);
    const sex = document.querySelector('#sex').value;
    const chestPainType = document.querySelector('#chest-pain').value;
    const restingBP = parseInt(document.querySelector('#resting-bp').value);
    const cholesterol = parseInt(document.querySelector('#cholesterol').value);
    const fastingBS = parseInt(document.querySelector('#fasting-bs').value);
    const restingECG = document.querySelector('#resting-ecg').value;
    const maxHR = parseInt(document.querySelector('#max-hr').value);
    const exerciseAngina = parseInt(document.querySelector('#exercise-angina').value);
    const oldpeak = parseFloat(document.querySelector('#oldpeak').value);
    const stSlope = document.querySelector('#st-slope').value;

    // Validate user input
    const errorMessage = document.querySelector('#error-message');
    errorMessage.innerHTML = '';

    if (isNaN(age) || age < 1 || age > 120) {
        errorMessage.innerHTML = 'Age must be a number between 1 and 120';
        return;
    }

    if (sex !== 'male' && sex !== 'female') {
        errorMessage.innerHTML = 'Please select a valid sex';
        return;
    }

    if (chestPainType !== 'typical-angina' && chestPainType !== 'atypical-angina' && chestPainType !== 'non-anginal-pain' && chestPainType !== 'asymptomatic') {
        errorMessage.innerHTML = 'Please select a valid chest pain type';
        return;
    }

    if (isNaN(restingBP) || restingBP < 80 || restingBP > 200) {
        errorMessage.innerHTML = 'Resting blood pressure must be a number between 80 and 200';
        return;
    }

    if (isNaN(cholesterol) || cholesterol < 100 || cholesterol > 600) {
        errorMessage.innerHTML = 'Cholesterol must be a number between 100 and 600';
        return;
    }

    if (fastingBS !== 0 && fastingBS !== 1) {
        errorMessage.innerHTML = 'Please select a valid fasting blood sugar value';
        return;
    }

    if (restingECG !== 'normal' && restingECG !== 'st-t-wave-abnormality' && restingECG !== 'left-ventricular-hypertrophy') {
        errorMessage.innerHTML = 'Please select a valid resting ECG value';
        return;
    }

    if (isNaN(maxHR) || maxHR < 60 || maxHR > 220) {
        errorMessage.innerHTML = 'Maximum heart rate must be a number between 60 and 220';
        return;
    }

    if (exerciseAngina !== 0 && exerciseAngina !== 1) {
        errorMessage.innerHTML = 'Please select a valid exercise-induced angina value';
        return;
    }

    if (isNaN(oldpeak) || oldpeak < 0 || oldpeak > 10) {
        errorMessage.innerHTML = 'ST depression must be a number between 0 and 10';
        return;
    }

    if (stSlope !== 'up-sloping' && stSlope !== 'flat' && stSlope !== 'down-sloping') {
        errorMessage.innerHTML = 'Please select a valid ST slope value';
        return;
    }

    // Prepare data for prediction
    const data = {
        age,
        sex,
        chestPainType,
        restingBP,
        cholesterol,
        fastingBS,
        restingECG,
        maxHR,
        exerciseAngina,
        oldpeak,
        stSlope
    };

// Send data to server for prediction
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(input_data)
        });
        if (!response.ok) {
            throw new Error('Server error');
        }

        const prediction = await response.json();

        // Display prediction results
        results.innerHTML = `<p>Based on the input data, the predicted probability of having heart disease is ${prediction.probability.toFixed(2)}.</p>
        <p>The model's prediction is ${prediction.prediction ? 'positive' : 'negative'}.</p>
        `;} catch (error) {
        console.error(error);
        errorMessage.innerHTML = 'An error occurred. Please try again later.';
    }
});


