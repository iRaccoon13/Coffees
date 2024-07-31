document.querySelector("#caffeine-slider").oninput = function() {
	document.querySelector("#caffeine-slider-output").innerText = this.value != 0 ? this.value : this.value + " - Decaf";
};

document.querySelector("#date").min = now();

var now = () => Date().toJSON();

document.querySelector("#date").value = now();

var coffee = document.querySelector("#coffee").value;
var flavor = document.querySelector("#flavor").value;

var var1 = !document.querySelector("#coffee").value == coffee

document.querySelector("form").onsubmit = () => {
	if (document.querySelector("#coffee").value != coffee && document.querySelector("#flavor").value != flavor) {
		return true;
	} else {
		alert("Select a coffee and flavor! ");
		return false;
	}
}
