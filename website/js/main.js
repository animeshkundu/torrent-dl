/**
 * torrent-dl Website - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            mobileMenuBtn.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navLinks.classList.remove('active');
                mobileMenuBtn.classList.remove('active');
            });
        });
    }
    
    // Copy to clipboard functionality
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const textToCopy = btn.getAttribute('data-copy');
            
            navigator.clipboard.writeText(textToCopy).then(function() {
                btn.classList.add('copied');
                
                // Show checkmark temporarily
                const originalHTML = btn.innerHTML;
                btn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>';
                
                setTimeout(function() {
                    btn.classList.remove('copied');
                    btn.innerHTML = originalHTML;
                }, 2000);
            }).catch(function(err) {
                console.error('Failed to copy:', err);
            });
        });
    });
    
    // Platform tabs
    const platformTabs = document.querySelectorAll('.platform-tab');
    const platformPanels = document.querySelectorAll('.platform-panel');
    
    platformTabs.forEach(function(tab) {
        tab.addEventListener('click', function() {
            const platform = tab.getAttribute('data-platform');
            
            // Update active tab
            platformTabs.forEach(function(t) {
                t.classList.remove('active');
            });
            tab.classList.add('active');
            
            // Update active panel
            platformPanels.forEach(function(panel) {
                panel.classList.remove('active');
            });
            document.getElementById(platform).classList.add('active');
        });
    });
    
    // Navbar background on scroll
    const navbar = document.getElementById('navbar');
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(12, 17, 23, 0.95)';
        } else {
            navbar.style.background = 'rgba(12, 17, 23, 0.9)';
        }
        lastScrollY = window.scrollY;
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const href = anchor.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});
