<!DOCTYPE html>
<html>
<head>
    <title> Heart Disease Diagnostic</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="Main.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>


</head>

<body>

<py-config>
    packages = ["matplotlib", "pandas", "seaborn"]

</py-config>

<header>
    <h1 class="title">Heart Disease Diagnostic</h1>
    <nav>
        <ul>
            <li><a href="https://github.com/comp195/senior-project-spring-2023-medical-ai-disease-diagnostic-tool">GITHUB Home</a></li>
            <li><a href="http://localhost:51195/WEB.html">About</a></li>
            <
        </ul>
    </nav>
</header>
<main>
    <section>
        <h2>Enter User Information</h2>
        <form onsubmit="return false">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" placeholder="ex. John Doe" required>


            <!-- AGE VALIDATION HERE -->
            <label for="age">Age (Year):</label>
            <input type="number" id="age" name="age" required>
            <span id="age-error" style="color: red;"></span>

            <script>
                var ageInput = document.getElementById("age");
                var ageError = document.getElementById("age-error");

                ageInput.addEventListener("blur", validateAge);
                ageInput.addEventListener("keydown", clearAgeError);

                function validateAge() {
                    var age = ageInput.value;
                    if (age < 1 || age > 112) {
                        ageError.textContent = "Invalid age. Age must be between 0 and 112.";
                        ageInput.focus();
                    } else {
                        ageError.textContent = "";
                    }
                }

                function clearAgeError() {
                    ageError.textContent = "";
                }
            </script>
            <!---------------------------------  -->

            <label for="gender">Gender:</label>
            <select id="gender" name="gender" required>
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
            </select>

            <input onclick="submitForm1()" type="submit" id="btn-form-1" value="submit">
        </form>


        <p id='output1'></p>

        <script>
            function submitForm1() {
                const name = document.getElementById("name").value;
                const age = document.getElementById("age").value;
                const gender = document.getElementById("gender").value;
                document.getElementById("output1").innerHTML = "Is this correct Info?" + " Name: " + name + ", Age: " + age + ", Gender: " + gender;
            }
        </script>

    </section>
    <section>
        <h2>Enter User Health Information?</h2>
        <div class="health-container">
            <form class="health-form">

                <!-- chol vs Bp HERE=-------------------------------------------------------------------- -->
                    <div>
                        <label class="health-label" for="cholesterol">Cholesterol Level:</label>
                        <input type="number" class="health-input" id="cholesterol" name="cholesterol" maxlength="3" required>
                        <span id="cholesterol-error" style="color: red;"></span>
                    </div>

                    <div>
                        <label class="health-label" for="blood-pressure">Blood Pressure:</label>
                        <input type="number" class="health-input" id="blood-pressure" name="blood_pressure" maxlength="3" required>
                        <span id="blood-pressure-error" style="color: red;"></span>
                    </div>

                    <button onclick="submitHealthInfo()">Data</button>

                    <div id="plot"></div>

                    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                    <script>
                        function submitHealthInfo() {
                            var cholesterol = parseFloat(document.getElementById("cholesterol").value);
                            var bloodPressure = parseFloat(document.getElementById("blood-pressure").value);
                            var cholesterolError = document.getElementById("cholesterol-error");
                            var bloodPressureError = document.getElementById("blood-pressure-error");

                            var isValid = true;

                            if (isNaN(cholesterol) || cholesterol < 10 || cholesterol > 500) {
                                cholesterolError.textContent = "Invalid cholesterol level. Cholesterol level must be between 10 and 500.";
                                isValid = false;
                            } else {
                                cholesterolError.textContent = "";
                            }

                            if (isNaN(bloodPressure) || bloodPressure < 50 || bloodPressure > 180) {
                                bloodPressureError.textContent = "Invalid blood pressure. Blood pressure must be between 50 and 180.";
                                isValid = false;
                            } else {
                                bloodPressureError.textContent = "";
                            }

                            if (isValid) {
                                var userColor = 'black';
                                var traceColor = 'light grey';

                                var userData = {x: [cholesterol], y: [bloodPressure], mode: 'markers', type: 'scatter', name: 'User Data', marker: {color: userColor}};

                                var traceData = {x: [], y: [], mode: 'markers', type: 'scatter', name: 'Heart Data', marker: {color: []}};

                                Plotly.newPlot('plot', [userData, traceData], {title: 'Resting Blood Pressure vs Cholesterol', xaxis: {title: 'Total Cholesterol mg/dL'}, yaxis: {title: 'Resting Blood Pressure mg/dL'}, boxmode: 'group'});

                                Plotly.d3.csv('https://raw.githubusercontent.com/KelvinLuk/CSVHEARTDATA/main/heart.csv', function(err, rows){
                                    // Define x and y arrays using data from heart.csv
                                    var xArray = [], yArray = [], colorArray = [];
                                    for(var i=0; i<rows.length; i++){
                                        xArray.push(rows[i].Cholesterol);
                                        yArray.push(rows[i].RestingBP);
                                        var bpRisk = getBPRisk(rows[i].RestingBP);
                                        var cholRisk = getCholRisk(rows[i].Cholesterol);
                                        if (bpRisk === 'danger' || cholRisk === 'danger') {
                                            colorArray.push('red');
                                        } else if (bpRisk === 'at risk' || cholRisk === 'at risk') {
                                            colorArray.push('yellow');
                                        } else {
                                            colorArray.push('green');
                                        }
                                    }

                                    // Add the heart data to the existing plot
                                    var traceData = {x: xArray, y: yArray, mode: 'markers', type: 'scatter', name: 'Heart Data', marker: {color: colorArray}};
                                    Plotly.addTraces('plot', traceData);
                                });
                            }
                        }

                        function getBPRisk(bp) {
                            if (bp >= 180) {
                                return 'danger';
                            } else if (bp >= 140 && bp <= 179) {
                                return 'at risk';
                            } else if (bp >= 120 && bp <= 139) {
                                return 'elevated';
                            } else {
                                return 'normal';
                            }
                        }

                        function getCholRisk(chol) {
                            if (chol >= 240 || chol <= 50) {
                                return 'danger';
                            } else if (chol >= 200 && chol <= 239) {
                                return 'at risk';
                            } else {
                                return 'safe';
                            }
                        }

                    </script>
                <!------------------------------------------------------------------------------->

                <label class="health-label">Do You Have Any Existing Illness or Medical Condition?:</label>
                <div style="padding:0px">
                    < <div class="symptom-group">
                        <label class="symptom-label">Congenital Heart Defects:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="congenital_heart_defects" value="yes" required> Yes
                            <input type="radio" name="congenital_heart_defects" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Peripheral Artery Disease:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="peripheral_artery_disease" value="yes" required> Yes
                            <input type="radio" name="peripheral_artery_disease" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Blood Clots:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="blood_clots" value="yes" required> Yes
                            <input type="radio" name="blood_clots" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Heart Attack:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="heart_attack" value="yes" required> Yes
                            <input type="radio" name="heart_attack" value="no" required> No
                        </div>
                    </div>


            </form>
            <div id="myPlot" style="width:100%;max-width:700px"></div>
            <h2>Do You Have These Symptoms?</h2>
            <div class="symptom-container">
                <form class="symptom-form" onsubmit="return generateChart()">

                    <div class="symptom-group">
                        <label class="symptom-label">Shortness of Breath:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="shortness_of_breath" value="yes" required> Yes
                            <input type="radio" name="shortness_of_breath" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Swollen leg Or Belly:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="swollenlegOrBelly" value="yes" required> Yes
                            <input type="radio" name="swollenlegOrBelly" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Dizziness or Lightheadedness:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="dizzy" value="yes" required> Yes
                            <input type="radio" name="dizzy" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Numbness in the Legs or Arms:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="numbness" value="yes" required> Yes
                            <input type="radio" name="numbness" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Chest Pain:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="chest_pain" value="yes" required> Yes
                            <input type="radio" name="chest_pain" value="no" required> No
                        </div>
                    </div>




                    <div class="symptom-group">
                        <label class="symptom-label">Arrhythmia:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="arrhythmia"  value="yes" required> yes
                            <input type="radio" name="arrhythmia" value="no" required> No
                        </div>
                    </div>


                    <div class="symptom-group">
                        <label class="symptom-label">Swollen feet or Ankle:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="swollen_feet_or_ankle" value="yes" required> Yes
                            <input type="radio" name="swollen_feet_or_ankle" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Fatigue:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="fatigue" value="yes" required> Yes
                            <input type="radio" name="fatigue" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Fainting:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="fainting" value="yes" required> Yes
                            <input type="radio" name="fainting" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Skin rash:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="Rash" value="yes" required> Yes
                            <input type="radio" name="Rash" value="no" required> No
                        </div>
                    </div>
                    <div class="symptom-group">
                        <label class="symptom-label">Pain in the neck, back, jaw, upperbelly, throat:</label>
                        <div class="symptom-radio">
                            <input type="radio" name="PainNB" value="yes" required> Yes
                            <input type="radio" name="PainNB" value="no" required> No
                        </div>
                    </div>





                    <button type="submit">Submit</button>
                </form>
            </div>


    </section>
