const path = require('path');
const url = require('url');
const electron = require('electron');
const { app, BrowserWindow, ipcMain } = electron;

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: false,
            contextIsolation: true,
        },
    });

    win.loadFile('index.html');

    win.webContents.openDevTools();
}

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

app.on('ready', createWindow);

ipcMain.on('runPythonScript', (event, dataString) => {
    console.log("hello")
    console.log(dataString)
    console.log(`python3 data_input.py '${dataString}'`)

    const { spawn } = require("child_process");

    let dataToSend = '';
    let python = spawn('python3', ["./data_input.py", dataString]);
    python.stdout.on('data', function (data) {
        console.log("Reading");
        dataToSend = data.toString();
    });
    python.on('close', (code) => {
        console.log("Closing");
        console.log(dataToSend);
        try{
            const jsonData = JSON.parse(dataToSend);
            event.sender.send('pythonScriptResult', jsonData);
        } catch (error){
            console.error('Error parsing JSON: ${dataToSend}');
            console.error(error);
            event.sender.send('pythonScriptResult', { error: error.message});
        }

    })
    /*
    exec(`python3 data_input.py '${dataString}'`,
        function (error, stdout, stderr) {
            if (error) {
                console.error(`exec error: ${error}`);
                return;
            }
            let result = JSON.parse('{}')
            try {
                let b = stdout;
                result = JSON.parse(b);
            }
            catch {
                console.log("asdf " + stdout);
            }
            event.sender.send('pythonScriptResult', result);
    });*/
});
