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

function sortOffersByName(){
	var pattern = $("#search").val().toLowerCase()
	var offers = document.getElementsByTagName("li") 

	for(var i=0; i<offers.length; ++i){
		var title = offers[i].getElementsByClassName("title")[0].textContent
		var location = offers[i].getElementsByClassName("location")[0].textContent

		if(matchWords(title, pattern) || matchWords(location, pattern))
			offers[i].style.display = ""
		else
			offers[i].setAttribute("style", "display: none !important")
	}
}

function sortOffersByPrice(){
	var priceMin = $("#price-min").val() 
	var priceMax = $("#price-max").val()

	priceMin = (priceMin != "" && !isNaN(priceMin)) ? parseInt(priceMin) : -INFINITY
	priceMax = (priceMax != "" && !isNaN(priceMax)) ? parseInt(priceMax) : INFINITY

	var offers = document.getElementsByTagName("li") 

	for(var i=0; i<offers.length; ++i){
		var price = parseInt(offers[i].getElementsByClassName("price")[0].textContent.replace(/\D/g,''));

		if(price >= priceMin && price <= priceMax)
			offers[i].style.display = ""
		else
			offers[i].setAttribute("style", "display: none !important")
	}
}

$("#search").on("keyup", function(){
 	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffersByName, doneTypingInterval)
})

$("#search").on('keydown', function () {
  clearTimeout(typingTimer)
})

$("#price-min, #price-max").on("keyup", function(){
	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffersByPrice, doneTypingInterval)
})

$("#price-min, #price-max").on("keydown", function(){
	clearTimeout(typingTimer)
  	typingTimer = setTimeout(sortOffersByPrice, doneTypingInterval)	
})