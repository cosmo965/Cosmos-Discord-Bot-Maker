const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const child_process = require('child_process');
const {PythonShell} = require('python-shell');

// Handling the back-end

/* 
Transporting data format-
bot_name=(botname)
owner_id=(ownerid)
token=(token)
client_id=(clientid)
directory=(directory) [e.g: {C:\Users\chevr\Desktop\Python projects\Cosmo productions\applications} ]
minigames={"rps":[True/False, int, int], "coinFlip":[True/False, int, int]}
currency={"currencies":[_1,_2,_3]}
*/

function startPython (bot_name,owner_id,token,client_id,directory,minigames,currency,bot_commands) {
  let result;
  let options = {
    mode: 'text',
    args: [
      `["${bot_name}"]`,
      `["${owner_id}"]`,
      `["${token}"]`,
      `["${client_id}"]`,
      `[r"${directory}"]`,
      `{'rps': {'bool':${minigames["rps"]["bool"].toString()}, 'cooldown':${minigames["rps"]["cooldown"].toString()}, 'currencies':${JSON.stringify(minigames["rps"]["currencies"]).replace(/null/g,"None")}, 'other_args':${JSON.stringify(minigames["rps"]["other_args"]).replace(/null/g,"None")}},'coinFlip':{'bool':${minigames["coinFlip"]["bool"].toString()}, 'cooldown':${minigames["coinFlip"]["cooldown"].toString()}, 'currencies':${JSON.stringify(minigames["coinFlip"]["currencies"]).replace(/null/g,"None")}, 'other_args':${JSON.stringify(minigames["coinFlip"]["other_args"]).replace(/null/g,"None")}}}`,
      `[${currency}]`,
      `{'balance':${bot_commands["balance"].toString()},'simp':${bot_commands["simp"].toString()},'constant_commands':${bot_commands["constants"].toString()}}`,
    ],
  };
  PythonShell.run('../__main__.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log('results: ', results);
  });
};

ipcMain.on("pass_newbot_data", function(event,data){
  startPython(
    data["bot_name"],
    data["owner_id"],
    data["token"],
    data["client_id"],
    data["directory"],
    data["minigames"],
    data["currency"],
    data["bot_commands"],
  )
});
ipcMain.on("open_directory", function(event,sent_directory) {
  var directory = dialog.showOpenDialogSync({ properties: ["openDirectory", "createDirectory"] });
  event.reply("open_directory", directory)
});

// Handling the display of user interface

function createWindow () {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    //frame: false,
    minWidth:1000,
    minHeight:800,
    maxWidth:1000,
    maxHeight:800,
    icon: path.join(__dirname, 'images/icon.png'),
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      preload: path.join(__dirname, 'preload.js'),
    },
  })
  win.webContents.openDevTools();
  win.removeMenu();
  win.loadFile(path.join(__dirname, 'index.html'));
  ipcMain.on("alert_max_currencies", function(event) {
    dialog.showMessageBox(win,{title:"Cosmo's Bot Maker",message:"You can only create up to 5 currencies."})
  });
  ipcMain.on("alert_currency_same_name", function(event) {
    dialog.showMessageBox(win, {title:"Same currency name",message:"Currencies cannot have the same name"})
  });
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    };
  });
});

// Stops the application when the application is closed.

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  };
});
