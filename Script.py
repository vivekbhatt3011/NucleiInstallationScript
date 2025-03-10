import os
import subprocess

def run_command(command):
    """Runs a shell command and prints the output."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")
        exit(1)

def update_system():
    print("Updating system...")
    run_command("sudo apt update && sudo apt upgrade -y")

def install_golang():
    print("Installing Golang...")
    run_command("sudo apt install golang -y")
    run_command("go version")

def install_nuclei():
    print("Installing Nuclei...")
    run_command("go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest")
    run_command("sudo mv ~/go/bin/nuclei /usr/local/bin/")
    run_command("nuclei -version")

def update_nuclei_templates():
    print("Updating Nuclei templates...")
    run_command("nuclei -update-templates")

def main():
    update_system()
    install_golang()
    install_nuclei()
    update_nuclei_templates()
    print("Nuclei installation and setup completed successfully!")

if __name__ == "__main__":
    main()
