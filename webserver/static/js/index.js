$(document).ready(function(){
	$('#offers-table').DataTable()
	$("#offers-table").on('page.dt', function() {
  		$('html, body').animate({
    	scrollTop: $(".dataTables_wrapper").offset().top
  		}, 'slow');
	});
})

$(document).on("click", function(){
	window.scrollTo(0, 0)
}, ".paginate_button")

$(".img-thumbnail").on("click", function() {
   $('#imagepreview').attr('src', $(this).attr('src'));
   $('#imagemodal').modal('show'); 
});

$("#imagemodal").on("click", function(){
	$(this).modal("hide")
})