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
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
</header>
<main>
    <section>
        <h2>Enter User Information</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <!-- AGE VALIDATION HERE -->
            <form method="post">
                <label for="age">Age (Year):</label>
                <input type="number" id="age" name="age" required>
                <span id="age-error" style="color: red;"></span>

            </form>

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
        </form>
    </section>
    <section>
        <h2>Enter User Health Information?</h2>
        <div class="health-container">
            <form class="health-form">


                <!-- Cholestrol VALIDATION HERE -->
                <form method="post">
                    <label class="health-label" for="cholesterol">Cholesterol Level:</label>
                    <input type="number" class="health-input" id="cholesterol" name="cholesterol" maxlength="3" required>
                    <span id="cholesterol-error" style="color: red;"></span>

                </form>

                <script>
                    var cholesterolInput = document.getElementById("cholesterol");
                    var cholesterolError = document.getElementById("cholesterol-error");

                    cholesterolInput.addEventListener("blur", validateCholesterol);
                    cholesterolInput.addEventListener("keydown", clearCholesterolError);

                    function validateCholesterol() {
                        var cholesterol = cholesterolInput.value;
                        if (cholesterol < 10 || cholesterol > 500) {
                            cholesterolError.textContent = "Invalid cholesterol level. Cholesterol level must be between 10 and 500.";
                            cholesterolInput.focus();
                        } else {
                            cholesterolError.textContent = "";
                        }
                    }

                    function clearCholesterolError() {
                        cholesterolError.textContent = "";
                    }
                </script>
                <!---------------------------------  -->

                <!-- Bloodpressure VALIDATION HERE -->
                <form method="post">
                    <label class="health-label" for="blood-pressure">Blood Pressure:</label>
                    <input type="number" class="health-input" id="blood-pressure" name="blood_pressure" maxlength="3" required>
                    <span id="blood-pressure-error" style="color: red;"></span>

                </form>

                <script>
                    var bloodPressureInput = document.getElementById("blood-pressure");
                    var bloodPressureError = document.getElementById("blood-pressure-error");

                    bloodPressureInput.addEventListener("blur", validateBloodPressure);
                    bloodPressureInput.addEventListener("keydown", clearBloodPressureError);

                    function validateBloodPressure() {
                        var bloodPressure = bloodPressureInput.value;
                        if (bloodPressure < 50 || bloodPressure > 180) {
                            bloodPressureError.textContent = "Invalid blood pressure. Blood pressure must be between 50 and 180.";
                            bloodPressureInput.focus();
                        } else {
                            bloodPressureError.textContent = "";
                        }
                    }

                    function clearBloodPressureError() {
                        bloodPressureError.textContent = "";
                    }
                </script>

                <label class="health-label">Do You Have Any Existing Illness or Medical Condition?:</label>
                <div style="padding:0px">
                    <input type="radio" class="health-input" name="existing_illness value="yes" required> Yes

                    <input type="text" class="health-input" name="existing_illness">

                    <input type="radio" class="health-input" name="existing_illness" value="no" required> No

                    <div style="padding:10px">
                        <label class="health-label">Do You Exercise?:</label>
                        <input type="radio" class="health-input" name="exercise" value="yes" required> Yes
                        <input type="radio" class="health-input" name="exercise" value="no" required> No

                        <div style="padding:0px">
                            <label class="health-label">Did you travel:</label>
                            <input type="radio" class="health-input" name="chest_pain" value="yes" required> Yes
                            <input type="radio" class="health-input" name="chest_pain" value="no" required> No

                            <div style="padding:0px">
                                <label class="health-label">Medical History (such as family history of condition)?:</label>
                                <input type="radio" class="health-input" name="medical_history" value="yes" required> Yes

                                <input type="text" class="health-input" name="medical_history">

                                <input type="radio" class="health-input" name="medical_history" value="no" required> No

            </form>
        </div>
        <h2>Do You Have These Symptoms?</h2>
        <div class="symptom-container">
            <form class="symptom-form">


                <div class="symptom-group">
                    <label class="symptom-label">Fever:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="fever" value="yes" required> Yes
                        <input type="radio" name="fever" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Cough:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="cough" value="yes" required> Yes
                        <input type="radio" name="cough" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Shortness of Breath:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="shortness_of_breath" value="yes" required> Yes
                        <input type="radio" name="shortness_of_breath" value="no" required> No
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
                    <label class="symptom-label">Body Aches:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="body_aches" value="yes" required> Yes
                        <input type="radio" name="body_aches" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Loss of Smell or Taste:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="loss_of_smell_or_taste" value="yes" required> Yes
                        <input type="radio" name="loss_of_smell_or_taste" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Heart Attack:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="heart_attack" value="yes" required> Yes
                        <input type="radio" name="heart_attack" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Diabetes:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="diabetes" value="yes" required> Yes
                        <input type="radio" name="diabetes" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">High Blood Pressure:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="high_blood_pressure" value="yes" required> Yes
                        <input type="radio" name="high_blood_pressure" value="no" required> no
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Headache:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="headache" value="yes" required> Yes
                        <input type="radio" name="headache" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Sore Throat:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="sore_throat" value="yes" required> Yes
                        <input type="radio" name="sore_throat" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Runny Nose:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="runny_nose" value="yes" required> Yes
                        <input type="radio" name="runny_nose" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Nausea or Vomiting:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="nausea_or_vomiting" value="yes" required> Yes
                        <input type="radio" name="nausea_or_vomiting" value="no" required> No
                    </div>
                </div>
                <div class="symptom-group">
                    <label class="symptom-label">Chills:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="chills" value="yes" required> Yes
                        <input type="radio" name="chills" value="no" required> No
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
                    <label class="symptom-label">High Blood Pressure:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="high_blood_pressure" value="yes" required> Yes
                        <input type="radio" name="high_blood_pressure" value="no" required> No
                    </div>
                </div>

                <div class="symptom-group">
                    <label class="symptom-label">High Cholesterol:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="high_cholesterol" value="yes" required> Yes
                        <input type="radio" name="high_cholesterol" value="no" required> No
                    </div>
                </div>

                <div class="symptom-group">
                    <label class="symptom-label">Arrhythmia:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="arrhythmia" value="yes" required> Yes
                        <input type="radio" name="arrhythmia" value="no" required> No
                    </div>
                </div>

                <div class="symptom-group">
                    <label class="symptom-label">Heart Valve Problems:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="heart_valve_problems" value="yes" required> Yes
                        <input type="radio" name="heart_valve_problems" value="no" required> No
                    </div>
                </div>

                <div class="symptom-group">
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
                    <label class="symptom-label">Sleep Apnea:</label>
                    <div class="symptom-radio">
                        <input type="radio" name="sleep_apnea" value="yes" required> Yes
                        <input type="radio" name="sleep_apnea" value="no" required> No
                    </div>
                </div>


            </form>
            <input type="submit" value="Submit">

    </section>
