// ===== BOOK DETAILS PAGE FUNCTIONALITY =====
class BookDetailsPage {
    constructor() {
        this.bookId = null;
        this.bookData = null;
        this.init();
    }

    init() {
        console.log('Book details page initialized');
        
        // Get book ID from URL
        this.getBookIdFromURL();
        
        // Load book data
        this.loadBookData();
        
        // Initialize page features
        this.initTabs();
        this.initQuantitySelector();
        this.initThumbnails();
        this.initFAQ();
        this.initEventListeners();
        this.initShareButtons();
    }

    getBookIdFromURL() {
        const urlParams = new URLSearchParams(window.location.search);
        this.bookId = urlParams.get('id') || '1';
        console.log('Loading book ID:', this.bookId);
    }

    loadBookData() {
        // In a real app, you would fetch from an API
        // For now, use sample data based on book ID
        
        const booksDatabase = {
            '1': {
                id: '1',
                title: 'The Silent Patient',
                author: 'Alex Michaelides',
                price: 15.99,
                originalPrice: 24.99,
                discount: 35,
                image: 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                rating: 4.5,
                ratingCount: 4289,
                description: 'A psychological thriller of obsession and dangerous love. The Silent Patient is a shocking psychological thriller of a woman\'s act of violence against her husband - and of the therapist obsessed with uncovering her motive.',
                fullDescription: `Alicia Berenson's life is seemingly perfect. A famous painter married to an in-demand fashion photographer...`,
                format: 'Paperback, eBook, Audiobook',
                pages: '352 pages',
                publisher: 'Celadon Books',
                published: 'February 5, 2019',
                isbn: '978-1250301697',
                language: 'English',
                badge: 'Bestseller',
                inStock: true,
                authorName: 'Alex Michaelides',
                authorBio: 'British-Cypriot author and screenwriter. The Silent Patient is his debut novel and was a Sunday Times and New York Times bestseller.',
                genre: 'Psychological Thriller'
            },
            '2': {
                id: '2',
                title: 'Atomic Habits',
                author: 'James Clear',
                price: 18.99,
                originalPrice: null,
                discount: null,
                image: 'https://images.unsplash.com/photo-1512820790803-83ca734da794?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                rating: 4.8,
                ratingCount: 12450,
                description: 'Tiny Changes, Remarkable Results: An Easy & Proven Way to Build Good Habits & Break Bad Ones',
                fullDescription: `No matter your goals, Atomic Habits offers a proven framework for improving - every day...`,
                format: 'Hardcover, eBook, Audiobook',
                pages: '320 pages',
                publisher: 'Avery',
                published: 'October 16, 2018',
                isbn: '978-0735211292',
                language: 'English',
                badge: 'New',
                inStock: true,
                authorName: 'James Clear',
                authorBio: 'James Clear is a writer and speaker focused on habits, decision making, and continuous improvement.',
                genre: 'Self-Help'
            },
            '3': {
                id: '3',
                title: 'The Midnight Library',
                author: 'Matt Haig',
                price: 16.49,
                originalPrice: 22.99,
                discount: 28,
                image: 'https://images.unsplash.com/photo-1532012197267-da84d127e765?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                rating: 4.3,
                ratingCount: 8742,
                description: 'Between life and death there is a library, and within that library, the shelves go on forever. Every book provides a chance to try another life you could have lived.',
                fullDescription: `Somewhere out beyond the edge of the universe there is a library that contains an infinite number of books...`,
                format: 'Paperback, eBook',
                pages: '304 pages',
                publisher: 'Viking',
                published: 'August 13, 2020',
                isbn: '978-0525559474',
                language: 'English',
                badge: 'Book of the Month',
                inStock: true,
                authorName: 'Matt Haig',
                authorBio: 'Matt Haig is the author of internationally bestselling novels and nonfiction books.',
                genre: 'Fiction'
            }
        };
        
        this.bookData = booksDatabase[this.bookId] || booksDatabase['1'];
        this.updateUI();
    }

