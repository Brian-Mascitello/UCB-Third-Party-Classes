// Enemies our player must avoid
var Enemy = function (x, y, speed) {
    // Variables applied to each of our instances go here,
    // we've provided one for you to get started

    // The image/sprite for our enemies, this uses
    // a helper we've provided to easily load images
    this.sprite = 'images/enemy-bug.png';

    // Starting location of enemy bug.
    this.x = x;
    this.y = y;
    this.row = getEnemyRowNumber(y);

    // Enemy bug's movement speed.
    this.speed = speed;

    // Half dimenions of enemy-bug.png in pixels.
    // this.height = 33; // unused
    this.width = 49;
};

// Update the enemy's position, required method for game
// Parameter: dt, a time delta between ticks
Enemy.prototype.update = function (dt) {
    // You should multiply any movement by the dt parameter
    // which will ensure the game runs at the same speed for
    // all computers.
    this.x += this.speed * dt;

    // Reset to left side of play area and selects a new speed and row for enemy unit.
    if (this.x > 505) {
        this.x = -this.width;
        this.y = randomEnemyRow();
        this.row = getEnemyRowNumber(this.y);
        this.speed = randomNumber(100, 300);
    }
};

// Draw the enemy on the screen, required method for game
Enemy.prototype.render = function () {
    ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
};

// Now write your own player class
// This class requires an update(), render() and
// a handleInput() method.
var Player = function () {
    this.sprite = 'images/char-boy.png';

    // Starting location of player.
    this.x = 202;
    this.y = 379;
    this.row = 0;
    this.col = 2;

    /* // Half dimenions of char-boy.png in pixels. 
    this.height = 38;
    this.width = 33; */

    // Adjusted half-width for better collisions.
    this.width = 22;

    this.handleInput = function (key) {
        switch (key) {
            case 'up':
                if (this.y > -41) {
                    this.y -= 84;
                    this.row += 1;
                }

                if (this.y == -41) {
                    alert('Winner!');

                    // Move back to player's starting location.
                    this.x = 202;
                    this.y = 379;
                    this.row = 0;
                    this.col = 2;
                }
                break;

            case 'down':
                if (this.y < 379) {
                    this.y += 84;
                    this.row -= 1;
                }
                break;

            case 'left':
                if (this.x > 0) {
                    this.x -= 101;
                    this.col -= 1;
                }
                break;

            case 'right':
                if (this.x < 404) {
                    this.x += 101;
                    this.col += 1;
                }
                break;

            default:
                break;
        }
    }
};

Player.prototype.update = function (dt) {

};

Player.prototype.render = function () {
    ctx.drawImage(Resources.get(this.sprite), this.x, this.y);
};

// Now instantiate your objects.
// Place all enemy objects in an array called allEnemies
// Place the player object in a variable called player
var enemy1 = new Enemy(0, randomEnemyRow(), randomNumber(100, 300));
var enemy2 = new Enemy(0, randomEnemyRow(), randomNumber(100, 300));
var enemy3 = new Enemy(0, randomEnemyRow(), randomNumber(100, 300));
var enemy4 = new Enemy(0, randomEnemyRow(), randomNumber(100, 300));
var allEnemies = [enemy1, enemy2, enemy3, enemy4];

var player = new Player();

// This listens for key presses and sends the keys to your
// Player.handleInput() method. You don't need to modify this.
document.addEventListener('keyup', function (e) {
    var allowedKeys = {
        37: 'left',
        38: 'up',
        39: 'right',
        40: 'down'
    };

    player.handleInput(allowedKeys[e.keyCode]);
});

// Selects a position for the enemy to be in.
function randomEnemyRow() {
    const rows = [60, 144, 228]
    let rowNumber = Math.floor(Math.random() * rows.length);

    return rows[rowNumber];
}

// Looks up the row of an emeny.
function getEnemyRowNumber(yValue) {
    const rowDictionary = {
        60: 4,
        144: 3,
        228: 2
    };

    return rowDictionary[yValue];
}

// Generates a random value between lowerBound and upperBound.
function randomNumber(lowerBound, upperBound) {
    let multiplier = upperBound - lowerBound;
    let randomInteger = Math.floor(Math.random() * multiplier);
    let finalValue = randomInteger + lowerBound;

    return finalValue;
    // return 50; // Testing slow speed.
}
