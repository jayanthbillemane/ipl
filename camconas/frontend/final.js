// header('Access-Control-Allow-Origin: *');
// header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
// header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token');

const uri = "http://127.0.0.1:5000/match_list";
let ipl = [];

function getMatchDetails() {
  fetch(uri)
    .then(response => response.json())
    .then(data => _displayItems(data))
    .catch(error => console.error("Unable to get Details.", error));
}

function addMatchDetails() {
  const cityInputText = document.getElementById("add-city");
  const stadiumInputText = document.getElementById("add-stadium");
  const team1InputText = document.getElementById("add-team1");
  const team2InputText = document.getElementById("add-team2");
  const dateInputText = document.getElementById("add-date");
  const pomInputText = document.getElementById("add-pom");
  const neuvenInputText = document.getElementById("add-neuven");

  const item = {
    city: cityInputText.value.trim(),
    venue: stadiumInputText.value.trim(),
    team1: team1InputText.value.trim(),
    team1: team2InputText.value.trim(),
    date: parseInt(dateInputText.value.trim()),
    player_of_match: pomInputText.value.trim(),
    neutral_venue: neuvenInputText.value.trim(),
  };
  console.log(JSON.stringify(item));
  fetch(uri, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(item)
  })
    .then(response => response.json())
    .then(() => {
      getMatchDetails();
      cityInputText.value = "";
      stadiumInputText.value = "";
      team1InputText.value = "";
      team2InputText.value = "";
      dateInputText.value = "";
      pomInputText.value = "";
      neuvenInputText.value = "";
    })
    .catch(error => console.error("Unable to Add Team.", error));
}

function deleteBookItem() {
  const itemId = document.getElementById("delete-id").value.trim();
  fetch(`${uri}/${itemId}`, {
    method: "DELETE"
  })
    .then(() => getMatchDetails())
    .catch(error => console.error("Unable to delete Book.", error));
}

function displayDeleteForm(id) {
  const item = ipl.find(item => item.id === id);
  document.getElementById("delete-id").value = item.id;
}

function displayEditForm(id) {
  const item = ipl.find(item => item.id === id);
  document.getElementById("edit-id").value = item.id;
  document.getElementById("edit-city").value = item.city;
  document.getElementById("edit-stadium").value = item.venue;
  document.getElementById("edit-team1").value = item.team1;
  document.getElementById("edit-team2").value = item.team2;
  document.getElementById("edit-date").value = item.date;
  document.getElementById("edit-pom").value = item.player_of_match;
  document.getElementById("edit-neuven").value = item.neutral_venue;
}

function updateBookItem() {
  const itemId = document.getElementById("edit-id").value.trim();
  const item = {
    id: parseInt(itemId, 10),
    city: document.getElementById("edit-city").value.trim(),
    venue: document.getElementById("edit-stadium").value.trim(),
    team1: document.getElementById("edit-team1").value.trim(),
    team2: document.getElementById("edit-team2").value.trim(),
    date: document.getElementById("edit-date").value.trim(),
    player_of_match: document.getElementById("edit-pom").value.trim(),
    neutral_venue: document.getElementById("edit-neuven").value.trim(),


  };
// console.log(date)

  fetch(`${uri}/${itemId}`, {
    method: "PUT",
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        crossOrigin: null,
        credentials: 'same-origin',
        referrerPolicy: 'no-referrer',
    },
    body: JSON.stringify(item)
  })
    .then(() => getMatchDetails())
    .catch(error => console.error("Unable to update item.", error));

  return false;
}

function _displayCount(itemCount) {
  const name = itemCount === 1 ? "entry" : "entries";
  document.getElementById(
    "counter"
  ).innerHTML = `Showing <b>${itemCount}</b> ${name}`;
}

function _displayItems(data) {
  const tBody = document.getElementById("ipl");
  tBody.innerHTML = "";
  _displayCount(data.length);
  const button = document.createElement("button");

  data.forEach(item => {
    let editButton = document.createElement("a");
    editButton.href = "#editIplModal";
    editButton.className = "edit";
    editButton.setAttribute("onclick", `displayEditForm(${item.id})`);
    editButton.setAttribute("data-toggle", "modal");
    editButton.innerHTML =
      "<i class='material-icons' data-toggle='tooltip' title='Edit'>&#xE254;</i>";

    // let deleteButton = document.createElement("a");
    // deleteButton.href = "#deleteIplModal";
    // deleteButton.className = "delete";
    // deleteButton.setAttribute("onclick", `displayDeleteForm(${item.id})`);
    // deleteButton.setAttribute("data-toggle", "modal");
    // deleteButton.innerHTML =
    //   "<i class='material-icons' data-toggle='tooltip' title='Delete'>&#xE872;</i>";

    let tr = tBody.insertRow();

    let td1 = tr.insertCell(0);
    let textCity = document.createTextNode(item.city);
    td1.appendChild(textCity);

    let td2 = tr.insertCell(1);
    let textVenue = document.createTextNode(item.venue);
    td2.appendChild(textVenue);

    let td3 = tr.insertCell(2);
    let textTeam1 = document.createTextNode(item.team1);
    td3.appendChild(textTeam1);

    let td4 = tr.insertCell(3);
    let textTeam2 = document.createTextNode(item.team2);
    td4.appendChild(textTeam2);

    let td5 = tr.insertCell(4);
    let textDate = document.createTextNode(item.date);
    td5.appendChild(textDate);

    let td6 = tr.insertCell(5);
    let textpom = document.createTextNode(item.player_of_match);
    td6.appendChild(textpom);

    let td7 = tr.insertCell(6);
    let neuven = document.createTextNode(item.neutral_venue);
    td7.appendChild(neuven);

    let td8 = tr.insertCell(7);
    td8.appendChild(editButton);
    // td8.appendChild(deleteButton);
  });

  ipl = data;
}