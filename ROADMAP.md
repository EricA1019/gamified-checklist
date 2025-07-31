# Project Roadmap: Gamified Checklist App

This document outlines the development plan for the Gamified Checklist App, following the "Close-to-Shore" iterative methodology. Each "hop" represents a small, self-contained, and runnable vertical slice of the application.

## Development Approach

- **Short hops**: Small, testable, end-to-end features.
- **Test-driven**: Tests first, implementation second.
- **Data-driven**: JSON-based task storage and configuration.
- **Always bootable**: Each hop results in a runnable app.

---

## Roadmap (Hops)

### Foundation Hops

1.  **Project Structure Setup** ✅
    -   [x] Create directory structure and basic files (`main.py`, etc.).
    -   [x] Set up testing framework (e.g., `pytest`).
    -   [x] Implement a basic, tagged logging system.
    -   [x] Create a minimal Kivy app that boots to a black screen.

2.  **Data Models**
    -   [ ] Define `Task`, `Category`, and `User` data classes.
    -   [ ] Write unit tests for all model operations (creation, modification).
    -   [ ] Implement a JSON storage utility to save/load model data.

3.  **XP and Level System**
    -   [ ] Implement XP calculation logic based on task difficulty/type.
    -   [ ] Create a leveling algorithm (e.g., exponential XP curve).
    -   [ ] Add logic to track and update user streaks.
    -   [ ] Write unit tests for all XP and leveling logic.

### UI Hops

4.  **Basic UI Framework**
    -   [ ] Create the main screen layout with placeholders for UI components.
    -   [ ] Implement basic navigation (if multiple screens are planned early).
    -   [ ] Define a simple color and font theme.

5.  **Task List Display**
    -   [ ] Create a `RecycleView` to display a list of tasks.
    -   [ ] Implement a checkbox or button to mark tasks as complete.
    -   [ ] Add basic filtering by category.
    -   [ ] Use emojis to represent task categories or status.

6.  **Task Creation UI**
    -   [ ] Build a form (`ModalView` or new screen) to add/edit tasks.
    -   [ ] Add input fields for title, description, difficulty, and category.
    -   [ ] Connect the form to the task controller to save new tasks.

7.  **Progress Visualization**
    -   [ ] Add a `ProgressBar` to the UI to show XP progress toward the next level.
    -   [ ] Display the current level and total XP.
    -   [ ] Show the current streak count.

### System Hops

8.  **Task Persistence**
    -   [ ] Integrate the JSON storage utility to save all user data on exit.
    -   [ ] Load user data on startup.
    -   [ ] Test for data integrity across sessions.

9.  **Daily Reset System**
    -   [ ] Implement a mechanism to check the time at startup.
    -   [ ] Reset daily tasks if the day has changed.
    -   [ ] Update or reset streaks based on the last completion date.

10. **Notification System**
    -   [ ] Integrate a library like `plyer` for local notifications.
    -   [ ] Create a system to schedule notifications for task due dates.
    -   [ ] Test notification delivery on target platforms.

### Final Hops

11. **Settings and Customization**
    -   [ ] Create a settings screen.
    -   [ ] Add options to customize the theme or app behavior.
    -   [ ] Implement data export/import functionality.

12. **Packaging and Deployment**
    -   [ ] Configure `buildozer` for Android/iOS packaging.
    -   [ ] Create a GitHub repository and push the code.
    -   [ ] Write final `README.md` and add `LICENSE` file.
    -   [ ] Create a release build.
