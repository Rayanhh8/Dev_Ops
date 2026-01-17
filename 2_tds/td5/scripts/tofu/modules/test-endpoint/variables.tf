# ---------------------------------------------------------------------------------------------------------------------
# REQUIRED PARAMETERS
# ---------------------------------------------------------------------------------------------------------------------

variable "endpoint" {
  description = "The endpoint to make an HTTP request to"
  type        = string
}

variable "name" {
  description = "The base name for the function and all other resources"
  type        = string
  default     = "lambda-sample"
}
