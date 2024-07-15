document.querySelector("#submit_btn").onclick = function(e) {
	var coffees = [];
	var flavors = [];
	for (elem of document.querySelector("#coffees").firstElementChild.children) {
		if (elem.innerText != "\n" && elem.innerText != "") coffees.push(elem.innerText);
	};
	for (elem of document.querySelector("#flavors").firstElementChild.children) {
		if (elem.innerText != "\n" && elem.innerText != "") flavors.push(elem.innerText);
	};
	console.log(coffees);
	console.log(flavors);

	fetch("/menu/", {
		method: "PUT",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify({"coffees": coffees, "flavors": flavors})
	})
};