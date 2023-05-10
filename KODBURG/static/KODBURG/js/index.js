
// 

(function () {
  var top_1 = document.querySelector(".welc");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelector(".card-title");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInLeft");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelector(".card-img-top");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInRight");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelector(".card-text");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInUp");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelector(".what-you-learn");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });

  observer.observe(top_1);
})();
(function () {
  var top_1 = document.querySelectorAll(".card")[1];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInRight");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".card")[2];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__zoomIn");
      }
    });
  });

  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".card")[3];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInLeft");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".from-h2")[0];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".from-h2")[1];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".from-h2")[2];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelector(".submit");

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInUp");
      }
    });
  });
  observer.observe(top_1);
})();
(function () {
  var top_1 = document.querySelectorAll(".input-class")[0];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".input-class")[1];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__zoomIn");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".input-class")[2];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__zoomIn");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll(".input-class")[3];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInUp");
      }
    });
  });
  observer.observe(top_1);
})();



(function () {
  var top_1 = document.querySelectorAll("label")[0];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInDown");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll("label")[1];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__zoomIn");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll("label")[2];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__zoomIn");
      }
    });
  });
  observer.observe(top_1);
})();

(function () {
  var top_1 = document.querySelectorAll("label")[3];

  var observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (
        typeof getCurrentAnimationPreference === "function" &&
        !getCurrentAnimationPreference()
      ) {
        return;
      }

      if (entry.isIntersecting) {
        entry.target.classList.add("animate__animated");
        entry.target.classList.add("animate__fadeInUp");
      }
    });
  });
  observer.observe(top_1);
})();


