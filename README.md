# ProjectQ4
# geometry clone

A 2D platformer inspired by the mechanics of Geometry Dash. Navigate through  levels  with spikes and obstacles where timing is everything.

## Purpose
The goal of this project is to implement a precise physics-based game loop, focusing on  movement, collision detection, and "one-more-try" gameplay loops. 

## Target User
- Fans of high-difficulty platformers.
- Players who enjoy "trial and error" gaming mechanics.


---

## Features
* **Gravity-Flipping Physics:** Precise jumping and falling mechanics with a "fixed-timestep" for consistency.
* **Collision Detection:** Pixel-perfect hitbox logic for spikes vs. solid blocks.
* **Attempt System:** Automatic instant-respawn and attempt counter tracking.
* **Dynamic HUD:** Progress bars, attempt counters, and pause menus.

---

## Technical Architecture

The program is built using a  Class-based structure to separate logic from rendering.

### Class Breakdown
| Class | Responsibility |
| :--- | :--- |
| **GameManager** | Controls the game state (Menu, Playing, Game Over). |
| **Player** | Handles jump input, gravity, and death triggers. |
| **LevelManager** | Manages obstacle spawning and the scrolling background. |
| **Obstacle** | Base class for spikes and blocks with defined hitboxes. |
| **GameUI** | Updates the progress bar, attempt count, and menus. |

---


1. Clone the repo.
2. Open in your preferred IDE.
3. Run the main executable/index file.
