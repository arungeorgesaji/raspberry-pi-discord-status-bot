import discord
import psutil
import time
import subprocess
import asyncio
import os
from dotenv import load_dotenv
import atexit
load_dotenv()
BOT_TOKEN = "BOT_TOKEN"
CHANNEL_ID = int("CHANNEL_ID")
ALERT_CHANNEL_ID = int("ALERT_CHANNEL_ID")

# Thresholds for alerts
RAM_THRESHOLD = 90.0  # Send an alert if RAM usage exceeds 90%
CPU_THRESHOLD = 90.0  # Send an alert if CPU usage exceeds 90%
TEMP_THRESHOLD = 50.0  # Send an alert if CPU temperature exceeds 50°C

# Define the intents your bot will use
intents = discord.Intents.default()

# Explicitly enable the necessary intents for this bot
intents.typing = False
intents.presences = False

# Create the discord.Client instance
client = discord.Client(intents=intents)

# Function to get CPU temperature
def get_cpu_temperature():
    try:
        temp_output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        cpu_temp = float(temp_output.strip().split('=')[1][:-2])
        return cpu_temp
    except Exception as e:
        print(f"Error reading CPU temperature: {e}")
        return None

# Function to get system information as an embed
def get_system_info_embed():
    ram_usage = psutil.virtual_memory().percent
    cpu_usage = psutil.cpu_percent()
    cpu_temp = get_cpu_temperature()

    # Convert uptime to different time units
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_months = uptime_days // 30  # Approximation: 30 days in a month
    uptime_years = uptime_months // 12  # Approximation: 12 months in a year

    system_info_embed = discord.Embed(
        title="System Status",
        description="Current status of the Raspberry Pi:",
        color=0x00FF00  # You can change the color code as you like
    )
    system_info_embed.add_field(name="📱RAM Usage", value=f"{ram_usage:.2f}%", inline=True)
    system_info_embed.add_field(name="💻CPU Usage", value=f"{cpu_usage:.2f}%", inline=True)
    system_info_embed.add_field(name="⏱️Uptime", value=f"{uptime_years:.0f} years, {uptime_months % 12:.0f} months, "
                                                     f"{uptime_days % 30:.0f} days, {uptime_hours % 24:.0f} hours, "
                                                     f"{uptime_minutes % 60:.0f} minutes", inline=False)
    system_info_embed.add_field(name="🌡️CPU Temperature", value=f"{cpu_temp:.2f}°C", inline=True)
    
    # Display the current time in the footer of the embed
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    system_info_embed.set_footer(text=f"Current Time: {current_time}")

    # Create alert messages if any of the thresholds are exceeded
    alerts = []
    if ram_usage > RAM_THRESHOLD:
        alerts.append(f"🚨 ALERT: RAM usage is at {ram_usage:.2f}%")
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f" 🚨 ALERT: CPU usage is at {cpu_usage:.2f}%")
    if cpu_temp and cpu_temp > TEMP_THRESHOLD:
        alerts.append(f" 🚨 ALERT: CPU temperature is at {cpu_temp:.2f}°C")

    return system_info_embed, alerts

# Variables to store message IDs for editing
status_message_id = None
alerts_message_ids = []

#Function which returns a string regarding the version of rasberry pi
#For Example rasberry pi 5 model b returns:Raspberry Pi 5 Model B Rev 1.0
def detect_model() -> str:
    with open('/proc/device-tree/model') as f:
        model = f.read()
    return model
#get the model
model=detect_model()

# Function to be called when rasberry pi is disconnected
def exit_function():
    print(f"Connection to {model} has been halted.")
atexit.register(exit_function)

# Main event to run the bot
@client.event
async def on_ready():
    global status_message_id  # Declare status_message_id as a global variable
    print(f'We have logged in as {client.user}')
    while True:
        system_info_embed, alerts = get_system_info_embed()
        channel = client.get_channel(CHANNEL_ID)

        if not status_message_id:
            # Send the initial system status as an embed and store the message ID
            status_message = await channel.send(embed=system_info_embed)
            status_message_id = status_message.id
        else:
            # Edit the existing status message with the updated system status
            status_message = await channel.fetch_message(status_message_id)
            await status_message.edit(embed=system_info_embed)

        # Handle alerts
        alert_channel = client.get_channel(ALERT_CHANNEL_ID)
        for alert_message_id in alerts_message_ids:
            # Delete old alert messages
            alert_message = await alert_channel.fetch_message(alert_message_id)
            await alert_message.delete()

        for alert in alerts:
            # Send new alert messages and store their message IDs
            alert_message = await alert_channel.send(alert)
            alerts_message_ids.append(alert_message.id)

        await asyncio.sleep(15)  # Wait for 15 seconds before the next update (dont make it too short discord might rate limit your bot)

# Main function to run the bot
def run_bot():
    client.run(BOT_TOKEN)

if __name__ == '__main__':
    run_bot()
