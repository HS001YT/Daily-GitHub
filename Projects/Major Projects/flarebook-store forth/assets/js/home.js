// ===== HOME PAGE FUNCTIONALITY =====
class HomePage {
    constructor() {
        // Slider state
        this.currentSlide = 0;
        this.slides = [];
        this.slideInterval = null;
        this.slideDuration = 5000; // 5 seconds
        
        // Carousel state
        this.carouselPosition = 0;
        this.carouselStep = 270; // Card width + gap
        
        this.initHeroActionButtons();
        this.init();
    }

    init() {
        console.log('Home page initialized');
        
        // Initialize features
        this.initHeroSlider();
        this.initBookCarousels();
        this.initBookInteractions();
        this.initBannerEffects();
        this.initScrollAnimations();
        this.initPreOrderFunctionality();
        
        // Update cart/wishlist counts
        this.updateCartWishlistCounts();
    }

    initHeroActionButtons() {
    // Hero slider action buttons
    const heroWishlistBtns = document.querySelectorAll('.wishlist-action');
    const heroCartBtns = document.querySelectorAll('.cart-action');
    
    heroWishlistBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            // Navigate to wishlist page
            if (window.flareBookApp) {
                window.flareBookApp.navigateToPage('wishlist');
            }
        });
    });
    
    heroCartBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            // Navigate to cart page
            if (window.flareBookApp) {
                window.flareBookApp.navigateToPage('cart');
            }
        });
    });
    
    // Update counts on hero buttons
    this.updateHeroButtonCounts();
}

