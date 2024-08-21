let socket = new WebSocket("wss://" + location.host + "/fetchorders/");
console.log("happy birthday");

var refresh_btns = () => {document.querySelectorAll("#orders_container div button").forEach((elem) => {
	elem.onclick = (e) => {
		fetch("/order/"+e.target.parentElement.getAttribute('data-orderid')+"/", {
			method: "PATCH", 
			headers: {"Content-Type": 'application/json'},
			body: JSON.stringify({"is_completed": true, "is_archived": true})
		});
		e.target.parentElement.remove();
		console.log("goodbye cruel world")
	};
});};

socket.onmessage = (e) => {
	console.log("ding")
	console.log(e.data);
	//alert("ding");
	document.querySelector("#orders_container").innerHTML = e.data;
	refresh_btns();
};

socket.onopen = () => {
	console.log("yay");
};
socket.onclose = () => {
	console.log("uh oh");
	//alert("oops");
};
