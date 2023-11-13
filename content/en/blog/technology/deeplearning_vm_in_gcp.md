---
title: "DeepLearning VM in Google Cloud"
linkTitle: "DeepLearning VM in Google Cloud"
tags: [deepleaning, devops, terraform, google-cloud] 
categories: ["technology"]
weight: 102
description: >-
     Creating a DeepLearning VM in Google Cloud with Terraform. In this article we show you how we setup on-demand Deep Learning VMs in Google Cloud with Terraform.
---

Are your AI experiments pushing your MacBook to its limits? It might be time to harness the power of the cloud. Google Cloud Platform (GCP) offers GPU-equipped virtual machines that can supercharge your machine learning and AI tasks.

In this quick guide, I will walk you through creating a GPU VM on GCP using Terraform. Plus, I will show you how to effortlessly destroy the VM to avoid unexpected bills.

## Step 1: Set Up Your Google Cloud Environment

Before we start creating our GPU instance, ensure that you have the following prerequisites in place:

- A Google Cloud Platform (GCP) account with billing enabled.
- A GCP project with the necessary permissions to create resources.
- Google Cloud SDK installed and configured with the necessary credentials.

## Step 2: Define Your Variables

In your Terraform project directory, create a file named `variables.tf` to define the variables needed for your GPU instance configuration.

These variables will allow you to customise your instance’s region, project, image, accelerator type, and machine type.

Below is a sample setup with some example settings that you can use as a foundation for creating a basic GPU virtual machine (VM) suitable for tasks like Stable Diffusion. Please note that these settings are for reference and should be adjusted according to your specific requirements.

```
variable "project" {
  default     = "your-project-id"
  description = "GCP project_id"
}

variable "machine-name" {
  default     = "gpu-vm"
  description = "GCP VM Name"
}

variable "region" {
  default     = "us-central1-c"
  description = "GCP region"
}

variable "machine-type" {
  default     = "n1-standard-4"
  description = "Machine type to use. The type used here has 16GB Memory and is suitable for running Stable Diffusion"
}

variable "image" {
  default     = "deeplearning-platform-release/common-cu113-debian-11-py310"
  description = "VM image to use. A number of images are available for free in the deeplearning-platform-release family of images"
}

variable "accelerator-type" {
  default     = "nvidia-tesla-t4"
  description = "Accelerator type to use. the T4 is the least expensive option."
}
```

Replace `your-region`, `your-project-id`, `your-vm-image`, `your-accelerator-type`, and `your-machine-type` with your specific values.

At the end of document I have provided some useful commands for getting project_id, machine-types and accelerator-types.

## Step 3: Create Your GPU Instance Configuration

Now, create a Terraform configuration file, typically named `main.tf`, to specify your GPU instance configuration using the variables defined earlier. Below is an example of how to create a Google Compute Engine instance with GPU:

```
resource "google_compute_instance" "gpu-vm" {
  count        = 1
  name         = "gpu-vm"
  machine_type = var.machine-type
  zone         = var.region
  project      = var.project
  tags         = ["http"]

  boot_disk {
    initialize_params {
      image = var.image
      size  = 50 // 50 GB Storage
    }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP — leaving this block empty will generate a new external IP and assign it to the machine
    }
  }

  guest_accelerator {
    type  = var.accelerator-type
    count = 1
  }

  scheduling {
    on_host_maintenance = "TERMINATE"
  }
}
```

This Terraform configuration creates a single GPU instance with the specified settings. Ensure you’ve replaced the variables with the correct values.

## Step 4: Initialise and Apply Terraform

Navigate to your Terraform project directory in your terminal and run the following commands:

```
terraform init
```

This command initialises your Terraform environment and downloads the required plugins.

Next, execute:

```
terraform apply
```

Terraform will prompt you to confirm the creation of the resources. Type “yes” and press Enter. It will then create the GPU instance and any other defined resources.

## Step 5: Verify Your GPU Instance

