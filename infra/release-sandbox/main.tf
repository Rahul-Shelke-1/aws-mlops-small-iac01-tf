
terraform {
  required_version = ">= 1.6.0"
}

output "release_sandbox_message" {
  description = "Confirms that the OpenTofu release sandbox is configured."
  value       = "Release Please sandbox is ready"
}