</main
<style>
    .image-grid {
        display: flex;

    }
</style>

<script>
    // Define the symptoms and their associated weights
    const symptomWeights = {
        fever: 1,
        cough: 1,
        shortness_of_breath: 1,
        fatigue: 1,
        body_aches: 1,
        loss_of_smell_or_taste: 1,
        heart_attack: 1,
        diabetes: 1,
        high_blood_pressure: 1,
        headache: 1,
        sore_throat: 1,
        runny_nose: 1,
        nausea_or_vomiting: 1
    };

    // Calculate the total weight of the selected symptoms
    function calculateWeight() {
        let weight = 0;
        for (const symptom in symptomWeights) {
            const value = document.querySelector(`input[name="${symptom}"]:checked`).value;
            if (value === 'yes') {
                weight += symptomWeights[symptom];
            }
        }
        return weight;
    }

    // Calculate the percentage chance of getting a heart attack
    function calculatePercentage(weight) {
        const percentage = Math.min(Math.round(weight / 20 * 100), 100);
        return percentage;
    }

    // Draw the circular chart
    function drawChart(percentage) {
        const canvas = document.getElementById('chart');
        const ctx = canvas.getContext('2d');
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = canvas.width / 3;
        const startAngle = -Math.PI / 2;
        const endAngle = startAngle + percentage / 100 * 2 * Math.PI;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, startAngle, startAngle + 2 * Math.PI);
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 30;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, startAngle, endAngle);
        ctx.strokeStyle = '#f00';
        ctx.lineWidth = 30;
        ctx.stroke();
        ctx.font = 'bold 50px sans-serif';
        ctx.fillStyle = '#f00';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`${percentage}%`, centerX, centerY);
    }

    // Display the result text message
    function displayResult(percentage) {
        const result = document.getElementById('result');
        if (percentage >= 50) {
            result.innerText = 'You have a high chance of getting a heart attack. Please seek medical attention immediately.';
        } else {
            result.innerText = 'Your chance of getting a heart attack is low. However, if you have any concerns, please consult a doctor.';
        }
    }

    // Handle the form submission
    const form = document.querySelector('.symptom-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const weight = calculateWeight();
        const percentage = calculatePercentage(weight);
        drawChart(percentage);
        displayResult(percentage);
    });

    // Add event listeners to symptom radio buttons
    const symptomRadios = document.querySelectorAll('.symptom-radio input');
    symptomRadios.forEach(radio => {
        radio.addEventListener('change', () => {
            const weight = calculateWeight();
            const percentage = calculatePercentage(weight);
            drawChart(percentage);
            displayResult(percentage);
        });
    });