updateHeroButtonCounts() {
    const cart = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
    const wishlist = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
    
    // Update hero slider buttons
    const wishlistCounts = document.querySelectorAll('.wishlist-action .action-count');
    const cartCounts = document.querySelectorAll('.cart-action .action-count');
    
    wishlistCounts.forEach(el => {
        el.textContent = `${wishlist.length} ${wishlist.length === 1 ? 'Item' : 'Items'}`;
    });
    
    cartCounts.forEach(el => {
        el.textContent = `${cart.length} ${cart.length === 1 ? 'Item' : 'Items'}`;
    });
}

    // ===== HERO SLIDER =====
    initHeroSlider() {
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelectorAll('.dot');
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        const track = document.querySelector('.slider-track');
        
        if (!slides.length || !track) return;
        
        this.slides = slides;
        
        // Set up dots
        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.goToSlide(index);
            });
        });
        
        // Previous button
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                this.prevSlide();
            });
        }
        
        // Next button
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                this.nextSlide();
            });
        }
        
        // Auto slide
        this.startAutoSlide();
        
        // Pause on hover
        const sliderContainer = document.querySelector('.slider-container');
        if (sliderContainer) {
            sliderContainer.addEventListener('mouseenter', () => {
                this.stopAutoSlide();
            });
            
            sliderContainer.addEventListener('mouseleave', () => {
                this.startAutoSlide();
            });
        }
    }

    goToSlide(index) {
        // Wrap around if out of bounds
        if (index >= this.slides.length) index = 0;
        if (index < 0) index = this.slides.length - 1;
        
        // Update current slide
        this.currentSlide = index;
        
        // Move track
        const track = document.querySelector('.slider-track');
        if (track) {
            track.style.transform = `translateX(-${index * 100}%)`;
        }
        
        // Update dots
        document.querySelectorAll('.dot').forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        
        // Update slides
        this.slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
    }

    nextSlide() {
        this.goToSlide(this.currentSlide + 1);
    }

    prevSlide() {
        this.goToSlide(this.currentSlide - 1);
    }

    startAutoSlide() {
        this.stopAutoSlide(); // Clear any existing interval
        this.slideInterval = setInterval(() => {
            this.nextSlide();
        }, this.slideDuration);
    }

    stopAutoSlide() {
        if (this.slideInterval) {
            clearInterval(this.slideInterval);
            this.slideInterval = null;
        }
    }

    // ===== BOOK CAROUSELS =====
    initBookCarousels() {
        // Featured books carousel
        const featuredTrack = document.querySelector('.books-track');
        const featuredLeftBtn = document.querySelector('.left-scroll');
        const featuredRightBtn = document.querySelector('.right-scroll');
        
        if (featuredTrack && featuredLeftBtn && featuredRightBtn) {
            const itemCount = featuredTrack.children.length;
            const visibleItems = Math.floor(featuredTrack.parentElement.offsetWidth / this.carouselStep);
            const maxScroll = (itemCount - visibleItems) * this.carouselStep;
            
            featuredLeftBtn.addEventListener('click', () => {
                this.carouselPosition = Math.max(0, this.carouselPosition - this.carouselStep);
                featuredTrack.style.transform = `translateX(-${this.carouselPosition}px)`;
                this.updateCarouselButtons(featuredLeftBtn, featuredRightBtn, maxScroll);
            });
            
            featuredRightBtn.addEventListener('click', () => {
                this.carouselPosition = Math.min(maxScroll, this.carouselPosition + this.carouselStep);
                featuredTrack.style.transform = `translateX(-${this.carouselPosition}px)`;
                this.updateCarouselButtons(featuredLeftBtn, featuredRightBtn, maxScroll);
            });
            
            // Initialize button states
            this.updateCarouselButtons(featuredLeftBtn, featuredRightBtn, maxScroll);
            
            // Touch/swipe support
            let startX = 0;
            let isDragging = false;
            
            featuredTrack.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
                isDragging = true;
            });
            
            featuredTrack.addEventListener('touchmove', (e) => {
                if (!isDragging) return;
                e.preventDefault();
                
                const currentX = e.touches[0].clientX;
                const diff = startX - currentX;
                
                if (Math.abs(diff) > 50) {
                    if (diff > 0) {
                        // Swipe left
                        this.carouselPosition = Math.min(maxScroll, this.carouselPosition + this.carouselStep);
                    } else {
                        // Swipe right
                        this.carouselPosition = Math.max(0, this.carouselPosition - this.carouselStep);
                    }
                    featuredTrack.style.transform = `translateX(-${this.carouselPosition}px)`;
                    this.updateCarouselButtons(featuredLeftBtn, featuredRightBtn, maxScroll);
                    isDragging = false;
                }
            });
            
            featuredTrack.addEventListener('touchend', () => {
                isDragging = false;
            });
        }
    }

    updateCarouselButtons(leftBtn, rightBtn, maxScroll) {
        if (!leftBtn || !rightBtn) return;
        
        leftBtn.disabled = this.carouselPosition <= 0;
        rightBtn.disabled = this.carouselPosition >= maxScroll;
        
        leftBtn.style.opacity = leftBtn.disabled ? '0.5' : '1';
        rightBtn.style.opacity = rightBtn.disabled ? '0.5' : '1';
    }

    // ===== BOOK INTERACTIONS =====
    initBookInteractions() {
        // Cart buttons
        document.querySelectorAll('.cart-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.addToCart(e.target.closest('[data-book-id]'));
            });
        });
        
        // Wishlist buttons
        document.querySelectorAll('.wishlist-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.addToWishlist(e.target.closest('[data-book-id]'));
            });
        });
        
        // Quick view buttons
        document.querySelectorAll('.quick-view-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.showQuickView(e.target.closest('[data-book-id]'));
            });
        });
        
        // Pre-order buttons
        document.querySelectorAll('.preorder-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                this.handlePreOrder(e.target);
            });
        });
        
        // Free download buttons
        document.querySelectorAll('.btn-free').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                this.handleFreeDownload(e.target);
            });
        });
        
        // Book card clicks (for potential detail view)
        document.querySelectorAll('.book-card').forEach(card => {
            card.addEventListener('click', (e) => {
                // Only trigger if not clicking on buttons
                if (!e.target.closest('.overlay-btn')) {
                    const bookId = card.querySelector('[data-book-id]')?.dataset.bookId;
                    if (bookId) {
                        this.viewBookDetails(bookId);
                    }
                }
            });
        });
    }

    addToCart(element) {
        const bookId = element?.dataset?.bookId || element.closest('[data-book-id]')?.dataset.bookId;
        if (!bookId) return;
        
        // Get book info
        const bookCard = element.closest('.book-card, .sale-book-card');
        const title = bookCard?.querySelector('.book-title, .sale-book-title')?.textContent || 'Unknown Book';
        const price = bookCard?.querySelector('.current-price, .sale-current')?.textContent || '$0.00';
        
        // Get existing cart
        let cart = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
        
        // Check if already in cart
        const existingItem = cart.find(item => item.id === bookId);
        
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({
                id: bookId,
                title: title,
                price: price,
                quantity: 1,
                image: bookCard?.querySelector('img')?.src || ''
            });
        }
        
        // Save to localStorage
        localStorage.setItem('flarebook_cart', JSON.stringify(cart));
        
        // Update UI
        this.updateCartWishlistCounts();
        this.updateHeroButtonCounts();

        // Show feedback
        this.showToast('Added to cart!', 'success');
        
        // Update badge with animation
        const cartBadge = document.querySelector('#cartBtn .icon-badge');
        if (cartBadge) {
            cartBadge.textContent = cart.length;
            cartBadge.classList.add('pulse');
            setTimeout(() => cartBadge.classList.remove('pulse'), 300);
        }
    }

    addToWishlist(element) {
        const bookId = element?.dataset?.bookId || element.closest('[data-book-id]')?.dataset.bookId;
        if (!bookId) return;
        
        // Get book info
        const bookCard = element.closest('.book-card');
        const title = bookCard?.querySelector('.book-title')?.textContent || 'Unknown Book';
        const price = bookCard?.querySelector('.current-price')?.textContent || '$0.00';
        
        // Get existing wishlist
        let wishlist = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
        
        // Check if already in wishlist
        const existingItem = wishlist.find(item => item.id === bookId);
        
        if (!existingItem) {
            wishlist.push({
                id: bookId,
                title: title,
                price: price,
                image: bookCard?.querySelector('img')?.src || '',
                addedAt: new Date().toISOString()
            });
            
            // Save to localStorage
            localStorage.setItem('flarebook_wishlist', JSON.stringify(wishlist));
            
            // Update UI
            this.updateCartWishlistCounts();
            this.updateHeroButtonCounts();

            // Show feedback
            this.showToast('Added to wishlist!', 'success');
            
            // Update badge with animation
            const wishlistBadge = document.querySelector('#favoritesBtn .icon-badge');
            if (wishlistBadge) {
                wishlistBadge.textContent = wishlist.length;
                wishlistBadge.classList.add('pulse');
                setTimeout(() => wishlistBadge.classList.remove('pulse'), 300);
            }
            
            // Change heart icon to filled
            const heartIcon = element.querySelector('i');
            if (heartIcon) {
                heartIcon.classList.remove('far');
                heartIcon.classList.add('fas');
            }
        } else {
            this.showToast('Already in wishlist!', 'info');
        }
    }

    showQuickView(element) {
        const bookId = element?.dataset?.bookId;
        if (!bookId) return;
        
        // In a real app, this would fetch book details
        // For now, show a preview alert
        const bookCard = element.closest('.book-card');
        const title = bookCard?.querySelector('.book-title')?.textContent || 'Unknown Book';
        const author = bookCard?.querySelector('.book-author')?.textContent || 'Unknown Author';
        const price = bookCard?.querySelector('.current-price')?.textContent || '$0.00';
        
        // Create quick view modal
        this.createQuickViewModal(title, author, price, bookId);
    }

    createQuickViewModal(title, author, price, bookId) {
        // Remove existing modal
        const existingModal = document.querySelector('.quick-view-modal');
        if (existingModal) existingModal.remove();
        
        // Create modal
        const modal = document.createElement('div');
        modal.className = 'quick-view-modal';
        modal.innerHTML = `
            <div class="modal-overlay"></div>
            <div class="modal-content">
                <button class="modal-close">
                    <i class="fas fa-times"></i>
                </button>
                <div class="modal-body">
                    <div class="modal-book-image">
                        <img src="https://images.unsplash.com/photo-1543002588-bfa74002ed7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="${title}">
                    </div>
                    <div class="modal-book-info">
                        <h2 class="modal-book-title">${title}</h2>
                        <p class="modal-book-author">by ${author}</p>
                        <div class="modal-book-price">${price}</div>
                        <p class="modal-book-desc">
                            A captivating story that will keep you on the edge of your seat. 
                            This book has received rave reviews from critics and readers alike.
                        </p>
                        <div class="modal-book-details">
                            <div class="detail-item">
                                <span class="detail-label">Format:</span>
                                <span class="detail-value">Paperback, eBook</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Pages:</span>
                                <span class="detail-value">320 pages</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Publisher:</span>
                                <span class="detail-value">FlareBook Press</span>
                            </div>
                        </div>
                        <div class="modal-actions">
                            <button class="btn btn-primary add-to-cart-modal" data-book-id="${bookId}">
                                <i class="fas fa-shopping-cart"></i> Add to Cart
                            </button>
                            <button class="btn btn-outline add-to-wishlist-modal" data-book-id="${bookId}">
                                <i class="far fa-heart"></i> Add to Wishlist
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        // Add modal styles
        this.addModalStyles();
        
        // Add event listeners
        const closeBtn = modal.querySelector('.modal-close');
        const overlay = modal.querySelector('.modal-overlay');
        const addToCartBtn = modal.querySelector('.add-to-cart-modal');
        const addToWishlistBtn = modal.querySelector('.add-to-wishlist-modal');
        
        closeBtn.addEventListener('click', () => this.closeModal(modal));
        overlay.addEventListener('click', () => this.closeModal(modal));
        
        if (addToCartBtn) {
            addToCartBtn.addEventListener('click', () => {
                this.addToCart(addToCartBtn);
                this.closeModal(modal);
            });
        }
        
        if (addToWishlistBtn) {
            addToWishlistBtn.addEventListener('click', () => {
                this.addToWishlist(addToWishlistBtn);
                this.closeModal(modal);
            });
        }
        
        // Prevent body scroll
        document.body.style.overflow = 'hidden';
    }

    closeModal(modal) {
        if (modal) {
            modal.classList.add('fade-out');
            setTimeout(() => {
                if (modal.parentNode) {
                    modal.remove();
                }
                document.body.style.overflow = '';
            }, 300);
        }
    }

    addModalStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .quick-view-modal {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                animation: fadeIn 0.3s ease;
            }
            
            .quick-view-modal.fade-out {
                animation: fadeOut 0.3s ease;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
            
            .modal-overlay {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(5px);
            }
            
            .modal-content {
                position: relative;
                background: var(--flare-card-bg);
                border-radius: 20px;
                width: 90%;
                max-width: 900px;
                max-height: 90vh;
                overflow-y: auto;
                border: 1px solid var(--flare-gray);
                box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
                animation: slideUp 0.4s ease;
            }
            
            @keyframes slideUp {
                from { transform: translateY(50px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            
            .modal-close {
                position: absolute;
                top: 20px;
                right: 20px;
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background: rgba(255, 107, 0, 0.1);
                border: 2px solid rgba(255, 107, 0, 0.3);
                color: var(--flare-primary);
                font-size: 1.2rem;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all var(--transition-normal);
                z-index: 10;
            }
            
            .modal-close:hover {
                background: rgba(255, 107, 0, 0.2);
                transform: rotate(90deg);
            }
            
            .modal-body {
                display: flex;
                padding: 40px;
                gap: 40px;
            }
            
            .modal-book-image {
                flex: 1;
            }
            
            .modal-book-image img {
                width: 100%;
                max-height: 500px;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
            }
            
            .modal-book-info {
                flex: 1;
            }
            
            .modal-book-title {
                font-family: 'Playfair Display', serif;
                font-size: 2.2rem;
                font-weight: 700;
                margin-bottom: 10px;
                color: var(--flare-text);
            }
            
            .modal-book-author {
                color: var(--flare-text-secondary);
                font-size: 1.1rem;
                margin-bottom: 20px;
            }
            
            .modal-book-price {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--flare-primary);
                margin-bottom: 25px;
            }
            
            .modal-book-desc {
                color: var(--flare-text-secondary);
                line-height: 1.6;
                margin-bottom: 30px;
                font-size: 1rem;
            }
            
            .modal-book-details {
                background: rgba(26, 26, 26, 0.5);
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 30px;
            }
            
            .detail-item {
                display: flex;
                justify-content: space-between;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            .detail-item:last-child {
                border-bottom: none;
            }
            
            .detail-label {
                color: var(--flare-text-secondary);
                font-weight: 600;
            }
            
            .detail-value {
                color: var(--flare-text);
            }
            
            .modal-actions {
                display: flex;
                gap: 15px;
            }
            
            @media (max-width: 768px) {
                .modal-body {
                    flex-direction: column;
                    padding: 20px;
                }
                
                .modal-book-title {
                    font-size: 1.8rem;
                }
                
                .modal-actions {
                    flex-direction: column;
                }
            }
        `;
        document.head.appendChild(style);
    }

    viewBookDetails(bookId) {
        // In a real app, this would navigate to book details page
        console.log(`Viewing details for book ${bookId}`);
        // For now, show quick view
        this.showQuickView({ dataset: { bookId } });
    }

    handlePreOrder(button) {
        const card = button.closest('.upcoming-book-card');
        const title = card?.querySelector('.upcoming-book-title')?.textContent || 'Upcoming Book';
        
        this.showToast(`Pre-ordered "${title}"!`, 'success');
        
        // Disable button and change text
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-check"></i> Pre-ordered';
        button.classList.remove('btn-outline');
        button.classList.add('btn-primary');
    }

    handleFreeDownload(button) {
        const card = button.closest('.free-book-card');
        const title = card?.querySelector('.free-book-title')?.textContent || 'Free Book';
        
        this.showToast(`Downloading "${title}"...`, 'info');
        
        // Simulate download
        button.disabled = true;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Downloading...';
        
        setTimeout(() => {
            button.innerHTML = '<i class="fas fa-check"></i> Downloaded';
            button.classList.remove('btn-free');
            button.classList.add('btn-outline');
        }, 1500);
    }

    // ===== BANNER EFFECTS =====
    initBannerEffects() {
        // BOGO banner animation
        const bogoBanner = document.querySelector('.bogo-banner');
        if (bogoBanner) {
            // Add subtle pulse animation
            setInterval(() => {
                bogoBanner.style.boxShadow = `
                    0 0 30px rgba(255, 107, 0, 0.3),
                    0 0 60px rgba(255, 107, 0, 0.2),
                    0 0 90px rgba(255, 61, 0, 0.1)
                `;
                setTimeout(() => {
                    bogoBanner.style.boxShadow = 'none';
                }, 1000);
            }, 5000);
        }
        
        // Sale badges animation
        const saleBadges = document.querySelectorAll('.sale-badge, .free-badge');
        saleBadges.forEach(badge => {
            badge.addEventListener('mouseenter', () => {
                badge.style.transform = 'scale(1.1) rotate(5deg)';
            });
            
            badge.addEventListener('mouseleave', () => {
                badge.style.transform = 'scale(1) rotate(0deg)';
            });
        });
    }

    // ===== SCROLL ANIMATIONS =====
    initScrollAnimations() {
        // Intersection Observer for fade-in animations
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);
        
        // Observe sections
        document.querySelectorAll('.section').forEach(section => {
            observer.observe(section);
        });
        
        // Add animation styles
        this.addAnimationStyles();
    }

    addAnimationStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .section {
                opacity: 0;
                transform: translateY(30px);
                transition: opacity 0.6s ease, transform 0.6s ease;
            }
            
            .section.animate-in {
                opacity: 1;
                transform: translateY(0);
            }
            
            .book-card, .sale-book-card, .free-book-card, .author-card {
                opacity: 0;
                transform: translateY(20px);
                transition: opacity 0.4s ease, transform 0.4s ease, all var(--transition-normal);
            }
            
            .section.animate-in .book-card,
            .section.animate-in .sale-book-card,
            .section.animate-in .free-book-card,
            .section.animate-in .author-card {
                opacity: 1;
                transform: translateY(0);
            }
            
            /* Staggered animation for cards */
            .section.animate-in .book-card:nth-child(1) { transition-delay: 0.1s; }
            .section.animate-in .book-card:nth-child(2) { transition-delay: 0.2s; }
            .section.animate-in .book-card:nth-child(3) { transition-delay: 0.3s; }
            .section.animate-in .book-card:nth-child(4) { transition-delay: 0.4s; }
            .section.animate-in .book-card:nth-child(5) { transition-delay: 0.5s; }
            .section.animate-in .book-card:nth-child(6) { transition-delay: 0.6s; }
            
            /* Badge pulse animation */
            .icon-badge.pulse {
                animation: pulse 0.3s ease;
            }
            
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.3); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);
    }

    // ===== UTILITY FUNCTIONS =====
    updateCartWishlistCounts() {
        // This will be called by the main app, but we update our own UI too
        const cart = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
        const wishlist = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
        
        // Update header badges if they exist
        const cartBadge = document.querySelector('#cartBtn .icon-badge');
        const wishlistBadge = document.querySelector('#favoritesBtn .icon-badge');
        
        if (cartBadge) cartBadge.textContent = cart.length;
        if (wishlistBadge) wishlistBadge.textContent = wishlist.length;

        this.updateHeroButtonCounts();
    }

    showToast(message, type = 'info') {
        // Remove existing toast
        const existingToast = document.querySelector('.toast-notification');
        if (existingToast) existingToast.remove();
        
        // Create toast
        const toast = document.createElement('div');
        toast.className = `toast-notification toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
                <span>${message}</span>
            </div>
            <button class="toast-close">
                <i class="fas fa-times"></i>
            </button>
        `;
        
        document.body.appendChild(toast);
        
        // Add toast styles
        this.addToastStyles();
        
        // Show toast
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
        // Auto remove after 3 seconds
        const autoRemove = setTimeout(() => {
            this.hideToast(toast);
        }, 3000);
        
        // Close button
        const closeBtn = toast.querySelector('.toast-close');
        closeBtn.addEventListener('click', () => {
            clearTimeout(autoRemove);
            this.hideToast(toast);
        });
    }

    hideToast(toast) {
        if (toast) {
            toast.classList.remove('show');
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.remove();
                }
            }, 300);
        }
    }

    addToastStyles() {
        if (document.querySelector('#toast-styles')) return;
        
        const style = document.createElement('style');
        style.id = 'toast-styles';
        style.textContent = `
            .toast-notification {
                position: fixed;
                bottom: 30px;
                right: 30px;
                background: var(--flare-card-bg);
                border-left: 4px solid var(--flare-primary);
                border-radius: 10px;
                padding: 15px 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 15px;
                min-width: 300px;
                max-width: 400px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                transform: translateY(100px);
                opacity: 0;
                transition: all 0.3s ease;
                z-index: 9998;
            }
            
            .toast-notification.show {
                transform: translateY(0);
                opacity: 1;
            }
            
            .toast-success {
                border-left-color: #00D4FF;
            }
            
            .toast-error {
                border-left-color: #FF3D00;
            }
            
            .toast-info {
                border-left-color: #FF6B00;
            }
            
            .toast-content {
                display: flex;
                align-items: center;
                gap: 10px;
                flex: 1;
            }
            
            .toast-content i {
                font-size: 1.2rem;
            }
            
            .toast-success .toast-content i {
                color: #00D4FF;
            }
            
            .toast-error .toast-content i {
                color: #FF3D00;
            }
            
            .toast-info .toast-content i {
                color: #FF6B00;
            }
            
            .toast-close {
                background: transparent;
                border: none;
                color: var(--flare-text-secondary);
                font-size: 1rem;
                cursor: pointer;
                padding: 5px;
                transition: all var(--transition-normal);
            }
            
            .toast-close:hover {
                color: var(--flare-primary);
                transform: rotate(90deg);
            }
            
            @media (max-width: 768px) {
                .toast-notification {
                    left: 20px;
                    right: 20px;
                    min-width: auto;
                    max-width: none;
                    bottom: 20px;
                }
            }
        `;
        document.head.appendChild(style);
    }

    // ===== PAGE TRANSITION =====
    handleNavigation(link) {
        // Add page transition effect
        const pageTransition = document.createElement('div');
        pageTransition.className = 'page-transition';
        document.body.appendChild(pageTransition);
        
        // Add transition styles
        if (!document.querySelector('#page-transition-styles')) {
            const style = document.createElement('style');
            style.id = 'page-transition-styles';
            style.textContent = `
                .page-transition {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: var(--flare-dark);
                    z-index: 9999;
                    transform: scaleY(0);
                    transform-origin: top;
                    transition: transform 0.5s ease-in-out;
                }
            `;
            document.head.appendChild(style);
        }
        
        // Animate transition
        setTimeout(() => {
            pageTransition.style.transform = 'scaleY(1)';
            
            // Navigate after animation
            setTimeout(() => {
                if (link.href) {
                    window.location.href = link.href;
                }
            }, 500);
        }, 10);
    }
    // ===== PRE-ORDER FUNCTIONALITY =====
