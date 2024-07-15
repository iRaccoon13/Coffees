document.querySelectorAll("#orders_container div button").forEach(function(elem) {
	elem.onclick = function(e) {
		fetch("/order/"+this.parentElement.getAttribute('data-orderid')+"/", {
			method: "PATCH", 
			headers: {"Content-Type": 'application/json'},
			body: JSON.stringify({"is_completed": true, "is_archived": true})
		});
		this.parentElement.remove();
	};
});