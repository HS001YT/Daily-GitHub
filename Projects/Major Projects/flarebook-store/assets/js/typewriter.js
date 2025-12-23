// ===== SIMPLE AUTO-START TYPEWRITER =====
class TypewriterSearch {
    constructor() {
        this.phrases = [
            "Search books, authors, categories...",
            "Try 'Harry Potter'",
            "Looking for 'The Great Gatsby'?",
            "Search for bestsellers...",
            "Find your next favorite book...",
            "Browse by 'Science Fiction'",
            "Discover new releases...",
            "Search 'Stephen King' books"
        ];
        this.init();
    }

    init() {
        const searchInput = document.getElementById('searchInput');
        if (!searchInput) {
            console.error('Search input not found');
            return;
        }
        
        // Remove default placeholder
        searchInput.removeAttribute('placeholder');
        
        // Create placeholder element
        let placeholderEl = document.getElementById('typewriterPlaceholder');
        if (!placeholderEl) {
            placeholderEl = document.createElement('div');
            placeholderEl.id = 'typewriterPlaceholder';
            placeholderEl.className = 'typewriter-placeholder';
            placeholderEl.textContent = '';
            
            const searchBox = document.querySelector('.search-box');
            if (searchBox) {
                searchBox.appendChild(placeholderEl);
            }
        }
        
        // Make sure it's visible
        placeholderEl.style.opacity = '1';
        placeholderEl.style.visibility = 'visible';
        
        // START ANIMATION IMMEDIATELY
        this.startAnimation(placeholderEl);
        
        // Handle user interactions
        this.setupEventListeners(searchInput, placeholderEl);
    }
    
    startAnimation(placeholderEl) {
        let phraseIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        
        const type = () => {
            const currentPhrase = this.phrases[phraseIndex];
            
            if (isDeleting) {
                // Delete
                placeholderEl.textContent = currentPhrase.substring(0, charIndex - 1);
                charIndex--;
                
                if (charIndex === 0) {
                    isDeleting = false;
                    phraseIndex = (phraseIndex + 1) % this.phrases.length;
                    setTimeout(type, 1000); // Pause before typing next
                    return;
                }
            } else {
                // Type
                placeholderEl.textContent = currentPhrase.substring(0, charIndex + 1);
                charIndex++;
                
                if (charIndex === currentPhrase.length) {
                    isDeleting = true;
                    setTimeout(type, 2000); // Pause before deleting
                    return;
                }
            }
            
            // Continue typing/deleting
            setTimeout(type, isDeleting ? 50 : 100);
        };
        
        // Start the animation
        setTimeout(type, 300); // Small delay to ensure visibility
    }
    
    setupEventListeners(searchInput, placeholderEl) {
        searchInput.addEventListener('focus', () => {
            placeholderEl.style.opacity = '0.3';
        });
        
        searchInput.addEventListener('blur', () => {
            if (!searchInput.value.trim()) {
                placeholderEl.style.opacity = '1';
            }
        });
        
        searchInput.addEventListener('input', () => {
            if (searchInput.value.trim()) {
                placeholderEl.style.opacity = '0';
            } else {
                placeholderEl.style.opacity = '1';
            }
        });
    }
}

// Start automatically as soon as possible
function startTypewriterWhenReady() {
    // Check every 100ms if search input exists
    const checkInterval = setInterval(() => {
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            clearInterval(checkInterval);
            console.log('Starting typewriter automatically...');
            window.typewriterSearch = new TypewriterSearch();
        }
    }, 100);
    
    // Timeout after 5 seconds
    setTimeout(() => clearInterval(checkInterval), 5000);
}

// Start checking immediately
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startTypewriterWhenReady);
} else {
    startTypewriterWhenReady(); // DOM already loaded
}