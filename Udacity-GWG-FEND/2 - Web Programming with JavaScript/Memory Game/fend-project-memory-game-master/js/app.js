/*
 * Create a list that holds all of your cards ✓
 */

let cards = ['fa-anchor', 'fa-anchor', 'fa-bicycle', 'fa-bicycle', 'fa-bolt', 'fa-bolt', 'fa-bomb', 'fa-bomb',
    'fa-cube', 'fa-cube', 'fa-diamond', 'fa-diamond', 'fa-leaf', 'fa-leaf', 'fa-paper-plane-o', 'fa-paper-plane-o'];

/*
 * Display the cards on the page
 *   - shuffle the list of cards using the provided "shuffle" method below ✓
 *   - loop through each card and create its HTML ✓
 *   - add each card's HTML to the page ✓
 */

let deck = document.getElementsByClassName('deck')[0];
let ulStars = document.getElementsByClassName('stars')[0];

function startGame() {
    let cardHTML = [];
    let starsHTML = [];

    // Shuffles the cards from cards into a random list.
    shuffle(cards).forEach(function (card) {
        cardHTML.push(`<li class="card"><i class="fa ${card}"></i></li>`);
    });

    // Forms the deck's HTML from the cardHTML.
    deck.innerHTML = cardHTML.join('');

    // Adds the stars to the score panel.
    for (let i = 0; i < 3; i++) {
        starsHTML.push('<li class="card"><i class="fa fa-star"></i></li>');
    }

    // Forms the star's HTML from the starsHTML.
    ulStars.innerHTML = starsHTML.join('');

    addCardClicks();
}

// Starts the game when the website is called.
startGame();

// Shuffle function from http://stackoverflow.com/a/2450976
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

/*
 * set up the event listener for a card. If a card is clicked:
 *  - display the card's symbol (put this functionality in another function that you call from this one)
 *  - add the card to a *list* of "open" cards (put this functionality in another function that you call from this one)
 *  - if the list already has another card, check to see if the two cards match
 *    + if the cards do match, lock the cards in the open position (put this functionality in another function that you call from this one)
 *    + if the cards do not match, remove the cards from the list and hide the card's symbol (put this functionality in another function that you call from this one)
 *    + increment the move counter and display it on the page (put this functionality in another function that you call from this one)
 *    + if all cards have matched, display a message with the final score (put this functionality in another function that you call from this one)
 */

let matches = 0;

// Adds clickable functionality to all cards in the deck.
// Also contains the playable game logic.
// Got the idea for adding clicks to each individual card from Mike's webinar.
function addCardClicks() {
    let allCards = document.querySelectorAll('.card');
    let flippedCards = [];

    // Adds the ability to flip each card.
    allCards.forEach(function (card) {
        card.addEventListener('click', function (flip) {
            flippedCards.push(card);
            openShowCard(card);
            incrementMoves();

            // Triggers when there are two flipped cards.
            if (flippedCards.length == 2) {
                setTimeout(function () {

                    // Checks if both cards are the same symbol and if a legal amount of cards are open.
                    if ((checkMatch(flippedCards)) && countChecker()) {

                        // Only toggle matches on the first two cards clicked.
                        matchCard(flippedCards[0]);
                        matchCard(flippedCards[1]);

                        matches++;

                        if (matches == 8) {
                            winner();
                        }

                    } else {
                        closeHideCards();
                    }

                    // Removes everything from the flippedCards list.
                    while (flippedCards.length > 0) {
                        flippedCards.pop()
                    }
                }, 500);
            }
        });
    });
};

// Verifies if the cards are a matching set or not.
function checkMatch(cardSet) {
    let firstCardType = cardSet[0].querySelector('i').classList[1];
    let secondCardType = cardSet[1].querySelector('i').classList[1];

    if (firstCardType == secondCardType) {
        return true;
    }
    return false;
}

// Closes and hides all cards that are not matches.
function closeHideCards() {
    let allCards = document.querySelectorAll('.card');
    allCards.forEach(function (card) {
        if ((!card.classList.contains('match')) && (card.classList.contains('open'))) {
            card.classList.remove('open', 'show');
        };
    });
}

// Ensures the user has not double clicked a single card and has not opened more than two.
function countChecker() {
    let allCards = document.querySelectorAll('.card');
    openCards = 0;
    matchedCards = 0;
    allCards.forEach(function (card) {
        if (card.classList.contains('open')) {
            openCards++;
        };
        if (card.classList.contains('match')) {
            matchedCards++;
        };
    });

    if (openCards - matchedCards != 2) {
        return false;
    }
    return true;
}


function matchCard(card) {
    card.classList.add('match');
}

function openShowCard(card) {
    card.classList.add('open', 'show');
}

let moves = document.getElementsByClassName('moves')[0];
let movesCount = parseInt(moves.textContent);

function incrementMoves() {
    movesCount++;

    moves.innerHTML = `<span class="moves">${movesCount}</span>`;

    decrementStars();
}

function resetMoves() {
    movesCount = 0;

    moves.innerHTML = `<span class="moves">${movesCount}</span>`;
}

function winner() {
    let endTime = time;
    let endStars = ulStars.childElementCount;
    let modal = document.getElementById('win');
    let timeTaken = document.getElementsByClassName('time-taken')[0];
    let starRating = document.getElementsByClassName('star-rating')[0];

    timeTaken.innerHTML = `<p class="time-taken">Completed puzzle in ${endTime} seconds!</p>`;
    starRating.innerHTML = `<p class="star-rating">You finished with ${endStars} stars!</p>`;

    modal.style.display = "flex";
}

let resetButton = document.getElementsByClassName('restart')[0];

resetButton.addEventListener('click', playAgain);

function playAgain() {
    let modal = document.getElementById('win');

    // Reset number of matches so if user plays again the stopping condition will be met.
    matches = 0;

    // Remove all stars from score panel, will be replenished in startGame().
    while (ulStars.hasChildNodes()) {
        ulStars.removeChild(ulStars.lastChild);
    }

    // Remove all cards from the deck, will be replenished in startGame().
    while (deck.hasChildNodes()) {
        deck.removeChild(deck.lastChild);
    }

    resetMoves();

    resetTimeClock();

    startGame();

    modal.style.display = "none";
}

function decrementStars() {
    if (movesCount == 32) {
        ulStars.firstElementChild.remove();
    }
    if (movesCount == 64) {
        ulStars.firstElementChild.remove();
    }
}

// Learned how to make a timer from Ryan's webinar.
var time = 0;
var timeClock = 0;
let timeDisplay = document.getElementsByClassName('timer')[0];

startTimeClock();

function startTimeClock() {
    timeClock = setInterval(function () {
        time++;

        timeDisplay.innerHTML = `<span class="timer">${time}</span>`;
    }, 1000);
}

function resetTimeClock() {
    time = 0;
}
