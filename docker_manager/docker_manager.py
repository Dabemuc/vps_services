import os
import docker
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Docker client to communicate with the Docker daemon
client = docker.DockerClient(base_url='unix://var/run/docker.sock')


# Function to rebuild a specific service using docker-compose
def rebuild_service(service_name):
    try:
        # Rebuild the service using docker-compose
        os.system(f"pwd")
        os.system(f"ls")
        os.system(f"ls quartz")
        print(f"Rebuilding the service {service_name}...")
        rebuild_result = os.system(f"docker-compose up --force-recreate --build -d {service_name}")
        if rebuild_result != 0:
            return f"Error rebuilding service {service_name}", 500

        return f"Successfully rebuilt service {service_name}", 200
    except Exception as e:
        return f"Error: {str(e)}", 500


# API route to rebuild a service
@app.route('/rebuild', methods=['POST'])
def rebuild():
    service_name = request.args.get('service')
    if not service_name:
        return jsonify({"message": "Service name not provided"}), 400

    result, statusCode = rebuild_service(service_name)
    return jsonify({"message": result}), statusCode


# Optional: API route to list running services
@app.route('/services', methods=['GET'])
def list_services():
    try:
        # List all running containers
        containers = client.containers.list()
        service_names = [container.name for container in containers]
        return jsonify({"running_services": service_names})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
