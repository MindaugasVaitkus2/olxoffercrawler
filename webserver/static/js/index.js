function copyToClipboard(link) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(link).select();
    document.execCommand("copy");
    $temp.remove();
}

$(document).ready(function(){
	$('#offers-table').DataTable()
	$("#offers-table").on('page.dt', function() {
  		$('html, body').animate({
    	scrollTop: $(".dataTables_wrapper").offset().top
  		}, 'slow');
	});

 	$(".img-thumbnail").on("click", function() {
   		$('#imagepreview').attr('src', $(this).attr('src'));
   		$('#imagemodal').modal('show'); 
	});

	$("#imagemodal").on("click", function(){
		$(this).modal("hide")
	})

	$(".clipboard").on("click", function(){
		var link = $(this).parent().parent().parent().children("h2").children("a").attr("href")
		copyToClipboard(link)
	})

})