</main
<style>
    .image-grid {
        display: flex;

    }
</style>


<div class="container">
    <nav>
        <!-- Navigation links here -->
    </nav>
    <div class="image-container">

    </div>
    <div class="image-grid">
        <div class="image-block">

            <img src="RBPvsCholestrol.jpg" alt="Trulli">

            <img src="RBPvsCholestrol.jpg" alt="Trulli">
        </div>


    </div>
</div>


<!-- OVERLAY OUTPUT HERE -->

<div id="Outputoverlay">
    <div id="left">
        <div class="Outputbox Outputred" onclick="Outputenlarge(this)"></div>
        <div class="Outputbox Outputblue" onclick="Outputenlarge(this)"></div>
        <div class="Outputbox Outputgreen" onclick="Outputenlarge(this)"></div>
        <div class="Outputbox Outputyellow" onclick="Outputenlarge(this)"></div>
    </div>
    <div id="Outputcenter">
        <p>Diagnosis text goes here.</p>
        <button onclick="off()">Done</button>
    </div>
</div>

<div style="padding:500px">
    <h2>Overlay with Text</h2>
    <button onclick="on()">Turn on overlay effect</button>
</div>

<script>
    var OutputenlargedBox;

    function on() {
        document.getElementById("Outputoverlay").style.display = "block";
    }

    function off() {
        document.getElementById("Outputoverlay").style.display = "none";
    }

    function Outputenlarge(Outputbox) {
        OutputenlargedBox = Outputbox.cloneNode(true);
        OutputenlargedBox.classList.add("Ouputenlarge-box");
        Ouputbox.parentElement.parentElement.parentElement.parentElement.parentElement.appendChild(OutputenlargedBox);
    }


