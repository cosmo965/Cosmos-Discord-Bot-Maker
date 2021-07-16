// 
//
//
//
window.addEventListener("load", function () {
  const electron = require('electron');
  const ipcRenderer = electron.ipcRenderer
  // do things after the DOM loads fully
  console.log("Everything is loaded");

  var update_log_div = document.querySelector('.update_log');
  var credits_div = document.querySelector('.credits');
  var documentation_div = document.querySelector('.documentation');
  var create_bot_ui = document.querySelector('.create_bot_interface');

  var container = document.querySelector('#container');
  var container2 = document.querySelector('#container2');
  
  // Create new bot ui activate
  
  var create_new_bot_btn = document.querySelector('.create_bot_button');

  create_new_bot_btn.addEventListener('click', function(){
     console.log('Creating new bot pressed...');
     create_bot_ui.style.display = "block";
     documentation_div.style.display = "none";
     credits_div.style.display = "none";
     update_log_div.style.display = "none";
  });

  // Credits open
  var credits_btn = document.querySelector('.credits_button');
  credits_btn.addEventListener('click', function () {
    credits_div.style.display = "block";
    update_log_div.style.display = "none";
    create_bot_ui.style.display = "none";
    documentation_div.style.display = "none";
  });

  // Update log open
  var update_log_btn = document.querySelector('.update_log_button');
  update_log_btn.addEventListener('click', function () {
    credits_div.style.display = "none";
    update_log_div.style.display = "block";
    create_bot_ui.style.display = "none";
    documentation_div.style.display = "none";
  });

  // Documentation open
  var documentation_btn = document.querySelector('.documentation_button');
  documentation_btn.addEventListener('click', function () {
    credits_div.style.display = "none";
    update_log_div.style.display = "none";
    create_bot_ui.style.display = "none";
    documentation_div.style.display = "block";
  });

  // Settings
  var choose_file_button = document.querySelector("#choose_file_button");
  var directory_display = document.querySelector("#directory_input");

  choose_file_button.addEventListener('click', function() {
    ipcRenderer.send("open_directory");
  });
  ipcRenderer.on("open_directory", function(event,sent_directory) {
    if (sent_directory == null) {return null}
    directory_display.value = sent_directory.toString();
  });

  // Minigames
  var rps_options = document.querySelector('#rps_options');
  var coinFlip_options = document.querySelector('#coin_flip_options');

  var rps_bool_input = document.querySelector('#rps_bool_input');
  var coinFlip_bool_input = document.querySelector('#coinFlip_bool_input');

  // RPS
  rps_bool_input.addEventListener('change', function() {
    if (rps_bool_input.checked == true) {
        rps_options.style.display = "block";
    } else {
        rps_options.style.display = "none";
    }
  });
  var rps_earnings_bool_input = document.querySelector('#rps_earnings_bool_input');
  var rps_earnings_options = document.querySelector('#rps_earnings');

  rps_earnings_bool_input.addEventListener('change', function() {
    if (rps_earnings_bool_input.checked == true) {
      rps_earnings_options.style.display = "block";
    } else {
      rps_earnings_options.style.display = "none";
    }
  });

  var list_currencies = document.getElementsByClassName("currency_input")
  var rps_earning_currency_OG = document.querySelector('.rps_earning_currency_OG')

  function refreshCurrencyListRps() {
    // Deleting current currencies
    document.querySelectorAll('.rps_earning_currency').forEach(e => e.remove());
    
    // Creating the new currencies
    for (i = 0; i < list_currencies.length; i++) {
      if (list_currencies[i].style.display == "block" && list_currencies[i].getAttribute("currency_name") != "") {
        let cloneRpsEarning = rps_earning_currency_OG.cloneNode(true);
        cloneRpsEarning.className = "rps_earning_currency";
        cloneRpsEarning.setAttribute("currency",list_currencies[i].getAttribute("currency_name"));
        cloneRpsEarning.childNodes[1].innerHTML = list_currencies[i].getAttribute("currency_name");
        cloneRpsEarning.childNodes[3].addEventListener('change', function(){
            // Minimum
          cloneRpsEarning.setAttribute("min",cloneRpsEarning.childNodes[3].value)
        });
        cloneRpsEarning.childNodes[5].addEventListener('change', function(){
            // Maximum
          cloneRpsEarning.setAttribute("max",cloneRpsEarning.childNodes[5].value)
        });

        cloneRpsEarning.style.display = "block";
        rps_earnings_options.append(cloneRpsEarning);
      };
    };
  };

  //COINFLIP
  var coinFlip_earnings_options = document.querySelector("#coinFlip_earnings");
  var coinFlip_earnings_bool_input = document.querySelector("#coinFlip_earnings_bool_input");
  var coinFlip_earning_currency_original = document.querySelector(".coinFlip_earning_currency_OG");

  coinFlip_bool_input.addEventListener('change', function() {
    if (coinFlip_bool_input.checked == true) {
        coinFlip_options.style.display = "block";
    } else {
      coinFlip_options.style.display = "none";
    }
  });

  coinFlip_earnings_bool_input.addEventListener('change', function() {
    if (coinFlip_earnings_bool_input.checked == true) {
      coinFlip_earnings_options.style.display = "block";
    } else {
      coinFlip_earnings_options.style.display = "none";
    }
  });

  coinFlip_earnings_options.addEventListener('change', function() {
    if (rps_earnings_bool_input.checked == true) {
      rps_earnings_options.style.display = "block";
    } else {
      rps_earnings_options.style.display = "none";
    }
  });

  function refreshCurrencyListCoinFlip() {
    // Deleting current currencies
    document.querySelectorAll('.coinFlip_earning_currency').forEach(e => e.remove());
    
    // Creating the new currencies
    for (i = 0; i < list_currencies.length; i++) {
      if (list_currencies[i].style.display == "block" && list_currencies[i].getAttribute("currency_name") != "") {
        let cloneCoinFlipEarning = coinFlip_earning_currency_original.cloneNode(true);
        cloneCoinFlipEarning.className = "coinFlip_earning_currency";
        cloneCoinFlipEarning.setAttribute("currency",list_currencies[i].getAttribute("currency_name"));
        cloneCoinFlipEarning.childNodes[1].innerHTML = list_currencies[i].getAttribute("currency_name");
        cloneCoinFlipEarning.childNodes[3].addEventListener('change', function(){
            // Minimum
            cloneCoinFlipEarning.setAttribute("min",cloneCoinFlipEarning.childNodes[3].value)
        });
        cloneCoinFlipEarning.childNodes[5].addEventListener('change', function(){
            // Maximum
            cloneCoinFlipEarning.setAttribute("max",cloneCoinFlipEarning.childNodes[5].value)
        });

        cloneCoinFlipEarning.style.display = "block";
        coinFlip_earnings_options.append(cloneCoinFlipEarning);
      };
    };
  };

  // BACKUP REFRESH (TESTING PURPOSES)
  var refresh_currency_list_rps = document.querySelector('#refresh_currencies_rps_earnings');
  var refresh_currencies_coinFlip_earnings = document.querySelector("#refresh_currencies_coinFlip_earnings");
  refresh_currency_list_rps.addEventListener('click', function() {refreshCurrencyListRps()});
  refresh_currencies_coinFlip_earnings.addEventListener('click', function() {refreshCurrencyListCoinFlip()});

  // CURRENCIES
  var currencies_bool_input = document.querySelector('#currencies_bool_input');
  var currencies_creator = document.querySelector('#currencies_creator');

  currencies_bool_input.addEventListener('change', function() {
    if (currencies_bool_input.checked == true) {
      currencies_creator.style.display = "block";
    } else {
      currencies_creator.style.display = "none";
    }
  });

  // Creating a new currency
  var create_new_currency_btn = document.querySelector('#create_new_currency_btn');
  var org_currency_input = document.querySelector('.currency_input');
  

  create_new_currency_btn.addEventListener('click', function() {
    var number_of_currency_inputs = document.getElementsByClassName("currency_input").length;
    if (number_of_currency_inputs < 6) {
      var clone_currency_input = org_currency_input.cloneNode(true);
      currencies_creator.appendChild(clone_currency_input); 
      clone_currency_input.style.display = "block";
  
      var currency_name_input = clone_currency_input.childNodes[1];
      var remove_btn = clone_currency_input.childNodes[3];
      
      currency_name_input.addEventListener('change', function(){
        clone_currency_input.setAttribute("currency_name", currency_name_input.value);

        let qualificate = [];
        for (var i = 0; i < document.getElementsByClassName("currency_input").length; i++) {
          if (document.getElementsByClassName("currency_input")[i] != clone_currency_input) {
            if (clone_currency_input.getAttribute("currency_name") != document.getElementsByClassName("currency_input")[i].getAttribute("currency_name")){
              qualificate.push(true);
            } else {
              qualificate.push(false);
            };
          };
        };
        if (qualificate.includes(false)) { qualificate = false; } else { qualificate = true; };
        if (qualificate == true) {
            refreshCurrencyListCoinFlip();
            refreshCurrencyListRps();
        } else {
            // has the same currency name
            console.log('same name!!');
            ipcRenderer.send("alert_currency_same_name");
            currency_name_input.value = "";
            clone_currency_input.setAttribute("currency_name", "");
            refreshCurrencyListCoinFlip();
            refreshCurrencyListRps();
        };
      });
      remove_btn.addEventListener('click', function() {
        clone_currency_input.remove();
        refreshCurrencyListCoinFlip();
        refreshCurrencyListRps();
      });
    } else {
      ipcRenderer.send('alert_max_currencies');
    };
  });

  // Submitting

  var submit_bot_create_button = document.getElementById("submit_bot_create_button");
  submit_bot_create_button.addEventListener('click', function(){
      // DEFINING SETTING SUBMIT DATA
      var bot_name_submit = document.querySelector("#bot_name_input").value;
      var owner_id_submit = document.querySelector("#owner_id_input").value;
      var token_submit = document.querySelector("#token_input").value;
      var client_id_submit = document.querySelector("#client_id_input").value;
      var directory_submit = document.querySelector("#directory_input").value;

      // DEFINING RPS SUBMIT DATA
      var rps_bool_submit = document.querySelector("#rps_bool_input").checked;
      rps_bool_submit = rps_bool_submit.toString().charAt(0).toUpperCase() + rps_bool_submit.toString().slice(1);

      var rpsearncurin = document.getElementsByClassName("rps_earning_currency");
      var rps_currency_values_submit = {};
      for (var i=0;i<rpsearncurin.length;i++) {
          let current = rpsearncurin[i];
          let current_currency_name = current.getAttribute("currency")
          let current_currency_min = parseInt(current.getAttribute("min"));
          let current_currency_max = parseInt(current.getAttribute("max"));
          rps_currency_values_submit[current_currency_name] = [current_currency_min,current_currency_max]
          console.log(current_currency_name);
      };
      var rps_victory_message = document.querySelector("#rps_victory_message").value;
      var rps_defeat_message = document.querySelector("#rps_defeat_message").value;
      var rps_tie_message = document.querySelector("#rps_tie_message").value;
      
      var rps_cooldown = document.querySelector("#rps_cooldown").value;
      // DEFINING COINFLIP SUBMIT DATA
      var coinFlip_bool_submit = document.querySelector("#coinFlip_bool_input").checked;
      coinFlip_bool_submit = coinFlip_bool_submit.toString().charAt(0).toUpperCase() + coinFlip_bool_submit.toString().slice(1);
      
      var coinFlip_victory_message = document.querySelector("#coinFlip_victory_message").value;
      var coinFlip_defeat_message = document.querySelector("#coinFlip_defeat_message").value;

      var cFlipearncurin = document.getElementsByClassName("coinFlip_earning_currency");
      var coinFlip_currency_values_submit = {};
      for (var i=0;i<cFlipearncurin.length;i++) {
          let current = cFlipearncurin[i];
          let current_currency_name = current.getAttribute("currency")
          let current_currency_min = parseInt(current.getAttribute("min"));
          let current_currency_max = parseInt(current.getAttribute("max"));
          coinFlip_currency_values_submit[current_currency_name] = [current_currency_min,current_currency_max]
          console.log(current_currency_name);
      };
      var coinFlip_cooldown = document.querySelector("#coinFlip_cooldown").value;

      // DEFINING CURRENCY SUBMIT DATA
      var list_of_currencies = [];
      for (var i=0;i<document.getElementsByClassName("currency_input").length;i++){
          if (document.getElementsByClassName("currency_input")[i].getAttribute("currency_name") != "") {
            list_of_currencies.push(`"${document.getElementsByClassName("currency_input")[i].getAttribute("currency_name")}"`);
          }
      };

      // DEFINING BOT COMMAND SUBMIT DATA
      var balance_command = document.querySelector("#balance_command_bool_input").checked;
      var simp_command = document.querySelector("#simp_command_bool_input").checked;
      var constant_commands = document.querySelector("#constant_commands_bool_input").checked;
      
      balance_command = balance_command.toString().charAt(0).toUpperCase() + balance_command.toString().slice(1);
      simp_command = simp_command.toString().charAt(0).toUpperCase() + simp_command.toString().slice(1);
      constant_commands = constant_commands.toString().charAt(0).toUpperCase() + constant_commands.toString().slice(1);
      
      // MINIGAMES FINAL DATA
      if (rps_cooldown == ''){rps_cooldown=0};
      if (coinFlip_cooldown == ''){coinFlip_cooldown=0};
      
      var minigames_submit = {
        ["rps"]: {"bool":rps_bool_submit, "cooldown": rps_cooldown,"currencies": rps_currency_values_submit, "other_args": {"messages":[rps_victory_message,rps_defeat_message,rps_tie_message]}},
        ["coinFlip"]: {"bool":coinFlip_bool_submit, "cooldown": coinFlip_cooldown,"currencies": coinFlip_currency_values_submit, "other_args": {"messages":[coinFlip_victory_message,coinFlip_defeat_message]}},
      };

      // CURRENCY FINAL DATA
      var currency_submit = list_of_currencies;

      // BOT COMMANDS FINAL DATA
      var bot_commands_submit = {
        "balance": balance_command,
        "simp": simp_command,

        "constants": constant_commands,
      };
      
      // SUBMITTING DATA
      if (
          bot_name_submit != "" &&
          token_submit != "" &&
          owner_id_submit != "" &&
          client_id_submit != "" &&
          directory_submit != ""
      ) {
          var sendingData = {
            "bot_name": bot_name_submit,
            "owner_id": owner_id_submit,
            "token": token_submit,
            "client_id": client_id_submit,
            "directory": directory_submit,
            "minigames": minigames_submit,
            "currency": currency_submit,
            "bot_commands": bot_commands_submit,
          };
          ipcRenderer.send("pass_newbot_data", sendingData);
      };
   });
});

