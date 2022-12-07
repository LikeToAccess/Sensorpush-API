function httpPostAsync(url, callback) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() {
		// console.log(xmlHttp);
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
			callback(xmlHttp.responseText);
		else if (xmlHttp.readyState == 4 && xmlHttp.status != 200)
			alert(xmlHttp.responseText);
	};
	xmlHttp.open("POST", url, true); // true for asynchronous
	xmlHttp.send(null);
}

function httpGetAsync(url, callback) {
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.onreadystatechange = function() {
		// console.log(xmlHttp);
		if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
			callback(xmlHttp);
		else if (xmlHttp.readyState == 4 && xmlHttp.status != 200)
			alert(xmlHttp);
	};
	xmlHttp.open("GET", url, true); // true for asynchronous
	xmlHttp.send(null);
}

function displayData(response) {
	responseCodeElement = document.getElementById("response-code");
	dataElement = document.getElementById("data");

	data = JSON.parse(response.responseText).data;

	// console.log(response.status);
	// console.log(data);

	responseCodeElement.innerHTML = response.status;
	dataElement.innerHTML = JSON.stringify(data);
}

button = document.getElementById("button");
button.addEventListener("click", () => {
	httpGetAsync("http://127.0.0.1:8080/api/v1/sensorpush", displayData);
	// console.log(response);
});
