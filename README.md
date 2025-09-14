# SmallChatGPT 🤖

A lightweight, intelligent chatbot built with Standard ML (SML) for core logic and FastHTML for the web interface. This project demonstrates the integration of functional programming principles with modern web technologies to create an efficient and responsive conversational AI.

## 🌟 Features

- **Functional Core**: Built with Standard ML for robust, type-safe chatbot logic
- **Modern Web Interface**: FastHTML-powered responsive web UI
- **Lightweight**: Minimal dependencies and fast response times
- **Extensible**: Modular architecture for easy customization
- **Real-time Chat**: Interactive conversation interface
- **Cross-platform**: Runs on any system with SML and Python support

## 🏗️ Architecture

SmallChatGPT follows a clean architecture pattern:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FastHTML      │    │   Bridge        │    │   SML Core      │
│   (Web UI)      │◄──►│   (Python)      │◄──►│   (Logic)       │
│                 │    │                 │    │                 │
│ • Routes        │    │ • FFI calls     │    │ • NLP           │
│ • Templates     │    │ • Data transform│    │ • Responses     │
│ • Static files  │    │ • Error handling│    │ • State mgmt    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Standard ML**: SML/NJ or MLton compiler
- **Python 3.8+**: For FastHTML web framework
- **pip**: Python package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CllsPy/SmallChatGPT.git
   cd SmallChatGPT
   ```

2. **Install Python dependencies**
   ```bash
   pip install fasthtml
   ```

3. **Compile SML components**
   ```bash
   # For SML/NJ
   sml chatbot.sml
   
   # For MLton (if preferred)
   mlton -output chatbot chatbot.sml
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8000` to start chatting!

## 💡 Usage

### Basic Chat Interface

Once the server is running, you can:

1. Type your message in the input field
2. Press Enter or click Send
3. View the AI's response in real-time
4. Continue the conversation naturally

### Example Conversation

```
You: Hello! How are you?
Bot: Hello! I'm doing well, thank you for asking. I'm ready to help you with 
     any questions or tasks you have. What would you like to talk about?

You: What's the weather like?
Bot: I don't have access to real-time weather data, but I'd be happy to 
     discuss weather patterns, climate, or help you find weather resources!
```

## 🛠️ Development

### Project Structure

```
SmallChatGPT/
├── README.md              # This file
├── app.py                 # FastHTML web application
├── chatbot.sml           # SML chatbot core logic
├── static/               # Static web assets
│   ├── style.css        # Styling
│   └── script.js        # Client-side JavaScript
├── templates/           # HTML templates
│   └── chat.html       # Main chat interface
└── requirements.txt     # Python dependencies
```

### Key Components

#### SML Core (`chatbot.sml`)
The heart of the chatbot, written in Standard ML:
- Pattern matching for input processing
- Functional response generation
- State management using immutable data structures
- Type-safe conversation handling

#### FastHTML Interface (`app.py`)
Modern web framework handling:
- HTTP routing and request handling
- WebSocket connections for real-time chat
- Template rendering
- Static file serving
- Bridge to SML backend

### Adding New Features

1. **Extend SML Logic**: Add new response patterns in `chatbot.sml`
2. **Update Web UI**: Modify templates and static files
3. **Bridge Integration**: Update the Python-SML interface in `app.py`

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Test SML components
sml test_chatbot.sml

# Test Python components
python -m pytest tests/

# Integration tests
python test_integration.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests**
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Development Guidelines

- Follow functional programming principles in SML code
- Use type annotations where beneficial
- Write tests for new features
- Update documentation as needed
- Keep the web interface responsive and accessible

## 📚 Technical Details

### Why SML + FastHTML?

- **SML**: Provides strong typing, pattern matching, and functional programming benefits ideal for NLP tasks
- **FastHTML**: Modern Python framework offering simplicity and performance for web interfaces
- **Integration**: Clean separation of concerns with efficient communication between components

### Performance Considerations

- SML compiled code offers excellent performance for core logic
- FastHTML provides efficient HTTP handling and templating
- Minimal JavaScript for optimal load times
- Stateless design enables easy scaling

## 🐛 Troubleshooting

### Common Issues

**SML Compilation Errors**
```bash
# Ensure SML/NJ is properly installed
which sml

# Check syntax in SML files
sml chatbot.sml
```

**Python Dependencies**
```bash
# Upgrade pip and reinstall dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

**Port Already in Use**
```bash
# Kill existing processes on port 8000
lsof -ti:8000 | xargs kill -9
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

- Standard ML community for the excellent functional programming foundation
- FastHTML team for the intuitive web framework
- Contributors who make this project better

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/CllsPy/SmallChatGPT/issues)
- **Discussions**: [GitHub Discussions](https://github.com/CllsPy/SmallChatGPT/discussions)
- **Documentation**: [Wiki](https://github.com/CllsPy/SmallChatGPT/wiki)

---

<p align="center">
  Made with ❤️ using Standard ML and FastHTML
</p>
