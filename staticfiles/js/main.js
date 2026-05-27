// Counter animation
function animateCounters() {
  const counters = document.querySelectorAll('[data-count]');
  counters.forEach(el => {
    const target = parseInt(el.dataset.count);
    const suffix = el.dataset.suffix || '';
    let current = 0;
    const increment = target / 60;
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current) + suffix;
    }, 24);
  });
}

// Intersection observer for counters
const statsSection = document.querySelector('.stats-strip');
if (statsSection) {
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      animateCounters();
      observer.disconnect();
    }
  }, { threshold: 0.3 });
  observer.observe(statsSection);
}

// Mobile nav
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');
if (hamburger && navLinks) {
  hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('open');
  });
}

// Scroll reveal
const reveals = document.querySelectorAll('.reveal');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('revealed');
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
reveals.forEach(r => revealObs.observe(r));

// Active nav
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.getAttribute('href') === currentPath ||
     (currentPath === '/' && link.getAttribute('href') === '/')) {
    link.classList.add('active');
  }
});
