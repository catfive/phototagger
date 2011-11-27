$(document).ready(function(){

	$('div.photo').hover(function(){
		$(this).css({
			'border':'5px solid white'
		});	
	},
	function(){
		$(this).css({
			'background':'#494949',
			'border':'5px solid #494949'
		});	
	})
	.click(function(e){
		if ( ! $(this).hasClass('selected') ){
			$('div.selected').removeClass('selected');
			$('div.fields').fadeOut('fast');
			$(this)
				.addClass('selected')
				.children('form')
					.children('div.fields')
						.css({
							'top':e.pageY-51,
							'left':e.pageX+20
						})
						.fadeIn('fast');		
		}
		else if ( ! $('div.fields').is(':visible') ){
			$(this).children('form')
				.children('div.fields')
					.css({
						'top':e.pageY-51,
						'left':e.pageX+20
					})
					.fadeIn('fast');
		}
	});
	$('a.close').click(function(){
		$(this).parent('div.fields').fadeOut('fast');
	});
	$('textarea#id_description').prev('label')
		.click(function(){
			$(this).next('textarea').slideDown();	
		});
});
