$(document).ready(function() {

    /* ======= Scrollspy ======= */
   $('body').scrollspy({ target: '#page-nav-wrapper', offset: 100});
    
    /* ======= ScrollTo ======= */
    $('.scrollto').on('click', function(e){
        
        //store hash
        var target = this.hash;
                
        e.preventDefault();
        
		$('body').scrollTo(target, 800, {offset: -60, axis:'y'});
		
	});
	
	/* ======= Fixed page nav when scrolled ======= */    
    $(window).on('scroll resize load', function() {
        
        $('#page-nav-wrapper').removeClass('fixed');
         
         var scrollTop = $(this).scrollTop();
         var topDistance = $('#page-nav-wrapper').offset().top;
         
         if ( (topDistance) > scrollTop ) {
            $('#page-nav-wrapper').removeClass('fixed');
            $('body').removeClass('sticky-page-nav');
         }
         else {
            $('#page-nav-wrapper').addClass('fixed');
            $('body').addClass('sticky-page-nav');
         }

    });
    
    new Clipboard('.clipboard-copy');
    hljs.initHighlightingOnLoad();
    $('.clipboard-copy').prop('title', 'Copy to Clipboard').tooltip();

    $('.linkable').each(function() {
        let e = $(this);
        let eId = e.attr('id');
        if (e.prop('tagName') == "A") {
            e.after(
                '<a id="' + eId + 'LinkButton" class="headerlink" style="opacity:0" href="#' + eId + '" title="Permalink to this headline">¶</a><a class="offsetAnchor" id="' + eId + '"></a>'
            );
        } else {
            e.append(
                '<a id="' + eId + 'LinkButton" class="headerlink" style="opacity:0" href="#' + eId + '" title="Permalink to this headline">¶</a><a class="offsetAnchor" id="' + eId + '"></a>'
            );
        }
        e.attr('id', eId + 'Text').hover(
            function() {  // Mouse Enter
                $('#' + eId + 'LinkButton').css('opacity', 1);
            },
            function() {  // Mouse Exit
                $('#' + eId + 'LinkButton').css('opacity', '0');
            }
        );
    });

});