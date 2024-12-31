variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "image-recognition"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "prod"
}