 $(document).ready(function() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var csrftoken = getCookie('csrftoken');

    var jssor_1_SlideshowTransitions = [
              {$Duration:1200,x:-0.3,$During:{$Left:[0.3,0.7]},$Easing:{$Left:$Jease$.$InCubic,$Opacity:$Jease$.$Linear},$Opacity:2},
              {$Duration:1200,x:0.3,$SlideOut:true,$Easing:{$Left:$Jease$.$InCubic,$Opacity:$Jease$.$Linear},$Opacity:2}
            ];

            var jssor_1_options = {
              $AutoPlay: 1,
              $SlideshowOptions: {
                $Class: $JssorSlideshowRunner$,
                $Transitions: jssor_1_SlideshowTransitions,
                $TransitionsOrder: 1
              },
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              },
              $BulletNavigatorOptions: {
                $Class: $JssorBulletNavigator$
              },
              $ThumbnailNavigatorOptions: {
                $Class: $JssorThumbnailNavigator$,
                $Cols: 1,
                $Align: 0,
                $NoDrag: true
              }
            };

            try {
                var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);
                //alert(jssor_1_slider);

                function ScaleSlider() {
                var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
                if (refSize) {
                    refSize = Math.min(refSize, 1290);
                    jssor_1_slider.$ScaleWidth(refSize);
                }
                else {
                    window.setTimeout(ScaleSlider, 30);
                }
            }
            }
            catch(err) {
            //alert('ups');
            }



            /*responsive code begin*/
            /*remove responsive code if you don't want the slider scales while window resizing*/

            ScaleSlider();
            $(window).bind("load", ScaleSlider);
            $(window).bind("resize", ScaleSlider);
            $(window).bind("orientationchange", ScaleSlider);

            $('.partners_slick').slick({
                infinite: true,
                slidesToShow: 6,
                slidesToScroll: 6
            });

            $('.video_slick').slick({
                infinite: true,
                slidesToShow: 4,
                slidesToScroll: 4
            });

            $('#ps_wrap').css( "font", "15px 'DINPro'" );

            $('.popup-gallery').magnificPopup({
		        delegate: 'a',
		        type: 'image',
		        tLoading: 'Loading image #%curr%...',
		        mainClass: 'mfp-img-mobile',
		        gallery: {
		        	enabled: true,
			        navigateByImgClick: true,
			        preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		        },
		        image: {
			        tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
			        titleSrc: function(item) {
				        return item.el.attr('title') + '<small>by Marsel Van Oosten</small>';
			        }
		        }
	        });
});

function loadingpartner(data)
{
    alert('Bang');
    alert(data);
    $("#partnerList").append(data);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}