    updateUI() {
        // Update all book information
        document.getElementById('bookTitle').textContent = this.bookData.title;
        document.getElementById('bookAuthor').textContent = `By ${this.bookData.author}`;
        document.getElementById('currentPrice').textContent = `$${this.bookData.price}`;
        document.getElementById('bookDescription').textContent = this.bookData.description;
        document.getElementById('fullDescription').textContent = this.bookData.fullDescription;
        document.getElementById('bookFormat').textContent = this.bookData.format;
        document.getElementById('bookPages').textContent = this.bookData.pages;
        document.getElementById('bookPublisher').textContent = this.bookData.publisher;
        document.getElementById('bookPublished').textContent = this.bookData.published;
        document.getElementById('bookISBN').textContent = this.bookData.isbn;
        document.getElementById('bookLanguage').textContent = this.bookData.language;
        document.getElementById('authorName').textContent = this.bookData.authorName;
        document.getElementById('breadcrumbTitle').textContent = this.bookData.title;
        
        // Update image
        const mainImage = document.getElementById('bookMainImage');
        const thumbImage = document.getElementById('bookThumb1');
        if (mainImage) mainImage.src = this.bookData.image;
        if (thumbImage) thumbImage.src = this.bookData.image;
        
        // Update badge
        const badgeElement = document.getElementById('bookBadge');
        if (badgeElement) {
            badgeElement.textContent = this.bookData.badge;
            badgeElement.className = 'book-badge ' + this.bookData.badge.toLowerCase().replace(' ', '-');
        }
        
        // Update price display
        const originalPrice = document.getElementById('originalPrice');
        const discountPercent = document.getElementById('discountPercent');
        
        if (this.bookData.originalPrice) {
            originalPrice.textContent = `$${this.bookData.originalPrice}`;
            discountPercent.textContent = `-${this.bookData.discount}%`;
        } else {
            originalPrice.style.display = 'none';
            discountPercent.style.display = 'none';
        }
        
        // Update stock status
        const stockStatus = document.getElementById('stockStatus');
        if (stockStatus) {
            stockStatus.textContent = this.bookData.inStock ? 'In Stock' : 'Out of Stock';
            stockStatus.className = this.bookData.inStock ? 'stock-status in-stock' : 'stock-status out-of-stock';
        }
        
        // Update rating
        const ratingCount = document.getElementById('ratingCount');
        if (ratingCount) {
            ratingCount.textContent = `(${this.bookData.ratingCount.toLocaleString()} ratings)`;
        }
        
        // Update page title
        document.title = `${this.bookData.title} - FlareBook Store`;
    }

