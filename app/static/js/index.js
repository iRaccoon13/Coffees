document.querySelectorAll("#favorites button").forEach(function(elem) {
	elem.onclick = function(event) {
		let node = document.querySelector("#favorites_popup").cloneNode(true);
		node.firstElementChild.innerText = elem.getAttribute("data-coffee");
		node.setAttribute("data-orderid", elem.getAttribute("data-orderid"));
		node.setAttribute("id", "popup")
		node.lastElementChild.onclick = popup_cancel;
		node.children[1].innerText = elem.getAttribute("data-flavor");
		node.children[2].innerText = elem.getAttribute("data-special");
		node.children[3].onclick = orderthis
		node.children[5].onclick = delfav;
		document.body.appendChild(node);
		node.style.display = "block";
	};
});

function popup_cancel() {
	document.querySelectorAll(".popup").forEach(function(elem) {
		elem.remove();
	})
};

async function delfav(e) {
	if (confirm("Are you sure you want to remove this favorite?")) {
		let response = await fetch("/order/"+e.target.parentElement.getAttribute("data-orderid")+"/removefavorite/", {method:"POST"});
		if (response.status == 200) {
			location.reload();
			alert("Success!");
		} else {
			alert("There was an issue removing this favorite. ");
		}
	} else {
		alert("Nothing happened! ")
	}
};

async function orderthis(e) {
	if (confirm('Are you sure you want to order this?')) {
		let response = await fetch("/order/"+e.target.parentElement.getAttribute("data-orderid")+"/copy/", {method: "POST"});
		if (response.status == 200) {
			popup_cancel();
			alert("Success!");
		} else {
			alert("There was an issue ordering this. ");
		}
	} else {
		alert("Nothing happened! ");
	}
};