</script>





<py-script>
    import js
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn

    from pyodide.http import open_url

    df = pd.read_csv(open_url("https://raw.githubusercontent.com/KelvinLuk/CSVHEARTDATA/main/heart.csv"))

    seaborn.scatterplot(data=df, x='Cholesterol', y='RestingBP', hue='Age', style='Sex', palette='coolwarm')

    plt.title('Resting Blood Pressure vs Cholesterol')
    plt.xlabel('Cholesterol')
    plt.ylabel('Resting Blood Pressure')

    display(plt)
</py-script>


<script>
    function submitAllForms() {
        const name = document.getElementById("name").value;
        const age = document.getElementById("age").value;
        const gender = document.getElementById("gender").value;

        var cholesterol = parseFloat(document.getElementById("cholesterol").value);
        var bloodPressure = parseFloat(document.getElementById("blood-pressure").value);
        var cholesterolError = document.getElementById("cholesterol-error");
        var bloodPressureError = document.getElementById("blood-pressure-error");

        var isValid = true;

        if (isNaN(cholesterol) || cholesterol < 10 || cholesterol > 500) {
            cholesterolError.textContent = "Invalid cholesterol level. Cholesterol level must be between 10 and 500.";
            isValid = false;
        } else {
            cholesterolError.textContent = "";
        }

        if (isNaN(bloodPressure) || bloodPressure < 50 || bloodPressure > 180) {
            bloodPressureError.textContent = "Invalid blood pressure. Blood pressure must be between 50 and 180.";
            isValid = false;
        } else {
            bloodPressureError.textContent = "";
        }

        var plotDiv = document.createElement('div');
        plotDiv.setAttribute('id', 'final-plot');

        var outputFinal = document.getElementById("output-final");
        outputFinal.innerHTML = "Name: " + name + "<br>Age: " + age + "<br>Gender: " + gender;
        outputFinal.appendChild(plotDiv);

        if (isValid) {
            var userColor = 'black';
            var traceColor = 'light grey';

            var userData = {x: [cholesterol], y: [bloodPressure], mode: 'markers', type: 'scatter', name: 'User Data', marker: {color: userColor}};

            var traceData = {x: [], y: [], mode: 'markers', type: 'scatter', name: 'Heart Data', marker: {color: []}};

            Plotly.newPlot('final-plot', [userData, traceData], {title: 'Resting Blood Pressure vs Cholesterol', xaxis: {title: 'Total Cholesterol mg/dL'}, yaxis: {title: 'Resting Blood Pressure mg/dL'}, boxmode: 'group'});

            Plotly.d3.csv('https://raw.githubusercontent.com/KelvinLuk/CSVHEARTDATA/main/heart.csv', function(err, rows){
                // Define x and y arrays using data from heart.csv
                var xArray = [], yArray = [], colorArray = [];
                for(var i=0; i<rows.length; i++){
                    xArray.push(rows[i].Cholesterol);
                    yArray.push(rows[i].RestingBP);
                    var bpRisk = getBPRisk(rows[i].RestingBP);
                    var cholRisk = getCholRisk(rows[i].Cholesterol);
                    if (bpRisk === 'danger' || cholRisk === 'danger') {
                        colorArray.push('red');
                    } else if (bpRisk === 'at risk' || cholRisk === 'at risk') {
                        colorArray.push('yellow');
                    } else {
                        colorArray.push('green');
                    }
                }

                // Add the heart data to the existing plot
                var traceData = {x: xArray, y: yArray, mode: 'markers', type: 'scatter', name: 'Heart Data', marker: {color: colorArray}};
                Plotly.addTraces('final-plot', traceData);
            });

        }

        var cholesterol = parseFloat(document.getElementById("cholesterol").value);
        var bloodPressure = parseFloat(document.getElementById("blood-pressure").value);

        const ShortnessOfBreath = document.querySelector('input[name="shortness_of_breath"]:checked').value;
        const SwollenLegsOrBelly = document.querySelector('input[name="swollenlegOrBelly"]:checked').value;
        const Dizziness = document.querySelector('input[name="dizzy"]:checked').value;
        const numbnessInTheLeg = document.querySelector('input[name="numbness"]:checked').value;
        const chestPain = document.querySelector('input[name="chest_pain"]:checked').value;
        const fainting = document.querySelector('input[name="fainting"]:checked').value;
        const PainNeckBack = document.querySelector('input[name="PainNB"]:checked').value;

        const arrhythmia = document.querySelector('input[name="arrhythmia"]:checked').value;
        const SwollenFeetOrAnkle = document.querySelector('input[name="swollen_feet_or_ankle"]:checked').value;
        const fatigue = document.querySelector('input[name="fatigue"]:checked').value;
        const SkinRashes = document.querySelector('input[name="Rash"]:checked').value;

        const heartattack = document.querySelector('input[name="heart_attack"]:checked').value;
        const bloodclots = document.querySelector('input[name="blood_clots"]:checked').value;
        const CongenitalHeartDefects = document.querySelector('input[name="congenital_heart_defects"]:checked').value;
        const PeripheralArteryDisease = document.querySelector('input[name="peripheral_artery_disease"]:checked').value;
        // Calculate risk score
        let riskScore = 0;
        if (bloodPressure >= 180) {
            riskScore += 25;
        } else if (bloodPressure>= 140 && bp <= 179) {
            riskScore += 15;
        } else if (bloodPressure >= 120 && bp <= 139) {
            riskScore += 10;
        } else {
            return 'normal';
        }


        if (cholesterol >= 240 || chol <= 50) {
            riskScore += 25;
        } else if (cholesterol >= 200 && chol <= 239) {
            riskScore += 15;
        } else {
            return 'safe';
        }



        if (fainting === 'yes') {
            riskScore += 20;
        }
        if (fatigue === 'yes') {
            riskScore += 5;
        }
        if (ShortnessOfBreath === 'yes') {
            riskScore += 20;
        }
        if (SwollenLegsOrBelly === 'yes') {
            riskScore += 5;
        }
        if (Dizziness === 'yes') {
            riskScore += 7;
        }
        if (numbnessInTheLeg === 'yes') {
            riskScore += 5;
        }
        if (chestPain === 'yes') {
            riskScore += 10;
        }
        if (PainNeckBack === 'yes') {
            riskScore += 15;
        }
        if (SkinRashes === 'yes') {
            riskScore += 3;
        }

        if (arrhythmia === 'yes') {
            riskScore += 9;
        }

        if (SwollenFeetOrAnkle === 'yes') {
            riskScore += 5;
        }


        if (CongenitalHeartDefects === 'yes') {
            riskScore += 20;
        }
        if (PeripheralArteryDisease === 'yes') {
            riskScore += 10;
        }
        if (bloodclots === 'yes') {
            riskScore += 25;
        }
        if (heartattack === 'yes') {
            riskScore += 30;
        }
        // Calculate remaining score out of 100
        const remainingScore = 100 - riskScore;

        // Create chart
        const data = [
            {
                values: [riskScore, remainingScore],
                labels: ['Chance of Risk', ' Chance of Not Risk '],
                hole: 0.5,
                type: 'pie',
                marker: {
                    colors: ['#FF4136', '#DDDDDD'],
                },
            },
        ];

        const layout = {
            title: 'Heart Disease Prediction',
        };

        Plotly.newPlot('myPlot', data, layout);

    }






