$(window).scroll(function () {
    if ($(document).scrollTop() > 100) {
       $(".navbar").css("animation", "NavBGAnimationBack .3s ease-in-out forwards");
       $("nav a").css("animation", "NavFontAnimationBack .3s ease-in-out forwards");
       $(".navbar-right a").css("animation", "NavFontAnimationBack .3s ease-in-out forwards");
    } else {
       $(".navbar").css("animation", "NavBGAnimation .3s ease-in-out forwards");
       $("nav a").css("animation", "NavFontAnimation .3s ease-in-out forwards");
       $(".navbar-right a").css("animation", "NavFontAnimationBack .3s ease-in-out forwards");
    }
 });
 