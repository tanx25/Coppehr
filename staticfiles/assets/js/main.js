/**
* Template Name: ZenBlog
* Updated: Jan 29 2024 with Bootstrap v5.3.2
* Template URL: https://bootstrapmade.com/zenblog-bootstrap-blog-template/
* Author: BootstrapMade.com
* License: https:///bootstrapmade.com/license/
*/
document.addEventListener('DOMContentLoaded', () => {
  "use strict";

  const selectAsideEntries = document.querySelectorAll('.post-entry-1.border-bottom');
  
  if (selectAsideEntries) {
    selectAsideEntries.forEach(post => {
      post.querySelector('h2').addEventListener('click', function(event) {
        event.preventDefault();
        toggleDisplay(post);
      });
    });
  }
  
  function toggleDisplay(element) {
    let el = element.querySelector('p');
    if(!el) return;
    if (el.style.display === '' || el.style.display === 'none') {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
    el = element.querySelector('h2~a');
    if(!el) return;
    if (el.style.display === '' || el.style.display === 'none') {
      el.style.display = 'block';
    } else {
      el.style.display = 'none';
    }
  }
  
  /**
   * Sticky header on scroll
   */
  const selectHeader = document.querySelector('#header');
  if (selectHeader) {
    document.addEventListener('scroll', () => {
      window.scrollY > 100 ? selectHeader.classList.add('sticked') : selectHeader.classList.remove('sticked');
    });
  }

  /**
   * Mobile nav toggle
   */

  const mobileNavToogleButton = document.querySelector('.mobile-nav-toggle');

  if (mobileNavToogleButton) {
    mobileNavToogleButton.addEventListener('click', function(event) {
      event.preventDefault();
      mobileNavToogle();
    });
  }

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToogleButton.classList.toggle('bi-list');
    mobileNavToogleButton.classList.toggle('bi-x');
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navbar a').forEach(navbarlink => {

    if (!navbarlink.hash) return;

    let section = document.querySelector(navbarlink.hash);
    if (!section) return;

    navbarlink.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');

  navDropdowns.forEach(el => {
    el.addEventListener('click', function(event) {
      if (document.querySelector('.mobile-nav-active')) {
        event.preventDefault();
        this.classList.toggle('active');
        this.nextElementSibling.classList.toggle('dropdown-active');

        let dropDownIndicator = this.querySelector('.dropdown-indicator');
        dropDownIndicator.classList.toggle('bi-chevron-up');
        dropDownIndicator.classList.toggle('bi-chevron-down');
      }
    })
  });

  /**
   * Scroll top button
   */
  const scrollTop = document.querySelector('.scroll-top');
  if (scrollTop) {
    const togglescrollTop = function() {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
    window.addEventListener('load', togglescrollTop);
    document.addEventListener('scroll', togglescrollTop);
    scrollTop.addEventListener('click', window.scrollTo({
      top: 0,
      behavior: 'smooth'
    }));
  }

  /**
   * Hero Slider
   */
  var swiper = new Swiper(".sliderFeaturedPosts", {
    spaceBetween: 0,
    speed: 1000,  // CHANGED 500 -> 1000
    centeredSlides: true,
    loop: true,
    slideToClickedSlide: true,
    autoplay: {
      delay: 7000,  // CHANGED 3000 -> 7000
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".custom-swiper-button-next",
      prevEl: ".custom-swiper-button-prev",
    },
  });

  /**
   * Open and close the search form.
   */
  const searchOpen = document.querySelector('.js-search-open');
  const searchClose = document.querySelector('.js-search-close');
  const searchWrap = document.querySelector(".js-search-form-wrap");

  if (!!searchOpen && !!searchClose && !!searchWrap) {
    searchOpen.addEventListener("click", (e) => {
      e.preventDefault();
      searchWrap.classList.add("active");
    });

    searchClose.addEventListener("click", (e) => {
      e.preventDefault();
      searchWrap.classList.remove("active");
    });
  }

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Animation on scroll function and init
   */
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', () => {
    aos_init();
  });



  /*NEW*/
  const myItemsButton = document.getElementById('myItemsButton');
  const myItemsPanel = document.getElementById('myItemsPanel');
  const closeMenuButton = document.getElementById('closeMenuButton');
  const menuOverlay = document.getElementById('menuOverlay');

  if (myItemsButton && myItemsPanel && closeMenuButton && menuOverlay) {
    // Show the My Items panel
    myItemsButton.addEventListener('click', () => {
      myItemsPanel.classList.add('open');
      menuOverlay.classList.add('open');
    });

    // Hide the My Items panel
    closeMenuButton.addEventListener('click', closeMenuPanel);
    menuOverlay.addEventListener('click', closeMenuPanel);

    function closeMenuPanel() {
      myItemsPanel.classList.remove('open');
      menuOverlay.classList.remove('open');
    }
  } else {
    console.error("My Items panel error.");
  }

});



