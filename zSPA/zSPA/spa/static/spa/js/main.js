$(document).ready(function() {

  function convertRemToPixels(rem) {    
    return rem * parseInt(getComputedStyle(document.documentElement).fontSize);
  }

  $('a[href^="#"]').on('click', function(e) {
    e.preventDefault();

    let xOffset = convertRemToPixels($('header').height()/10);   

    var target = this.hash;
    var $target = $(target);

    $('html, body').stop().animate({
      'scrollTop': $target.offset().top - xOffset
    }, 900, 'swing', 
    function() {      
      window.location.hash = target - xOffset;
    }
    );

  });


});
