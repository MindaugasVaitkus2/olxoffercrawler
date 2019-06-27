function searchOffers(){
	var pattern = $("#search").val()
	var offers = document.getElementsByTagName("li") 

	for(var i=0; i<offers.length; ++i){
		var title = offers[i].getElementsByClassName("title")[0].textContent
		var location = offers[i].getElementsByClassName("location")[0].textContent

		if(title.toLowerCase().indexOf(pattern) !== -1 ||
				location.toLowerCase().indexOf(pattern) !== -1)
			offers[i].style.display = ""
		else
			offers[i].setAttribute("style", "display: none !important")
	}
}

$("#search").on("keyup", function(){
	searchOffers()
})