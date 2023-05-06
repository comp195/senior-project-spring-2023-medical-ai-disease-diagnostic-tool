const { send, on } = window.electronAPI;

const form = document.querySelector('form');
const error = document.querySelector('#error-message');
const resultText = document.querySelector('#result-text');
const resultChart = document.querySelector('#resultChart');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Retrieve user input
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
    error.innerHTML = '';
    resultText.innerHTML = '';
    resultChart.innerHTML = '';

    if (isNaN(age) || age < 1 || age > 120) {
        error.innerHTML = 'Age must be a number between 1 and 120';
        return;
    }

    if (sex !== 'male' && sex !== 'female') {
        error.innerHTML = 'Please select a valid sex';
        return;
    }

    if (chestPainType !== 'typical-angina' && chestPainType !== 'atypical-angina' && chestPainType !== 'non-anginal-pain' && chestPainType !== 'asymptomatic') {
        error.innerHTML = 'Please select a valid chest pain type';
        return;
    }

    if (isNaN(restingBP) || restingBP < 80 || restingBP > 200) {
        error.innerHTML = 'Resting blood pressure must be a number between 80 and 200';
        return;
    }

    if (isNaN(cholesterol) || cholesterol < 100 || cholesterol > 600) {
        error.innerHTML = 'Cholesterol must be a number between 100 and 600';
        return;
    }

    if (fastingBS !== 0 && fastingBS !== 1) {
        error.innerHTML = 'Please select a valid fasting blood sugar value';
        return;
    }

    if (restingECG !== 'normal' && restingECG !== 'st-t-wave-abnormality' && restingECG !== 'left-ventricular-hypertrophy') {
        error.innerHTML = 'Please select a valid resting ECG value';
        return;
    }

    if (isNaN(maxHR) || maxHR < 60 || maxHR > 220) {
        error.innerHTML = 'Maximum heart rate must be a number between 60 and 220';
        return;
    }

    if (exerciseAngina !== 0 && exerciseAngina !== 1) {
        error.innerHTML = 'Please select a valid exercise-induced angina value';
        return;
    }

    if (isNaN(oldpeak) || oldpeak < 0 || oldpeak > 10) {
        error.innerHTML = 'ST depression must be a number between 0 and 10';
        return;
    }

    if (stSlope !== 'up-sloping' && stSlope !== 'flat' && stSlope !== 'down-sloping') {
        error.innerHTML = 'Please select a valid ST slope value';
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
    const dataString = JSON.stringify(data);
    send('runPythonScript', dataString);
    on('pythonScriptResult', (result) => {
        console.log('Received result:', result);

        resultChart.innerHTML = '';
        // Create an element to display the results
        const resultsContainer = document.createElement('div');

        // Loop through each model in the result object
        for (const modelName in result) {
            const prediction = result[modelName][1];
            console.log(`${modelName} Prediction:`, prediction);

            // Check if prediction is a valid number
            if (typeof prediction !== 'number' || isNaN(prediction)) {
                error.innerHTML = 'Invalid prediction result';
                return;
            }

            const predictionPercentage = (prediction * 100).toFixed(1);
            const remainingPercentage = (100 - predictionPercentage);

            // Create elements to display the model name and prediction percentage
            const modelTitle = document.createElement('h3');
            modelTitle.textContent = modelName;
            resultsContainer.appendChild(modelTitle);

            const modelResultText = document.createElement('p');
            modelResultText.innerHTML = `Prediction: ${predictionPercentage}%`;
            resultsContainer.appendChild(modelResultText);

            const modelResultChart = document.createElement('div');
            modelResultChart.innerHTML = `
            <svg height="200" width="200">
              <circle cx="100" cy="100" r="90" stroke="#ddd" stroke-width="20" fill="none"/>
              <circle cx="100" cy="100" r="90" stroke="#33c3f0" stroke-dasharray="565.48" stroke-dashoffset="565.48" stroke-width="20" fill="none">
                <animate attributeName="stroke-dashoffset" from="565.48" to="${565.48 - predictionPercentage / 100 * 565.48}" dur="2s" fill="freeze" />
              </circle>
              <text x="50%" y="50%" text-anchor="middle" alignment-baseline="middle" font-size="32">${predictionPercentage}%</text>
            </svg>
        `;
            resultsContainer.appendChild(modelResultChart);
        }

        // Add the results container to the page
        resultChart.appendChild(resultsContainer);
    });
});