initPreOrderFunctionality() {
    // Pre-order buttons
    const preorderBtns = document.querySelectorAll('.preorder-btn');
    
    preorderBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            const bookId = btn.dataset.bookId;
            this.handlePreOrder(bookId, btn);
        });
    });
    
    // Initialize pre-order counts from localStorage
    this.updatePreOrderCounts();
}

handlePreOrder(bookId, button) {
    // Check if user is logged in
    if (!window.flareBookApp || !window.flareBookApp.currentUser) {
        this.showToast('Please login to pre-order books!', 'error');
        
        // Redirect to login page after 1.5 seconds
        setTimeout(() => {
            if (window.flareBookApp) {
                window.flareBookApp.navigateToPage('login');
            }
        }, 1500);
        return;
    }
    
    // Check if already pre-ordered
    const userPreOrders = JSON.parse(localStorage.getItem('flarebook_preorders') || '{}');
    const userId = window.flareBookApp.currentUser.email || window.flareBookApp.currentUser.id;
    
    if (userPreOrders[userId] && userPreOrders[userId].includes(bookId)) {
        this.showToast('You have already pre-ordered this book!', 'info');
        return;
    }
    
    // Add pre-order
    if (!userPreOrders[userId]) {
        userPreOrders[userId] = [];
    }
    userPreOrders[userId].push(bookId);
    localStorage.setItem('flarebook_preorders', JSON.stringify(userPreOrders));
    
    // Update global pre-order count
    let preOrderCounts = JSON.parse(localStorage.getItem('flarebook_preorder_counts') || '{}');
    if (!preOrderCounts[bookId]) {
        preOrderCounts[bookId] = 1;
    } else {
        preOrderCounts[bookId]++;
    }
    localStorage.setItem('flarebook_preorder_counts', JSON.stringify(preOrderCounts));
    
    // Update UI
    this.updatePreOrderCount(bookId);
    
    // Update button state
    button.disabled = true;
    button.innerHTML = '<i class="fas fa-check"></i> Pre-ordered';
    button.classList.remove('btn-outline');
    button.classList.add('btn-primary');
    
    // Show success message
    const bookCard = button.closest('.upcoming-book-card');
    const bookTitle = bookCard?.querySelector('.upcoming-book-title')?.textContent || 'this book';
    
    this.showToast(`Successfully pre-ordered "${bookTitle}"!`, 'success');
    
    // Update user's pre-orders in localStorage
    this.updateUserPreOrders(bookId);
}

