let slideIndex = 0;
        showSlides();

        function showSlides() {
            let i;
            let slides = document.getElementsByClassName("slide");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slideIndex++;
            if (slideIndex > slides.length) {
                slideIndex = 1;
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex - 1].style.display = "block";
            dots[slideIndex - 1].className += " active";
            setTimeout(showSlides, 5000); // Change image every 5 seconds
        }

        function moveSlide(n) {
            slideIndex += n - 1;
            showSlides();
        }

        function currentSlide(n) {
            slideIndex = n;
            showSlides();
        }
        document.addEventListener('DOMContentLoaded', function () {
        const popup = document.getElementById('popup');
        const closeButton = document.getElementById('close-btn');

        if (!popup || !closeButton) {
            console.error('Popup or close button not found.');
            return;
        }

        // Check if the popup should be shown
        function shouldShowPopup() {
            const lastShown = localStorage.getItem('popupLastShown');
            if (lastShown) {
                const now = new Date().getTime();
                const fiveMinutes = 5 * 60 * 1000; // 5 minutes in milliseconds
                return now - lastShown >= fiveMinutes;
            }
            return true;
        }

        // Show the popup
        function showPopup() {
            popup.style.display = 'flex';
            localStorage.setItem('popupLastShown', new Date().getTime());
        }

        // Hide the popup
        function hidePopup() {
            popup.style.display = 'none';
        }

        // Event listeners
        if (shouldShowPopup()) {
            showPopup();
        }

        closeButton.addEventListener('click', hidePopup);

        // Optional: Hide the popup when clicking outside the content
        popup.addEventListener('click', function (event) {
            if (event.target === popup) {
                hidePopup();
            }
        });
    });



  tinymce.init({
    selector: 'textarea#editor',
    menubar: false,
    plugins: 'link image media',
    toolbar: 'undo redo | formatselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image media',
    content_css: '//www.tiny.cloud/css/codepen.min.css'
  });

  document.querySelectorAll('.dropdown a').forEach(function(dropdownToggle) {
    dropdownToggle.addEventListener('click', function() {
        this.parentElement.classList.toggle('active');
    });
});
