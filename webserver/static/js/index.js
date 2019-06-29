function copyToClipboard(link) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val(link).select();
    document.execCommand("copy");
    $temp.remove();
}

$(document).ready(function(){
	$('#offers-table').DataTable({
		"fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {
			var $clipboard = $(nRow).find(".clipboard")

			$clipboard.on("click", function(){
				var link = $(this).parent().parent().parent().children("h2").children("a").attr("href")
				copyToClipboard(link)

				$(this).animate({opacity: 0.5},  250, function(){
					$(this).animate({opacity: 1}, 250)
				})
			})		
			
			var $thumbnail = $(nRow).find(".img-thumbnail")

			$thumbnail.on("click", function() {
   				$('#imagepreview').attr('src', $(this).attr('src'));
   				$('#imagemodal').modal('show'); 
			});

		}
	})

	$("#offers-table").on('page.dt', function() {
  		$('html, body').animate({
    		scrollTop: $(".dataTables_wrapper").offset().top
  		}, 'slow');
	});
	
	$("#imagemodal").on("click", function(){
		$(this).modal("hide")
	})
})
