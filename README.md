<img src="./assets/logo2.png" alt="Drox Dynamics" width="full"/>

<br/>

[![Discord](https://img.shields.io/badge/Discord-DroxDynamics-blue)](https://discord.gg/HnUTabuM)
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://drox-dynamics.gitbook.io/docs)
[![WebHiveOS](https://img.shields.io/twitter/follow/DroxDynamics?style=social)](https://x.com/droxdynamics)


This project builds upon the foundation of the [Drox Dynamics](https://github.com/IgorKhrupin/Drox-Dynamics), which is designed to make websites accessible for AI agents.

We sincerely appreciate [WarmShao](https://github.com/warmshao) valuable contribution to this project.

**Drox Dynamics UI:** It is built on Gradio and supports most **browser-related** functionalities. This user-friendly UI facilitates seamless interaction with the browser agent.

**Expanded LLM Support:** We've integrated support for various Large Language Models (LLMs), including Google, OpenAI, Azure OpenAI, Anthropic, DeepSeek, and Ollama. Additionally, we plan to expand support for even more models.

**Custom Browser Support:** With our tool, you can use your own browser, eliminating the need to re-login to websites or handle authentication issues. Additionally, this feature supports high-definition screen recording.

**Persistent Browser Sessions:** You have the option to keep the browser window open between AI tasks, enabling you to view the full history and state of AI interactions.



## Installation Guide

### Prerequisites
- Python 3.11 or higher
- Git (for cloning the repository)

### Option 1: Local Installation

Read the [quickstart guide](https://docs.browser-use.com/quickstart#prepare-the-environment) or follow the steps below to get started.

#### Step 1: Clone the Repository
```bash
git clone https://github.com/IgorKhrupin/Drox-Dynamics.git
cd Drox-Dynamics
```

#### Step 2: Set Up Python Environment
We recommend using [uv](https://docs.astral.sh/uv/) for managing the Python environment.

Using uv (recommended):
```bash
uv venv --python 3.11
```

Activate the virtual environment:
- Windows (Command Prompt):
```cmd
.venv\Scripts\activate
```
- Windows (PowerShell):
```powershell
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
source .venv/bin/activate
```

#### Step 3: Install Dependencies
Install Python packages:
```bash
uv pip install -r requirements.txt
```

Install Playwright:
```bash
playwright install
```

#### Step 4: Configure Environment
1. Create a copy of the example environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
2. Open `.env` in your preferred text editor and add your API keys and other settings

### Option 2: Docker Installation

#### Prerequisites
- Docker and Docker Compose installed
  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) (For Windows/macOS)
  - [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) (For Linux)

#### Installation Steps
1. Clone the repository:
```bash
git clone https://github.com/IgorKhrupin/Drox-Dynamics.git
cd Drox-Dynamics
```

2. Create and configure environment file:
- Windows (Command Prompt):
```bash
copy .env.example .env
```
- macOS/Linux/Windows (PowerShell):
```bash
cp .env.example .env
```
Edit `.env` with your preferred text editor and add your API keys

3. Run with Docker:
```bash
# Build and start the container with default settings (browser closes after AI tasks)
docker compose up --build
```
```bash
# Or run with persistent browser (browser stays open between AI tasks)
CHROME_PERSISTENT_SESSION=true docker compose up --build
```


4. Access the Application:  
- **Web Interface:** Open [`http://localhost:7788`](http://localhost:7788) in your browser.  
- **VNC Viewer (for monitoring browser interactions):** Open [`http://localhost:6080/vnc.html`](http://localhost:6080/vnc.html).  
  - **Default VNC password:** `"youvncpassword"`  
  - You can change it by setting `VNC_PASSWORD` in your `.env` file.

## Usage

### Local Setup
1.  **Start the Drox Dynamics UI:**
    Once the installation steps are complete, launch the application using the following command:
    ```bash
    python droxdx.py --ip 127.0.0.1 --port 7788
    ```
2. UI options:
   - `--ip`: Specifies the IP address to bind the UI to. Default is `127.0.0.1`.
   - `--port`: Defines the port to bind the UI to. Default is `7788`.
   - `--theme`: Sets the theme for the user interface. Default is `Ocean`.
     - **Default**: A balanced design with a standard layout.
     - **Soft**: A muted, gentle color scheme for a soothing viewing experience.
     - **Monochrome**: A grayscale theme with minimal color for clarity and focus.
     - **Glass**: A modern, semi-transparent design for a sleek appearance.
     - **Origin**: A retro-inspired theme for a nostalgic touch.
     - **Citrus**: A lively, citrus-toned palette featuring bright and fresh colors.
     - **Ocean** (default): A calming, ocean-themed interface for a tranquil effect.
   - `--dark-mode`: Activates dark mode for the user interface.
3.  **Access the UI:** Open your web browser and go to `http://127.0.0.1:7788`.
4.  **Using Your Own Browser (Optional):**
    - Set `CHROME_PATH` to the executable path of your browser and `CHROME_USER_DATA` to the user data directory of your browser. Leave `CHROME_USER_DATA` empty to use local user data.
      - **Windows**
        ```env
         CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
         CHROME_USER_DATA="C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
        ```
        > Note: Replace `YourUsername` with your actual Windows username.
      - **Mac**
        ```env
         CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
         CHROME_USER_DATA="/Users/YourUsername/Library/Application Support/Google/Chrome"
        ```
    - Close all Chrome windows.
    - Open the UI in a non-Chrome browser, such as Firefox or Edge. This is necessary since the persistent browser context will use Chrome data while running the agent.
    - Enable the "Use Own Browser" option in the Browser Settings.
5. **Keep Browser Open (Optional):**
    - Set `CHROME_PERSISTENT_SESSION=true` in the `.env` file.

### Docker Setup
1. **Environment Variables:**
   - All configuration is managed through the `.env` file.
   - Available environment variables:
     ```
     # LLM API Keys
     OPENAI_API_KEY=your_key_here
     ANTHROPIC_API_KEY=your_key_here
     GOOGLE_API_KEY=your_key_here

     # Browser Settings
     CHROME_PERSISTENT_SESSION=true   # Set to true to keep the browser open between AI tasks
     RESOLUTION=1920x1080x24         # Custom resolution format: WIDTHxHEIGHTxDEPTH
     RESOLUTION_WIDTH=1920           # Custom width in pixels
     RESOLUTION_HEIGHT=1080          # Custom height in pixels

     # VNC Settings
     VNC_PASSWORD=your_vnc_password  # Optional, defaults to "vncpassword"
     ```

2. **Platform Support:**
   - Supports both AMD64 and ARM64 architectures.
   - For ARM64 systems (e.g., Apple Silicon Macs), the container will automatically use the appropriate image.

3. **Browser Persistence Modes:**
   - **Default Mode (`CHROME_PERSISTENT_SESSION=false`):**
     - Browser opens and closes with each AI task.
     - Provides a clean state for each interaction.
     - Uses fewer system resources.

   - **Persistent Mode (`CHROME_PERSISTENT_SESSION=true`):**
     - Keeps the browser open between AI tasks.
     - Retains history and state.
     - Enables viewing previous AI interactions.
     - Can be set in the `.env` file or as an environment variable when starting the container.

4. **Viewing Browser Interactions:**
   - Open the noVNC viewer at `http://localhost:6080/vnc.html`.
   - Enter the VNC password (default: "vncpassword" or the value set in `VNC_PASSWORD`).
   - Direct VNC access is available on port `5900` (mapped to container port `5901`).
   - This allows you to monitor all browser interactions in real-time.

5. **Container Management:**
   ```bash
   # Start with persistent browser
   CHROME_PERSISTENT_SESSION=true docker compose up -d

   # Start with default mode (browser closes after tasks)
   docker compose up -d

   # View logs
   docker compose logs -f

   # Stop the container
   docker compose down
   ```
