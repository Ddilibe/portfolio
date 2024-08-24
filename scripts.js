$(document).ready(function() {
    var $navbar = $('#navbar');
  
    $(window).scroll(function() {
      var scrollTop = $(this).scrollTop();
      var section1Top = $('#section1').offset().top;
      var section2Top = $('#section2').offset().top;
      var section3Top = $('#section3').offset().top;
  
      if (scrollTop >= section1Top && scrollTop < section2Top) {
        $navbar.css('background-color', '#007bff');
      } else if (scrollTop >= section2Top && scrollTop < section3Top) {
        $navbar.css('background-color', '#28a745');
      } else if (scrollTop >= section3Top) {
        $navbar.css('background-color', '#dc3545');
      } else {
        $navbar.css('background-color', 'transparent');
      }
    });
  });