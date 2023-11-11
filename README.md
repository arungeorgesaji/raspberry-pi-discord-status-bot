# ![img_no_load](https://cdn.discordapp.com/attachments/1146751151946084362/1172155713011859456/icons8-raspberry-pi-48.png) Discord Raspberry Pi System Monitor Bot ![img_no_load](https://cdn.discordapp.com/attachments/1146751151946084362/1172155713011859456/icons8-raspberry-pi-48.png) 
## Overview
This Discord bot monitors the system status of a Raspberry Pi and provides real-time updates on RAM usage, CPU usage, CPU temperature, and uptime. Additionally, it sends alerts to a specified channel when certain thresholds are exceeded.

## Features
- **Real-time System Information:** The bot fetches and displays real-time information on RAM usage, CPU usage, CPU temperature, and system uptime.
- **Threshold Alerts:** Alerts are triggered and sent to a designated channel if RAM usage, CPU usage, or CPU temperature exceeds predefined thresholds.
- **Automatic Updates:** The bot regularly updates the system status information in the designated channel to keep users informed.

## Tested Raspberry Pi Models
This project has been tested and verified to work seamlessly with the following Raspberry Pi models:

- Raspberry Pi 4
- Raspberry Pi 5(more features will be added soon)
  
## Setup Instructions
1. Clone the repository to your Raspberry Pi.
   ```
   git clone https://github.com/MrInternetGitHub/raspberry-pi-discord-status-bot.git
   ```

2. Install the required Python packages.
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add the following variables (or rename the one on the repo to .env and add your variables):
   ```
   #current code makes you type this in the main.py itself you can adjust if needed
   BOT_TOKEN=your_bot_token
   CHANNEL_ID=your_channel_id
   ALERT_CHANNEL_ID=your_alert_channel_id
   ```

4. Adjust the threshold values in the `main.py` file if needed (Line 20-22) .

5. Run the bot using the following command:
   ```
   python main.py
   
   ```

6. Your bot is now active and monitoring the system. The initial system status will be displayed, and subsequent updates will follow.

## Example
![img2](https://cdn.discordapp.com/attachments/1146751151946084362/1172161078596214834/Screenshot_2023-11-09_183508.png)
![img1](https://cdn.discordapp.com/attachments/1146751151946084362/1172161078877229067/Screenshot_2023-11-09_183907.png)

## Important Note
Make sure to invite the bot to your Discord server and provide the necessary permissions. Also, ensure that the `vcgencmd` command is available on your Raspberry Pi for reading CPU temperature.

## Customization
Feel free to customize the bot according to your preferences. You can modify the color codes, update the alert messages, or add additional features as needed.

## Troubleshooting
If you encounter any issues or errors, please check the following:
- Ensure that the bot has the necessary permissions in the Discord server.
- Double-check the accuracy of the provided channel IDs and bot token in the `.env` file.
- Verify that the `vcgencmd` command is available on your Raspberry Pi for reading CPU temperature.
- Read and attempt to comprehend the errors present in the logs a simple search can help you.
  ## Contributing

We welcome contributions to enhance the functionality and compatibility of this Discord System Monitor Bot. If you have ideas for new features, bug fixes, or improvements, please follow the steps below:

1. Fork the repository to your GitHub account.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and test thoroughly.
4. Commit your changes with descriptive commit messages: `git commit -m "Add feature-name"`.
5. Push your branch to your fork: `git push origin feature-name`.
6. Open a pull request to the `main` branch of this repository.

We appreciate your contributions and look forward to working together to make this Discord bot even better!

Feel free to customize the instructions based on your preferred contribution workflow.

Happy monitoring!