Once Terraform completes the provisioning process, you can verify that your GPU instance is running in the Google Cloud Console.

Log in to your GCP account, navigate to the Compute Engine section, and find your newly created instance.

```
gcloud compute ssh --zone "YOUR-REGION" "YOUR-VM-NAME" --project "YOUR-PROJECTNAME"
```

Congratulations! You’ve successfully created a GPU instance on Google Cloud using Terraform. You can now use this GPU for machine learning and AI workloads as needed.

## Step 6: Clean Up (Optional)

If you want to remove the resources you’ve created, you can use Terraform to destroy them. In your project directory, run:

```
terraform destroy
```

Confirm the destruction by typing “yes” when prompted. This will remove all resources defined in your Terraform configuration.

## Conclusion and Additional Commands

To help you further navigate your GCP environment, here are some useful commands for retrieving essential information:

### Getting Your Project ID

To retrieve your Google Cloud project ID, run the following command in your `gcloud` terminal:

```
gcloud projects list
```

This command will display a list of all the projects associated with your account, along with their project IDs. Note down the project ID you need for your configurations.

### Listing Images in the “deeplearning-platform-release” Family

To list images belonging to the “deeplearning-platform-release” family, you can use the following command:

```
gcloud compute images list --project=deeplearning-platform-release
```

This command provides you with a list of available images within this specific family, which can be useful for selecting the appropriate image for your virtual machine.

### Retrieving Available Machine Types

To obtain a list of available machine types, which can be crucial for specifying the configuration of your virtual machines, you can execute the following command:

```
gcloud compute machine-types list
```

This command will display a list of machine types, including their names, CPUs, and memory configurations. Ensure that the selected machine type is available in your chosen region for your virtual machine.

### Listing Available Accelerator Types

When working with GPUs or other accelerators, it’s essential to know the available accelerator types within your selected region. You can acquire this information by running:

```
gcloud compute accelerator-types list
```

This command will provide you with a list of accelerator types, including details such as name, zone, and the number of GPUs available in each type. Ensure that the selected accelerator type is supported in your chosen region.

### Logging into Your VM via SSH and Tunneling

The Terraform code provided above creates a virtual machine (VM) in Google Cloud, but by default, it does not expose the VM to external access. To access your VM and potentially tunnel to a specific port, you can use the following commands.

### Logging into Your VM via SSH

You can log into your VM using SSH by running the following command. Replace `YOUR_REGION`, `YOUR_VM_NAME`, and `YOUR_PROJECT_NAME` with your specific values:

```
gcloud compute ssh --zone YOUR_REGION "YOUR_VM_NAME" --project "YOUR_PROJECT_NAME"
```

This command establishes an SSH connection to your VM, allowing you to interact with it remotely. Make sure you have the Google Cloud SDK installed and authenticated.

### Tunnel to a Port on Your VM

To tunnel to a specific port on your VM, allowing you to access a service running on that port, you can use the following command. Here, `YOUR-VM-NAME`, `YOUR-PROJECT-NAME`, `YOUR_REGION`, `8601`, and `7860` should be replaced with your specific values:

```
gcloud compute ssh YOUR-VM-NAME --project YOUR-PROJECT-NAME --zone YOUR_REGION -- -NL 8601:localhost:7860
```

In this command:

- `YOUR-VM-NAME`: Replace with the name of your VM.
- `YOUR-PROJECT-NAME`: Replace with the name of your Google Cloud project.
- `YOUR_REGION`: Replace with the desired region for your VM.
- `8601`: This is the local port on your machine where the tunnel will be established. You can choose any available port.
- `7860`: This is the port on your VM where your service is exposed. Make sure it matches the port on your VM where your service is running.

After running this command, you can access the service running on your VM via `http://localhost:8601` in your local web browser. The data will be securely tunneled to and from your VM. This is particularly useful for accessing web-based services running on your VM without exposing them directly to the internet.

Remember to replace the placeholders with your actual project and VM details to successfully log in and set up tunnels as needed for your specific use case.