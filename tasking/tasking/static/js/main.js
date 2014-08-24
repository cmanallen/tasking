$(document).ready(function() {
	/**
	 * Reserved Classes
	 */
	$('.datepicker').datepicker();
	$('.hidden').hide();


	/**
	 * Animations Controllers
	 */
	var display;
	// On click pop-up element
	$('.pop-up-controller').click(function() {
		display = $(this).attr("href");
		if ($(display).is(':visible')) {
			closeAnimation();
		} else {
			openAnimation();
		};
	});
	// Set <escape> key to call close animation
	$(document).keyup(function(e) {
		if (e.keyCode == 27) {
			closeAnimation();
		}
	});


	/**
	 * Functions
	 */
	var openAnimation = function() {
		$(display).fadeIn('fast');
		// Apply styling to animate from
		$(display + ' .pop-up-container .pop-up-head').css('margin-top', '600px');
		$(display + ' .pop-up-container .pop-up-body').css('margin-top', '500px');
		// Animate that styling
		$(display + ' .pop-up-container .pop-up-head').animate({
			'margin-top':'0px',
		}, 350);
		$(display + ' .pop-up-container .pop-up-body').animate({
			'margin-top':'30px',
		}, 300);
		$(display + ' .pop-up-container .pop-up-body').animate({
			'margin-top':'40px',
		}, 200);
	};
	var closeAnimation = function() {
		$(display).fadeOut('normal');
		$(display + ' .pop-up-container .pop-up-head').animate({
			'margin-top':'600px',
		}, 600);
		$(display + ' .pop-up-container .pop-up-body').animate({
			'margin-top':'500px',
		}, 600);
	};
});
