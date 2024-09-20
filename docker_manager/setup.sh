#!/bin/bash

# Navigate to the directory
cd ~/vps_services/docker_manager/

# Create a virtual environment
python3 -m venv venv

# Install dependencies
venv/bin/pip install -r requirements.txt

# Copy the service file to systemd directory
sudo cp docker_manager.service /etc/systemd/system/

# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Start the Docker Manager service
sudo systemctl start docker_manager.service

# Enable the service to start on boot
sudo systemctl enable docker_manager.service

# View logs (optional)
echo "To view logs, run:"
echo "journalctl -u docker_manager.service -f"
echo "Docker Manager service setup complete!"
