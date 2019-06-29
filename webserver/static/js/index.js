const doneTypingInterval = 300 
const INFINITY = 1000000001

var typingTimer;


function sortOffers(){
	var wordPattern = $("#search").val().toLowerCase()
	var priceMin = $("#price-min").val() 
	var priceMax = $("#price-max").val()

	priceMin = (priceMin != "" && !isNaN(priceMin)) ? parseInt(priceMin) : -INFINITY
	priceMax = (priceMax != "" && !isNaN(priceMax)) ? parseInt(priceMax) : INFINITY

	var offers = document.getElementsByTagName("li") 

	for(var i=0; i<offers.length; ++i){
		var price = parseInt(offers[i].getElementsByClassName("price")[0].textContent.replace(/\D/g,''));
		var title = offers[i].getElementsByClassName("title")[0].textContent
		var location = offers[i].getElementsByClassName("location")[0].textContent

		if(price >= priceMin && price <= priceMax && (matchWords(title, wordPattern) || matchWords(location, wordPattern)))
			offers[i].style.display = ""
		else
			offers[i].setAttribute("style", "display: none !important")
	}
}

$("#price-min, #price-max").on("keyup", function(e){
	if((e.keyCode < 48 || e.keyCode > 57) && $(this).val() != "")
		return 

	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffers, doneTypingInterval)
})

$("#price-min, #price-max").on("keydown", function(e){
	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffers, doneTypingInterval)	
})

$(document).ready(function(){
	$('#offers-table').DataTable();
})

$(".img-thumbnail").on("click", function() {
   $('#imagepreview').attr('src', $(this).attr('src'));
   $('#imagemodal').modal('show'); 
});

$("#imagemodal").on("click", function(){
	$(this).modal("hide")
})