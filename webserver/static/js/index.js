const doneTypingInterval = 300 
const INFINITY = 1000000001

var typingTimer;


function matchWords(str, pattern){
	var words = pattern.split(" ")
	var numberOfMatchedWords = 0

	for(var i=0; i<words.length; i++)
		if(str.indexOf(words[i]) !== -1){
			str.replace(words[i], "")
			++numberOfMatchedWords
		}
			
	return (numberOfMatchedWords === words.length)	
}

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

	updateNumberOfOffers()
}

function updateNumberOfOffers(){
	var offersLen = $("li:visible").length
	$("#offers-numbers").text(offersLen + " offers")
}

$("#search").on("keyup", function(){
 	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffers, doneTypingInterval)
})

$("#search").on('keydown', function () {
  clearTimeout(typingTimer)
})

$("#price-min, #price-max").on("keyup", function(){
	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffers, doneTypingInterval)
})

$("#price-min, #price-max").on("keydown", function(){
	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffers, doneTypingInterval)	
})

$(document).ready(function(){
	updateNumberOfOffers()
})