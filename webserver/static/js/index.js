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
})
