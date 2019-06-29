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