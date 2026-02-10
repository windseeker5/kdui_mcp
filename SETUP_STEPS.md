# KD UI Framework - Setup Instructions

## Quick Setup (3 Steps)

### Step 1: Create and Activate Virtual Environment

Run the setup script first - it will create the virtual environment for you:

```bash
python setup.py
```

This will create a `venv` folder and show you the activation command.

### Step 2: Activate the Virtual Environment

**On Windows (PowerShell):**
```powershell
venv\Scripts\activate
```

**On Windows (CMD):**
```cmd
venv\Scripts\activate
```

**On Linux/macOS:**
```bash
source venv/bin/activate
```

### Step 3: Configure Proxy (Corporate Networks Only)

If you're on a corporate network with a proxy, set these environment variables:

**PowerShell:**
```powershell
$env:HTTP_PROXY="http://your-proxy-server:port"
$env:HTTPS_PROXY="http://your-proxy-server:port"
```

**CMD:**
```cmd
set HTTP_PROXY=http://your-proxy-server:port
set HTTPS_PROXY=http://your-proxy-server:port
```

**Linux/macOS:**
```bash
export HTTP_PROXY="http://your-proxy-server:port"
export HTTPS_PROXY="http://your-proxy-server:port"
```

### Step 4: Install Dependencies

```bash
pip install -e mcp-server
```

### Step 5: Run Setup Wizard

```bash
python setup.py
```

The setup wizard will guide you through configuring your MCP client (Cline, Claude Desktop, etc.).

---

## Troubleshooting

### Proxy Errors
If you see errors like "Cannot connect to proxy" or "getaddrinfo failed", you need to configure your proxy settings (see Step 3).

### Virtual Environment Not Activated
Make sure you see `(venv)` at the beginning of your terminal prompt. If not, run the activation command again.

### Permission Errors
On Windows, you may need to run PowerShell as Administrator or enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## What Gets Installed

The setup process installs:
- KD UI Framework MCP Server
- Rich (for beautiful terminal output)
- Questionary (for interactive prompts)
- Click (for CLI commands)
- All necessary dependencies

## Next Steps

After setup completes:
1. The wizard will configure your MCP client
2. Restart your MCP client (Cline, Claude Desktop, etc.)
3. Start using the KD UI Framework tools!

See `QUICK_START.md` for usage examples.