</script>




<footer>
    <p>Copyright &copy;UOP 2023</p>
</footer>


<!-- Graph scatt OUTPUT HERE -->
<?php
$command ='ls';

echo exec (command , $out, $status);
/*
$command = 'python3 WEB/graph.py';
$output = shell_exec($command);
echo 'hello';
*/

?>
<style>
    #mytext{
        color: red;

    }
</style>
<div id = "mytext">


</div>




<py-script>
import js
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from pyodide.http import open_url

df = pd.read_csv(open_url("https://raw.githubusercontent.com/KelvinLuk/CSVHEARTDATA/main/heart.csv"))
print(df)
seaborn.scatterplot(data=df, x='Cholesterol', y='RestingBP', hue='Age', style='Sex', palette='coolwarm')

plt.title('Resting Blood Pressure vs Cholesterol')
plt.xlabel('Cholesterol')
plt.ylabel('Resting Blood Pressure')
print("hello3")
display(plt)
</py-script>





<div id="myPlot" style="width:100%;max-width:700px"></div>

<div class="health-container">
    <form onsubmit="submitForm()">
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


        <input type="submit" id="btn-form-1" value="Submit">

    </form>

    <p>Output:</p>
    <p id='output1'></p>

    <div id='myPlot' style='width:600px;height:400px;'></div>
</div>

<script>
    // Load heart.csv using Plotly's d3.csv method
    Plotly.d3.csv('https://raw.githubusercontent.com/KelvinLuk/CSVHEARTDATA/main/heart.csv', function(err, rows){
        // Define x and y arrays using data from heart.csv
        var xArray = [], yArray = [];
        for(var i=0; i<rows.length; i++){
            xArray.push(rows[i].Cholesterol);
            yArray.push(rows[i].RestingBP);
        }

        // Define data array and layout object for Plotly chart
        var data = [{
            x: xArray,
            y: yArray,
            mode: 'markers',
            marker: {
                color: rows.map(function(row){ return row.Age; }),  // Set color based on Age
                colorscale: 'Viridis',  // Set colorscale for color range
                size: 10  // Set marker size
            }
        }];

        var layout = {
            xaxis: {title: 'Cholesterol'},
            yaxis: {title: 'Resting Blood Pressure'},
            title: 'Resting Blood Pressure vs Cholesterol'
        };

        // Create scatter plot using Plotly's newPlot method
        Plotly.newPlot('myPlot', data, layout);

        // Define function to update scatter plot with user input
        function submitForm() {
            var cholesterolInput = document.getElementById("cholesterol").value;
            var bloodPressureInput = document.getElementById("blood-pressure").value;

            // Add user input to the data array
            data[0].x.push(cholesterolInput);
            data[0].y.push(bloodPressureInput);

            // Add 'You are here' marker to the data array
            data[0].x.push(cholesterolInput);
            data[0].y.push(bloodPressureInput);
            data[0].marker.color.push('black');
            data[0].marker.size.push(20);
            data[0].text = ['You are here'];
            data[0].textposition = 'top center';
            data[0].mode = 'markers+text';
            data[0].textfont = {size: 14};
            data[0].textfont.color = 'white';

            // Update scatter plot
            Plotly.update('myPlot', data, layout);

            // Clear form inputs
            document.getElementById("cholesterol").value = "";
            document.getElementById("blood-pressure").value = "";
        }
    });
</script>



</body>

</html>