</script>

<scrip>
    <form onsubmit="return false">


        <input onclick="submitAllForms()" type="submit" id="btn-final-submit" value="Submit All">
    </form>

    <p>Final Output:</p>
    <p id='output-final'></p>

</scrip>





<div class="chart-container">
    <canvas id="chart"></canvas>
</div>
<script>
    function generateChart(){
        // Get values of radio buttons
        const ShortnessOfBreath = document.querySelector('input[name="shortness_of_breath"]:checked').value;
        const SwollenLegsOrBelly = document.querySelector('input[name="swollenlegOrBelly"]:checked').value;
        const Dizziness = document.querySelector('input[name="dizzy"]:checked').value;
        const numbnessInTheLeg = document.querySelector('input[name="numbness"]:checked').value;
        const chestPain = document.querySelector('input[name="chest_pain"]:checked').value;
        const fainting = document.querySelector('input[name="fainting"]:checked').value;
        const PainNeckBack = document.querySelector('input[name="PainNB"]:checked').value;

        const arrhythmia = document.querySelector('input[name="arrhythmia"]:checked').value;
        const SwollenFeetOrAnkle = document.querySelector('input[name="swollen_feet_or_ankle"]:checked').value;
        const fatigue = document.querySelector('input[name="fatigue"]:checked').value;
        const SkinRashes = document.querySelector('input[name="Rash"]:checked').value;

        const heartattack = document.querySelector('input[name="heart_attack"]:checked').value;
        const bloodclots = document.querySelector('input[name="blood_clots"]:checked').value;
        const CongenitalHeartDefects = document.querySelector('input[name="congenital_heart_defects"]:checked').value;
        const PeripheralArteryDisease = document.querySelector('input[name="peripheral_artery_disease"]:checked').value;
        // Calculate risk score
        let riskScore = 0;

        if (fainting === 'yes') {
            riskScore += 20;
        }
        if (fatigue === 'yes') {
            riskScore += 5;
        }
        if (ShortnessOfBreath === 'yes') {
            riskScore += 20;
        }
        if (SwollenLegsOrBelly === 'yes') {
            riskScore += 5;
        }
        if (Dizziness === 'yes') {
            riskScore += 7;
        }
        if (numbnessInTheLeg === 'yes') {
            riskScore += 5;
        }
        if (chestPain === 'yes') {
            riskScore += 10;
        }
        if (PainNeckBack === 'yes') {
            riskScore += 15;
        }
        if (SkinRashes === 'yes') {
            riskScore += 3;
        }

        if (arrhythmia === 'yes') {
            riskScore += 9;
        }

        if (SwollenFeetOrAnkle === 'yes') {
            riskScore += 5;
        }


        if (CongenitalHeartDefects === 'yes') {
            riskScore += 20;
        }
        if (PeripheralArteryDisease === 'yes') {
            riskScore += 10;
        }
        if (bloodclots === 'yes') {
            riskScore += 25;
        }
        if (heartattack === 'yes') {
            riskScore += 30;
        }
        // Calculate remaining score out of 100
        const remainingScore = 100 - riskScore;

        // Create chart
        const data = [
            {
                values: [riskScore, remainingScore],
                labels: ['Chance of Risk', ' Chance of Not Risk '],
                hole: 0.5,
                type: 'pie',
                marker: {
                    colors: ['#FF4136', '#DDDDDD'],
                },
            },
        ];

        const layout = {
            title: 'Heart Disease Prediction',
        };

        Plotly.newPlot('myPlot', data, layout);

        return false; // Prevent form from submitting and reloading the page
    }

</script>




<footer>
    <p>Copyright &copy;UOP 2023</p>
</footer>


</body>

</html>



