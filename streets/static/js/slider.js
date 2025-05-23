
const runSlider = (selector) => {
	$(selector).slick({
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		variableWidth: false,
		centerMode: false,
		responsive: [
		  {
			breakpoint: 1000,
			settings: {
			  slidesToShow: 2,
			  slidesToScroll: 1,
			}
		  },
		  {
			breakpoint: 630,
			settings: {
				slidesToShow: 1,
				arrows: false,
			}
		  }
		]
	});
} 