    initTabs() {
        const tabButtons = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');
        
        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                const tabId = button.getAttribute('data-tab');
                
                // Remove active class from all buttons and contents
                tabButtons.forEach(btn => btn.classList.remove('active'));
                tabContents.forEach(content => content.classList.remove('active'));
                
                // Add active class to clicked button and corresponding content
                button.classList.add('active');
                document.getElementById(`${tabId}Tab`).classList.add('active');
            });
        });
    }

    initQuantitySelector() {
        const minusBtn = document.querySelector('.qty-btn.minus');
        const plusBtn = document.querySelector('.qty-btn.plus');
        const qtyInput = document.getElementById('quantityInput');
        
        minusBtn.addEventListener('click', () => {
            let value = parseInt(qtyInput.value);
            if (value > 1) {
                qtyInput.value = value - 1;
            }
        });
        
        plusBtn.addEventListener('click', () => {
            let value = parseInt(qtyInput.value);
            if (value < 10) {
                qtyInput.value = value + 1;
            }
        });
        
        qtyInput.addEventListener('change', () => {
            let value = parseInt(qtyInput.value);
            if (isNaN(value) || value < 1) qtyInput.value = 1;
            if (value > 10) qtyInput.value = 10;
        });
    }

    initThumbnails() {
        const thumbnails = document.querySelectorAll('.thumbnail');
        const mainImage = document.getElementById('bookMainImage');
        
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', () => {
                // Remove active class from all thumbnails
                thumbnails.forEach(t => t.classList.remove('active'));
                
                // Add active class to clicked thumbnail
                thumb.classList.add('active');
                
                // Update main image based on data-image attribute
                const imageType = thumb.getAttribute('data-image');
                if (imageType === 'main') {
                    mainImage.src = this.bookData.image;
                }
                // In real app, you would have different images for back, preview, etc.
            });
        });
    }

    initFAQ() {
        const faqQuestions = document.querySelectorAll('.faq-question');
        
        faqQuestions.forEach(question => {
            question.addEventListener('click', () => {
                const answer = question.nextElementSibling;
                const isActive = question.classList.contains('active');
                
                // Close all FAQ items
                faqQuestions.forEach(q => {
                    q.classList.remove('active');
                    q.nextElementSibling.classList.remove('active');
                });
                
                // Open clicked item if it wasn't active
                if (!isActive) {
                    question.classList.add('active');
                    answer.classList.add('active');
                }
            });
        });
    }

    initEventListeners() {
        // Add to Cart button
        const addToCartBtn = document.getElementById('addToCartBtn');
        if (addToCartBtn) {
            addToCartBtn.addEventListener('click', () => this.addToCart());
        }
        
        // Add to Wishlist button
        const addToWishlistBtn = document.getElementById('addToWishlistBtn');
        if (addToWishlistBtn) {
            addToWishlistBtn.addEventListener('click', () => this.addToWishlist());
        }
        
        // Buy Now button
        const buyNowBtn = document.getElementById('buyNowBtn');
        if (buyNowBtn) {
            buyNowBtn.addEventListener('click', () => this.buyNow());
        }
        
        // Read More button
        const readMoreBtn = document.getElementById('readMoreBtn');
        if (readMoreBtn) {
            readMoreBtn.addEventListener('click', () => this.toggleReadMore());
        }
    }

    initShareButtons() {
        const copyLinkBtn = document.querySelector('.share-btn.copy-link');
        if (copyLinkBtn) {
            copyLinkBtn.addEventListener('click', () => this.copyBookLink());
        }
    }

    addToCart() {
        const quantity = parseInt(document.getElementById('quantityInput').value) || 1;
        
        // Get existing cart
        let cart = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
        
        // Check if already in cart
        const existingIndex = cart.findIndex(item => item.id === this.bookId);
        
        if (existingIndex > -1) {
            // Update quantity
            cart[existingIndex].quantity += quantity;
        } else {
            // Add new item
            cart.push({
                id: this.bookId,
                title: this.bookData.title,
                author: this.bookData.author,
                price: this.bookData.price,
                image: this.bookData.image,
                quantity: quantity
            });
        }
        
        // Save to localStorage
        localStorage.setItem('flarebook_cart', JSON.stringify(cart));
        
        // Show success message
        this.showToast(`${quantity} ${quantity === 1 ? 'copy' : 'copies'} added to cart!`, 'success');
        
        // Update cart count in header
        this.updateCartCount();
    }

    addToWishlist() {
        // Get existing wishlist
        let wishlist = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
        
        // Check if already in wishlist
        const existingIndex = wishlist.findIndex(item => item.id === this.bookId);
        
        const wishlistBtn = document.getElementById('addToWishlistBtn');
        
        if (existingIndex > -1) {
            // Remove from wishlist
            wishlist.splice(existingIndex, 1);
            wishlistBtn.innerHTML = '<i class="far fa-heart"></i> Add to Wishlist';
            wishlistBtn.classList.remove('active');
            this.showToast('Removed from wishlist!', 'info');
        } else {
            // Add to wishlist
            wishlist.push({
                id: this.bookId,
                title: this.bookData.title,
                author: this.bookData.author,
                price: this.bookData.price,
                image: this.bookData.image,
                addedAt: new Date().toISOString()
            });
            wishlistBtn.innerHTML = '<i class="fas fa-heart"></i> Added to Wishlist';
            wishlistBtn.classList.add('active');
            this.showToast('Added to wishlist!', 'success');
        }
        
        // Save to localStorage
        localStorage.setItem('flarebook_wishlist', JSON.stringify(wishlist));
        
        // Update wishlist count in header
        this.updateWishlistCount();
    }

    buyNow() {
        // Add to cart first
        this.addToCart();
        
        // Then redirect to checkout (or cart page for now)
        setTimeout(() => {
            window.location.href = 'cart.html';
        }, 1000);
    }

    toggleReadMore() {
        const description = document.getElementById('bookDescription');
        const readMoreBtn = document.getElementById('readMoreBtn');
        
        if (description.style.webkitLineClamp === 'unset') {
            description.style.webkitLineClamp = '3';
            readMoreBtn.textContent = 'Read More';
        } else {
            description.style.webkitLineClamp = 'unset';
            readMoreBtn.textContent = 'Read Less';
        }
    }

    copyBookLink() {
        const currentUrl = window.location.href;
        navigator.clipboard.writeText(currentUrl)
            .then(() => {
                this.showToast('Link copied to clipboard!', 'success');
            })
            .catch(err => {
                console.error('Failed to copy link:', err);
                this.showToast('Failed to copy link', 'error');
            });
    }

    updateCartCount() {
        const cart = JSON.parse(localStorage.getItem('flarebook_cart')) || [];
        const cartBadge = document.querySelector('#cartBtn .icon-badge');
        if (cartBadge) {
            cartBadge.textContent = cart.length;
        }
    }

    updateWishlistCount() {
        const wishlist = JSON.parse(localStorage.getItem('flarebook_wishlist')) || [];
        const wishlistBadge = document.querySelector('#favoritesBtn .icon-badge');
        if (wishlistBadge) {
            wishlistBadge.textContent = wishlist.length;
        }
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
        `;
        
        document.body.appendChild(toast);
        
        // Show toast
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                if (toast.parentNode) toast.remove();
            }, 300);
        }, 3000);
    }
}

// Initialize book details page
document.addEventListener('DOMContentLoaded', () => {
    // Check if we're on book details page
    if (window.location.pathname.includes('book-details.html')) {
        window.bookDetailsPage = new BookDetailsPage();
    }
});