updatePreOrderCounts() {
    const preOrderCounts = JSON.parse(localStorage.getItem('flarebook_preorder_counts') || '{}');
    
    // Update all pre-order count displays
    document.querySelectorAll('[id^="preorderCount"]').forEach(element => {
        const bookId = element.closest('.upcoming-book-card')?.dataset.bookId;
        if (bookId && preOrderCounts[bookId]) {
            element.textContent = this.formatNumber(preOrderCounts[bookId]);
        }
    });
    
    // Check user's pre-orders and update button states
    this.updatePreOrderButtonStates();
}

updatePreOrderCount(bookId) {
    const preOrderCounts = JSON.parse(localStorage.getItem('flarebook_preorder_counts') || '{}');
    const countElement = document.querySelector(`[data-book-id="${bookId}"] .count-number`);
    
    if (countElement && preOrderCounts[bookId]) {
        countElement.textContent = this.formatNumber(preOrderCounts[bookId]);
    }
}

updatePreOrderButtonStates() {
    // Check if user is logged in
    if (!window.flareBookApp || !window.flareBookApp.currentUser) return;
    
    const userPreOrders = JSON.parse(localStorage.getItem('flarebook_preorders') || '{}');
    const userId = window.flareBookApp.currentUser.email || window.flareBookApp.currentUser.id;
    
    if (!userPreOrders[userId]) return;
    
    // Disable buttons for books user has already pre-ordered
    userPreOrders[userId].forEach(bookId => {
        const button = document.querySelector(`.preorder-btn[data-book-id="${bookId}"]`);
        if (button) {
            button.disabled = true;
            button.innerHTML = '<i class="fas fa-check"></i> Pre-ordered';
            button.classList.remove('btn-outline');
            button.classList.add('btn-primary');
        }
    });
}

