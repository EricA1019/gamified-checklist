# Gamified Checklist App 🎮✅

A mobile task management app that gamifies your productivity with XP, levels, and streaks.

## Features 🌟

- **📋 Daily Tasks & Quests**: Regular tasks for smaller XP, epic quests for bigger rewards
- **🎯 Difficulty Levels**: Easy, Medium, Hard tasks with different XP values
- **📂 Categories**: Organize tasks by work, personal, health, etc.
- **🔥 Streak System**: Build momentum with consecutive daily completions
- **📊 Progress Tracking**: Visual progress bars and level advancement
- **🎨 Emoji Interface**: Colorful, engaging UI with emoji enhancements
- **💾 Data Persistence**: Your progress saves automatically and resets daily at midnight
- **🔔 Smart Notifications**: Gentle reminders for pending tasks

## Technology Stack 🛠️

- **Framework**: Kivy (Python-based mobile framework)
- **Language**: Python 3.12+
- **Testing**: pytest
- **Data Storage**: JSON-based persistence
- **Notifications**: Plyer
- **Dependencies**: NumPy for calculations

## Quick Start 🚀

### Prerequisites
- Python 3.12 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "Gamefied Checklist"
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   python main.py
   ```

5. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

## Development Approach 🏗️

This project follows the **"Close-to-Shore Coding"** methodology:

- **🏃‍♂️ Short Hops**: Small, testable, end-to-end features
- **🧪 Test-Driven**: Tests first, implementation second
- **📊 Data-Driven**: JSON-based configuration and storage
- **✅ Always Bootable**: Each development iteration results in a runnable app

Each "hop" represents 1-3 hours of work that delivers a complete, working feature.

## Project Structure 📁

```
Gamefied Checklist/
├── main.py                     # App entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── ROADMAP.md                  # Development roadmap
├── gamified_checklist/         # Main app package
│   ├── models/                 # Data models (Task, User, Category)
│   ├── views/                  # UI components
│   │   ├── screens/            # Main app screens
│   │   └── widgets/            # Reusable UI widgets
│   ├── controllers/            # Business logic
│   └── utils/                  # Helper utilities
└── tests/                      # Test suite
    ├── test_models/
    ├── test_controllers/
    └── test_utils/
```

## Development Status 📈

**Current Version**: v0.0.1 ✅  
**Current Status**: Foundation & Core Models Complete

- [x] Project structure and testing framework
- [x] Complete data models (Task, Category, User) 
- [x] XP and leveling system with streak tracking
- [x] JSON-based data persistence with backup
- [x] Comprehensive test suite (35 passing tests)
- [ ] Basic UI framework and task display
- [ ] Task creation and management interface
- [ ] Progress visualization components
- [ ] Daily reset and notification system

See [ROADMAP.md](ROADMAP.md) for detailed development plan.

## Contributing 🤝

This is a personal learning project, but feedback and suggestions are welcome! 

### Development Workflow

1. **Pick a hop** from the roadmap
2. **Write tests first** for the feature
3. **Implement** minimal code to pass tests
4. **Refactor** if needed
5. **Test** that the app still boots and runs
6. **Commit** with clear message

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap 🗺️

For detailed development plans and progress tracking, see [ROADMAP.md](ROADMAP.md).

---

*Built with ❤️ using Python and Kivy*