updateUserPreOrders(bookId) {
    const user = window.flareBookApp?.currentUser;
    if (!user) return;
    
    let userData = JSON.parse(localStorage.getItem('flarebook_user_data') || '{}');
    const userKey = user.email || user.id;
    
    if (!userData[userKey]) {
        userData[userKey] = {
            name: user.name,
            email: user.email,
            preOrders: []
        };
    }
    
    if (!userData[userKey].preOrders.includes(bookId)) {
        userData[userKey].preOrders.push(bookId);
        localStorage.setItem('flarebook_user_data', JSON.stringify(userData));
    }
}

formatNumber(num) {
    if (num >= 1000000) {
        return (num / 1000000).toFixed(1) + 'M';
    } else if (num >= 1000) {
        return (num / 1000).toFixed(1) + 'K';
    }
    return num.toString();
}
}

// Initialize home page when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Check if we're on the home page
    const isHomePage = document.querySelector('.hero-slider-section') !== null;
    
    if (isHomePage) {
        window.homePage = new HomePage();
    }
});

// Add CSS for new elements
document.addEventListener('DOMContentLoaded', () => {
    // Add additional styles for new components
    const additionalStyles = document.createElement('style');
    additionalStyles.textContent = `
        /* BOGO Banner Animation */
        .bogo-banner {
            transition: box-shadow 1s ease;
        }
        
        /* Sale Badge Animation */
        .sale-badge, .free-badge {
            transition: transform var(--transition-normal);
        }
        
        /* Button hover effects */
        .slide-btn, .bogo-btn, .preorder-btn, .btn-free, .author-link {
            transition: all var(--transition-normal);
        }
        
        /* Book overlay buttons positioning */
        .overlay-buttons {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        /* Responsive improvements */
        @media (max-width: 768px) {
            .modal-content {
                width: 95%;
                margin: 10px;
            }
            
            .modal-body {
                flex-direction: column;
                padding: 20px;
            }
            
            .modal-book-image {
                margin-bottom: 20px;
            }
        }
        
        /* Loading animation for buttons */
        .fa-spinner {
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    `;
    document.head.appendChild(additionalStyles);
});